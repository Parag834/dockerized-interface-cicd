from fastapi import FastAPI
from app.model import predict

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Running on AWS EC2"}

@app.post("/predict")
def inference(text: str):
    return predict(text)

