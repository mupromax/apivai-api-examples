/**
 * Streaming chat completion example using APIVAI (OpenAI-compatible).
 * Requires Node.js 18+ for built-in fetch and Web Streams support.
 */

const apiKey = process.env.APIVAI_API_KEY || "YOUR_APIVAI_API_KEY";
const baseUrl = process.env.APIVAI_BASE_URL || "https://api.apivai.com/v1";
const model = process.env.APIVAI_MODEL || "YOUR_MODEL_NAME";

function extractContent(chunk) {
  const choice = chunk?.choices?.[0];
  const content = choice?.delta?.content;
  return typeof content === "string" ? content : "";
}

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
        { role: "user", content: "Write a three-item API testing checklist." },
      ],
      temperature: 0.2,
      stream: true,
    }),
  });

  if (!response.ok) {
    const errText = await response.text();
    throw new Error(`HTTP ${response.status}: ${errText}`);
  }

  if (!response.body) {
    throw new Error("Streaming response body is not available.");
  }

  const decoder = new TextDecoder();
  let buffer = "";

  for await (const chunk of response.body) {
    buffer += decoder.decode(chunk, { stream: true });
    const lines = buffer.split("\n");
    buffer = lines.pop() || "";

    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed || !trimmed.startsWith("data:")) {
        continue;
      }

      const data = trimmed.replace(/^data:\s*/, "");
      if (data === "[DONE]") {
        process.stdout.write("\n");
        return;
      }

      try {
        const parsed = JSON.parse(data);
        const text = extractContent(parsed);
        if (text) {
          process.stdout.write(text);
        }
      } catch (err) {
        console.error(`\nSkipping non-JSON stream chunk: ${data}`);
      }
    }
  }

  process.stdout.write("\n");
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
