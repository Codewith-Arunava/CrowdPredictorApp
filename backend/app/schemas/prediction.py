from pydantic import BaseModel

class PredictionRequest(BaseModel):
    station: str
    time: str

class PredictionResponse(BaseModel):
    station: str
    predicted_crowd: int