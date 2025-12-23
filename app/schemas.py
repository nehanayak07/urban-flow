from pydantic import BaseModel

class TrafficCreate(BaseModel):
    location: str
    vehicle_count: int
    avg_speed: float

class TrafficResponse(TrafficCreate):
    congestion_level: str

    class Config:
        from_attributes = True
