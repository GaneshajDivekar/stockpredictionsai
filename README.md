# Stock Prediction AI

A FastAPI-based backend for stock prediction and news impact analysis using Mistral LLM and Excel data files, following Clean Architecture principles.

---

## Features
- Upload and process multiple `.xls`/`.xlsx` files (e.g., portfolios, news, impact data)
- Analyze news/impact using Mistral LLM API
- Predict stock actions (buy/sell/hold) based on news and data
- Clean, extensible architecture

---

## Project Structure

```
stockpredictionsai/
│
├── app/
│   ├── api/                # FastAPI routers
│   ├── core/               # LLM integration and config
│   ├── domain/             # (For future use: Entities, value objects)
│   ├── use_cases/          # Business logic (XLS processing, prediction)
│   ├── infrastructure/     # (For future use: File/data access)
│   ├── services/           # (For future use: Service layer)
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

## API Endpoints

### 1. Upload XLS File
- **POST** `/upload/`
- **Body:** Multipart form with a file field
- **Description:** Uploads a new `.xls` or `.xlsx` file to the `data/` directory.

### 2. Predict Stock Action
- **POST** `/predict/`
- **Description:**
    - Reads all `.xls`/`.xlsx` files in `data/`
    - Extracts news/impact text from the news file (filename containing `news`)
    - Sends news text to Mistral LLM for analysis
    - Returns a prediction (buy/sell) and the LLM's analysis

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
- Add new endpoints in `app/api/endpoints.py`
- Implement domain models in `app/domain/` as needed

---

## License
MIT (or your preferred license) 