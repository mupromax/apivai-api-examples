# Continue.dev with APIVAI

[Continue.dev](https://continue.dev) (VS Code / JetBrains) speaks the OpenAI-compatible API
format, so it works with APIVAI by setting a custom `apiBase` and key — no custom integration.

## Configure

Edit your Continue config (`~/.continue/config.json`, or the YAML config in newer versions) and
add a model with `provider: "openai"` pointed at the APIVAI base URL:

```json
{
  "models": [
    {
      "title": "APIVAI - Claude Sonnet",
      "provider": "openai",
      "model": "claude-sonnet-4-6",
      "apiBase": "https://api.apivai.com/v1",
      "apiKey": "YOUR_APIVAI_API_KEY"
    }
  ]
}
```

Reload Continue; the model appears in the model dropdown.

## Pick a valid model

Model availability varies — list what's available instead of guessing:

```bash
curl -s https://api.apivai.com/v1/models \
  -H "Authorization: Bearer $APIVAI_API_KEY"
```

Use a returned name for the `model` field.

## Checklist

- `apiBase` ends with `/v1`.
- `provider` is `openai` (the compatible format), `apiKey` is your APIVAI key.
- The `model` matches a name from `GET /v1/models` (avoids `model_not_found`).
- Streaming should pass through as real SSE chunks so output appears token by token.

## Notes

- Use a smaller/faster model for autocomplete and a more powerful one for chat/edits to control cost.
- Keep keys out of shared configs; prefer environment variables or a local, untracked config.
