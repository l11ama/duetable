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
  * NOTES_ONCE - recording only once till amount of notes is reached and equal to `buffer_length`
  * TIME_ONCE - recording only once till amount of time is reached and equal to `buffer_time`
* `record_when_playing` - if the system should record when playing
* `append_to_play_buffer` - if set will append to newly detected notes to previous ones
* `upper_meter` - upper meter for the regenerated melody
* `lower_meter` - lower meter for the regenerated melody 
* `bpm` - tempo for the regenerated melody
* `regenerator` - specify method for regenerating recorded midi notes, possible values are:
  * `HttpMuptRegenerator` - regenerates melody using MUPT API
  * `MuptWithMarkovChainRegenerator` - first regeneration is executed with MUTP API and all other iterations with MarkovChain
  * `MarkovChainRegenerator` - regenerates melody using MarkovChain
  * `DummyRegenerator` - returns the same melody as input
* `n_bars` - number of bars to generate with Mupt API
* `temperature` - temperature for melody generation with Mupt API
* `model_size` - LLM model type for Mupt API, possible values: `small`, `large`
* `loop_playback` - if set will loop the playback of the regenerated melody (to disable Question-Answer melody style)
* `transformers` - list of transformers to apply on the input melody after regeneration, possible values are:
  * `RandomMuteTransformer` - mute random notes in the melody, accept function to determine probability of muting
  * `SimpleTransposeTransformer` - transpose melody note by random number of semitones, accept function to determine range of transposition 
  * `SimpleTimeTransformer` - change duration time of the note by random factor, accept function to determine range of time change 
  * `MidiRangeTransformer` - clip midi range of the melody, accept from to midi values 
  * `FixedRangeTransformer` - creates a correlation between Input data and output, pitch-wise
  * `ApproachNotesTransformer` - creates an approach note for each note in melody
* `converter` - plugin responsible for audio-to-midi conversion, possible values are:
  * `AudioToMidiWithEssentia` - uses Essentia for audio-to-midi conversion (!not fully implemented yet!)
  * `AudioToMidiWithAubio` - uses Aubio for audio-to-midi conversion
  * `AudioToMidiWithBasicPitch` - uses BasicPitch for audio-to-midi conversion (!uses temporary files because lib does not support buffers, requires better implementation!)
  * `AudioToMidiDummy` - no midi detection, returns random notes
* `device_name` - name of the audio input device, default: 'MacBook Pro Microphone'
* `open_output` - method for setting up output midi device, possible to route to many devices at once

Low level settings:

* `frames_per_buffer` - frames per buffer for audio-to-midi conversion and audio in, default 512
* `sample_rate` - sample rate for audio-to-midi conversion and audio in, default 44100
* `win_s` - window size for audio-to-midi conversion, default 1024
* `hop_s` - hop size for audio-to-midi conversion and audio in, default 128

# Realtime midi detection

We have implemented three different Audio To Midi wrappers with usage of API from Essentia, Aubio and Basic Pitch (Spotify).
Essentia and Basic Pitch are not good for realtime applications. Which one to use is subject of configuration. Default is: `AudioToMidiWithAubio`

Example configuration for stream input signal to audio:
```python
settings = DuetableSettings()
settings.buffer_length = 4
app = Duetable(
    converter=AudioToMidiWithAubio(down_sample=1),
    settings=settings,
    # device_name="U46",
    regenerator=HttpMuptRegenerator()
)
app.read()
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