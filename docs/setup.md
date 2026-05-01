# Setup Guide

This guide helps you run APIVAI OpenAI-compatible examples locally.

- Website: [apivai.com](https://apivai.com)
- Base URL used in examples: `https://api.apivai.com/v1`

## Prerequisites

- An APIVAI API key
- Python 3.9+ (for Python example)
- Node.js 18+ (for Node example)
- cURL

## 1) Configure API key

Set your key as an environment variable.

```bash
export APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
```

PowerShell:

```powershell
$env:APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
```

## 2) Run Python example

```bash
python3 -m pip install requests
python3 examples/python-chat.py
```

## 3) Run Node.js example

```bash
node examples/node-chat.js
```

## 4) Run cURL example

See [../examples/curl-chat.md](../examples/curl-chat.md).

## Troubleshooting

- `401 Unauthorized`: Verify your API key and `Authorization` header.
- `429 Too Many Requests`: Retry with backoff.
- `5xx`: Retry after a short delay and log request IDs where available.

For additional help, see [faq.md](./faq.md).
