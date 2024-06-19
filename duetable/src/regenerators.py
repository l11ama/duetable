from typing import List

import requests
from music21 import converter, note

from duetable.src.interfaces import MidiBufferRegenerator


class DummyRegenerator(MidiBufferRegenerator):

    def regenerate_sequence(self, sequence: List[tuple[str, int, int, int]]) -> List[tuple[str, int, int, int]]:
        return sequence


class HttpMuptRegenerator(MidiBufferRegenerator):

    def __init__(self):
        self._url = "http://92.38.241.195:2345/generate"
        self._http_request_session = requests.Session()

    def regenerate_sequence(self, sequence: List[tuple[str, int, int, int]]) -> List[tuple[str, int, int, int]]:
        request_headers = {"Accept": "application/json", "Content-Type": "application/json"}

        json_payload = {
            "prefix": self._generate_abc_from_sequence(sequence),
            "max_length": 64
        }
        print('Querying mupt with: ', json_payload)

        try:
            response = self._http_request_session.post(
                url=self._url,
                json=json_payload,
                headers=request_headers,
                timeout=10
            )

            if response.status_code != 200:
                print(f'ERROR: Error from mupt regenerator: {response.text}')
                print(f'WARNING: regenerator failed, returning original sequence.')
                return sequence

            mupt_json_response = response.json()
            generated_melody = mupt_json_response['content']['melody'].replace('|:', '\n')
            return self._generate_sequence_from_abc(generated_melody)

        except Exception as e:
            print(f'ERROR: Error from mupt regenerator: {e}')
            print(f'WARNING: regenerator failed, returning original sequence.')
            return sequence

    def _generate_abc_from_sequence(self, sequence: List[tuple[str, int, int, int]]) -> str:
        melody_abc = ''.join([note[0] for note in sequence])
        return f"X:1<n>L:1/8<n>Q:1/8=200<n>M:4/4|: {melody_abc} :|"

    def _generate_sequence_from_abc(self, generated_melody_in_abc: str) -> List[tuple[str, int, int, int]]:
        print(f'Regenerated melody in ABC:\n{generated_melody_in_abc}')
        abc_stream = converter.parse(generated_melody_in_abc, format='abc')

        modified_sequence = []
        for element in abc_stream.flat.notesAndRests:
            if isinstance(element, note.Note):  # FIXME support rest
                print(f"Note: {element.nameWithOctave} "
                      f"(duration ql: {element.quarterLength})"
                      f"(duration: {element.duration.quarterLength})"
                      f"(element.pitch.midi: {element.pitch.midi})"
                      f"(element.volume.velocity: {element.volume.velocity})")
                reg_note = (
                    element.nameWithOctave,
                    element.pitch.midi,
                    element.volume.velocity if element.volume.velocity else 64,
                    element.duration.quarterLength
                )
                modified_sequence.append(reg_note)

        return modified_sequence
