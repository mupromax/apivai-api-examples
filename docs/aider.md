# Aider with APIVAI

Aider reads an OpenAI-compatible base URL and key from environment variables, so it works with
APIVAI without extra configuration.

## Environment variables

```bash
export OPENAI_API_BASE="https://api.apivai.com/v1"
export OPENAI_API_KEY="YOUR_APIVAI_API_KEY"
```

PowerShell:

```powershell
$env:OPENAI_API_BASE="https://api.apivai.com/v1"
$env:OPENAI_API_KEY="YOUR_APIVAI_API_KEY"
```

## Run

```bash
aider --model claude-sonnet-4-6
```

Use a model ID returned by `GET /v1/models`. For routine edits a cheaper model is usually
enough; switch to a stronger model only for harder changes.

## Pick a model

```bash
curl https://api.apivai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

## Troubleshooting

- `401` — key not exported in the shell that launched Aider.
- `404` — base URL missing `/v1` or has it twice.
- `model_not_found` — the model isn't in the current `/v1/models` response.

See also [`cline.md`](./cline.md), [`cursor.md`](./cursor.md), and
[`openai-compatible-endpoint.md`](./openai-compatible-endpoint.md).
