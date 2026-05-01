# FAQ

## Is APIVAI compatible with OpenAI-style APIs?

This repository uses OpenAI-style request patterns against `https://api.apivai.com/v1`.

## Where do I get an API key?

From your APIVAI account at [apivai.com](https://apivai.com).

## Can I call APIVAI directly from browser frontend code?

Avoid exposing secret keys in browser code. Route requests through your backend whenever possible.

## What should I do if my key is exposed?

Revoke or rotate the key immediately and replace it in all environments.

## Why are examples using placeholder values?

To keep credentials out of source control and make templates safe to copy.

## Which model should I use?

Model availability can change. Check current APIVAI documentation before deploying.
