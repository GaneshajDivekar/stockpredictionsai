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

async def predict_for_each_stock(data, news_text):
    results = []
    for user in data:
        df = user["data"]
        user_result = {
            "user_file": user["filename"],
            "stocks": []
        }
        for idx, row in df.iterrows():
            stock_name = str(row.iloc[0])
            stock_info = row.to_dict()
            stock_summary = ", ".join(f"{k}: {v}" for k, v in stock_info.items())
            prompt = (
                f"Stock: {stock_name}\n"
                f"Details: {stock_summary}\n"
                f"News: {news_text}\n\n"
                "Based on the stock details and the news, should the user BUY, SELL, or HOLD this stock? "
                "Explain your reasoning and give a one-word recommendation (buy/sell/hold)."
            )
            llm_response = await analyze_news(prompt)
            rec = "hold"
            for word in ["buy", "sell", "hold"]:
                if word in llm_response.lower():
                    rec = word
                    break
            user_result["stocks"].append({
                "stock": stock_name,
                "recommendation": rec,
                "llm_analysis": llm_response
            })
        results.append(user_result)
    return results

async def predict_all_investors_stocks(data, news_text):
    """
    Returns a single response with all investors and all their stocks, each with buy/sell/hold and reasoning.
    """
    all_recommendations = []
    for user in data:
        df = user["data"]
        investor = {
            "investor": user["filename"],
            "stocks": []
        }
        for idx, row in df.iterrows():
            stock_name = str(row.iloc[0])
            stock_info = row.to_dict()
            stock_summary = ", ".join(f"{k}: {v}" for k, v in stock_info.items())
            prompt = (
                f"Investor: {user['filename']}\n"
                f"Stock: {stock_name}\n"
                f"Details: {stock_summary}\n"
                f"News: {news_text}\n\n"
                "Based on the stock details, the investor's portfolio, and the news, should the investor BUY, SELL, or HOLD this stock? "
                "Explain your reasoning and give a one-word recommendation (buy/sell/hold)."
            )
            llm_response = await analyze_news(prompt)
            rec = "hold"
            for word in ["buy", "sell", "hold"]:
                if word in llm_response.lower():
                    rec = word
                    break
            investor["stocks"].append({
                "stock": stock_name,
                "recommendation": rec,
                "llm_analysis": llm_response
            })
        all_recommendations.append(investor)
    return {"all_investors_stock_recommendations": all_recommendations} 