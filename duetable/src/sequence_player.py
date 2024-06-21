import time
from fractions import Fraction
from threading import Thread

from midi_devices import play_note_in_midi_devices
from midi_utils import note_length_in_seconds


class SequencePlayer(Thread):

    def __init__(self, loop=False, bpm=120, lower_meter=4, sleep_with_note=True):
        super(SequencePlayer, self).__init__(name="SequencePlayer")
        self._midi_notes_sequence = []

        self.loop = loop
        self.bpm = bpm
        self.lower_meter = lower_meter
        self.sleep_with_note = sleep_with_note

        self.daemon = True
        self.start()

    def add_generator_bars_notes(self, midi_notes_sequence, reset=False):
        if reset:
            self._reset_notes_sequence()

        self._midi_notes_sequence.extend(midi_notes_sequence)
        print(f'-------------> notes to play: {len(self._midi_notes_sequence)}')

    def is_playing(self):
        return len(self._midi_notes_sequence) > 0

    def run(self):
        current_note_idx = 0
        while True:
            if len(self._midi_notes_sequence) > 0:
                note = self._midi_notes_sequence[current_note_idx]

                print(f'-------------> PLAY note: {note[0]}({note[1]}), curr idx: {current_note_idx}')

                msg = None
                play_note_in_midi_devices(note)

                if self.sleep_with_note:
                    if isinstance(note[3], Fraction):
                        print(float(sum(Fraction(s) for s in '1 2/3'.split())))
                    else:
                        if note[3] > 0:  # can be negative due to trimming if TIME strategy of recorded buffer
                            time.sleep(note[3])
                else:
                    time.sleep(note_length_in_seconds(self.bpm, self.lower_meter))

                current_note_idx += 1
                if current_note_idx >= len(self._midi_notes_sequence):
                    current_note_idx = 0

                if not self.loop and current_note_idx == 0:
                    self._reset_notes_sequence()
                    print(f'-------------> Sequence reset')

    def _reset_notes_sequence(self):
        self._midi_notes_sequence = []
