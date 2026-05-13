# Troubleshooting APIVAI Example Requests

Use this guide when an APIVAI example does not return the response you expected. Start with environment variables, then verify the endpoint, model, request body, and network path.

## 1) Confirm local configuration

```bash
printf 'Base URL: %s\n' "${APIVAI_BASE_URL:-https://api.apivai.com/v1}"
printf 'Model: %s\n' "${APIVAI_MODEL:-not set}"
test -n "$APIVAI_API_KEY" && echo "API key is set" || echo "API key is missing"
```

The examples expect:

```bash
export APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
export APIVAI_BASE_URL="https://api.apivai.com/v1"
export APIVAI_MODEL="YOUR_MODEL_NAME"
```

Do not print real API keys in shared terminals, logs, screenshots, or issue reports.

## 2) Check model discovery

```bash
curl -i "$APIVAI_BASE_URL/models" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json"
```

If this fails, fix authentication or base URL configuration before testing chat completions.

## 3) Check a minimal chat request

```bash
curl -i -X POST "$APIVAI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "'"$APIVAI_MODEL"'",
    "messages": [
      {"role": "user", "content": "Return one short sentence."}
    ]
  }'
```

Keep the request small until the endpoint, key, and model all work.

## Status code reference

| Symptom | Common cause | What to check |
| --- | --- | --- |
| `401 Unauthorized` | Missing or invalid bearer token | Confirm `APIVAI_API_KEY` is set and sent as `Authorization: Bearer <key>`. |
| `403 Forbidden` | Key or account cannot access the requested resource | Confirm account access and try a model returned by `GET /models`. |
| `404 Not Found` | Wrong base URL or endpoint path | Confirm `APIVAI_BASE_URL` includes `/v1` and the path is `/chat/completions` or `/models`. |
| `408` or connection timeout | Network path or client timeout issue | Retry from the same shell, then test another network if needed. |
| `429 Too Many Requests` | Request rate or account limit reached | Reduce concurrency and add retry with backoff. |
| `5xx` | Server-side or upstream error | Retry after a short delay and keep timestamps for support. |

## Streaming issues

If streaming examples print nothing:

- Confirm the request body includes `"stream": true`.
- Confirm your HTTP client reads the body incrementally.
- Try the non-streaming chat example to separate streaming parsing from authentication or model issues.
- Log raw `data:` lines temporarily, but redact prompts or responses before sharing them.

If chunks appear but text is missing, inspect the JSON shape. Some chunks may only carry metadata, role changes, or finish information.

## JSON and shell quoting

Shell quoting is a frequent source of request errors. If a cURL command fails with a JSON parse error, place the body in a temporary file and send it with `--data @body.json`.

Example `body.json`:

```json
{
  "model": "YOUR_MODEL_NAME",
  "messages": [
    {"role": "user", "content": "Return one short sentence."}
  ]
}
```

Then run:

```bash
curl -i -X POST "$APIVAI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json" \
  --data @body.json
```

## What to collect before asking for help

Share only sanitized details:

- HTTP status code.
- Endpoint path, without the secret key.
- Approximate timestamp and timezone.
- Request body with sensitive prompt content removed.
- Response body with secrets and user data removed.
- Runtime and version, such as Python or Node.js.
