from app.core.llm import analyze_news
import pandas as pd

async def predict_stock_action(data, news_text):
    news_impact = await analyze_news(news_text)
    # Dummy logic: if news is positive, suggest buy, else sell
    action = "buy" if "positive" in news_impact.lower() else "sell"
    return {"action": action, "news_impact": news_impact}

async def predict_for_each_user(data, news_text):
    results = []
    for user in data:
        # Summarize the user's portfolio for the LLM
        df = user["data"]
        # Create a summary string (e.g., top holdings, total value, etc.)
        summary = df.to_string(index=False)
        prompt = f"User portfolio:\n{summary}\n\nNews:\n{news_text}\n\nBased on the user's portfolio and the news, should the user BUY, SELL, or HOLD? Explain your reasoning and give a one-word recommendation (buy/sell/hold)."
        llm_response = await analyze_news(prompt)
        # Extract recommendation (look for buy/sell/hold in the response)
        rec = "hold"
        for word in ["buy", "sell", "hold"]:
            if word in llm_response.lower():
                rec = word
                break
        results.append({
            "user_file": user["filename"],
            "recommendation": rec,
            "llm_analysis": llm_response
        })
    return results 