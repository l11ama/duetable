import tempfile
import wave

from basic_pitch.commandline_printing import file_saved_confirmation
from basic_pitch.inference import predict, build_output_path, OutputExtensions

from duetable.src.interfaces import AudioToMidi


class AudioToMidiWithSpotify(AudioToMidi):
    """
    Perform midi detection for audio buffer / file.
    Not good for real time application as is based on NN and kind of slow.
    """

    def __init__(self):
        pass

    def convert(self, input_file_name, output_file_name):
        model_output, midi_data, note_events = predict(input_file_name)

        output_file_name_slices = output_file_name.split('/')
        audio_path = output_file_name_slices[-1]
        output_directory = '/'.join(output_file_name_slices[:-1])

        midi_path = build_output_path(audio_path, output_directory, OutputExtensions.MIDI)
        midi_data.write(str(midi_path))
        file_saved_confirmation(OutputExtensions.MIDI.name, midi_path)

    def convert_from_buffer(self, samples_buffer, **kwargs) -> (str, int):
        nothing_to_return = 0, 0
        if len(samples_buffer) == 0:
            return nothing_to_return

        temp_fd, temp_filename = tempfile.mkstemp(suffix='.wav')
        with wave.open(temp_filename, 'wb') as wf:
            wf.setnchannels(kwargs.get("CHANNELS", 1))
            wf.setsampwidth(kwargs.get("SAMPWIDTH", 1))
            wf.setframerate(kwargs.get("RATE", 44100))
            wf.writeframes(samples_buffer.tobytes())

        try:
            model_output, midi_data, note_events = predict(temp_filename)
            if len(midi_data.instruments) == 0:
                print('Nothing predicted by Spotify....')
                return nothing_to_return

            print(f"instruments len: {len(midi_data.instruments)}")
            detected_data = [(md.pitch, md.velocity) for md in midi_data.instruments[0].notes]
            print(f"spotify-from-buffer: detected data={detected_data}")
        except Exception as e:
            print(f'Nothing to predict due to: {e}')
            return nothing_to_return

        return detected_data[0]  # FIXME, maybe converter should return array!? :)


# audio_2_midi = AudioToMidiWithSpotify()
# audio_2_midi.convert('../audio_files/test_piano-full-notes.wav', './test_piano-full-notes-spoti.mid')
