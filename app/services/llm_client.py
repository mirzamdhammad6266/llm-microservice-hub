from typing import List


class LLMClient:
    """
    Placeholder LLM client.

    In a real deployment, this class would wrap calls to providers such as:
    - OpenAI (gpt-4.x)
    - Anthropic Claude
    - Groq
    - Self-hosted / custom LLMs

    The interface is intentionally simple so it can be swapped later without
    changing the API routes.
    """

    async def generate_reply(self, message: str) -> str:
        # TODO: Replace with a call to a real LLM provider.
        # For portfolio/demo purposes we return a deterministic, friendly reply.
        return f"Thanks for your message: '{message}'. This is a demo LLM response."

    async def generate_embedding(self, text: str) -> List[float]:
        # TODO: Replace with a real embeddings endpoint from an LLM provider.
        # Here we just create a fake, deterministic embedding based on char codes.
        base_values = [float(ord(c) % 97) / 100.0 for c in text[:8]]
        # Pad / trim to fixed length for demo
        while len(base_values) < 8:
            base_values.append(0.0)
        return base_values[:8]


# Single shared client instance
llm_client = LLMClient()
