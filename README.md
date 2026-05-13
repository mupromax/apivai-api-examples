# APIVAI API Examples

Developer-focused examples for calling APIVAI with OpenAI-compatible request patterns. The repository keeps each example intentionally small so you can inspect the request shape, confirm credentials, and adapt the code to your own application.

- APIVAI website: [https://apivai.com/](https://apivai.com/)
- Product documentation: [https://apivai.com/docs](https://apivai.com/docs)
- OpenAI-compatible API guide: [https://apivai.com/openai-compatible-api](https://apivai.com/openai-compatible-api)
- Claude API proxy notes: [https://apivai.com/claude-api-proxy](https://apivai.com/claude-api-proxy)
- Pricing: [https://apivai.com/pricing](https://apivai.com/pricing)

Default API base URL used by these examples:

```text
https://api.apivai.com/v1
```

## What this repository is for

Use this repository when you want to:

- Check that your APIVAI API key and network path are configured correctly.
- See minimal Python, Node.js, and cURL requests before integrating a full SDK or application.
- Verify model names with `GET /v1/models` instead of hardcoding a value.
- Keep example code simple enough to copy into a local prototype and then replace with your own error handling, logging, and configuration.

This repository is not a production application framework. Treat it as a set of small connectivity and request-format examples.

## Example entry points

| Runtime | File | Purpose |
| --- | --- | --- |
| Python | [`examples/python-chat.py`](./examples/python-chat.py) | Sends a chat completion request from a small Python script. |
| Node.js | [`examples/node-chat.js`](./examples/node-chat.js) | Sends a chat completion request with the built-in Node.js `fetch` API. |
| cURL | [`examples/curl-chat.md`](./examples/curl-chat.md) | Shows a shell-based request that is useful for quick endpoint testing. |
| Python streaming | [`examples/python-streaming.py`](./examples/python-streaming.py) | Reads streamed chat-completion chunks from APIVAI. |
| Node.js streaming | [`examples/node-streaming.js`](./examples/node-streaming.js) | Reads streamed chat-completion chunks with built-in Node.js APIs. |
| Models cURL | [`examples/models-list-curl.md`](./examples/models-list-curl.md) | Lists available models before setting `APIVAI_MODEL`. |

## Tooling notes

- **Claude Code:** You can use the examples as a starting point for local agent workflows that need an OpenAI-compatible endpoint. For Claude-specific workflows, check whether your tool expects OpenAI-compatible or Anthropic-compatible settings. See the APIVAI Claude API proxy page for current endpoint guidance: [https://apivai.com/claude-api-proxy](https://apivai.com/claude-api-proxy).
- **Cursor:** Use the same API key, base URL, and model-discovery approach described below when configuring editor or agent tooling that accepts OpenAI-compatible settings. Refer to [APIVAI docs](https://apivai.com/docs) for current configuration details.

## Requirements

Before running examples, make sure you have:

- An APIVAI API key from your account.
- Network access to `https://api.apivai.com/v1`.
- One of the following local runtimes:
  - Python 3.9+ for `examples/python-chat.py`.
  - Node.js 18+ for `examples/node-chat.js`.
  - `curl` for `examples/curl-chat.md`.

## Quick start

### 1) Set environment variables

All examples read these environment variables:

- `APIVAI_API_KEY`: your secret API key.
- `APIVAI_BASE_URL`: defaults to `https://api.apivai.com/v1` when not set in supported examples.
- `APIVAI_MODEL`: a model name returned for your account.

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

### 2) Discover available models

Model availability can vary by account and over time. Start by calling:

```text
GET https://api.apivai.com/v1/models
```

Example:

```bash
curl -s "$APIVAI_BASE_URL/models" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json"
```

Set `APIVAI_MODEL` to a model name returned by that response.

### 3) Run an example

```bash
python3 examples/python-chat.py
```

```bash
node examples/node-chat.js
```

For cURL, follow [`examples/curl-chat.md`](./examples/curl-chat.md).

## Common errors / troubleshooting

- `401 Unauthorized`: Confirm that `APIVAI_API_KEY` is set, has no extra spaces, and is sent as `Authorization: Bearer <key>`.
- `404 Not Found`: Check that `APIVAI_BASE_URL` includes `/v1` and that the endpoint path is correct.
- `model_not_found` or similar model errors: call `GET /v1/models` again and use a returned model name.
- `429 Too Many Requests`: Reduce request rate and retry with exponential backoff.
- `5xx` responses: retry after a short delay and capture any request identifiers or timestamps for support/debugging.
- Empty or malformed responses: verify that the request body is valid JSON and that `Content-Type: application/json` is present.

For a longer setup walkthrough, see [`docs/setup.md`](./docs/setup.md). For testing commands, see [`docs/testing.md`](./docs/testing.md). For common questions, see [`docs/faq.md`](./docs/faq.md).

Additional developer guides:

- [`docs/openai-compatible-endpoint.md`](./docs/openai-compatible-endpoint.md) explains the OpenAI-compatible base URL, request shape, and streaming behavior.
- [`docs/claude-code.md`](./docs/claude-code.md) maps APIVAI environment variables to Claude Code-style OpenAI-compatible settings.
- [`docs/cursor.md`](./docs/cursor.md) outlines editor configuration checks for Cursor-style tools.
- [`docs/troubleshooting.md`](./docs/troubleshooting.md) provides status-code and streaming debugging steps.

## Security notes

- Never commit real API keys, tokens, or account identifiers.
- Do not expose secret keys in browser or mobile client code; route requests through a server you control.
- Prefer environment variables, a local `.env` file excluded from Git, or a managed secrets store.
- Rotate keys immediately if they are pasted into logs, screenshots, issues, pull requests, or chat messages.
- Review logs before sharing them publicly; request and response bodies may contain sensitive user data.

## Repository structure

```text
.
├── README.md
├── .env.example
├── examples/
│   ├── python-chat.py
│   ├── node-chat.js
│   ├── curl-chat.md
│   ├── python-streaming.py
│   ├── node-streaming.js
│   └── models-list-curl.md
├── docs/
│   ├── setup.md
│   ├── faq.md
│   ├── testing.md
│   ├── openai-compatible-endpoint.md
│   ├── claude-code.md
│   ├── cursor.md
│   └── troubleshooting.md
└── .github/
    └── ISSUE_TEMPLATE/
```

## License

See [LICENSE](./LICENSE).
