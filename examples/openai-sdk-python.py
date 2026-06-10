#!/usr/bin/env python3
"""Chat completion using the official OpenAI Python SDK pointed at APIVAI.

APIVAI exposes an OpenAI-compatible endpoint, so the official `openai` SDK works
unchanged — you only override base_url and api_key.

    pip install openai
"""

import os
from openai import OpenAI

API_KEY = os.getenv("APIVAI_API_KEY", "YOUR_APIVAI_API_KEY")
BASE_URL = os.getenv("APIVAI_BASE_URL", "https://api.apivai.com/v1")
MODEL = os.getenv("APIVAI_MODEL", "claude-sonnet-4-6")


def main() -> None:
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a concise technical assistant."},
            {"role": "user", "content": "Explain API gateways in 2 sentences."},
        ],
        temperature=0.2,
    )
    print(resp.choices[0].message.content)


if __name__ == "__main__":
    if API_KEY == "YOUR_APIVAI_API_KEY":
        print("Warning: set APIVAI_API_KEY before sending real requests.")
    main()
