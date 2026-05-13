#!/usr/bin/env python3
"""Streaming chat completion example using APIVAI (OpenAI-compatible)."""

import json
import os
import sys
from typing import Any

import requests

API_KEY = os.getenv("APIVAI_API_KEY", "YOUR_APIVAI_API_KEY")
BASE_URL = os.getenv("APIVAI_BASE_URL", "https://api.apivai.com/v1")
MODEL = os.getenv("APIVAI_MODEL", "YOUR_MODEL_NAME")


def extract_content(chunk: dict[str, Any]) -> str:
    """Return text content from an OpenAI-style streaming chunk."""
    choices = chunk.get("choices") or []
    if not choices:
        return ""

    delta = choices[0].get("delta") or {}
    content = delta.get("content")
    return content if isinstance(content, str) else ""


def main() -> None:
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a concise technical assistant."},
            {"role": "user", "content": "Write a three-item API testing checklist."},
        ],
        "temperature": 0.2,
        "stream": True,
    }

    with requests.post(url, headers=headers, json=payload, stream=True, timeout=60) as response:
        response.raise_for_status()

        for raw_line in response.iter_lines(decode_unicode=True):
            if not raw_line:
                continue
            if not raw_line.startswith("data:"):
                continue

            data = raw_line.removeprefix("data:").strip()
            if data == "[DONE]":
                break

            try:
                chunk = json.loads(data)
            except json.JSONDecodeError:
                print(f"\nSkipping non-JSON stream chunk: {data}", file=sys.stderr)
                continue

            text = extract_content(chunk)
            if text:
                print(text, end="", flush=True)

    print()


if __name__ == "__main__":
    if API_KEY == "YOUR_APIVAI_API_KEY":
        print("Warning: set APIVAI_API_KEY before sending real requests.", file=sys.stderr)
    if MODEL == "YOUR_MODEL_NAME":
        print("Warning: set APIVAI_MODEL to a model returned by GET /models.", file=sys.stderr)
    main()
