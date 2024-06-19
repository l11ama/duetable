import mido


def _log_input_output_devices():
    onn = mido.get_output_names()
    print(f'all available outputs: {onn}')

    inn = mido.get_input_names()
    print(f'all available inputs: {inn}')


_log_input_output_devices()


output_device = 'Elektron Model:Cycles'

_elektron_outport = None
try:
    _elektron_outport = mido.open_output(output_device)
except Exception as e:
    print(f'warn: could not open {output_device} MIDI output port!')
    elektron_outport = None


def get_elektron_outport():
    return _elektron_outport
