from typing import List, Callable

from duetable.src.interfaces import MidiBufferPostTransformation
from duetable.src.midi_utils import MIDI_DATA_BY_NO


class SimpleTransposeTransformer(MidiBufferPostTransformation):

    def __init__(self, transpose_by_fn: Callable):
        self.transpose_by_fn = transpose_by_fn

    def transform(self, sequence: List[tuple[str, int, int, int]]) -> List[tuple[str, int, int, int]]:
        if not sequence:
            return sequence

        transpose_by = self.transpose_by_fn()

        new_sequence = []
        for seq in sequence:
            new_midi_no = seq[1] + transpose_by
            if new_midi_no < 21 or new_midi_no > 127:
                new_midi_no = seq[1]

            new_sequence.append(
                (
                    MIDI_DATA_BY_NO[new_midi_no]['name'],
                    new_midi_no,
                    seq[2],
                    seq[3]
                )
            )

        return new_sequence
