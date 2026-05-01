#!/usr/bin/env python3
"""Minimal chat completion example using APIVAI (OpenAI-compatible)."""

import os
import requests

API_KEY = os.getenv("APIVAI_API_KEY", "YOUR_APIVAI_API_KEY")
BASE_URL = "https://api.apivai.com/v1"


def main() -> None:
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a concise technical assistant."},
            {"role": "user", "content": "Explain API gateways in 2 sentences."},
        ],
        "temperature": 0.2,
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()

    data = response.json()
    print(data["choices"][0]["message"]["content"])


if __name__ == "__main__":
    if API_KEY == "YOUR_APIVAI_API_KEY":
        print("Warning: replace YOUR_APIVAI_API_KEY before production use.")
    main()
