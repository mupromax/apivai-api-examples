# Testing Guide

This guide provides repeatable checks for APIVAI endpoints using environment variables. Use these commands to confirm credentials, endpoint reachability, and request formatting before moving code into an application.

## Environment variables

macOS/Linux:

```bash
export APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
export APIVAI_BASE_URL="https://api.apivai.com/v1"
export APIVAI_MODEL="YOUR_MODEL_NAME"
```

PowerShell:

```powershell
$env:APIVAI_API_KEY="YOUR_APIVAI_API_KEY"
$env:APIVAI_BASE_URL="https://api.apivai.com/v1"
$env:APIVAI_MODEL="YOUR_MODEL_NAME"
```

## 1) Test `GET /v1/models`

Use this endpoint first to discover valid model names for your account.

macOS/Linux:

```bash
curl -s "$APIVAI_BASE_URL/models" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json"
```

PowerShell:

```powershell
Invoke-RestMethod -Method GET -Uri "$env:APIVAI_BASE_URL/models" -Headers @{
  Authorization = "Bearer $env:APIVAI_API_KEY"
  "Content-Type" = "application/json"
}
```

Set `APIVAI_MODEL` to one of the returned model names before running chat-completion tests.

## 2) Test `POST /v1/chat/completions`

macOS/Linux:

```bash
curl -s -X POST "$APIVAI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $APIVAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "'"$APIVAI_MODEL"'",
    "messages": [
      {"role": "system", "content": "You are a concise technical assistant."},
      {"role": "user", "content": "Return one short sentence about API testing."}
    ]
  }'
```

PowerShell:

```powershell
$body = @{
  model = $env:APIVAI_MODEL
  messages = @(
    @{ role = "system"; content = "You are a concise technical assistant." },
    @{ role = "user"; content = "Return one short sentence about API testing." }
  )
} | ConvertTo-Json -Depth 5

Invoke-RestMethod -Method POST -Uri "$env:APIVAI_BASE_URL/chat/completions" -Headers @{
  Authorization = "Bearer $env:APIVAI_API_KEY"
  "Content-Type" = "application/json"
} -Body $body
```

## Expected result

A successful response should include generated assistant content. If the request fails, record the HTTP status, timestamp, endpoint, and sanitized response body before troubleshooting.

## Troubleshooting checks

- Confirm `APIVAI_API_KEY` is present in the shell running the command.
- Confirm `APIVAI_BASE_URL` is `https://api.apivai.com/v1` unless you intentionally use another endpoint.
- Confirm `APIVAI_MODEL` matches a model returned by `GET /v1/models`.
- Confirm the JSON body is valid and the request includes `Content-Type: application/json`.

## Security warning

- Never commit real API keys.
- Never paste real API keys into issues, pull requests, screenshots, or shared terminal logs.
- Redact prompts and responses if they include user data, account information, or internal identifiers.
