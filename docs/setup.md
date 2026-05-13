# Setup Guide

This guide walks through the local setup needed to run the APIVAI examples in this repository.

- APIVAI website: [https://apivai.com/](https://apivai.com/)
- Documentation: [https://apivai.com/docs](https://apivai.com/docs)
- OpenAI-compatible API guide: [https://apivai.com/openai-compatible-api](https://apivai.com/openai-compatible-api)
- Base URL used in examples: `https://api.apivai.com/v1`

## Prerequisites

- An APIVAI API key from your account.
- Network access to `https://api.apivai.com/v1`.
- Python 3.9+ for the Python example.
- Node.js 18+ for the Node.js example.
- cURL for shell-based testing.

## 1) Configure environment variables

Set your API key and endpoint before running examples.

macOS/Linux:

```bash
export APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
export APIVAI_BASE_URL="https://api.apivai.com/v1"
export APIVAI_MODEL="YOUR_MODEL_NAME"
```

PowerShell:

```powershell
$env:APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
$env:APIVAI_BASE_URL="https://api.apivai.com/v1"
$env:APIVAI_MODEL="YOUR_MODEL_NAME"
```

## 2) Discover a model name

Before running chat examples, call `GET /v1/models` and choose a model name returned for your account.

```bash
curl -s "$APIVAI_BASE_URL/models" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json"
```

Then update `APIVAI_MODEL` with a returned model name.

## 3) Run the Python example

```bash
python3 -m pip install requests
python3 examples/python-chat.py
```

## 4) Run the Node.js example

```bash
node examples/node-chat.js
```

## 5) Run the cURL example

See [`../examples/curl-chat.md`](../examples/curl-chat.md).

## Troubleshooting

- `401 Unauthorized`: Verify the API key and the `Authorization: Bearer <key>` header.
- `404 Not Found`: Confirm that the base URL includes `/v1`.
- Model errors: refresh the model list with `GET /v1/models` and use a returned model name.
- `429 Too Many Requests`: slow down requests and retry with backoff.
- `5xx`: retry after a short delay and keep timestamps or request identifiers when available.

For additional questions, see [`faq.md`](./faq.md). For repeatable endpoint checks, see [`testing.md`](./testing.md).
