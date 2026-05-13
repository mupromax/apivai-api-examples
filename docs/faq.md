# FAQ

## Is APIVAI compatible with OpenAI-style APIs?

These examples use OpenAI-compatible request patterns against `https://api.apivai.com/v1`. For the current API surface, see the APIVAI documentation at [https://apivai.com/docs](https://apivai.com/docs) and the OpenAI-compatible API guide at [https://apivai.com/openai-compatible-api](https://apivai.com/openai-compatible-api).

## Where do I get an API key?

Create or manage keys from your APIVAI account at [https://apivai.com/](https://apivai.com/).

## How do I choose a model?

Call `GET /v1/models` with your API key and select a model name returned for your account. Avoid hardcoding model names from older notes or screenshots because availability may change.

## Can I use these examples with Claude-related tooling?

The README includes a short Claude Code entry point. For current Claude API proxy guidance, refer to [https://apivai.com/claude-api-proxy](https://apivai.com/claude-api-proxy).

## Can I configure Cursor or other editor agents?

If a tool supports OpenAI-compatible configuration, use the same base URL, API key, and model-discovery flow shown in this repository. Check [https://apivai.com/docs](https://apivai.com/docs) for current service details before relying on a specific setup.

## Can I call APIVAI directly from browser frontend code?

Do not expose secret API keys in browser code. Route requests through a backend service you control, then enforce your own authentication, authorization, rate limiting, and logging policies.

## What should I do if my key is exposed?

Revoke or rotate the key immediately, remove it from logs or source control if possible, and update every environment that used the old key.

## Why do examples use placeholder values?

Placeholders keep credentials out of source control and make the examples safer to copy. Replace `YOUR_APIVAI_API_KEY` and `YOUR_MODEL_NAME` only in your local environment or secrets manager.

## Where can I review pricing?

See the current pricing page at [https://apivai.com/pricing](https://apivai.com/pricing). Avoid assuming that local examples reflect account limits, billing behavior, or model availability.
