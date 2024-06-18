class DuetableSettings:

    def __init__(self):
        self._buffer_length = 16

    @property
    def buffer_length(self):
        return self._buffer_length

    @buffer_length.setter
    def buffer_length(self, value):
        self._buffer_length = value
