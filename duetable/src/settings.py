from enum import Enum


class RecordingStrategy(Enum):
    NOTES = 'notes'
    TIME = 'time'


class DuetableSettings:

    def __init__(self):
        self._buffer_length = 16  # used if recording_strategy = RecordingStrategy.NOTES
        self._buffer_time = 16.0  # used if recording_strategy = RecordingStrategy.TIME, in seconds
        self._recording_strategy = RecordingStrategy.NOTES
        self._record_when_playing = True
        self._append_to_play_buffer = False

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
