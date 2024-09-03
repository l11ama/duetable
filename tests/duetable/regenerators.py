from duetable.abc_utils import generate_sequence_from_abc
from duetable.regenerators import MuptRegenerator
from duetable.duetable import DuetableSettings

gen = MuptRegenerator()

abc_seq = """
X: 1
M: 4/4
L: 1/8
| ^d' f g |
"""
settings = DuetableSettings()

settings.upper_meter = 4
settings.lower_meter = 4
settings.bpm = 120

settings.n_bars = 2
settings.temperature = 1.
settings.model_size = "small"
settings.mel_key = "Dm"

settings.loop_playback = False

gen.regenerate_sequence(generate_sequence_from_abc(abc_seq), settings)