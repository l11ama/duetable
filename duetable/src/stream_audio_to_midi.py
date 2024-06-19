from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from time import time
from typing import List, Optional

import pyaudio
import numpy as np
from miditoolkit.midi import parser as mid_parser
from miditoolkit.midi import containers as ct
from mido import second2tick, bpm2tempo
from numpy import median, diff

from duetable.src.audio_to_midi_aub import AudioToMidiWithAubio
from duetable.src.audio_to_midi_spoti import AudioToMidiWithSpotify
from duetable.src.midi_devices import get_elektron_outport
from duetable.src.interfaces import AudioToMidi, MidiBufferRegenerator
from duetable.src.midi_utils import MIDI_DATA_BY_NO
from duetable.src.regenerators import DummyRegenerator, HttpMuptRegenerator
from duetable.src.sequence_player import SequencePlayer
from duetable.src.settings import DuetableSettings, RecordingStrategy


class StreamAudioToMidi:

    def __init__(
            self,
            settings: DuetableSettings,
            converter: AudioToMidi,
            frames_per_buffer=512,
            sample_rate=44100,
            win_s=1024,
            hop_s=128,
            device_name='MacBook Pro Microphone',
            regenerator: MidiBufferRegenerator = DummyRegenerator()
    ):
        self.settings = settings
        self.converter = converter
        self.regenerator = regenerator

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

        print(f'Using: {device_name} with idx={input_device_index}')

        self._stream = self._audio.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=self.sample_rate,
            input=True,
            input_device_index=input_device_index,
            frames_per_buffer=frames_per_buffer
        )

        self.buffer = []
        self.thread_pool_executor = ThreadPoolExecutor(max_workers=1)
        self.debug_output_to_midi = False

        self.sequence_player = SequencePlayer(get_elektron_outport())

    def read(self):
        start_time = time()
        duration = 0

        stop_recording_condition = None
        if self.settings.recording_strategy == RecordingStrategy.NOTES:
            stop_recording_condition = lambda: len(self.buffer) == self.settings.buffer_length + 1

        if self.settings.recording_strategy == RecordingStrategy.TIME:
            stop_recording_condition = lambda: time() - start_time >= self.settings.buffer_time

        if not stop_recording_condition:
            raise ValueError('Unknown recording strategy')

        while True:
            if not settings.record_when_playing and self.sequence_player.is_playing():
                continue

            stream_data = self._stream.read(self.hop_s, exception_on_overflow=False)
            samples_buffer = np.frombuffer(stream_data, dtype=np.float32)

            midi_note, velocity = self.converter.convert_from_buffer(
                samples_buffer,
                SAMPWIDTH=self._audio.get_sample_size(pyaudio.paInt16)
            )

            if midi_note != 0:
                print(f"Detected note: {midi_note}/{MIDI_DATA_BY_NO[midi_note]['name']}, velocity: {velocity}")

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

                    # remove last note because it is either over size limit or time
                    last_note = self.buffer.pop()

                    # if recording strategy is TIME, and buffer has more than one note
                    # let's trim last note to fit the total buffer time
                    if self.settings.recording_strategy == RecordingStrategy.TIME and len(self.buffer) > 1:
                        last_idx = len(self.buffer) - 1

                        total_buffer_time = sum([t[3] for t in self.buffer])
                        print(f'Total buffer time: {total_buffer_time} sec.')

                        sum_except_last = sum([t[3] for t in self.buffer[:last_idx]])
                        print(f'Total buffer time except last item: {sum_except_last} sec.')

                        if total_buffer_time > settings.buffer_time:
                            l_l_note = self.buffer[last_idx]
                            self.buffer[last_idx] = (
                                l_l_note[0],
                                l_l_note[1],
                                l_l_note[2],
                                round(settings.buffer_time - sum_except_last, 2)
                            )

                        trimmed_total_buffer_time = sum([t[3] for t in self.buffer])
                        print(f'Total buffer time after trim: {trimmed_total_buffer_time} sec.')

                    # if recording strategy is TIME, reset start time
                    if self.settings.recording_strategy == RecordingStrategy.TIME:
                        start_time = time()

                    self.thread_pool_executor.submit(self._process_buffer, self.buffer)

                    self.buffer = []
                    self.buffer.append(last_note)

    def _process_buffer(self, buffer):
        print("Processing buffer:")
        pprint(buffer)

        tempo_in_bpm = self._detect_bpm_from_buffer(buffer)
        print(f"Possible buffer tempo: {tempo_in_bpm}")

        # modify detected buffer
        regenerated_buffer = self.regenerator.regenerate_sequence(buffer)  # FIXME consider providing BPM

        # add modified buffer to the player
        self.sequence_player.add_generator_bars_notes(regenerated_buffer, reset=True)  # FIXME consider exposing reset to global settings

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


settings = DuetableSettings()
settings.buffer_length = 4
settings.buffer_time = 8.0
settings.recording_strategy = RecordingStrategy.TIME
settings.record_when_playing = False

stream_2_midi = StreamAudioToMidi(
    # midi converter
    converter=AudioToMidiWithAubio(down_sample=1),
    # hop_s=10*2048,  # set for Spotify due to natural network nature for prediction, comment out for Aubio
    # converter=AudioToMidiWithSpotify(),

    # setting
    settings=settings,

    # audio in
    # device_name="U46",

    # detected midi regenerator
    # regenerator=HttpMuptRegenerator()
)
stream_2_midi.read()
