// Anthropic SDK (Node.js) against APIVAI's Anthropic-compatible /v1/messages endpoint.
//
// Install:  npm install @anthropic-ai/sdk
// Run:      node examples/anthropic-sdk-node.js
//
// Env:
//   APIVAI_API_KEY  - your APIVAI key
//   APIVAI_BASE_URL - defaults to https://api.apivai.com  (SDK appends /v1/messages)
//   APIVAI_MODEL    - a model name from GET /v1/models (e.g. a Claude model)

import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.APIVAI_API_KEY,
  baseURL: process.env.APIVAI_BASE_URL || "https://api.apivai.com",
});

const model = process.env.APIVAI_MODEL || "claude-sonnet-4-6";

async function main() {
  const message = await client.messages.create({
    model,
    max_tokens: 256,
    messages: [{ role: "user", content: "In one sentence, what is an OpenAI-compatible API gateway?" }],
  });
  // message.content is an array of content blocks
  const text = message.content.map((b) => (b.type === "text" ? b.text : "")).join("");
  console.log(text.trim());
}

main().catch((err) => {
  console.error("Request failed:", err?.message || err);
  process.exit(1);
});
