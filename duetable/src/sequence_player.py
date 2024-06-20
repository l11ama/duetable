import time
from fractions import Fraction
from threading import Thread

import mido


class SequencePlayer(Thread):

    def __init__(self, output_midi_device):
        super(SequencePlayer, self).__init__(name="SequencePlayer")
        self._output_midi_device = output_midi_device
        self._midi_notes_sequence = []

        self.loop = False  # FIXME move to settings

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
                # if current_note_idx >= len(self._midi_notes_sequence):
                #     current_note_idx = 0
                #     continue  # FIXME probably not the best solution

                note = self._midi_notes_sequence[current_note_idx]

                print(f'-------------> PLAY note: {note[0]}({note[1]}), curr idx: {current_note_idx}')

                msg = None
                if note[0] != 'z':
                    msg = mido.Message(
                        'note_on',
                        channel=0,
                        note=note[1],
                        velocity=127 if note[2] > 127 else note[2],
                        time=note[3],
                    )

                if self._output_midi_device and msg:
                    self._output_midi_device.send(msg)
                else:
                    print(f'-------------> Output MIDI device not set, midi msg: {msg}')

                if isinstance(note[3], Fraction):
                    print(float(sum(Fraction(s) for s in '1 2/3'.split())))
                else:
                    if note[3] > 0:  # can be negative due to trimming if TIME strategy of recorded buffer
                        time.sleep(note[3])

                current_note_idx += 1
                if current_note_idx >= len(self._midi_notes_sequence):
                    current_note_idx = 0

                if not self.loop and current_note_idx == 0:
                    self._reset_notes_sequence()
                    print(f'-------------> Sequence reset')

    def _reset_notes_sequence(self):
        self._midi_notes_sequence = []
