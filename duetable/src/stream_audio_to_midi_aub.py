from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from time import time

import aubio
import pyaudio
import numpy as np
from miditoolkit.midi import parser as mid_parser
from miditoolkit.midi import containers as ct
from mido import second2tick, bpm2tempo
from numpy import median, diff

from duetable.src.midi_utils import MIDI_DATA_BY_NO
from duetable.src.settings import DuetableSettings


class StreamAudioToMidiWithAub:

    def __init__(
            self,
            settings: DuetableSettings,
            frames_per_buffer=512,
            sample_rate=44100,
            win_s=1024,
            hop_s=128,
            device_name='MacBook Pro Microphone'
    ):
        self.settings = settings
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
        self.debug_output_to_midi = True

    def read(self):
        note_detector_method = "default"
        notes_detector = aubio.notes(note_detector_method, self.win_s, self.hop_s, self.sample_rate)  # TODO try with aubio.pitch

        duration = 0
        while True:
            data = self._stream.read(self.hop_s, exception_on_overflow=False)
            samples = np.frombuffer(data, dtype=np.float32)

            note_detection_result = notes_detector(samples)
            midi_note, velocity, midi_note_to_turn_off = note_detection_result
            midi_note = int(midi_note)
            velocity = int(velocity)
            midi_note_to_turn_off = int(midi_note_to_turn_off)

            if midi_note != 0:
                print(f"Detected note: {midi_note}/{MIDI_DATA_BY_NO[midi_note]['name']}, "
                          f"velocity: {velocity}, "
                          f"note to turn off: {midi_note_to_turn_off}")

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

                if len(self.buffer) == self.settings.buffer_length + 1:  # checking if buffer reached its limit
                    print("\nBuffer is full:")
                    last_note = self.buffer.pop()
                    pprint(self.buffer)
                    self.thread_pool_executor.submit(self._process_buffer, self.buffer)

                    self.buffer = []
                    self.buffer.append(last_note)

    def _process_buffer(self, buffer):
        print("\nProcessing buffer:")
        pprint(buffer)

        beats = [buf_note[3] for buf_note in buffer]
        try:
            tempo_in_bpm = int(abs(median(60. / diff(beats))))
        except ZeroDivisionError:  # :)
            tempo_in_bpm = 120
        print(f"Buffer tempo: {tempo_in_bpm}")
        midi_tempo = bpm2tempo(tempo_in_bpm)

        mido_obj = mid_parser.MidiFile()
        beat_resol = mido_obj.ticks_per_beat

        track = ct.Instrument(program=0, is_drum=False, name='duetable recorder buffer')
        mido_obj.instruments = [track]

        start_off = 0.0
        for buffer_note in buffer:
            start = second2tick(start_off, beat_resol, midi_tempo)
            end = second2tick(buffer_note[3], beat_resol, midi_tempo)
            # print(f'start_off={start_off}, start={start}, end={end}')

            note = ct.Note(
                start=start,
                end=end,
                pitch=buffer_note[1],
                velocity=buffer_note[2]
            )
            mido_obj.instruments[0].notes.append(note)

            start_off = start_off + buffer_note[3]

        if self.debug_output_to_midi:
            debug_file_name = f'./buffer_result_{int(time())}.midi'
            mido_obj.dump(debug_file_name)
            print(f'Saved for debug purpose: {debug_file_name}')


settings = DuetableSettings()
settings.buffer_length = 4
stream_2_midi = StreamAudioToMidiWithAub(settings=settings, device_name="U46")
stream_2_midi.read()
