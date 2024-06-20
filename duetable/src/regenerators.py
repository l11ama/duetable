from typing import List

from duetable.src.abc_utils import generate_abc_from_sequence, generate_sequence_from_abc
from duetable.src.interfaces import MidiBufferRegenerator
from duetable.src.melody_markov_chain import MarkovRegenerator
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
            n_bars=settings.n_bars,
            temperature=settings.temperature,
            n_samples=8,
            model=settings.model_size
        )
        if not new_abc_score:
            print('WARN: Could not generate new ABC score, returning original')
            return sequence

        return generate_sequence_from_abc(new_abc_score)


class MuptWithMarkovChainRegenerator(HttpMuptRegenerator):

    def __init__(self):
        super(MuptWithMarkovChainRegenerator, self).__init__()
        self._markov = MarkovRegenerator()
        self._mupt_sequence = None

    def regenerate_sequence(self, sequence: List[tuple[str, int, int, int]], settings: DuetableSettings) -> List[tuple[str, int, int, int]]:
        if not self._mupt_sequence:
            self._mupt_sequence = super(MuptWithMarkovChainRegenerator, self).regenerate_sequence(sequence, settings)

        return self._markov.regenerate(self._mupt_sequence)
