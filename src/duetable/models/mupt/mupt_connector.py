import logging
import random
import requests
import torch

from typing import Optional
from transformers import AutoModelForCausalLM, AutoTokenizer
from duetable.models.mupt.processing import decode, validate_abc


class BaseMuptConnector:

    def generate_new_abc_score(
            self, abc_score: str,
            n_bars: int = 4,
            temperature: float = 0.7,
            n_samples: int = 5,
            model: str = "small"
    ) -> Optional[str]:
        raise NotImplementedError()


class MuptConnector(BaseMuptConnector):

    MODEL_MAP = {
        "small": "m-a-p/MuPT-v1-8192-190M",
        "large": "m-a-p/MuPT_v1_8192_1.3B"
    }

    def __init__(self):
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

        self.tokenizer = AutoTokenizer.from_pretrained("m-a-p/MuPT-v1-8192-190M", trust_remote_code=True, use_fast=False)
        self.model = AutoModelForCausalLM.from_pretrained("m-a-p/MuPT-v1-8192-190M").eval().half().to(self.device)

    def generate_new_abc_score(
            self,
            prefix: str,
            n_bars: int = 4,
            temperature: float = 0.7,
            n_samples: int = 5,
            model: str = "small"
    ) -> Optional[str]:
        assert model == "small", "For local inference only small model is recommended"

        # Preprocess the input
        prefix = prefix.replace("\n", "<n>")  # replace "\n" with "<n>"
        prefix = prefix.replace(":|", "|")

        inputs = self.tokenizer(prefix, return_tensors="pt").to(self.device)

        # Generate text
        outputs = self.model.generate(
            inputs.input_ids,
            max_length=inputs.input_ids.shape[1] + n_bars * 32,
            temperature=temperature,
            num_return_sequences=n_samples,
            do_sample=True
        )

        outputs = [self.tokenizer.decode(outputs[i]) for i in range(outputs.shape[0])]

        correct_outputs = []
        for output in outputs:
            print(output)
            try:

                res = decode(output, n_bars=n_bars)
                res = res.replace('<n>', '\n')
                res = res.replace('|:', '|')
                res = res.replace(']', '')
                eos_split = res.split('<eos>')
                if len(eos_split) > 0:
                    res = eos_split[0]

                if validate_abc(res):
                    logging.debug("Valid")
                    correct_outputs.append(res)
            except:
                pass

        if not correct_outputs:
            logging.error("All model outputs are wrong. Please try again.")
            return None

        abc_notation = random.choice(correct_outputs)

        return abc_notation


class HttpMuptConnector(BaseMuptConnector):

    def __init__(self):
        self._url = "http://92.38.241.195:2345/generate"
        self._http_request_session = requests.Session()

    def generate_new_abc_score(
            self, abc_score: str,
            n_bars: int = 4,
            temperature: float = 0.7,
            n_samples: int = 5,
            model: str = "small"
    ) -> Optional[str]:
        request_headers = {"Accept": "application/json", "Content-Type": "application/json"}

        json_payload = {
            "prefix": abc_score,
            "n_bars": n_bars,
            "temperature": temperature,
            "n_samples": n_samples,
            "model": model
        }
        print('Querying mupt with: ', json_payload)

        try:
            response = self._http_request_session.post(
                url=self._url,
                json=json_payload,
                headers=request_headers,
                timeout=10
            )

            if response.status_code != 200:
                return None

            mupt_json_response = response.json()
            generated_melody = mupt_json_response['content']['melody']
            return generated_melody

        except Exception as e:
            print(f'ERROR: Error from mupt regenerator: {e}')
            return None
