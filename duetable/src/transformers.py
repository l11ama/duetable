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


class SimpleTimeTransformer(MidiBufferPostTransformation):

    def __init__(self, change_time_fn: Callable):
        self.change_time_fn = change_time_fn

    def transform(self, sequence: List[tuple[str, int, int, int]]) -> List[tuple[str, int, int, int]]:
        if not sequence:
            return sequence

        new_sequence = []
        for seq in sequence:
            new_midi_duration = seq[3] + self.change_time_fn()
            new_sequence.append(
                (
                    seq[0],
                    seq[1],
                    seq[2],
                    new_midi_duration
                )
            )

        return new_sequence


class MidiRangeTransformer(MidiBufferPostTransformation):

    def __init__(self, from_midi_no, to_midi_no):
        self.from_midi_no = from_midi_no
        self.to_midi_no = to_midi_no

    def transform(self, sequence: List[tuple[str, int, int, int]]) -> List[tuple[str, int, int, int]]:
        if not sequence:
            return sequence

        new_sequence = []
        for seq in sequence:
            midi_no = seq[1]

            if midi_no > self.to_midi_no:
                midi_no = self.to_midi_no

            if midi_no < self.from_midi_no:
                midi_no = self.from_midi_no

            new_sequence.append(
                (
                    MIDI_DATA_BY_NO[midi_no]['name'],
                    midi_no,
                    seq[2],
                    seq[3]
                )
            )

        return new_sequence


