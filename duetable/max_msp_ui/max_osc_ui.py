import logging

from pythonosc import dispatcher
from pythonosc import osc_server

from audio_to_midi_aub import AudioToMidiWithAubio
from duetable import Duetable
from regenerators import HttpMuptRegenerator, MarkovChainRegenerator, MuptWithMarkovChainRegenerator
from settings import DuetableSettings, RecordingStrategy

settings = DuetableSettings()

# settings.buffer_length = 12
settings.buffer_time = 4.0
settings.recording_strategy = RecordingStrategy.TIME
settings.record_when_playing = False
settings.append_to_play_buffer = False

settings.upper_meter = 4
settings.lower_meter = 4
settings.bpm = 60

settings.n_bars = 2
settings.temperature = 1.0
settings.model_size = "large"
settings.mel_key = "C"

settings.loop_playback = False

regenerator = HttpMuptRegenerator()
# regenerator=MuptWithMarkovChainRegenerator()

transformers = [
 #   FixedRangeTransformer(2, 4)
]


def regenerator_handler(unused_addr, args, value):
    global regenerator
    if value == 0:
        regenerator = HttpMuptRegenerator()
    elif value == 1:
        regenerator = MarkovChainRegenerator()
    elif value == 2:
        regenerator = MuptWithMarkovChainRegenerator()
    else:
        logging.error("Bad regenerator")


dispatcher = dispatcher.Dispatcher()
dispatcher.map("/RegeneratorNo", regenerator_handler, "RegeneratorType")

ip = "127.0.0.1"  # Localhost
port = 12345  # Port to listen on

server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
print(f"Serving on {server.server_address}")


duetable = Duetable(
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
duetable.start()
duetable.run()

server.serve_forever()
