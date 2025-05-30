# Stock Prediction AI

## Setup

1. Place your `.xls` files in the `data/` folder.
2. Install dependencies:
   pip install -r requirements.txt
3. Run the server:
   uvicorn app.main:app --reload

## API Endpoints

- `/upload/` - Upload new .xls files
- `/predict/` - Get stock prediction based on news and data

## Project Structure

```
stockpredictionsai/
│
├── app/
│   ├── api/                # FastAPI routers
│   ├── core/               # Core config, LLM integration
│   ├── domain/             # Entities, value objects
│   ├── use_cases/          # Business logic
│   ├── infrastructure/     # File handling, data access
│   ├── services/           # Service layer (e.g., stock prediction)
│   └── main.py             # FastAPI entrypoint
│
├── data/                   # Place your .xls files here
│
├── requirements.txt
└── README.md
``` 