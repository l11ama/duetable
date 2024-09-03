import random
import time

from music21 import scale

from duetable.interfaces import AudioToMidi


class AudioToMidiDummy(AudioToMidi):

    def __init__(self):
        self._notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
        self._default_scale_root_note = 'c'
        self._scales = ['major', 'minor', 'harmonic_minor', 'melodic_minor']
        self._default_scale = 'major'

    def convert_from_buffer(self, samples_buffer, **kwargs) -> (int, int):
        """
        Create random midi note and velocity.

        :param samples_buffer:
        :param kwargs:
            scale_root_note: str, default c
            scale_type: str
        :return:
        """
        scale_root_note = kwargs.get('scale_root_note', self._default_scale_root_note)
        if scale_root_note not in self._notes:
            print(f'WARN: invalid root note, supported values: {self._notes}, '
                  f'set to default={self._default_scale_root_note}!')
            scale_root_note = self._default_scale_root_note

        scale_type = kwargs.get('scale_type', self._default_scale)
        if scale_type not in self._scales:
            print(f'WARN: invalid scale, supported values: {self._scales}, '
                  f'set to default={self._default_scale}!')

        s = None
        if scale_type == 'major':
            s = scale.MajorScale(scale_root_note)

        if scale_type == 'minor':
            s = scale.MinorScale(scale_root_note)

        if scale_type == 'melodic_minor':
            s = scale.MelodicMinorScale(scale_root_note)

        if scale_type == 'melodic_major':
            s = scale.HarmonicMinorScale(scale_root_note)

        if not s:
            print(f'WARN: could not create scale, default to major!')
            s = scale.MajorScale(scale_root_note)

        time.sleep(0.2)

        return s.getPitches(f'{random.choice(self._notes)}{random.randint(1, 8)}')[0].midi, random.randint(1, 127)
