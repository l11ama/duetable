from typing import List

from duetable.src.abc_utils import generate_abc_from_sequence, generate_sequence_from_abc
from duetable.src.interfaces import MidiBufferRegenerator
from duetable.src.mupt_connector import MuptConnector
from duetable.src.settings import DuetableSettings


class DummyRegenerator(MidiBufferRegenerator):

    def regenerate_sequence(self, sequence: List[tuple[str, int, int, int]], settings: DuetableSettings) -> List[tuple[str, int, int, int]]:
        return sequence


class HttpMuptRegenerator(MidiBufferRegenerator):

    def __init__(self):
        self._mupt_connector = MuptConnector()

    def regenerate_sequence(self, sequence: List[tuple[str, int, int, int]], settings: DuetableSettings) -> List[tuple[str, int, int, int]]:
        new_abc_score = self._mupt_connector.generate_new_abc_score(
            generate_abc_from_sequence(sequence, settings),
            n_bars=4,
            temperature=0.7,
            n_samples=5,
            model="small"
        )
        if not new_abc_score:
            print('WARN: Could not generate new ABC score, returning original')
            return sequence

        return generate_sequence_from_abc(new_abc_score)

