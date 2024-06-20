import random
from pprint import pprint
from typing import List, Set


class MarkovRegenerator:
    def get_states(self, melody_score: List[tuple[str, int, int, int]]) -> List[int]:
        return sorted(set([item[1] for item in melody_score]))

    def find_all_after(self, state_note: int, melody_score: List[tuple[str, int, int, int]]) -> List[tuple[str, int, int, int]]:
        all = []
        for idx, note in enumerate(melody_score):
            midi_name, midi_no, midi_velocity, midi_duration = note
            if midi_no == state_note:
                if idx + 1 == len(melody_score):
                    all.append(melody_score[0])
                else:
                    all.append(melody_score[idx + 1])
        return all

    def create_stats_for_possible_notes(self, all_possible_notes: List[tuple[str, int, int, int]]):
        unique_notes: Set[int] = set([item[1] for item in all_possible_notes])
        all_possible_notes_mid = [item[1] for item in all_possible_notes]
        occurrences = {}
        for unique_note in unique_notes:
            occurrences[unique_note] = all_possible_notes_mid.count(unique_note)

        probabilities = {}
        total = sum(occurrences.values())
        for note, occurrence in occurrences.items():
            prob = occurrence / total
            probabilities[note] = prob

        ranges = {}
        prob_keys = probabilities.keys()
        total = 0
        for idx, note in enumerate(prob_keys):
            prob = probabilities[note]
            ranges[note] = {
                "min": total,
                "max": total + prob
            }
            total = total + prob

        return occurrences, probabilities, ranges

    def regenerate(self, melody: List[tuple[str, int, int, int]]) -> List[tuple[str, int, int, int]]:
        chain = {}
        states = self.get_states(melody)
        for state in states:
            all_possible_notes_after = self.find_all_after(state, melody)

            if state not in chain:
                chain[state] = {}
            chain[state]['all_possible_notes_after'] = all_possible_notes_after
            occurrences, probabilities, ranges = self.create_stats_for_possible_notes(all_possible_notes_after)
            chain[state]['occurrences'] = occurrences
            chain[state]['probabilities'] = probabilities
            chain[state]['ranges'] = ranges

        pprint(chain)

        selected_midi_no: int = states[random.randint(0, len(states) - 1)]
        system_random = random.SystemRandom()
        new_melody = []
        for step in range(0, len(melody)):
            new_melody.append([melody_item for melody_item in melody if melody_item[1] == selected_midi_no][0])
            r = system_random.random()
            selected_midi_no = [note for note, ra in chain[selected_midi_no]['ranges'].items() if ra['max'] > r > ra['min']][0]

        print(f' input melody={melody}')
        print(f'output melody={new_melody}')
        return new_melody
