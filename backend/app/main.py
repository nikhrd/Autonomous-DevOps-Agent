from fastapi import FastAPI

from app.models.database import engine
from app.models.schemas import Base
from app.routers.agent import router as agent_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Project Rift Backend"
)
app.include_router(
    agent_router,
    prefix="/api"
)

@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "service": "project-rift"
    }