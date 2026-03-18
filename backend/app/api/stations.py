from fastapi import APIRouter

router = APIRouter(prefix="/stations", tags=["Stations"])

stations_list = [
    "Howrah",
    "Sealdah",
    "Durgapur",
    "Asansol",
    "Kolkata"
]

@router.get("/")
def get_stations():
    return {"stations": stations_list}