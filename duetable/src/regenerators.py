from typing import List

import requests
from music21 import converter, note

from duetable.src.interfaces import MidiBufferRegenerator
from duetable.src.midi_utils import MIDI_NO_TO_ABC
from duetable.src.settings import DuetableSettings


class DummyRegenerator(MidiBufferRegenerator):

    def regenerate_sequence(self, sequence: List[tuple[str, int, int, int]], settings: DuetableSettings) -> List[tuple[str, int, int, int]]:
        return sequence


class HttpMuptRegenerator(MidiBufferRegenerator):

    def __init__(self):
        self._url = "http://92.38.241.195:2345/generate"
        self._http_request_session = requests.Session()

    def regenerate_sequence(self, sequence: List[tuple[str, int, int, int]], settings: DuetableSettings) -> List[tuple[str, int, int, int]]:
        request_headers = {"Accept": "application/json", "Content-Type": "application/json"}

        json_payload = {
            "prefix": self._generate_abc_from_sequence(sequence, settings),
            "n_bars": 4,
            "temperature": 0.7,
            "n_samples": 5,
            # "model": "small"
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
            generated_melody = mupt_json_response['content']['melody']
            return self._generate_sequence_from_abc(generated_melody)

        except Exception as e:
            print(f'ERROR: Error from mupt regenerator: {e}')
            print(f'WARNING: regenerator failed, returning original sequence.')
            return sequence

    def _generate_abc_from_sequence(self, sequence: List[tuple[str, int, int, int]], settings: DuetableSettings) -> str:
        upper_meter = settings.upper_meter
        lower_meter = settings.lower_meter
        bars = []
        for note_name, midi_no, midi_velocity, midi_duration in sequence:
            if len(bars) > 0:
                curr_bar = bars[len(bars) - 1]
            else:
                curr_bar = []
                bars.append(curr_bar)

            if len(curr_bar) == upper_meter:
                curr_bar = []
                bars.append(curr_bar)

            curr_bar.append(
                (note_name, midi_no, midi_velocity, midi_duration, self._midi_duration_to_abc_length(lower_meter)))

        if len(bars[len(bars) - 1]) != upper_meter:
            last_bar = bars[len(bars) - 1]
            for i in range(upper_meter - len(last_bar)):
                last_bar.append(('z', 0, 0, 0, self._midi_duration_to_abc_length(lower_meter)))

        # abc header
        abc_notation = f"X: 1\nT: Duetable detected score\nL: 1/{settings.lower_meter}\n" \
                       f"Q: 1/4={settings.bpm}\nM: 4/4\nK: C\n"

        for bar in bars[:-2]:
            abc_notation += "| "
            for note_name, midi_number, midi_velocity, midi_duration, note_duration in bar:
                abc_note = MIDI_NO_TO_ABC.get(midi_number, "z")  # Use 'z' (rest) if note is not found
                abc_length = note_duration
                abc_notation += f"{abc_note}{abc_length} "
        # abc_notation += "|"

        return abc_notation.replace("\n", "<n>")

    # def _generate_abc_from_sequence(sequence: List[tuple[str, int, int, int]], settings: DuetableSettings) -> str:
    #     melody_abc = ''.join([note[0] for note in sequence])
    #     return f"X:1<n>L:1/8<n>Q:1/8=200<n>M:4/4|: {melody_abc} :|"

    def _midi_duration_to_abc_length(self, duration):
        if duration == 1:
            return "1/8"
        elif duration == 2:
            return "1/4"
        elif duration == 4:
            return "1/2"
        elif duration == 8:
            return "1"
        # Add more mappings as needed
        else:
            return "1/4"  # Default to quarter note if unknown

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
