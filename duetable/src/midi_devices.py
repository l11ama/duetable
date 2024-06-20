import mido


def log_input_output_devices():
    onn = mido.get_output_names()
    print(f'all available outputs: {onn}')

    inn = mido.get_input_names()
    print(f'all available inputs: {inn}')


midi_devices = []


def open_output(output_device_name):
    try:
        midi_devices.append(mido.open_output(output_device_name))
    except Exception as e:
        print(f'warn: could not open {output_device_name} MIDI output port!')


def play_note_in_midi_devices(note):
    if len(midi_devices) == 0:
        return

    if note[0] != 'z':
        msg = mido.Message(
            'note_on',
            channel=0,
            note=note[1],
            velocity=127 if note[2] > 127 else note[2],
            time=note[3],
        )

        for midi_device in midi_devices:
            midi_device.send(msg)
