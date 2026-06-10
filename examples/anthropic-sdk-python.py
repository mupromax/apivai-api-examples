#!/usr/bin/env python3
"""Message using the official Anthropic Python SDK pointed at APIVAI.

APIVAI also exposes an Anthropic-compatible endpoint (/v1/messages), so the
official `anthropic` SDK works by overriding base_url. Note the Anthropic SDK
appends `/v1/messages` itself, so base_url is the host root WITHOUT `/v1`.

    pip install anthropic
"""

import os
from anthropic import Anthropic

API_KEY = os.getenv("APIVAI_API_KEY", "YOUR_APIVAI_API_KEY")
# The Anthropic SDK adds /v1/messages, so strip a trailing /v1 from APIVAI_BASE_URL.
BASE_URL = os.getenv("APIVAI_BASE_URL", "https://api.apivai.com/v1").removesuffix("/v1")
MODEL = os.getenv("APIVAI_MODEL", "claude-sonnet-4-6")


def main() -> None:
    client = Anthropic(api_key=API_KEY, base_url=BASE_URL)
    msg = client.messages.create(
        model=MODEL,
        max_tokens=512,
        system="You are a concise technical assistant.",
        messages=[{"role": "user", "content": "Explain API gateways in 2 sentences."}],
    )
    print("".join(block.text for block in msg.content if block.type == "text"))


if __name__ == "__main__":
    if API_KEY == "YOUR_APIVAI_API_KEY":
        print("Warning: set APIVAI_API_KEY before sending real requests.")
    main()
