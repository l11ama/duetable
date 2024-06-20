from typing import Optional

import requests


class MuptConnector:

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
