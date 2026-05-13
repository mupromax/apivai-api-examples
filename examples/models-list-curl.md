# List APIVAI Models with cURL

Use this example to discover model names available to your account before setting `APIVAI_MODEL`.

## Environment variables

```bash
export APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
export APIVAI_BASE_URL="https://api.apivai.com/v1"
export APIVAI_MODEL="YOUR_MODEL_NAME"
```

`APIVAI_MODEL` is not required for the model-list request, but setting it after this step keeps the chat examples consistent.

## Request

```bash
curl -s "$APIVAI_BASE_URL/models" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json"
```

## Optional status output

Use `-i` when you want to see HTTP status and headers while debugging:

```bash
curl -i "$APIVAI_BASE_URL/models" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json"
```

## Next step

Pick a model identifier from the response and export it:

```bash
export APIVAI_MODEL="MODEL_FROM_RESPONSE"
```

Then run a chat or streaming example.
