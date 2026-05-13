# OpenAI-Compatible Endpoint Guide

APIVAI examples in this repository use OpenAI-compatible HTTP shapes so developers can test requests with familiar paths, headers, and JSON fields.

Default base URL:

```text
https://api.apivai.com/v1
```

Set it with `APIVAI_BASE_URL` so local scripts, CI smoke tests, and editor tools can share the same configuration.

## Required environment variables

```bash
export APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
export APIVAI_BASE_URL="https://api.apivai.com/v1"
export APIVAI_MODEL="YOUR_MODEL_NAME"
```

- `APIVAI_API_KEY` is sent as a bearer token.
- `APIVAI_BASE_URL` should include `/v1`.
- `APIVAI_MODEL` should be selected from the model list returned for your account.

## Common endpoints

| Purpose | Method and path | Notes |
| --- | --- | --- |
| List models | `GET /models` | Use this before hardcoding a model name. |
| Chat completions | `POST /chat/completions` | Sends an OpenAI-style `messages` array. |
| Streaming chat | `POST /chat/completions` with `stream: true` | Returns incremental server-sent event chunks. |

## Headers

Every authenticated JSON request should include:

```text
Authorization: Bearer $APIVAI_API_KEY
Content-Type: application/json
```

For streaming calls, clients should read the response body incrementally instead of waiting for a single JSON object.

## Chat request shape

```json
{
  "model": "YOUR_MODEL_NAME",
  "messages": [
    {"role": "system", "content": "You are a concise technical assistant."},
    {"role": "user", "content": "Return one sentence about API compatibility."}
  ],
  "temperature": 0.2
}
```

The `messages` array follows the usual chat-completion pattern: system instructions first when needed, followed by user and assistant turns.

## Streaming request shape

```json
{
  "model": "YOUR_MODEL_NAME",
  "messages": [
    {"role": "user", "content": "Write a short deployment checklist."}
  ],
  "stream": true
}
```

Streaming responses are typically delivered as lines beginning with `data:`. The stream ends when the server sends a terminal marker such as `[DONE]` or closes the response body.

## Model selection workflow

1. Call `GET $APIVAI_BASE_URL/models` with your API key.
2. Pick a model identifier returned by that response.
3. Export it as `APIVAI_MODEL`.
4. Run a small chat request before adding the model to application code.

This avoids stale model names in scripts, screenshots, or notes.

## Compatibility expectations

OpenAI-compatible means the request style is intentionally familiar, not that every parameter from every OpenAI SDK or endpoint is supported in every context. When moving an existing integration, start with the smallest request body, verify the model, then add optional parameters one at a time.

## Related examples

- [`../examples/models-list-curl.md`](../examples/models-list-curl.md)
- [`../examples/python-streaming.py`](../examples/python-streaming.py)
- [`../examples/node-streaming.js`](../examples/node-streaming.js)
- [`../examples/curl-chat.md`](../examples/curl-chat.md)
