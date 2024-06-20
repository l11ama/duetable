# ======================================================
# ======================================================
# ======================================================
from duetable.src.audio_to_midi_aub import AudioToMidiWithAubio
from duetable.src.midi_devices import log_input_output_devices, open_output
from duetable.src.regenerators import HttpMuptRegenerator, MuptWithMarkovChainRegenerator, DummyRegenerator, \
    MarkovChainRegenerator
from duetable.src.settings import DuetableSettings, RecordingStrategy
from duetable.src.stream_audio_to_midi import StreamAudioToMidi

log_input_output_devices()
open_output('Elektron Model:Cycles')
open_output('Duetable Bus 1')

settings = DuetableSettings()

# ======================================================
# ====================================================== Johnathan's settings
# ======================================================

settings.buffer_length = 11
settings.buffer_time = 4.0
settings.recording_strategy = RecordingStrategy.NOTES
settings.record_when_playing = True
settings.append_to_play_buffer = False

settings.upper_meter = 4
settings.lower_meter = 4
settings.bpm = 60

settings.n_bars = 2
settings.temperature = 0.8
settings.model_size = "large"

settings.loop_playback = True

# regenerator = HttpMuptRegenerator()
# regenerator = MuptWithMarkovChainRegenerator()
regenerator = MarkovChainRegenerator()
# regenerator = DummyRegenerator()

transformers = [
    # SimpleTransposeTransformer(lambda: random.randint(-12, 12)),
    # SimpleTimeTransformer(lambda: random.randint(5, 35)/10)
    # MidiRangeTransformer(from_midi_no=26, to_midi_no=90)
]

# ====================================================== RUNNER ======================================================

stream_2_midi = StreamAudioToMidi(
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

stream_2_midi.read()
