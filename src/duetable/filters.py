from music21 import converter, note, articulations, interval
import random

# Read ABC notation
abc_string = """
X: 1
T: Scale
M: 4/4
L: 1/4
K: C
C D E F |
"""
score = converter.parse(abc_string, format='abc')

# Extract all notes from the score
notes = score.flatten()

# Print the original notes with durations
print("Original Notes:")
for n in notes:
    if isinstance(n, note.Note):
        print(f"{n.nameWithOctave}({n.duration.quarterLength})", end=' ')
print()

# User-controlled transposition interval for odd-indexed notes
odd_index_interval = 'm3'  # Minor third for odd-indexed notes

interval_probabilities = {
    'P1': 0.4,   # 20% probability
    'P4': 0.1,   # 20% probability
    'P5': 0.1,    # 10% probability
    'P8': 0.4
}
duration_probabilities = {
    1.0: 0.5,   # Quarter note (1.0 quarter length) with 50% probability
    0.5: 0.15,   # Eighth note (0.5 quarter length) with 30% probability
    0.25: 0.15,   # Sixteenth note (0.25 quarter length) with 20% probability
    0.125: 0.15,
    1.5: 0.1

}

# Function to get a random interval
# Function to randomly select an interval based on probabilities
def select_random_interval(interval_probabilities):
    return random.choices(list(interval_probabilities.keys()), weights=list(interval_probabilities.values()))[0]

# Function to randomly select a duration based on probabilities
def select_random_duration(duration_probabilities):
    return random.choices(list(duration_probabilities.keys()), weights=list(duration_probabilities.values()))[0]

# Manipulate each note
for n in notes:
    if isinstance(n, note.Note):
        # Randomly select an interval
        selected_interval = select_random_interval(interval_probabilities)
        n.transpose(selected_interval, inPlace=True)


# Print the manipulated notes with durations
print("Manipulated Notes:")
for n in notes:
    if isinstance(n, note.Note):
        print(f"{n.nameWithOctave}({n.duration.quarterLength})", end=' ')
print()
