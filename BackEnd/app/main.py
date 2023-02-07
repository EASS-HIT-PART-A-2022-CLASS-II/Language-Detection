#imports
import redis
from fastapi import FastAPI
from pydantic import BaseModel
from app.ML_model.model import predict_pipeline
from app.ML_model.model import __version__ as model_version


app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)

    # initialize Redis connection
    r = redis.Redis(host='localhost', port=6379, db=0)

    # increment the counter for the prediction language
    r.incr(language)

    return {"language": language}