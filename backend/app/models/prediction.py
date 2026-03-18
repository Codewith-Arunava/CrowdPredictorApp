from pydantic import BaseModel

class PredictionInput(BaseModel):
    station: str
    time: str

class PredictionOutput(BaseModel):
    station: str
    predicted_crowd: int