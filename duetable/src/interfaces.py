class AudioToMidi:

    def convert(self, input_file_name, output_file_name):
        """
        Converts audio file to midi file

        :param input_file_name:
        :param output_file_name:
        :return:
        """
        raise NotImplemented()

    def convert_from_buffer(self, samples_buffer, **kwargs) -> (str, int):
        """
        Converts audio buffer to midi note and velocity.

        :param samples_buffer:
        :return: Midi note no and velocity
        """
        raise NotImplemented()

    def _log(self, message):
        print(f"audio-to-midi: {message}")
