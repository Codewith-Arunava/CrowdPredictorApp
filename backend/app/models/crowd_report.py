from pydantic import BaseModel
from datetime import datetime

class CrowdReport(BaseModel):
    station: str
    crowd_level: int  # 1 to 10 scale
    timestamp: datetime