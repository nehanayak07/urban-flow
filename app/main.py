from fastapi import FastAPI
from .database import engine, Base
from .routes import traffic

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Urban Flow Traffic API",
    description="Smart City Traffic Monitoring using FastAPI & MySQL",
    version="1.0.0"
)

app.include_router(traffic.router)

@app.get("/")
def health_check():
    return {"status": "Urban Flow API is running 🚦"}
