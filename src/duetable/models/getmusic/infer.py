from copy import deepcopy

from miditoolkit import MidiFile
from sympy.strategies import condition

from duetable.models.getmusic.helper import GetMusicHelper, ConditionalException
from duetable.models.getmusic.utils.midi import Instrument

helper = GetMusicHelper()

def main(input_file_path: str):

	midi_obj = MidiFile(input_file_path)
	instrument = Instrument.lead_melody
	conditional_track, condition_inst = helper.validate_conditional_instruments(midi_obj, [Instrument.lead_melody])
	content_track, content_inst_idx = helper.get_content_track(instrument)

	# inpainting the lead melody
	params = {
		"type": "inpaint",
		"instrument": instrument.name,
		"keep_prob": 0.75,
		"diffusion_steps": 100,
		"truncate": 256
	}
	new_midi_obj = helper.inference_song(midi_obj, conditional_track, content_track, condition_inst, params)
	target_track = None
	for track in new_midi_obj.instruments:
		if track.name == str(instrument.value):
			target_track = track
			break
	if target_track is None:
		raise RuntimeError(f"Instrument {instrument.name} not found in the output midi")

	target_track.program = instrument.value

	assert midi_obj.ticks_per_beat == new_midi_obj.ticks_per_beat
	assert midi_obj.tempo_changes[0].tempo == new_midi_obj.tempo_changes[0].tempo

	inpainted_midi_obj = deepcopy(midi_obj)
	inpainted_midi_obj.instruments = [
		track for track in inpainted_midi_obj.instruments
		if (track.program != target_track.program)
	]
	inpainted_midi_obj.instruments.append(target_track)
	inpainted_midi_obj.dump(input_file_path.replace('.mid', '_inpainted.mid'))

	# continue melody




	# melody based on accompaniment
	# conditional_track[content_inst_idx] = False
	# condition_inst = list(filter(lambda x: x != str(instrument.value), condition_inst))
	# print(content_track, conditional_track, condition_inst)
	# new_midi_obj = helper.inference_song(midi_obj, conditional_track, content_track, condition_inst)
	# target_track = None
	# for track in new_midi_obj.instruments:
	# 	if track.name == str(instrument.value):
	# 		target_track = track
	# 		break
	# if target_track is None:
	# 	raise RuntimeError(f"Instrument {instrument.name} not found in the output midi")
	#
	# assert midi_obj.ticks_per_beat == new_midi_obj.ticks_per_beat
	# assert midi_obj.tempo_changes[0].tempo == new_midi_obj.tempo_changes[0].tempo
	#
	# new_midi_obj.dump(input_file_path.replace('.mid', '_accompaniment.mid'))


if __name__ == "__main__":
	main("./MIDI Files/SynthSolo1.mid")
