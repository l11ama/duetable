# ======================================================
# ======================================================
# ======================================================
from duetable.audio_to_midi_aub import AudioToMidiWithAubio
from duetable.midi_devices import log_input_output_devices, open_output
from duetable.regenerators import MuptRegenerator
from duetable.settings import DuetableSettings, RecordingStrategy
from duetable.duetable import Duetable

log_input_output_devices()
# open_output('Elektron Model:Cycles')
open_output('Duetable Bus 1')

settings = DuetableSettings()

# ======================================================
# ====================================================== Johnathan's settings
# ======================================================

settings.buffer_length = 12
settings.buffer_time = 4.0
settings.recording_strategy = RecordingStrategy.TIME
settings.record_when_playing = False
settings.append_to_play_buffer = False

settings.upper_meter = 4
settings.lower_meter = 4
settings.bpm = 120

settings.n_bars = 2
settings.temperature = 0.8
settings.model_size = "small"
settings.mel_key = "Gmin"

settings.loop_playback = False

regenerator = MuptRegenerator()
# regenerator=MuptWithMarkovChainRegenerator(),

transformers = [
]

# ====================================================== RUNNER ======================================================

stream_2_midi = Duetable(
    # midi converter
    converter=AudioToMidiWithAubio(down_sample=1),
    # hop_s=10*2048,  # set for Spotify due to natural network nature for prediction, comment out for Aubio
    # converter=AudioToMidiWithSpotify(),

    # setting
    settings=settings,

    # audio in
    device_name="U46",

    # detected midi regenerator
    regenerator=regenerator,

    # post transformers
    transformations=transformers
)

stream_2_midi.read()
