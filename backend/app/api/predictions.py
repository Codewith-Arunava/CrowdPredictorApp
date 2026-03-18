from fastapi import APIRouter
from pydantic import BaseModel
import random

router = APIRouter(prefix="/predictions", tags=["Predictions"])

class PredictionInput(BaseModel):
    station: str
    time: str

class PredictionOutput(BaseModel):
    station: str
    predicted_crowd: int

@router.post("/", response_model=PredictionOutput)
def predict_crowd(data: PredictionInput):
    # Dummy ML logic (replace with model later)
    prediction = random.randint(1, 10)

    return PredictionOutput(
        station=data.station,
        predicted_crowd=prediction
    )