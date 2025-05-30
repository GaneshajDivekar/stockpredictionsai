from fastapi import APIRouter, UploadFile, File
from app.use_cases.process_xls import process_xls_files, extract_news_text
from app.use_cases.predict import predict_stock_action
import os

router = APIRouter()

@router.post("/upload/")
async def upload_xls(file: UploadFile = File(...)):
    file_location = f"data/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {"info": f"file '{file.filename}' saved"}

@router.post("/predict/")
async def predict():
    data = process_xls_files("data/")
    news_text = extract_news_text("data/")
    result = await predict_stock_action(data, news_text)
    return result 