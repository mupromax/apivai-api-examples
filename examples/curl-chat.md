# cURL Chat Example

Use this request format to call APIVAI chat completions.

## Environment variables

```bash
export APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
export APIVAI_BASE_URL="https://api.apivai.com/v1"
export APIVAI_MODEL="YOUR_MODEL_NAME"
```

## Check available models first

```bash
curl -s "$APIVAI_BASE_URL/models" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json"
```

Set `APIVAI_MODEL` to one of the model names returned by this endpoint.

## Chat completion request

```bash
curl -X POST "$APIVAI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "'"$APIVAI_MODEL"'",
    "messages": [
      {"role": "system", "content": "You are a concise technical assistant."},
      {"role": "user", "content": "Explain API gateways in 2 sentences."}
    ],
    "temperature": 0.2
  }'
```

## Security note

Do not commit real API keys to source control.
