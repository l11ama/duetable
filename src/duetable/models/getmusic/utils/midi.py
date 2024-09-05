import math
import torch
import numpy as np
import pickle
import miditoolkit

from enum import Enum

from duetable.models.getmusic.utils.magenta_chord_recognition import infer_chords_for_sequence, _key_chord_distribution, \
    _key_chord_transition_distribution, _CHORDS, _PITCH_CLASS_NAMES, NO_CHORD


class Instrument(int, Enum):
    lead_melody = 80
    bass = 32
    drums = 128
    guitar = 25
    piano = 0
    strings = 48

inst_to_row = { '80':0, '32':1, '128':2,  '25':3, '0':4, '48':5, '129':6}
prog_to_abrv = {'0': 'P', '25': 'G', '32': 'B', '48': 'S', '80': 'M', '128': 'D'}

root_dict = {'C': 0, 'C#': 1, 'D': 2, 'Eb': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'Ab': 8, 'A': 9, 'Bb': 10, 'B': 11}
kind_dict = {'null': 0, 'm': 1, '+': 2, 'dim': 3, 'seven': 4, 'maj7': 5, 'm7': 6, 'm7b5': 7}
root_list = list(root_dict.keys())
kind_list = list(kind_dict.keys())

_CHORD_KIND_PITCHES = {
    'null': [0, 4, 7],
    'm': [0, 3, 7],
    '+': [0, 4, 8],
    'dim': [0, 3, 6],
    'seven': [0, 4, 7, 10],
    'maj7': [0, 4, 7, 11],
    'm7': [0, 3, 7, 10],
    'm7b5': [0, 3, 6, 10],
}

pos_resolution = 4 # 16  # per beat (quarter note)
bar_max = 32
velocity_quant = 4
tempo_quant = 12  # 2 ** (1 / 12)
min_tempo = 16
max_tempo = 256
duration_max = 4  # 2 ** 8 * beat
max_ts_denominator = 6  # x/1 x/2 x/4 ... x/64
max_notes_per_bar = 1  # 1/64 ... 128/64 #
beat_note_factor = 4  # In MIDI format a note is always 4 beats
deduplicate = True
filter_symbolic = False
filter_symbolic_ppl = 16
trunc_pos = 2 ** 16  # approx 30 minutes (1024 measures)
sample_len_max = 1024  # window length max
sample_overlap_rate = 1.5
ts_filter = True
pool_num = 200
max_inst = 127
max_pitch = 127
max_velocity = 127
tracks_start = [16, 144, 997, 5366, 6921, 10489]
tracks_end = [143, 996, 5365, 6920, 10488, 11858]


ts_dict = dict()
ts_list = list()
for i in range(0, max_ts_denominator + 1):  # 1 ~ 64
    for j in range(1, ((2 ** i) * max_notes_per_bar) + 1):
        ts_dict[(j, 2 ** i)] = len(ts_dict)
        ts_list.append((j, 2 ** i))
dur_enc = list()
dur_dec = list()
for i in range(duration_max):
    for j in range(pos_resolution):
        dur_dec.append(len(dur_enc))
        for k in range(2 ** i):
            dur_enc.append(len(dur_dec) - 1)

tokens_to_ids = {}
ids_to_tokens = []
pad_index = None
empty_index = None

key_profile = pickle.load(open('getmusic/utils/key_profile.pickle', 'rb'))

pos_in_bar = beat_note_factor * max_notes_per_bar * pos_resolution

chord_pitch_out_of_key_prob = 0.01
key_change_prob = 0.001
chord_change_prob = 0.5
key_chord_distribution = _key_chord_distribution(
    chord_pitch_out_of_key_prob=chord_pitch_out_of_key_prob)
key_chord_loglik = np.log(key_chord_distribution)
key_chord_transition_distribution = _key_chord_transition_distribution(
    key_chord_distribution,
    key_change_prob=key_change_prob,
    chord_change_prob=chord_change_prob)
key_chord_transition_loglik = np.log(key_chord_transition_distribution)


