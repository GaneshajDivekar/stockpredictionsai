import httpx

LLM_API_URL = "https://api.mistral.ai/v1/chat/completions"  # Replace with actual endpoint
LLM_API_KEY = "YlbbZFOFK7IXz4HiR8FO4zHxBzJDJOSM"  # Replace with your API key

async def analyze_news(news_text):
    # Example payload, adjust as per Mistral API
    payload = {
        "model": "mistral-tiny",
        "messages": [
            {"role": "system", "content": "You are a financial news analyst."},
            {"role": "user", "content": f"Analyze the following news and its impact on the stock market: {news_text}"}
        ],
        "temperature": 0.7,
        "max_tokens": 512
    }
    headers = {"Authorization": f"Bearer {LLM_API_KEY}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(LLM_API_URL, json=payload, headers=headers)
        if response.status_code != 200:
            print("Mistral API error:", response.status_code, response.text)
        response.raise_for_status()
        result = response.json()
        print("response", response)
        return result["choices"][0]["message"]["content"]

# For sync compatibility in use_cases, provide a sync wrapper
import asyncio
def analyze_news_sync(news_text):
    return asyncio.run(analyze_news(news_text)) 