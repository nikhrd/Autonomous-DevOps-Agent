from fastapi import FastAPI

from app.models.database import engine
from app.models.schemas import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Project Rift Backend"
)


@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "service": "project-rift"
    }