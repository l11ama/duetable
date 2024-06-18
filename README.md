# duetable

A generative system which listens to an audio input, and "reacts" - plays output similar to input - and can create a "duet" between the human and the machine - similar to Continuator, but duet-able (:

## high level design

![Alt text](./docs/hld.jpg?raw=true "High level design")

## requirements

* Python 3.11
* poetry

## setup

```shell
poetry install
```

for Essentia please do:

* activate your virtual environment and from there:
* `pip install essentia`
* `brew install sdl2`
* `pip install basic-pitch`

for PyAudio please do:

* `brew install portaudio`

# Realtime midi detection

We have implemented three different Audio To Midi wrappers with usage of API from Essentia, Aubio and Basic Pitch (Spotify).
Essentia and Basic Pitch are not good for realtime applications. Which one to use is subject of configuration. Default is: `AudioToMidiWithAubio`

Example configuration for stream input signal to audio:
```python
settings = DuetableSettings()
settings.buffer_length = 4
stream_2_midi = StreamAudioToMidiWithAub(
    converter=AudioToMidiWithAubio(down_sample=1),
    settings=settings,
    # device_name="U46"
)
stream_2_midi.read()
```

By default data will be read from build in microphone = `'MacBook Pro Microphone'`.
To adjust please set correct `device_name`. On start, stream class log to console all possible input devices.
