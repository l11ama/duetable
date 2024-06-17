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

* activate your virtual environment
* `pip install essentia`
* `brew install sdl2`

for PyAudio please do:

* `brew install portaudio`

