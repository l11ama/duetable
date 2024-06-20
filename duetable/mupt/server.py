import logging
from typing import re

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import random

from processing import decode, validate_abc
import logging

logging.basicConfig(level=logging.DEBUG)
app = FastAPI(debug=True)

# Load the model and tokenizer
tokenizer_large = AutoTokenizer.from_pretrained("m-a-p/MuPT_v1_8192_1.3B", trust_remote_code=True, use_fast=False)
model_large = AutoModelForCausalLM.from_pretrained("m-a-p/MuPT_v1_8192_1.3B").eval().half().cuda()

tokenizer_small = AutoTokenizer.from_pretrained("m-a-p/MuPT-v1-8192-190M", trust_remote_code=True, use_fast=False)
model_small = AutoModelForCausalLM.from_pretrained("m-a-p/MuPT-v1-8192-190M").eval().half().cuda()


class TextGenerationRequest(BaseModel):
    prefix: str
    n_bars: int = 3
    temperature = 1.0
    n_samples = 8
    model = "large"


@app.post("/generate/")
async def generate_text(request: TextGenerationRequest):
    # Preprocess the input
    prefix = request.prefix.replace("\n", "<n>")  # replace "\n" with "<n>"
    prefix = prefix.replace("<n>T: Duetable detected score", '')

    prefix = prefix.replace(":|", "|")

    if request.model == 'large':
        tokenizer = tokenizer_large
        model = model_large
    else:
        tokenizer = tokenizer_small
        model = model_small

    inputs = tokenizer(prefix, return_tensors="pt").to(model.device)

    # Generate text
    outputs = model.generate(
        inputs.input_ids,
        max_length=inputs.input_ids.shape[1] + request.n_bars * 16,
        temperature=request.temperature,
        num_return_sequences=request.n_samples,
        do_sample=True
    )

    outputs = [tokenizer.decode(outputs[i]) for i in range(outputs.shape[0])]

    correct_outputs = []
    for output in outputs:
        print(output)
        try:
            res = decode(output, n_bars=request.n_bars).replace('<n>', '\n')
            res = res.replace('|:', '\n')
            res = res.replace(']', '')

            print(res)
            if validate_abc(res):
                logging.debug("Valid")
                correct_outputs.append(res)
        except:
            pass

    if len(correct_outputs) == 0:
        raise HTTPException(status_code=500, detail="All model outputs are wrong. Please try again.")
    abc_notation = random.choice(correct_outputs)

    return {"melody": abc_notation}
