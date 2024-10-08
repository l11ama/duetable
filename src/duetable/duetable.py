import warnings
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from threading import Thread
from time import time
from typing import List

import pyaudio
import numpy as np
from miditoolkit.midi import parser as mid_parser
from miditoolkit.midi import containers as ct
from mido import second2tick, bpm2tempo
from numpy import median, diff

from duetable.interfaces import AudioToMidi, MidiBufferRegenerator, MidiBufferPostTransformation
from duetable.midi_utils import MIDI_DATA_BY_NO
from duetable.regenerators import DummyRegenerator
from duetable.sequence_player import SequencePlayer
from duetable.settings import DuetableSettings, RecordingStrategy


class DuetableThreadPoolExecutor(ThreadPoolExecutor):

    def __init__(self, *args, **kwargs):
        super(DuetableThreadPoolExecutor, self).__init__(*args, **kwargs)

    def queue_size(self) -> int:
        return self._work_queue.qsize()


class Duetable(Thread):

    def __init__(
            self,
            settings: DuetableSettings,
            converter: AudioToMidi,
            frames_per_buffer=512,
            sample_rate=44100,
            win_s=1024,
            hop_s=128,
            device_name='MacBook Pro Microphone',
            regenerator: MidiBufferRegenerator = DummyRegenerator(),
            transformations: List[MidiBufferPostTransformation] = None
    ):
        super(Duetable, self).__init__(name="Duetable App")
        self.settings = settings
        self.converter = converter
        self.regenerator = regenerator
        self.transformations = transformations

        down_sample = 1  # FIXME maybe should be use for pyaudio rate?
        self.sample_rate = sample_rate // down_sample
        self.win_s = win_s // down_sample
        self.hop_s = hop_s // down_sample

        self._audio = pyaudio.PyAudio()
        input_device_index = None
        print(f"Device count: {self._audio.get_device_count()}")
        for idx in range(self._audio.get_device_count()):
            print(f"Device {idx}: {self._audio.get_device_info_by_index(idx)}")
            if device_name in self._audio.get_device_info_by_index(idx)['name']:
                input_device_index = idx
                break

        if input_device_index is None:
            raise ValueError(f"Device {device_name} not found!")

        print(f'Using: {device_name} with idx={input_device_index}', flush=True)

        self._stream = self._audio.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=self.sample_rate,
            input=True,
            input_device_index=input_device_index,
            frames_per_buffer=frames_per_buffer
        )

        self.buffer = []
        self.thread_pool_executor = DuetableThreadPoolExecutor(max_workers=1)
        self.debug_output_to_midi = False

        self.sequence_player = SequencePlayer(
            loop=settings.loop_playback,
            bpm=settings.bpm,
            lower_meter=settings.lower_meter,
            sleep_with_note=settings.sleep_with_note,
        )
        self._is_once_recorded = False

        # self.daemon = True
        # self.start()

    def run(self):
        """
        Main loop of the Duetable. Execute `read()` method.

        :return:
        """
        self.read()

    def read(self):
        """
        Read data from the audio stream and run the processing based on the settings.

        :return:
        """
        start_time = time()
        duration = 0

        stop_recording_condition = None
        if self.settings.recording_strategy == RecordingStrategy.NOTES:
            stop_recording_condition = lambda: len(self.buffer) == self.settings.buffer_length# + 1

        if self.settings.recording_strategy == RecordingStrategy.TIME:
            stop_recording_condition = lambda: time() - start_time >= self.settings.buffer_time

        if self.settings.recording_strategy == RecordingStrategy.TIME_ONCE:
            stop_recording_condition = lambda: self._is_time_once_executed(start_time)

        if self.settings.recording_strategy == RecordingStrategy.NOTES_ONCE:
            stop_recording_condition = lambda: self._is_note_once_executed()

        if not stop_recording_condition:
            raise ValueError('Unknown recording strategy')

        while True:
            if not self.settings.record_when_playing:
                if self.sequence_player.is_playing() or self.thread_pool_executor.queue_size() > 0:
                    start_time = time()

                    if self.settings.recording_strategy not in (RecordingStrategy.TIME_ONCE, RecordingStrategy.NOTES_ONCE):
                        self.buffer = []

                    if self._stream.is_active():
                        self._stream.stop_stream()
                        print('Stopped recording')

                    continue
                else:
                    if self._stream.is_stopped():
                        self._stream.start_stream()
                        print('Started recording')

            stream_data = self._stream.read(self.hop_s, exception_on_overflow=False)
            samples_buffer = np.frombuffer(stream_data, dtype=np.float32)

            midi_note, velocity = self.converter.convert_from_buffer(
                samples_buffer,
                SAMPWIDTH=self._audio.get_sample_size(pyaudio.paInt16)
            )

            if midi_note != 0:
                print(f"Detected note: {midi_note}/{MIDI_DATA_BY_NO[midi_note]['name']}, velocity: {velocity}", flush=True)

                # appending detected noted into the buffer
                has_prev_note = len(self.buffer) > 0

                if has_prev_note:  # setting duration of the prev note
                    prev_idx = len(self.buffer) - 1
                    prev_note_from_buffer = self.buffer[prev_idx]
                    self.buffer[prev_idx] = (
                        prev_note_from_buffer[0],
                        prev_note_from_buffer[1],
                        prev_note_from_buffer[2],
                        round(time() - duration, 2)
                    )

                self.buffer.append(
                    (
                        MIDI_DATA_BY_NO[midi_note]['name'],
                        midi_note,
                        velocity,
                        0
                    ))  # adding new note to the buffer

                duration = time()

            if stop_recording_condition():  # checking if buffer reached its limit
                print("Buffer is full...")
                if len(self.buffer) == 0:
                    print("but nothing to reprocess...")
                    if self.settings.recording_strategy == RecordingStrategy.TIME:
                        start_time = time()
                    continue

                # if recording strategy is NOTES, and buffer has more than one note
                # let's estimate last note time
                if self.settings.recording_strategy == RecordingStrategy.NOTES and len(self.buffer) > 1:
                    last_idx = len(self.buffer) - 1
                    sum_except_last = sum([t[3] for t in self.buffer[:last_idx]])
                    self.buffer[last_idx] = (
                        self.buffer[last_idx][0],
                        self.buffer[last_idx][1],
                        self.buffer[last_idx][2],
                        round(sum_except_last/(len(self.buffer)-1), 2)
                    )

                # if recording strategy is TIME, and buffer has more than one note
                # let's trim last note to fit the total buffer time
                if self.settings.recording_strategy == RecordingStrategy.TIME and len(self.buffer) > 1:
                    last_idx = len(self.buffer) - 1

                    total_buffer_time = sum([t[3] for t in self.buffer])
                    print(f'Total buffer time: {total_buffer_time} sec.')

                    sum_except_last = sum([t[3] for t in self.buffer[:last_idx]])
                    print(f'Total buffer time except last item: {sum_except_last} sec.')

                    if total_buffer_time > self.settings.buffer_time:
                        l_l_note = self.buffer[last_idx]
                        self.buffer[last_idx] = (
                            l_l_note[0],
                            l_l_note[1],
                            l_l_note[2],
                            round(self.settings.buffer_time - sum_except_last, 2)
                        )

                    # TODO if total buff time is < setting buff time add REST

                    trimmed_total_buffer_time = sum([t[3] for t in self.buffer])
                    print(f'Total buffer time after trim: {trimmed_total_buffer_time} sec.')

                # if recording strategy is TIME, reset start time
                if self.settings.recording_strategy == RecordingStrategy.TIME:
                    start_time = time()

                self.thread_pool_executor.submit(self._process_buffer, self.buffer)

                if self.settings.recording_strategy not in (RecordingStrategy.TIME_ONCE, RecordingStrategy.NOTES_ONCE):
                    self.buffer = []

    def _is_time_once_executed(self, start_time):
        if time() - start_time >= self.settings.buffer_time and not self._is_once_recorded:
            self._is_once_recorded = True
            return True

        if self._is_once_recorded:
            return True

        return False

    def _is_note_once_executed(self):
        if len(self.buffer) == self.settings.buffer_length and not self._is_once_recorded:
            self._is_once_recorded = True
            return True

        if self._is_once_recorded:
            return True

        return False

    def _process_buffer(self, buffer):
        print("Processing buffer:")
        pprint(buffer)

        tempo_in_bpm = self._detect_bpm_from_buffer(buffer)
        print(f"Possible buffer tempo: {tempo_in_bpm}")

        # modify detected buffer
        regenerated_buffer = self.regenerator.regenerate_sequence(buffer, self.settings)  # FIXME consider providing BPM

        if self.transformations:
            for transformer in self.transformations:
                print(f'Transforming with {transformer}')
                regenerated_buffer = transformer.transform(regenerated_buffer)

                # add modified buffer to the player
        self.sequence_player.add_generator_bars_notes(
            regenerated_buffer,
            reset=not self.settings.append_to_play_buffer
        )

        if self.debug_output_to_midi:
            self._buffer_to_midi_obj(buffer, tempo_in_bpm)

    def _buffer_to_midi_obj(
            self,
            buffer: List[tuple[str, int, int, int]],
            tempo_in_bpm: float = 120.0
    ) -> mid_parser.MidiFile:
        """
        Convert detected buffer into MIdi File
        :param buffer:
        :param tempo_in_bpm:
        :return:
        """
        midi_tempo = bpm2tempo(tempo_in_bpm)
        mido_obj = mid_parser.MidiFile()
        beat_resol = mido_obj.ticks_per_beat

        track = ct.Instrument(program=0, is_drum=False, name='duetable recorder buffer')
        mido_obj.instruments = [track]

        start_off = 0.0
        for buffer_note in buffer:
            start = second2tick(start_off, beat_resol, midi_tempo)
            end = second2tick(buffer_note[3], beat_resol, midi_tempo)

            note = ct.Note(
                start=start,
                end=end,
                pitch=buffer_note[1],
                velocity=buffer_note[2]
            )
            mido_obj.instruments[0].notes.append(note)

            start_off = start_off + buffer_note[3]

        debug_file_name = f'./buffer_result_{int(time())}.midi'
        mido_obj.dump(debug_file_name)
        print(f'Saved buffer to MIDI for debug purpose: {debug_file_name}')

        return mido_obj

    def _detect_bpm_from_buffer(self, buffer: List[tuple[str, int, int, int]]) -> float:
        beats = [buf_note[3] for buf_note in buffer]
        try:
            tempo_in_bpm = int(abs(median(60. / diff(beats))))
        except Exception:  # FIXME :)
            tempo_in_bpm = 120

        return tempo_in_bpm


warnings.filterwarnings('ignore')

