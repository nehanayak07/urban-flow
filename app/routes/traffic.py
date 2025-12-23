from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import TrafficData
from ..schemas import TrafficCreate
from ..crud import calculate_congestion

router = APIRouter(prefix="/traffic", tags=["Traffic"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_traffic(data: TrafficCreate, db: Session = Depends(get_db)):
    congestion = calculate_congestion(
        data.vehicle_count,
        data.avg_speed
    )

    traffic = TrafficData(
        location=data.location,
        vehicle_count=data.vehicle_count,
        avg_speed=data.avg_speed,
        congestion_level=congestion
    )

    db.add(traffic)
    db.commit()
    db.refresh(traffic)

    return {
        "message": "Traffic data added successfully",
        "congestion_level": congestion
    }

@router.get("/")
def get_all_traffic(db: Session = Depends(get_db)):
    return db.query(TrafficData).all()
