import aubio
import pyaudio
import numpy as np

from duetable.src.midi_utils import MIDI_DATA_BY_NO


class StreamAudioToMidiWithAub:

    def __init__(self, frames_per_buffer=512, sample_rate=44100, win_s=1024, hop_s=128):
        down_sample = 1  # FIXME maybe should be use for pyaudio rate?
        self.sample_rate = sample_rate // down_sample
        self.win_s = win_s // down_sample
        self.hop_s = hop_s // down_sample

        self._audio = pyaudio.PyAudio()
        self._stream = self._audio.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=self.sample_rate,
            input=True,
            input_device_index=0,
            frames_per_buffer=frames_per_buffer
        )

    def read(self):
        note_detector_method = "default"
        notes_detector = aubio.notes(note_detector_method, self.win_s, self.hop_s, self.sample_rate)  # TODO try with aubio.notes

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


stream_2_midi = StreamAudioToMidiWithAub()
stream_2_midi.read()
