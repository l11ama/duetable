from typing import List

from duetable.src.interfaces import MidiBufferRegenerator


class DummyRegenerator(MidiBufferRegenerator):

    def regenerate_sequence(self, sequence: List[tuple[str, int, int, int]]):
        return sequence