class Item(object):
    def __init__(self, name, start, end, vel=0, pitch=0, track=0, value=''):
        self.name = name
        self.start = start  # start step
        self.end = end  # end step
        self.vel = vel
        self.pitch = pitch
        self.track = track
        self.value = value

    def __repr__(self):
        return f'Item(name={self.name:>10s}, start={self.start:>4d}, end={self.end:>4d}, ' \
               f'vel={self.vel:>3d}, pitch={self.pitch:>3d}, track={self.track:>2d}, ' \
               f'value={self.value:>10s})\n'

    def __eq__(self, other):
        return self.name == other.name and self.start == other.start and \
            self.pitch == other.pitch and self.track == other.track


def normalize_to_c_major(e):
    def get_pitch_class_histogram(notes, use_duration=True, use_velocity=True, normalize=True):
        weights = np.ones(len(notes))
        if use_duration:
            weights *= [note[4] for note in notes]
        if use_velocity:
            weights *= [note[5] for note in notes]
        histogram, _ = np.histogram([note[3] % 12 for note in notes], bins=np.arange(
            13), weights=weights, density=normalize)
        if normalize:
            histogram /= (histogram.sum() + (histogram.sum() == 0))
        return histogram

    pitch_histogram = [i for i in e if i[2] < 128]
    if len(pitch_histogram) == 0:
        return e, True, 0

    histogram = get_pitch_class_histogram(pitch_histogram)
    key_candidate = np.dot(key_profile, histogram)
    key_temp = np.where(key_candidate == max(key_candidate))
    major_index = key_temp[0][0]
    minor_index = key_temp[0][1]
    major_count = histogram[major_index]
    minor_count = histogram[minor_index % 12]
    key_number = 0
    if major_count < minor_count:
        key_number = minor_index
        is_major = False
    else:
        key_number = major_index
        is_major = True
    real_key = key_number
    # transposite to C major or A minor
    if real_key <= 11:
        trans = 0 - real_key
    else:
        trans = 21 - real_key
    pitch_shift = trans

    e = [tuple(k + pitch_shift if j == 3 and i[2] != 128 else k for j, k in enumerate(i))
         for i in e]
    return e, is_major, pitch_shift


def t2e(x):
    assert x in ts_dict, 'unsupported time signature: ' + str(x)
    return ts_dict[x]


def e2t(x):
    return ts_list[x]


def d2e(x):
    return dur_enc[x] if x < len(dur_enc) else dur_enc[-1]


def e2d(x):
    return dur_dec[x] if x < len(dur_dec) else dur_dec[-1]


def v2e(x):
    return x // velocity_quant


