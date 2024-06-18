import time
from threading import Thread

import mido


class SequencePlayer(Thread):

    def __init__(self, output_midi_device):
        super(SequencePlayer, self).__init__(name="SequencePlayer")
        self._output_midi_device = output_midi_device
        self._midi_notes_sequence = []

        self.loop = True

        self.daemon = True
        self.start()

    def add_generator_bars_notes(self, midi_notes_sequence, reset=False):
        if reset:
            self._midi_notes_sequence = []

        self._midi_notes_sequence.extend(midi_notes_sequence)

    def run(self):
        current_note_idx = 0
        while True:
            if len(self._midi_notes_sequence) > 0:
                note = self._midi_notes_sequence[current_note_idx]

                msg = mido.Message(
                    'note_on',
                    channel=0,
                    note=note[1],
                    velocity=note[2],
                    time=note[3],
                )
                self._output_midi_device.send(msg)

                current_note_idx += 1
                if self.loop and current_note_idx >= len(self._midi_notes_sequence):
                    current_note_idx = 0

                time.sleep(note[3])

