# Cline with APIVAI

Cline (the VS Code agent) supports an OpenAI-compatible provider, so it works with APIVAI by
setting a base URL and key.

## Configuration

In Cline's settings:

| Field | Value |
| --- | --- |
| API Provider | OpenAI Compatible |
| Base URL | `https://api.apivai.com/v1` |
| API Key | your `APIVAI_API_KEY` |
| Model | an ID from `GET /v1/models` |

## Pick a model first

```bash
curl https://api.apivai.com/v1/models \
  -H "Authorization: Bearer $APIVAI_API_KEY"
```

Choose a model ID from the response. Agentic tools send a lot of tokens, so start Cline on a
small task to confirm routing before a large refactor.

## Troubleshooting

- `401` — key not saved in Cline's settings.
- `404` — base URL missing `/v1`, or it appears twice.
- `model_not_found` — the configured model isn't in the current `/v1/models` list.

See also [`cursor.md`](./cursor.md), [`aider.md`](./aider.md), and
[`openai-compatible-endpoint.md`](./openai-compatible-endpoint.md).
