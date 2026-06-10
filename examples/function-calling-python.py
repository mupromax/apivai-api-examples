#!/usr/bin/env python3
"""Function calling (tool use) via the OpenAI SDK against APIVAI.

Shows the standard two-step flow: the model returns a tool call, you run the tool,
then send the result back for a final answer.

    pip install openai
"""

import json
import os
from openai import OpenAI

API_KEY = os.getenv("APIVAI_API_KEY", "YOUR_APIVAI_API_KEY")
BASE_URL = os.getenv("APIVAI_BASE_URL", "https://api.apivai.com/v1")
MODEL = os.getenv("APIVAI_MODEL", "claude-sonnet-4-6")

TOOLS = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]


def get_weather(city: str) -> dict:
    # Stub — replace with a real API call.
    return {"city": city, "temp_c": 21, "conditions": "clear"}


def main() -> None:
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    messages = [{"role": "user", "content": "What's the weather in Tokyo?"}]

    first = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
    choice = first.choices[0].message

    if not choice.tool_calls:
        print(choice.content)
        return

    messages.append(choice)
    for call in choice.tool_calls:
        args = json.loads(call.function.arguments)
        result = get_weather(**args)
        messages.append({
            "role": "tool",
            "tool_call_id": call.id,
            "content": json.dumps(result),
        })

    final = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
    print(final.choices[0].message.content)


if __name__ == "__main__":
    if API_KEY == "YOUR_APIVAI_API_KEY":
        print("Warning: set APIVAI_API_KEY before sending real requests.")
    main()
