#!/usr/bin/env python3
"""Use APIVAI from LlamaIndex via the OpenAILike LLM (OpenAI-compatible api_base).

    pip install llama-index-llms-openai-like
"""

import os
from llama_index.llms.openai_like import OpenAILike

API_KEY = os.getenv("APIVAI_API_KEY", "YOUR_APIVAI_API_KEY")
BASE_URL = os.getenv("APIVAI_BASE_URL", "https://api.apivai.com/v1")
MODEL = os.getenv("APIVAI_MODEL", "claude-sonnet-4-6")


def main() -> None:
    llm = OpenAILike(
        model=MODEL,
        api_base=BASE_URL,
        api_key=API_KEY,
        is_chat_model=True,
        temperature=0.2,
    )
    print(llm.complete("Explain API gateways in 2 sentences."))


if __name__ == "__main__":
    if API_KEY == "YOUR_APIVAI_API_KEY":
        print("Warning: set APIVAI_API_KEY before sending real requests.")
    main()
