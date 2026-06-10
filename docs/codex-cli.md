# Codex CLI with APIVAI

OpenAI Codex CLI talks to an OpenAI-compatible endpoint, so you can point it at APIVAI by
setting two environment variables — no other changes.

## Environment variables

Codex reads an OpenAI-style base URL and key:

```bash
export OPENAI_BASE_URL="https://api.apivai.com/v1"
export OPENAI_API_KEY="YOUR_APIVAI_API_KEY"
```

PowerShell:

```powershell
$env:OPENAI_BASE_URL="https://api.apivai.com/v1"
$env:OPENAI_API_KEY="YOUR_APIVAI_API_KEY"
```

## Pick a model

List available models and choose an ID instead of hardcoding one:

```bash
curl https://api.apivai.com/v1/models -H "Authorization: Bearer $OPENAI_API_KEY"
```

APIVAI exposes the OpenAI Responses API (`/v1/responses`) that Codex relies on, so tool calls
and streaming work as expected.

## Verify

Run a tiny task first to confirm routing:

```bash
codex "explain what this repo does in two sentences"
```

## Troubleshooting

- `401` — key missing or not exported in the shell that launched Codex.
- `404` — base URL missing `/v1` or has it twice.
- `model_not_found` — the model isn't in the current `/v1/models` response; pick a returned ID.

See also [`claude-code.md`](./claude-code.md), [`cursor.md`](./cursor.md), and
[`openai-compatible-endpoint.md`](./openai-compatible-endpoint.md).
