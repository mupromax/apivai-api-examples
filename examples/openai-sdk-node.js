/**
 * Chat completion using the official OpenAI Node SDK pointed at APIVAI.
 *
 * APIVAI exposes an OpenAI-compatible endpoint, so the official `openai` package
 * works unchanged — you only set baseURL and apiKey.
 *
 *   npm install openai
 */

import OpenAI from "openai";

const apiKey = process.env.APIVAI_API_KEY || "YOUR_APIVAI_API_KEY";
const baseURL = process.env.APIVAI_BASE_URL || "https://api.apivai.com/v1";
const model = process.env.APIVAI_MODEL || "claude-sonnet-4-6";

async function main() {
  const client = new OpenAI({ apiKey, baseURL });
  const resp = await client.chat.completions.create({
    model,
    messages: [
      { role: "system", content: "You are a concise technical assistant." },
      { role: "user", content: "Explain API gateways in 2 sentences." },
    ],
    temperature: 0.2,
  });
  console.log(resp.choices[0]?.message?.content ?? "No content returned.");
}

if (apiKey === "YOUR_APIVAI_API_KEY") {
  console.warn("Warning: set APIVAI_API_KEY before sending real requests.");
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
