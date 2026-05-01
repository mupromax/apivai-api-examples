# Testing Guide

This guide shows how to test APIVAI endpoints with environment variables.

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

Set `APIVAI_MODEL` to one of the returned model names.

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

## Security warning

- Never commit real API keys.
- Never paste real API keys into issues, pull requests, or screenshots.
