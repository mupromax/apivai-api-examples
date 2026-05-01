# APIVAI API Examples

Practical examples for using **APIVAI** as an OpenAI-compatible API gateway.

- Website: [apivai.com](https://apivai.com)
- Base URL: `https://api.apivai.com/v1`

This repository is designed for developers who want to quickly test chat completions using:

- Python
- Node.js
- cURL

## Why this repo exists

The goal of this repo is simple: provide a fast, low-friction starting point for developers who want to call APIVAI endpoints without building a full app first.

It focuses on:

- Minimal examples you can run in minutes
- Familiar OpenAI-style request patterns
- Clear setup and troubleshooting notes

Use it as a reference for local testing, onboarding teammates, or validating API connectivity in a new environment.

## Requirements

Before running examples, make sure you have:

- An APIVAI API key
- Network access to `https://api.apivai.com/v1`
- One of the following runtimes/tools:
  - Python 3 for `examples/python-chat.py`
  - Node.js for `examples/node-chat.js`
  - `curl` for `examples/curl-chat.md`

You should also be comfortable setting environment variables in your shell.

## Overview

APIVAI provides an OpenAI-compatible interface so you can reuse familiar client patterns while pointing requests to APIVAI endpoints.

This repo includes:

- Minimal runnable chat examples in `examples/`
- Setup instructions in `docs/setup.md`
- Common troubleshooting and usage guidance in `docs/faq.md`

## Quick Start

1. Get an API key from your APIVAI account.
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

## Contributing

Contributions are welcome, especially if they keep examples simple and easier to run.

Good contributions include:

- Fixing incorrect setup or usage details
- Improving clarity in examples or docs
- Adding small, focused examples that match the existing style

Before opening a PR:

1. Keep changes scoped and easy to review.
2. Avoid adding secrets, private endpoints, or environment-specific assumptions.
3. Update docs when behavior or commands change.

## Roadmap

Near-term improvements we expect to add:

- More task-focused examples (for example, structured output or tool-calling patterns)
- Basic error-handling patterns across Python and Node.js examples
- Optional environment setup helpers for faster local onboarding

If you want a specific example, open an issue with the use case and preferred language.

## Security Notes

- Never commit API keys to Git.
- Never expose API keys in frontend/browser code.
- Use environment variables or a secure secret manager.
- Rotate keys immediately if they are exposed.

## Compatibility Notes

Examples in this repository target OpenAI-style chat completion workflows against:

`https://api.apivai.com/v1`

Refer to APIVAI documentation for the latest model and endpoint details.

## License

See [LICENSE](./LICENSE).
