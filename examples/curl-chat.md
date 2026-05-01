# cURL Chat Example

Use this request format to call APIVAI's OpenAI-compatible chat completions endpoint.

## Endpoint

`POST https://api.apivai.com/v1/chat/completions`

## Example Request

```bash
curl -X POST "https://api.apivai.com/v1/chat/completions" \
  -H "Authorization: Bearer YOUR_APIVAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {"role": "system", "content": "You are a concise technical assistant."},
      {"role": "user", "content": "Explain API gateways in 2 sentences."}
    ],
    "temperature": 0.2
  }'
```

## Security Notes

- Do not paste real API keys into shared terminals, screenshots, or public docs.
- Prefer environment variables in local development and secret managers in production.
