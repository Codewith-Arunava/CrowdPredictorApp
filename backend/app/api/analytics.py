from fastapi import APIRouter

router = APIRouter(prefix="/analytics", tags=["Analytics"])

# Dummy analytics
@router.get("/summary")
def get_summary():
    return {
        "total_reports": 120,
        "avg_crowd": 6.5,
        "peak_station": "Howrah"
    }