# APIVAI API Examples

Practical examples for using **APIVAI** as an OpenAI-compatible API gateway.

- Website: [apivai.com](https://apivai.com)
- Base URL: `https://api.apivai.com/v1`

This repository is designed for developers who want to quickly test chat completions using:

- Python
- Node.js
- cURL

## Overview

APIVAI provides an OpenAI-compatible interface so you can reuse familiar client patterns while pointing requests to APIVAI endpoints.

This repo includes:

- Minimal runnable chat examples in `examples/`
- Setup instructions in `docs/setup.md`
- Common troubleshooting and usage guidance in `docs/faq.md`

## Quick Start

1. Get an API key from your APIVAI account at [apivai.com](https://apivai.com).
2. Set your API key as an environment variable.
3. Run one of the examples.

### 1) Set your API key

**macOS / Linux**

```bash
export APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
```

**Windows (PowerShell)**

```powershell
$env:APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
```

### 2) Run examples

- Python: `python3 examples/python-chat.py`
- Node.js: `node examples/node-chat.js`
- cURL: see `examples/curl-chat.md`

## Repository Structure

```text
.
├── README.md
├── examples/
│   ├── python-chat.py
│   ├── node-chat.js
│   └── curl-chat.md
└── docs/
    ├── setup.md
    └── faq.md
```

## Security Notes

- Never commit API keys to Git.
- Never expose API keys in frontend/browser code.
- Use environment variables or a secure secret manager.
- Rotate keys immediately if they are exposed.

## Compatibility Notes

Examples in this repository target OpenAI-style chat completion workflows against:

`https://api.apivai.com/v1`

Refer to [APIVAI](https://apivai.com) documentation for the latest model and endpoint details.

## License

See [LICENSE](./LICENSE).
