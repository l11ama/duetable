from pprint import pprint
from typing import List

from music21 import converter, note

from duetable.midi_utils import MIDI_NO_TO_ABC
from duetable.settings import DuetableSettings


def generate_abc_from_sequence(sequence: List[tuple[str, int, int, int]], settings: DuetableSettings) -> str:
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
            (note_name, midi_no, midi_velocity, midi_duration, midi_duration_to_abc_length(lower_meter)))

    if len(bars[len(bars) - 1]) != upper_meter:
        last_bar = bars[len(bars) - 1]
        for i in range(upper_meter - len(last_bar)):
            last_bar.append(('z', -1, 0, 0, midi_duration_to_abc_length(lower_meter)))

    # abc header
    abc_notation = f"X: 1\nL: 1/{settings.lower_meter}\n" \
                   f"Q: 1/4={settings.bpm}\nM: 4/4\nK: {settings.mel_key}\n"

    for bar in bars:
        abc_notation += "| "
        for note_name, midi_number, midi_velocity, midi_duration, note_duration in bar:
            abc_note = MIDI_NO_TO_ABC.get(midi_number, "z")  # Use 'z' (rest) if note is not found
            abc_length = note_duration
            # abc_notation += f"{abc_note}{abc_length} "
            abc_notation += f"{abc_note} "
    abc_notation += "|"

    return abc_notation  # .replace("\n", "\\n")


def midi_duration_to_abc_length(duration):
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


def generate_sequence_from_abc(generated_melody_in_abc: str) -> List[tuple[str, int, int, int]]:
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

    print(f"Sequence from ABC:")
    pprint(modified_sequence)
    return modified_sequence
