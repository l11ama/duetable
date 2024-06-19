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

# Artist configuration

Multiple parameters can be provided on runtime to configure the system. These are:
* `recording_strategy` - how the midi buffer is filled. Options are:
  * NOTES - recording till amount of notes is reached and equal to `buffer_length`
  * TIME - recording till amount of time is reached and equal to `buffer_time`
* `record_when_playing` - if the system should record the midi when playing regenerated data
* `append_to_play_buffer` - if set will append to detected notes to previous ones

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
    # device_name="U46",
    regenerator=HttpMuptRegenerator()
)
stream_2_midi.read()
```

By default data will be read from build in microphone = `'MacBook Pro Microphone'`.
To adjust please set correct `device_name`. On start, stream class log to console all possible input devices.

# MUPT API specification
Endpoint: `POST` `http://92.38.241.195:2345/generate/`

Request params:
* `prefix` - start of the melody in ABC notation
* `n_bars` - n bars after in output (Default: 2)
* `temperature` - temperature for sampling (Default: 1.)
* `n_samples` - samples to generate from (Default: 3)
* `model` - type of the model ['large', 'small'] (Default: large)
Example Request body
```
{
  "prefix": "X:1<n>L:1/8<n>Q:1/8=200<n>M:4/4|: BGdB",
  "n_bars": 4,
  "temperature": 0.7,
  "n_samples": 5,
  "model": "small"
}
```

Example Response
```
{
    "status_code": 200,
    "headers": {
        "date": "Wed, 19 Jun 2024 15:20:15 GMT",
        "server": "uvicorn",
        "content-length": "97",
        "content-type": "application/json"
    },
    "content": {
        "melody": "X:1\nL:1/8\nQ:1/8=200\nM:4/4\n BGdB Af g2 | g2 dc BG G2 | cAFA cAFA | BGdB A2 G2 |\n"
    }
}
```