def e2v(x):
    return (x * velocity_quant) + (velocity_quant // 2)


def b2e(x):
    x = max(x, min_tempo)
    x = min(x, max_tempo)
    x = x / min_tempo
    e = round(math.log2(x) * tempo_quant)
    return e


def e2b(x):
    return math.floor(2 ** (x / tempo_quant) * min_tempo)


def time_signature_reduce(numerator, denominator):
    while denominator > 2 ** max_ts_denominator and denominator % 2 == 0 and numerator % 2 == 0:
        denominator //= 2
        numerator //= 2
    while numerator > max_notes_per_bar * denominator:
        for i in range(2, numerator + 1):
            if numerator % i == 0:
                numerator //= i
                break
    return numerator, denominator


def MIDI_to_encoding(midi_obj, with_chord, condition_inst, chord_from_single):
    def time_to_pos(t):
        return round(t * pos_resolution / midi_obj.ticks_per_beat)

    notes_start_pos = [time_to_pos(j.start)
                       for i in midi_obj.instruments for j in i.notes]
    if len(notes_start_pos) == 0:
        return list()
    max_pos = max(notes_start_pos) + 1

    pos_to_info = [[None for _ in range(4)] for _ in range(
        max_pos)]
    tsc = midi_obj.time_signature_changes
    tpc = midi_obj.tempo_changes
    for i in range(len(tsc)):
        for j in range(time_to_pos(tsc[i].time), time_to_pos(tsc[i + 1].time) if i < len(tsc) - 1 else max_pos):
            if j < len(pos_to_info):
                pos_to_info[j][1] = t2e(time_signature_reduce(
                    tsc[i].numerator, tsc[i].denominator))
    for i in range(len(tpc)):
        for j in range(time_to_pos(tpc[i].time), time_to_pos(tpc[i + 1].time) if i < len(tpc) - 1 else max_pos):
            if j < len(pos_to_info):
                pos_to_info[j][3] = b2e(tpc[i].tempo)
    for j in range(len(pos_to_info)):
        if pos_to_info[j][1] is None:
            # MIDI default time signature
            pos_to_info[j][1] = t2e(time_signature_reduce(4, 4))
        if pos_to_info[j][3] is None:
            pos_to_info[j][3] = b2e(120.0)  # MIDI default tempo (BPM)
    cnt = 0
    bar = 0
    measure_length = None
    for j in range(len(pos_to_info)):
        ts = e2t(pos_to_info[j][1])
        if cnt == 0:
            measure_length = ts[0] * beat_note_factor * pos_resolution // ts[1]
        pos_to_info[j][0] = bar
        pos_to_info[j][2] = cnt
        cnt += 1
        if cnt >= measure_length:
            assert cnt == measure_length, 'invalid time signature change: pos = {}'.format(
                j)
            cnt -= measure_length
            bar += 1
    encoding = []

    for inst in midi_obj.instruments:
        for note in inst.notes:
            if time_to_pos(note.start) >= trunc_pos:
                continue

            info = pos_to_info[time_to_pos(note.start)]
            duration = d2e(time_to_pos(note.end) - time_to_pos(note.start))
            encoding.append([info[0], info[2], max_inst + 1 if inst.is_drum else inst.program, note.pitch + max_pitch +
                                                                                               1 if inst.is_drum else note.pitch,
                             duration, v2e(note.velocity), info[1], info[3]])
    if len(encoding) == 0:
        return list()

    encoding.sort()
    encoding, is_major, pitch_shift = normalize_to_c_major(encoding)

    # extract chords
    if with_chord:
        max_pos = 0
        note_items = []
        for note in encoding:
            if (0 < note[3] < 128) and (note[2] in [0, 25, 32, 48, 80]):
                if chord_from_single and (str(note[2]) not in condition_inst):
                    continue

                ts = e2t(note[6])
                measure_length = ts[0] * beat_note_factor * pos_resolution // ts[1]
                max_pos = max(
                    max_pos, measure_length * note[0] + note[1] + e2d(note[4]))
                note_items.append(Item(
                    name='On',
                    start=measure_length * note[0] + note[1],
                    end=measure_length * note[0] + note[1] + e2d(note[4]),
                    vel=e2v(note[5]),
                    pitch=note[3],
                    track=0))
        note_items.sort(key=lambda x: (x.start, -x.end))
        pos_per_chord = measure_length
        max_chords = round(max_pos // pos_per_chord + 0.5)
        if max_chords > 0:
            chords = infer_chords_for_sequence(note_items,
                                               pos_per_chord=pos_per_chord,
                                               max_chords=max_chords,
                                               key_chord_loglik=key_chord_loglik,
                                               key_chord_transition_loglik=key_chord_transition_loglik
                                               )
        else:
            chords = []

        bar_idx = 0
        for c in chords:
            if c == 'N.C.':
                bar_idx += 1
                continue
            r, k = c.split(':')
            if k == '':
                k = 'null'
            elif k == '7':
                k = 'seven'
            encoding.append((bar_idx, 0, 129, root_dict[r], kind_dict[k], 0, t2e(time_signature_reduce(4, 4)), 0))
            bar_idx += 1

        encoding.sort()

    return encoding, pitch_shift, tpc


def encoding_to_MIDI(encoding, tpc, decode_chord, ticks_per_beat):
    tmp = encoding.strip().split('<0-')[1:]

    encoding = []
    for item in tmp:
        tmp2 = item.strip()[:-1].split('> <')
        encoding.append([int(tmp2[0])] + [int(i[2:]) for i in tmp2[1:]])
    del tmp

    bar_to_timesig = [list()
                      for _ in range(max(map(lambda x: x[0], encoding)) + 1)]
    for i in encoding:
        bar_to_timesig[i[0]].append(i[6])
    bar_to_timesig = [max(set(i), key=i.count) if len(
        i) > 0 else None for i in bar_to_timesig]
    for i in range(len(bar_to_timesig)):
        if bar_to_timesig[i] is None:
            bar_to_timesig[i] = t2e(time_signature_reduce(
                4, 4)) if i == 0 else bar_to_timesig[i - 1]
    bar_to_pos = [None] * len(bar_to_timesig)
    cur_pos = 0
    for i in range(len(bar_to_pos)):
        bar_to_pos[i] = cur_pos
        ts = e2t(bar_to_timesig[i])
        measure_length = ts[0] * beat_note_factor * pos_resolution // ts[1]
        cur_pos += measure_length
    pos_to_tempo = [list() for _ in range(
        cur_pos + max(map(lambda x: x[1], encoding)))]
    for i in encoding:
        pos_to_tempo[bar_to_pos[i[0]] + i[1]].append(i[7])
    pos_to_tempo = [round(sum(i) / len(i)) if len(i) >
                                              0 else None for i in pos_to_tempo]
    for i in range(len(pos_to_tempo)):
        if pos_to_tempo[i] is None:
            pos_to_tempo[i] = b2e(120.0) if i == 0 else pos_to_tempo[i - 1]

    midi_obj = miditoolkit.midi.parser.MidiFile()
    midi_obj.ticks_per_beat = ticks_per_beat
    midi_obj.tempo_changes = tpc

    def get_tick(bar, pos):
        return (bar_to_pos[bar] + pos) * midi_obj.ticks_per_beat // pos_resolution

    midi_obj.instruments = [miditoolkit.Instrument(program=(
        0 if i == 128 else i), is_drum=(i == 128), name=str(i)) for i in range(128 + 1)]

    for i in encoding:
        start = get_tick(i[0], i[1])
        program = i[2]

        if program == 129 and decode_chord:
            root_name = root_list[i[3]]
            kind_name = kind_list[i[4]]
            root_pitch_shift = root_dict[root_name]
            end = start + get_tick(0, e2d(1))
            for kind_shift in _CHORD_KIND_PITCHES[kind_name]:
                pitch = 36 + root_pitch_shift + kind_shift
                midi_obj.instruments[1].notes.append(miditoolkit.Note(
                    start=start, end=end, pitch=pitch, velocity=e2v(20)))
        elif program != 129:
            pitch = (i[3] - 128 if program == 128 else i[3])
            if pitch < 0:
                continue
            duration = get_tick(0, e2d(i[4]))
            if duration == 0:
                duration = 1
            end = start + duration
            velocity = e2v(i[5])

            midi_obj.instruments[program].notes.append(miditoolkit.Note(
                start=start, end=end, pitch=pitch, velocity=velocity))
    midi_obj.instruments = [
        i for i in midi_obj.instruments if len(i.notes) > 0]
    cur_ts = None
    for i in range(len(bar_to_timesig)):
        new_ts = bar_to_timesig[i]
        if new_ts != cur_ts:
            numerator, denominator = e2t(new_ts)
            midi_obj.time_signature_changes.append(miditoolkit.TimeSignature(
                numerator=numerator, denominator=denominator, time=get_tick(i, 0)))
            cur_ts = new_ts
    cur_tp = None
    for i in range(len(pos_to_tempo)):
        new_tp = pos_to_tempo[i]
        if new_tp != cur_tp:
            tempo = e2b(new_tp)
            midi_obj.tempo_changes.append(
                miditoolkit.TempoChange(tempo=tempo, time=get_tick(0, i)))
            cur_tp = new_tp
    return midi_obj


def F(midi_obj, conditional_tracks, content_tracks, condition_inst, chord_from_single, params=None):
    global tokens_to_ids
    global ids_to_tokens
    global empty_index
    global pad_index

    empty_tracks = ~conditional_tracks & ~content_tracks

    conditional_tracks &= ~empty_tracks  # emptied tracks can not be condition
    conditional_tracks = torch.tensor(conditional_tracks).float()
    conditional_tracks = conditional_tracks.view(7, 1).repeat(1, 2).reshape(14, 1)
    empty_tracks = torch.tensor(empty_tracks).float()
    empty_tracks = empty_tracks.view(7, 1).repeat(1, 2).reshape(14, 1)

    if conditional_tracks[-1]:
        with_chord = True
    else:
        with_chord = False

    # try:
    encoding, pitch_shift, tpc = MIDI_to_encoding(midi_obj, with_chord, condition_inst, chord_from_single)

    if len(encoding) == 0:
        print('ERROR(BLANK)', end='')
        return None, 0

    bar_index_offset = 0

    figure_size = encoding[-1][0] * pos_in_bar + encoding[-1][1]

    pad_length = 1  # (512 - figure_size % 512)

    figure_size += pad_length

    conditional_bool = conditional_tracks.repeat(1, figure_size)

    empty_pos = empty_tracks.repeat(1, figure_size).type(torch.bool)

    datum = pad_index * torch.ones(14, figure_size, dtype=float)

    oov = 0
    inv = 0

    chord_list = []

    tempo = b2e(67)

    lead_start = 0

    idx = 0
    while idx != len(encoding) - 1:
        e = encoding[idx]

        bar = e[0]
        pos = e[1]
        inst = e[2]
        pitch = e[3]

        if inst == 80:
            tempo = e[7]
            assert tempo != 0, 'bad tempo'

        # assert e[6] == 6

        if e[2] == 129:
            row = inst_to_row[str(inst)]
            r = root_list[e[3]]
            k = kind_list[e[4]]
            datum[2 * row][pos_in_bar * bar + pos: pos_in_bar * (bar + 1) + pos] = tokens_to_ids[r]
            datum[2 * row + 1][pos_in_bar * bar + pos: pos_in_bar * (bar + 1) + pos] = tokens_to_ids[k]
            idx += 1
            continue

        chord_list = [str(e[3])]

        for f_idx in range(idx + 1, len(encoding)):
            if (encoding[f_idx][0] == bar) and (encoding[f_idx][1] == pos) and (encoding[f_idx][2] == inst):
                if encoding[f_idx][3] != pitch:
                    chord_list.append(str(encoding[f_idx][3]))
                    pitch = encoding[f_idx][3]
            else:
                break

        idx = max(idx + 1, f_idx)

        dur = e[4]
        if dur == 0:
            continue

        if not (str(inst) in inst_to_row):
            continue

        if inst == 128:
            pass

        row = inst_to_row[str(inst)]
        dur = tokens_to_ids['T' + str(e[4])]  # duration

        chord_string = ' '.join(chord_list)
        token = prog_to_abrv[str(inst)] + chord_string

        if token in tokens_to_ids:
            pitch = tokens_to_ids[token]
            assert (dur < pad_index) and (pitch > pad_index), 'pitch index is {} and dur index is {}'.format(pitch, dur)
            datum[2 * row][pos_in_bar * bar + pos] = pitch
            datum[2 * row + 1][pos_in_bar * bar + pos] = dur
            inv += 1
        else:
            oov += 1

    datum = torch.where(empty_pos, empty_index, datum)
    datum = torch.where(((datum != empty_index).float() * (1 - conditional_bool)).type(torch.bool), empty_index + 1,
                        datum)

    # datum = datum[:,:1280]
    # conditional_bool = conditional_bool[:,:1280]

    if params is not None:
        # trunc = 256
        trunc = params['truncate']
        datum = datum[:, -trunc:]
        conditional_bool = conditional_bool[:, -trunc:]

        if params['type'] == 'continue':
            datum = datum

    not_empty_pos = (torch.tensor(np.array(datum)) != empty_index).float()

    have_cond = True

    for i in range(14):
        if with_chord and conditional_tracks[i] == 1 and (
                (datum[i] == pad_index).sum() + (datum[i] == empty_index).sum()) == min(trunc, figure_size):
            have_cond = False
            break

    return (datum.unsqueeze(0), torch.tensor(tempo), not_empty_pos, conditional_bool, pitch_shift, tpc,
            midi_obj.ticks_per_beat, have_cond)
