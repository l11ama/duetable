from typing import List

from settings import DuetableSettings


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


class MidiBufferRegenerator:

    def regenerate_sequence(self, sequence: List[tuple[str, int, int, int]], settings: DuetableSettings) -> List[tuple[str, int, int, int]]:
        """
        Regenerate sequence from midi buffer

        :param sequence: List of tuple [midi_str, midi_note, midi_velocity, midi_time]
        :param settings: Duetable settings
        :return: same structure as input
        """
        raise NotImplemented()


class MidiBufferPostTransformation:

    def transform(self, sequence: List[tuple[str, int, int, int]]) -> List[tuple[str, int, int, int]]:
        """
        Regenerate sequence from midi buffer after main regeneration
        Which post transformation is subject of main configurattion
        :param sequence:
        :return:
        """
        raise NotImplemented()
