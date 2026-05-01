# APIVAI API Examples

Minimal Python, Node.js, and cURL examples for testing APIVAI's OpenAI-compatible API.

- API base URL (default): `https://api.apivai.com/v1`

## What this repository is for

This repository provides minimal examples for:

- Python
- Node.js
- cURL

Use it to validate connectivity and request format before integrating into your own application.

## Requirements

Before running examples, make sure you have:

- An API key from your APIVAI dashboard
- Network access to `https://api.apivai.com/v1`
- One of:
  - Python 3 for `examples/python-chat.py`
  - Node.js 18+ for `examples/node-chat.js`
  - `curl` for `examples/curl-chat.md`

## Tested flow

- Get an API key from the APIVAI dashboard.
- Call `GET /v1/models` to find available model names.
- Set `APIVAI_MODEL` to one returned model name.
- Run one of the examples.

## Quick start

### 1) Set environment variables

All examples use these variables:

- `APIVAI_API_KEY`
- `APIVAI_BASE_URL` (default: `https://api.apivai.com/v1`)
- `APIVAI_MODEL` (default placeholder: `YOUR_MODEL_NAME`)

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

### 2) Discover available models first

Do not hardcode a model name that may not be available for your account.

Call:

`GET https://api.apivai.com/v1/models`

Example:

```bash
curl -s "$APIVAI_BASE_URL/models" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json"
```

Then set `APIVAI_MODEL` to one of the returned model names.

### 3) Run examples

- Python: `python3 examples/python-chat.py`
- Node.js: `node examples/node-chat.js`
- cURL: see `examples/curl-chat.md`

## Repository structure

```text
.
├── README.md
├── .env.example
├── examples/
│   ├── python-chat.py
│   ├── node-chat.js
│   └── curl-chat.md
├── docs/
│   ├── setup.md
│   ├── faq.md
│   └── testing.md
└── .github/
    └── ISSUE_TEMPLATE/
```

## Security notes

- Never commit real API keys.
- Never expose API keys in browser/frontend code.
- Use environment variables or a secrets manager.
- Rotate keys immediately if exposed.

## License

See [LICENSE](./LICENSE).
