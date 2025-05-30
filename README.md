# 🚀 Stock Prediction AI

**Stock Prediction AI** is a robust, extensible backend platform for intelligent stock action recommendations. It leverages FastAPI, Clean Architecture, and the Mistral LLM to analyze investor portfolios and market news from Excel files, delivering actionable buy/sell/hold insights for each investor and each stock.

---

## 🌟 Features

- **Multi-Investor Support:** Analyze portfolios for any number of investors from `.xls`/`.xlsx` files.
- **Market News Integration:** Incorporate the latest market/news data for context-aware recommendations.
- **LLM-Powered Reasoning:** Uses Mistral LLM for deep, explainable AI-driven analysis.
- **Agentic (MCP) Flow:** Orchestrate multi-step, multi-agent reasoning for advanced workflows.
- **RESTful API:** Clean, documented endpoints for easy integration.
- **Extensible Architecture:** Built for growth—add new agents, tools, or business logic with ease.

---

## 🏗️ Project Structure

```
stockpredictionsai/
│
├── app/
│   ├── api/                # FastAPI routers and endpoints
│   ├── core/               # LLM integration and config
│   ├── domain/             # (For future use: Entities, value objects)
│   ├── use_cases/          # Business logic (XLS processing, prediction)
│   ├── infrastructure/     # (For future use: File/data access)
│   ├── services/           # (For future use: Service layer, agentic flows)
│   └── main.py             # FastAPI entrypoint
│
├── data/                   # Place your .xls/.xlsx files here
│
├── requirements.txt
└── README.md
```

---

## ⚡ Quickstart

1. **Clone the repository**
2. **Add your `.xls`/`.xlsx` files** to the `data/` folder (at least one news/impact file required, e.g., `Market_Impact_News_2024.xlsx`)
3. **Install dependencies in a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. **Configure your Mistral LLM API key:**
   - Edit `app/core/llm.py` and set `LLM_API_KEY` to your actual API key.
   - Ensure the `model` field matches a valid model for your account (e.g., `mistral-tiny`, `mistral-small`, etc.)
5. **Run the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```
6. **Explore the API docs:**
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive Swagger UI.

---

## 🧠 How It Works

- **Upload** investor and news files in Excel format.
- **Process**: The backend reads all files, extracts portfolios and news.
- **Analyze**: For each investor and each stock, the system combines portfolio data and news, then queries the Mistral LLM for a buy/sell/hold recommendation and detailed reasoning.
- **Respond**: Returns a structured, explainable report for every investor and every stock.

---

## 🔗 API Endpoints

### 1. Upload XLS File
- **POST** `/upload/`
- **Body:** Multipart form with a file field
- **Description:** Uploads a new `.xls` or `.xlsx` file to the `data/` directory.

### 2. Predict Stock Action (Global)
- **POST** `/predict/`
- **Description:** Returns a global buy/sell recommendation based on all portfolios and news.

### 3. Predict for Each User (Personalized)
- **POST** `/predict-each-user/`
- **Description:** Returns a buy/sell/hold recommendation and reasoning for each investor.

### 4. Predict for Each Stock (Per User)
- **POST** `/predict-each-stock/`
- **Description:** Returns a buy/sell/hold recommendation and reasoning for each stock in each investor's portfolio.

### 5. Predict All Investors' Stocks (Comprehensive)
- **POST** `/predict-all-investors-stocks/`
- **Description:** Returns a single, comprehensive response with all investors and all their stocks, each with a buy/sell/hold recommendation and detailed LLM explanation.

#### Example Output for `/predict-all-investors-stocks/`:
```json
{
  "all_investors_stock_recommendations": [
    {
      "investor": "Investor_1_Portfolio_2024.xlsx",
      "stocks": [
        {
          "stock": "AAPL",
          "recommendation": "buy",
          "llm_analysis": "Given the strong news and the user's holding, AAPL is a BUY."
        },
        {
          "stock": "TSLA",
          "recommendation": "hold",
          "llm_analysis": "TSLA is stable, and the news is neutral. HOLD."
        }
      ]
    }
    // ... more investors
  ]
}
```

---

## 🛠️ Example Code Snippets

### Reading and Processing XLS Files

```python
import pandas as pd
import os

def process_xls_files(data_dir):
    data = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".xls") or filename.endswith(".xlsx"):
            df = pd.read_excel(os.path.join(data_dir, filename))
            data.append({"filename": filename, "data": df})
    return data
```

### LLM Integration

```python
import httpx

LLM_API_URL = "https://api.mistral.ai/v1/chat/completions"
LLM_API_KEY = "your_mistral_api_key"

async def analyze_news(news_text):
    payload = {
        "model": "mistral-tiny",
        "messages": [
            {"role": "system", "content": "You are a financial news analyst."},
            {"role": "user", "content": news_text}
        ],
        "temperature": 0.7,
        "max_tokens": 512
    }
    headers = {"Authorization": f"Bearer {LLM_API_KEY}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(LLM_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
```

---

## 🤖 MCP Server: Agentic Flow Orchestration

The **MCP (Multi-Component Process) server** enables advanced agentic workflows. It orchestrates multiple reasoning steps, LLM calls, and data processing actions in a single, structured flow. This is ideal for:
- Multi-step decision making
- Tool-using agents
- Chained LLM reasoning
- Customizable, extensible AI pipelines

**How It Works:**
- The MCP server exposes endpoints (e.g., `/agentic-flow/`) that run a sequence of steps:
  1. Read and process all `.xls`/`.xlsx` files
  2. Extract and analyze news/impact data
  3. Optionally, analyze each user's portfolio
  4. Call the LLM (Mistral) with a custom prompt for each step
  5. Aggregate and return a structured, step-by-step output

**Extending the MCP Server:**
- Add new flows or agents in `app/services/agentic_flow.py`
- Add new endpoints in `app/api/mcp.py`
- Chain together multiple LLM calls, tool uses, or data processing steps

---

## 📂 Example `.xls` File Placement

- Place all investor and news files in the `data/` folder:
  - `data/Investor_1_Portfolio_2024.xlsx`
  - `data/Market_Impact_News_2024.xlsx`
  - ...

---

## 🧩 Extending the Project

- Add more business logic in `app/use_cases/`
- Add new endpoints in `app/api/endpoints.py` or `app/api/mcp.py`
- Implement domain models in `app/domain/` as needed
- Enhance agentic flows or add more LLM tools in `app/services/`

---

## 🐞 Troubleshooting

- **400 Bad Request from Mistral API:**
  - Check your API key and model name in `app/core/llm.py`.
  - Print/log the response to see the error message.
- **No news file found:**
  - Ensure at least one file in `data/` contains `news` in its filename.
- **Python or pip errors:**
  - Use a virtual environment as shown above.

---

## 📜 License

MIT (or your preferred license)

---

## 🙋‍♂️ Questions or Contributions?

- Open an issue or pull request!
- For feature requests, ideas, or help, contact the maintainer.

---

**Impress your team, investors, or users with this powerful, explainable, and extensible stock prediction backend!** 