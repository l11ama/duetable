from pprint import pprint

import essentia.standard as estd
import mido

from interfaces import AudioToMidi


class AudioToMidiWithEssentia(AudioToMidi):

    def __init__(self, sample_rate=44100.0, win_s=2048, hop_s=128):
        """
        Converts Audio to Midi using essentia library

        :param down_sample: sample downgrade factor, default is 2
        :param sample_rate: sampling rate, default is 44100
        :param win_s: fast fourier transformation window size, default is 1024
        :param hop_s: hop size between windows
        """
        self.sample_rate = sample_rate
        self.win_s = win_s
        self.hop_s = hop_s

    def convert(self, input_file_name, output_file_name):
        loader = estd.EqloudLoader(filename=input_file_name, sampleRate=self.sample_rate)
        audio = loader()
        self._log(f"Duration of the audio sample [sec]: {len(audio)/self.sample_rate}")

        # Extract the pitch curve
        # PitchMelodia takes the entire audio signal as input (no frame-wise processing is required).

        pitch_extractor = estd.PredominantPitchMelodia(frameSize=self.win_s, hopSize=self.hop_s)
        pitch_values, pitch_confidence = pitch_extractor(audio)

        self._log("Pitch values:")
        pprint(pitch_values)
        self._log("Pitch confidence:")
        pprint(pitch_confidence)

        onsets, durations, notes = estd.PitchContourSegmentation(hopSize=self.hop_s)(pitch_values, audio)
        self._log(f"MIDI notes: {notes}")
        self._log(f"MIDI note onsets: {onsets}")
        self._log(f"MIDI note durations: {durations}")

        # Compute onsets and offsets for all MIDI notes in ticks.
        # Relative tick positions start from time 0.
        offsets = onsets + durations
        silence_durations = list(onsets[1:] - offsets[:-1]) + [0]

        PPQ = 960  # Pulses per quarter note.
        BPM = 120  # Assuming a default tempo in Ableton to build a MIDI clip.  #ADD tempo detection.
        midi_tempo = mido.bpm2tempo(BPM)  # Microseconds per beat.

        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)

        # track.append(MetaMessage('set_tempo', tempo=midi_tempo))
        # track.append(MetaMessage('time_signature', numerator=4, denominator=4))  # FIXME simplification

        for note, onset, duration, silence_duration in zip(list(notes), list(onsets), list(durations), silence_durations):
            track.append(mido.Message('note_on', note=int(note), velocity=64,
                                      time=int(mido.second2tick(duration, PPQ, midi_tempo))))
            track.append(mido.Message('note_off', note=int(note),
                                      time=int(mido.second2tick(silence_duration, PPQ, midi_tempo))))

        mid.save(output_file_name)


# audio_2_midi = AudioToMidiWithEssentia()
# audio_2_midi.convert('../audio_files/test_piano-full-notes.wav', './test_piano-full-notes-ess.mid')
