from pydantic import BaseModel
from datetime import datetime

class CrowdReportBase(BaseModel):
    station: str
    crowd_level: int

class CrowdReportCreate(CrowdReportBase):
    pass

class CrowdReportResponse(CrowdReportBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True