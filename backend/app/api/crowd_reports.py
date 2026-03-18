from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/reports", tags=["Crowd Reports"])

# In-memory storage
crowd_data = []

class CrowdReport(BaseModel):
    station: str
    crowd_level: int   # 1–10 scale

@router.post("/")
def add_report(report: CrowdReport):
    crowd_data.append(report)
    return {"message": "Report added"}

@router.get("/", response_model=List[CrowdReport])
def get_reports():
    return crowd_data