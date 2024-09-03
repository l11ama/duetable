# ======================================================
# ======================================================
# ======================================================
import random

from duetable.audio_to_midi_aub import AudioToMidiWithAubio
from duetable.midi_devices import log_input_output_devices, open_output
from duetable.regenerators import MuptWithMarkovChainRegenerator
from duetable.settings import DuetableSettings, RecordingStrategy
from duetable.duetable import Duetable
from duetable.transformations import RandomMuteTransformer, MidiRangeTransformer

log_input_output_devices()
open_output('Elektron Model:Cycles')
open_output('Duetable Bus 1')

settings = DuetableSettings()

# ======================================================
# ====================================================== Jerzy's settings
# ======================================================

settings.buffer_length = 8
settings.buffer_time = 4.0
settings.recording_strategy = RecordingStrategy.TIME
settings.record_when_playing = True
settings.append_to_play_buffer = False

settings.upper_meter = 7
settings.lower_meter = 8
settings.bpm = 160

settings.n_bars = 4
settings.temperature = 0.8
settings.model_size = "small"

settings.loop_playback = True

# regenerator = HttpMuptRegenerator()
regenerator = MuptWithMarkovChainRegenerator()
# regenerator = MarkovChainRegenerator()
# regenerator = DummyRegenerator()

transformers = [
    RandomMuteTransformer(lambda: random.choice([True, False, False])),
    # SimpleTransposeTransformer(lambda: random.randint(-12, 12)),
    # SimpleTimeTransformer(lambda: random.randint(5, 35)/10)
    MidiRangeTransformer(from_midi_no=26, to_midi_no=90)
]

# ====================================================== RUNNER ======================================================

duetable = Duetable(
    # midi converter
    converter=AudioToMidiWithAubio(down_sample=1),
    # hop_s=10*2048,  # set for Spotify due to natural network nature for prediction, comment out for Aubio
    # converter=AudioToMidiWithSpotify(),

    # setting
    settings=settings,

    # audio in
    # device_name="U46",

    # detected midi regenerator
    regenerator=regenerator,

    # post transformers
    transformations=transformers
)

duetable.read()