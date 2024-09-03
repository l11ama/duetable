from enum import Enum


class RecordingStrategy(Enum):
    NOTES = 'notes'
    TIME = 'time'
    NOTES_ONCE = 'notes_once'
    TIME_ONCE = 'time_once'


class DuetableSettings:

    def __init__(self):
        self._buffer_length = 16  # used if recording_strategy = RecordingStrategy.NOTES
        self._buffer_time = 16.0  # used if recording_strategy = RecordingStrategy.TIME, in seconds
        self._recording_strategy = RecordingStrategy.NOTES
        self._record_when_playing = True
        self._append_to_play_buffer = False
        self._upper_meter = 4
        self._lower_meter = 4
        self._bpm = 120
        self._loop_playback = False
        self._n_bars = 2
        self._temperature = 1.0
        self._model_size = "small"
        self._mel_key = "C"
        self._sleep_with_note = True

    @property
    def buffer_time(self):
        return self._buffer_time

    @buffer_time.setter
    def buffer_time(self, value):
        self._buffer_time = value

    @property
    def buffer_length(self):
        return self._buffer_length

    @buffer_length.setter
    def buffer_length(self, value):
        self._buffer_length = value

    @property
    def recording_strategy(self):
        return self._recording_strategy

    @recording_strategy.setter
    def recording_strategy(self, value):
        self._recording_strategy = value

    @property
    def record_when_playing(self):
        return self._record_when_playing

    @record_when_playing.setter
    def record_when_playing(self, value):
        self._record_when_playing = value

    @property
    def append_to_play_buffer(self):
        return self._append_to_play_buffer

    @append_to_play_buffer.setter
    def append_to_play_buffer(self, value):
        self._append_to_play_buffer = value

    @property
    def upper_meter(self):
        return self._upper_meter

    @upper_meter.setter
    def upper_meter(self, value):
        self._upper_meter = value

    @property
    def lower_meter(self):
        return self._lower_meter

    @lower_meter.setter
    def lower_meter(self, value):
        self._lower_meter = value

    @property
    def bpm(self):
        return self._bpm

    @bpm.setter
    def bpm(self, value):
        self._bpm = value

    @property
    def loop_playback(self):
        return self._loop_playback

    @loop_playback.setter
    def loop_playback(self, value):
        self._loop_playback = value

    @property
    def n_bars(self):
        return self._n_bars

    @n_bars.setter
    def n_bars(self, value):
        self._n_bars = value

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    @property
    def model_size(self):
        return self._model_size

    @model_size.setter
    def model_size(self, value):
        self._model_size = value

    @property
    def mel_key(self):
        return self._mel_key

    @mel_key.setter
    def mel_key(self, mel_key):
        self._mel_key = mel_key

    @property
    def sleep_with_note(self):
        return self._sleep_with_note

    @sleep_with_note.setter
    def sleep_with_note(self, value):
        self._sleep_with_note = value
