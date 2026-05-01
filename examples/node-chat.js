/**
 * Minimal chat completion example using APIVAI (OpenAI-compatible).
 * Requires Node.js 18+ for built-in fetch.
 */

const apiKey = process.env.APIVAI_API_KEY || "YOUR_APIVAI_API_KEY";
const baseUrl = process.env.APIVAI_BASE_URL || "https://api.apivai.com/v1";
const model = process.env.APIVAI_MODEL || "YOUR_MODEL_NAME";

async function main() {
  const response = await fetch(`${baseUrl}/chat/completions`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model,
      messages: [
        { role: "system", content: "You are a concise technical assistant." },
        { role: "user", content: "Explain API gateways in 2 sentences." },
      ],
      temperature: 0.2,
    }),
  });

  if (!response.ok) {
    const errText = await response.text();
    throw new Error(`HTTP ${response.status}: ${errText}`);
  }

  const data = await response.json();
  console.log(data.choices?.[0]?.message?.content ?? "No content returned.");
}

if (apiKey === "YOUR_APIVAI_API_KEY") {
  console.warn("Warning: set APIVAI_API_KEY before sending real requests.");
}
if (model === "YOUR_MODEL_NAME") {
  console.warn("Warning: set APIVAI_MODEL to a model returned by GET /models.");
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
