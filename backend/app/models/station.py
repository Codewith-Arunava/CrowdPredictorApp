from pydantic import BaseModel

class Station(BaseModel):
    id: int
    name: str
    location: str