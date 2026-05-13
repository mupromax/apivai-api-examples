# Cursor with APIVAI

Use this guide when configuring Cursor or a similar editor assistant that supports OpenAI-compatible API settings.

Default APIVAI base URL:

```text
https://api.apivai.com/v1
```

## Environment values

Keep the same values across terminal examples and editor configuration:

```bash
export APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
export APIVAI_BASE_URL="https://api.apivai.com/v1"
export APIVAI_MODEL="YOUR_MODEL_NAME"
```

Use a model returned by the model-list endpoint for your account.

## Preflight check

Run this before changing editor settings:

```bash
curl -s "$APIVAI_BASE_URL/models" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json"
```

If model discovery works, verify a chat completion with `examples/curl-chat.md`, `examples/python-chat.py`, or `examples/node-chat.js`.

## Editor configuration mapping

| Cursor-style setting | Value to use |
| --- | --- |
| API provider type | OpenAI-compatible or custom OpenAI endpoint |
| API key | Your `APIVAI_API_KEY` value |
| Base URL | `https://api.apivai.com/v1` |
| Model | A model from `GET /models` |

If the editor lets you test the model from the settings screen, use a short prompt first. If it does not, keep a terminal open with the same environment variables and use the repository examples as a baseline.

## Practical checks

- Confirm the editor process can read the environment or has the key entered in its settings.
- Confirm the base URL includes `/v1` exactly once.
- Confirm the selected model appears in the current model list.
- Start with a small prompt before using agent workflows that make multiple tool calls.
- Keep secret keys out of workspace files and screenshots.

## When requests fail

Compare the editor behavior with a terminal request from the same machine:

```bash
node examples/node-chat.js
```

If the terminal example works but the editor fails, the issue is likely in editor configuration, environment loading, or model selection. If both fail, use [`troubleshooting.md`](./troubleshooting.md) to inspect status codes and request shape.
