# Claude Code with APIVAI

This note shows how to adapt the repository examples for Claude Code or similar local agent workflows when the tool accepts OpenAI-compatible endpoint settings.

Claude-specific workflows can differ by tool and provider configuration. Some tools accept OpenAI-compatible settings with `APIVAI_BASE_URL=https://api.apivai.com/v1`; Claude Code may also use Anthropic-compatible settings depending on the workflow and provider configuration. Follow APIVAI's current Claude proxy documentation when configuring Claude-specific workflows, and avoid assuming that every Claude workflow uses `/v1/chat/completions`.

The repository examples use:

```text
https://api.apivai.com/v1
```

as the default `APIVAI_BASE_URL`.

## Environment variables

Set these values in the shell that launches your local tool:

```bash
export APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
export APIVAI_BASE_URL="https://api.apivai.com/v1"
export APIVAI_MODEL="YOUR_MODEL_NAME"
```

Choose `APIVAI_MODEL` from `GET /models` rather than copying a model name from older notes.

## Verify the endpoint first

Before connecting an agent workflow, run a direct model-list request:

```bash
curl -s "$APIVAI_BASE_URL/models" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json"
```

Then run a small chat request or one of the examples in this repository. This helps separate endpoint configuration from tool-specific behavior.

## Configuration pattern

When a tool asks for OpenAI-compatible settings, map values this way:

| Tool field | APIVAI value |
| --- | --- |
| API key | `APIVAI_API_KEY` |
| Base URL | `https://api.apivai.com/v1` or your `APIVAI_BASE_URL` value |
| Model | A model returned by `GET /models` |
| Chat path | `/chat/completions` when a path is required separately |

Some tools expect a complete base URL including `/v1`; others ask for host and path separately. Avoid adding `/v1` twice.

## Recommended validation flow

1. Confirm `GET /models` works in the same shell.
2. Run `python3 examples/python-chat.py` or `node examples/node-chat.js`.
3. If you need streaming output, run `python3 examples/python-streaming.py` or `node examples/node-streaming.js`.
4. Copy the same API key, base URL, and model into the local tool configuration.
5. Start with a short prompt to verify request routing.

## Troubleshooting notes

- `401` usually means the key is missing, malformed, or not being read by the tool process.
- `404` often means the base URL is missing `/v1`, includes `/v1` twice, or uses the wrong path.
- Model errors usually mean the configured model is not in the current `GET /models` response.
- If the tool supports custom headers, confirm it sends `Authorization: Bearer <key>`.

For broader endpoint details, see [`openai-compatible-endpoint.md`](./openai-compatible-endpoint.md). For error handling, see [`troubleshooting.md`](./troubleshooting.md).
