import pandas as pd
import os

def process_xls_files(data_dir):
    data = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".xls") or filename.endswith(".xlsx"):
            df = pd.read_excel(os.path.join(data_dir, filename))
            data.append({"filename": filename, "data": df})
    return data

def extract_news_text(data_dir):
    for filename in os.listdir(data_dir):
        if "news" in filename.lower():
            df = pd.read_excel(os.path.join(data_dir, filename))
            return " ".join(str(x) for x in df.iloc[:, 0].dropna())
    return "" 