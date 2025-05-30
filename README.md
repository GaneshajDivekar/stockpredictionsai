# Stock Prediction AI

A FastAPI-based backend for stock prediction and news impact analysis using Mistral LLM and Excel data files, following Clean Architecture principles.

---

## Features
- Upload and process multiple `.xls`/`.xlsx` files (e.g., portfolios, news, impact data)
- Analyze news/impact using Mistral LLM API
- Predict stock actions (buy/sell/hold) for all users or each user individually, with reasoning
- **MCP (Multi-Component Process) server for agentic flows**
- Clean, extensible architecture for easy future enhancements

---

## Project Structure

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

## Setup Instructions

1. **Clone the repository**
2. **Place your `.xls`/`.xlsx` files** in the `data/` folder. (At least one news/impact file is required, e.g., `Market_Impact_News_2024.xlsx`)
3. **Create a virtual environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. **Configure your Mistral LLM API key**
   - Edit `app/core/llm.py` and set `LLM_API_KEY` to your actual API key.
   - Ensure the `model` field matches a valid model for your account (e.g., `mistral-tiny`, `mistral-small`, etc.)
5. **Run the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```
6. **Access the API docs:**
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser for interactive Swagger UI.

---

## MCP Server: Agentic Flow Orchestration

The **MCP (Multi-Component Process) server** is a core part of this project, enabling advanced agentic workflows. It allows you to orchestrate multiple reasoning steps, LLM calls, and data processing actions in a single, structured flow. This is ideal for:
- Multi-step decision making
- Tool-using agents
- Chained LLM reasoning
- Customizable, extensible AI pipelines

### How It Works
- The MCP server exposes endpoints (e.g., `/agentic-flow/`) that run a sequence of steps:
  1. Read and process all `.xls`/`.xlsx` files
  2. Extract and analyze news/impact data
  3. Optionally, analyze each user's portfolio
  4. Call the LLM (Mistral) with a custom prompt for each step
  5. Aggregate and return a structured, step-by-step output
- You can extend the MCP server to add more agents, tools, or reasoning steps as needed.

### Example Endpoint

#### **POST** `/agentic-flow/`
- **Description:**
    - Runs an agentic flow to analyze all data and news, and returns a structured output with reasoning steps.
- **Sample Output:**
```json
{
  "llm_analysis": "The news is positive for the stock market...",
  "action": "buy",
  "steps": [
    {"step": "LLM news analysis", "result": "The news is positive for the stock market..."},
    {"step": "Decision", "result": "buy"}
  ]
}
```

### Extending the MCP Server
- Add new flows or agents in `app/services/agentic_flow.py`
- Add new endpoints in `app/api/mcp.py`
- Chain together multiple LLM calls, tool uses, or data processing steps
- Use the MCP server as a controller for complex, multi-agent AI systems

---

## API Endpoints

### 1. Upload XLS File
- **POST** `/upload/`
- **Body:** Multipart form with a file field
- **Description:** Uploads a new `.xls` or `.xlsx` file to the `data/` directory.

### 2. Predict Stock Action (Global)
- **POST** `/predict/`
- **Description:**
    - Reads all `.xls`/`.xlsx` files in `data/`
    - Extracts news/impact text from the news file (filename containing `news`)
    - Sends news text to Mistral LLM for analysis
    - Returns a global prediction (buy/sell) and the LLM's analysis

### 3. Predict for Each User (Personalized)
- **POST** `/predict-each-user/`
- **Description:**
    - Reads all `.xls`/`.xlsx` files in `data/`
    - Extracts news/impact text from the news file (filename containing `news`)
    - For each user (investor), summarizes their portfolio and combines it with the news
    - Asks the LLM for a personalized buy/sell/hold recommendation and explanation for each user
    - Returns a list of recommendations and reasoning for each user

#### Example Output for `/predict-each-user/`:
```json
{
  "user_recommendations": [
    {
      "user_file": "Investor_1_Portfolio_2024.xlsx",
      "recommendation": "buy",
      "llm_analysis": "Based on the user's portfolio and the positive news, the user should BUY. The portfolio is well diversified and the news indicates a bullish trend."
    },
    {
      "user_file": "Investor_2_Portfolio_2024.xlsx",
      "recommendation": "hold",
      "llm_analysis": "The portfolio is stable and the news is neutral. The user should HOLD."
    }
    // ... more users
  ]
}
```

---

## LLM Integration (Mistral)
- The backend calls the Mistral LLM API using your API key.
- The model name must be valid for your account (see [Mistral API docs](https://docs.mistral.ai/)).
- If you get a 400 error with `invalid_model`, update the `model` field in `app/core/llm.py`.

---

## Example `.xls` File Placement
- Place all investor and news files in the `data/` folder:
  - `data/Investor_1_Portfolio_2024.xlsx`
  - `data/Market_Impact_News_2024.xlsx`
  - ...

---

## Troubleshooting
- **400 Bad Request from Mistral API:**
  - Check your API key and model name in `app/core/llm.py`.
  - Print/log the response to see the error message.
- **No news file found:**
  - Ensure at least one file in `data/` contains `news` in its filename.
- **Python or pip errors:**
  - Use a virtual environment as shown above.

---

## Extending the Project
- Add more business logic in `app/use_cases/`
- Add new endpoints in `app/api/endpoints.py` or `app/api/mcp.py`
- Implement domain models in `app/domain/` as needed
- Enhance agentic flows or add more LLM tools in `app/services/`

---

## License
MIT (or your preferred license) 