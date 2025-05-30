from app.core.llm import analyze_news

async def predict_stock_action(data, news_text):
    news_impact = await analyze_news(news_text)
    # Dummy logic: if news is positive, suggest buy, else sell
    action = "buy" if "positive" in news_impact.lower() else "sell"
    return {"action": action, "news_impact": news_impact} 