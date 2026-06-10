#!/usr/bin/env python3
"""Use APIVAI from LangChain via ChatOpenAI (OpenAI-compatible base_url).

Anything built on ChatOpenAI — chains, agents, tool calling — inherits the endpoint.

    pip install langchain-openai
"""

import os
from langchain_openai import ChatOpenAI

API_KEY = os.getenv("APIVAI_API_KEY", "YOUR_APIVAI_API_KEY")
BASE_URL = os.getenv("APIVAI_BASE_URL", "https://api.apivai.com/v1")
MODEL = os.getenv("APIVAI_MODEL", "claude-sonnet-4-6")


def main() -> None:
    llm = ChatOpenAI(base_url=BASE_URL, api_key=API_KEY, model=MODEL, temperature=0.2)
    result = llm.invoke("Explain API gateways in 2 sentences.")
    print(result.content)


if __name__ == "__main__":
    if API_KEY == "YOUR_APIVAI_API_KEY":
        print("Warning: set APIVAI_API_KEY before sending real requests.")
    main()
