import os
from argparse import Namespace

import numpy as np
import torch
import yaml

from miditoolkit import MidiFile

from duetable.models.getmusic.modeling.build import build_model
from duetable.models.getmusic.utils.io import load_yaml_config
from duetable.models.getmusic.utils.midi import Instrument, F, encoding_to_MIDI, inst_to_row
from duetable.models.getmusic.engine.logger import Logger
from duetable.models.getmusic.engine.solver import Solver
from duetable.models.getmusic.utils.misc import merge_opts_to_config


class GetMusicHelper:

    def __init__(self):
        with open("duetable/models/getmusic/configs/infer.yaml") as f:
            config = yaml.safe_load(f)
        os.makedirs(config['log_dir'], exist_ok=True)
        self.args = Namespace(**config)
        self.args.local_rank = 0
        self.args.ngpus_per_node = 1
        if torch.cuda.is_available():
            self.args.device = f'cuda:{self.args.local_rank}'
        else:
            self.args.device = 'cpu'
        self.args.world_size = 1
        self.args.node_rank = 0
        self.args.global_rank = self.args.local_rank + self.args.node_rank * self.args.ngpus_per_node
        self.args.distributed = self.args.world_size > 1
        self.logger = Logger(self.args)
        self.solver = self.load_model(self.args, self.logger)

    @staticmethod
    def validate_conditional_instruments(
            midi_obj: MidiFile,
            conditional_instruments: list[Instrument] = None
    ) -> tuple[np.ndarray, list[str]]:
        """
        Validate the midi file
        Args:
            midi_obj: MidiFile object
            conditional_instruments: list of the specific instruments to condition

        Returns:
            conditional track and condition instruments
        """
        conditional_track = np.array([False, False, False, False, False, False, True])
        condition_inst = []
        # conditional_programs = None
        #
        # if conditional_instruments:
        #     conditional_programs = [inst.value for inst in conditional_instruments]

        for track in midi_obj.instruments:

            # if conditional_programs and track.program not in conditional_programs:
            #     continue

            if track.program == 80:
                conditional_track[0] = True
                condition_inst.append('80')
            if track.program == 32:
                conditional_track[1] = True
                condition_inst.append('32')
            if track.is_drum:
                conditional_track[2] = True
            if track.program == 25:
                conditional_track[3] = True
                condition_inst.append('25')
            if track.program == 0 and not track.is_drum:
                conditional_track[4] = True
                condition_inst.append('0')
            if track.program == 48:
                conditional_track[5] = True
                condition_inst.append('48')

        if len(condition_inst) == 0:
            raise ConditionalException("Midi file has no track to condition")

        if conditional_instruments:
            for inst in conditional_instruments:
                if str(inst.value) not in condition_inst:
                    raise ConditionalException(f"{inst.name} instrument is not found in midi file")

        return conditional_track, condition_inst

    @staticmethod
    def get_content_track(instrument: Instrument) -> tuple[np.ndarray, int]:
        """
        Get content track
        Args:
            instrument: Instrument enum

        Returns:
            content track and instrument index
        """
        content_track = np.array([False, False, False, False, False, False, False])
        instrument_idx = inst_to_row[str(instrument.value)]
        content_track[instrument_idx] = True

        return content_track, instrument_idx

    @staticmethod
    def load_model(args: Namespace, logger: Logger) -> Solver:
        config = load_yaml_config('duetable/models/getmusic/configs/exp.yaml')
        config = merge_opts_to_config(config, None)

        global tokens_to_ids
        global ids_to_tokens
        global empty_index
        global pad_index

        with open(config['solver']['vocab_path'], 'r') as f:
            tokens = f.readlines()

            for id, token in enumerate(tokens):
                token, freq = token.strip().split('\t')
                tokens_to_ids[token] = id
                ids_to_tokens.append(token)
            pad_index = tokens_to_ids['<pad>']
            empty_index = len(ids_to_tokens)

        model = build_model(config, args)

        dataloader_info = None

        solver = Solver(config=config, args=args, model=model, dataloader=dataloader_info, logger=logger,
                        is_sample=True)
        assert args.load_path is not None
        solver.resume(path=args.load_path)

        return solver

    def inference_song(
            self, midi_obj: MidiFile,
            conditional_track: np.ndarray,
            content_track: np.ndarray,
            condition_inst: list[str],
            params = None
    ) -> MidiFile:
        """
        Inference song
        Args:
            midi_obj: MidiFile object
            conditional_track: conditional track
            content_track: content track
            condition_inst: condition instrument programs
            params: inference parameters
        Returns:
            New MidiFile object with generated track
        """
        x, tempo, not_empty_pos, condition_pos, pitch_shift, tpc, ticks_per_beat, have_cond = F(
            midi_obj,
            conditional_track,
            content_track,
            condition_inst,
            self.args.chord_from_single,
            params
        )

        if not have_cond:
            raise ConditionalException('chord error')

        oct_line = self.solver.infer_sample(x, tempo, not_empty_pos, condition_pos, use_ema=self.args.no_ema, params=params)

        data = oct_line.split(' ')

        oct_final_list = []
        for start in range(3, len(data), 8):
            if 'pad' not in data[start] and 'pad' not in data[start + 1]:
                pitch = int(data[start][:-1].split('-')[1])
                if data[start - 1] != '<2-129>' and data[start - 1] != '<2-128>':
                    pitch -= pitch_shift
                data[start] = '<3-{}>'.format(pitch)  # re-normalize
                oct_final_list.append(' '.join(data[start - 3:start + 5]))

        oct_final = ' '.join(oct_final_list)
        new_midi_obj = encoding_to_MIDI(oct_final, tpc, self.args.decode_chord, ticks_per_beat)

        return new_midi_obj


class ConditionalException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
