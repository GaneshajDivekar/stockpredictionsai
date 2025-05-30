from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(title="Stock Prediction AI")
app.include_router(api_router) 