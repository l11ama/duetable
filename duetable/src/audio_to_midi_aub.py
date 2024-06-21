import aubio
from mido import MidiFile, MidiTrack, bpm2tempo, MetaMessage, second2tick, Message
from numpy import median, diff

from interfaces import AudioToMidi
from midi_utils import MIDI_DATA_BY_NO


class AudioToMidiWithAubio(AudioToMidi):
    def __init__(self, down_sample=2, sample_rate=44100, win_s=1024, hop_s=128):
        """
        Converts Audio to Midi using aubio library

        :param down_sample: sample downgrade factor, default is 2
        :param sample_rate: sampling rate, default is 44100
        :param win_s: fast fourier transformation window size, default is 1024
        :param hop_s: hop size between windows
        """
        self.down_sample = down_sample
        self.sample_rate = sample_rate // down_sample
        self.win_s = win_s // down_sample
        self.hop_s = hop_s // down_sample

        note_detector_method = "default"
        self._log(f"Note detector method: {note_detector_method}")
        self.notes_detector = aubio.notes(note_detector_method, self.win_s, self.hop_s, self.sample_rate)

    def convert(self, input_file_name, output_file_name):
        self._log(f"Converting {input_file_name} to {output_file_name}")
        self._log(f"Using samplerate {self.sample_rate}")

        source = aubio.source(input_file_name, self.sample_rate, self.hop_s)
        self._log(f"Processing {source.channels} channels, "
                  f"duration: {source.duration/self.sample_rate/self.down_sample} seconds, "
                  f"hops: {source.hop_size}")

        detected_tempo_in_bpm = self._detect_tempo(source)
        self._log(f"Detected tempo: {detected_tempo_in_bpm} BPM")
        source.seek(0)  # set source to beginning of the file

        midi_tempo = bpm2tempo(detected_tempo_in_bpm)
        midi_file = MidiFile()
        track = MidiTrack()
        midi_file.tracks.append(track)
        track.append(MetaMessage('set_tempo', tempo=midi_tempo))
        track.append(MetaMessage('time_signature', numerator=4, denominator=4))  # FIXME simplification

        total_frames = 0
        last_time = 0
        delta = 0
        off_note = None

        while True:
            samples, read = source()

            note_detection_result = self.notes_detector(samples)
            midi_note, velocity, midi_note_to_turn_off = note_detection_result
            midi_note = int(midi_note)
            velocity = int(velocity)
            midi_note_to_turn_off = int(midi_note_to_turn_off)

            if midi_note != 0:
                delta = self._frames2tick(
                    total_frames, midi_tempo,
                ) - last_time

                self._log(f"Detected note: {midi_note}/{MIDI_DATA_BY_NO[midi_note]['name']}, "
                          f"velocity: {velocity}, "
                          f"note to turn off: {midi_note_to_turn_off}, "
                          f"time->{delta}")

                if off_note:
                    track.append(
                        Message(
                            'note_off',
                            # note=off_note,
                            velocity=127,  # FIXME ?
                            time=delta
                        )
                    )

                track.append(
                    Message(
                        'note_on',
                        note=midi_note,
                        velocity=velocity,
                        time=delta
                    )
                )

                off_note = midi_note
                last_time = self._frames2tick(
                    total_frames,
                    midi_tempo,
                )

            total_frames += read
            if read < self.hop_s:
                track.append(
                    Message(
                        'note_off',
                        note=off_note,
                        # velocity=127,
                        time=delta
                    )
                )
                break

        source.close()
        midi_file.save(output_file_name)

    def convert_from_buffer(self, samples_buffer, **kwargs) -> (int, int):
        note_detection_result = self.notes_detector(samples_buffer)
        midi_note, velocity, midi_note_to_turn_off = note_detection_result
        midi_note = int(midi_note)
        velocity = int(velocity)
        return midi_note, velocity

    def _detect_tempo(self, source):
        tempo_detector_method = "specdiff"
        tempo_detector = aubio.tempo(tempo_detector_method, self.win_s, self.hop_s, self.sample_rate)

        beats = []
        while True:
            samples, read = source()

            is_beat = tempo_detector(samples)
            if is_beat:
                this_beat = tempo_detector.get_last_s()
                beats.append(this_beat)

            if read < self.hop_s:
                break

        tempo_in_bpm = 0
        if len(beats) > 1:
            tempo_in_bpm = median(60./diff(beats))

        return tempo_in_bpm

    def _frames2tick(self, frames, tempo, ticks_per_beat=480):
        sec = frames / float(self.sample_rate)
        result = int(second2tick(sec, ticks_per_beat, tempo)/self.down_sample)  # FIXME 2 ??
        print(f"sec={sec}, result={result}, tempo={tempo}")
        return result


# audio_2_midi = AudioToMidiWithAubio()
# audio_2_midi.convert('../audio_files/test_piano-full-notes.wav', './test_piano-full-notes.mid')
# audio_2_midi.convert('../audio_files/test_piano-half-notes.wav', './test_piano-half-notes.mid')
# audio_2_midi.convert('../audio_files/MonophonicGuitarSignal.wav', './MonophonicGuitarSignal.mid')
