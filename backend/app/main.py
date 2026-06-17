from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #to recitfy cors access error
from app.models.database import engine
from app.models.schemas import Base
from app.routers.agent import router as agent_router
from app.routers.results import (
    router as results_router
)
from fastapi import WebSocket

from app.utils.websocket_manager import (
    ConnectionManager
)

manager = ConnectionManager()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Project Rift Backend"
)
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)
app.include_router(
    agent_router,
    prefix="/api"
)
app.include_router(
    results_router,
    prefix="/api"
)

@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "service": "project-rift"
    }

@app.websocket(
    "/ws/{run_id}"
)
async def websocket_endpoint(
    websocket: WebSocket,
    run_id: str
):

    await manager.connect(
        run_id,
        websocket
    )

    try:

        while True:

            await websocket.receive_text()

    except:

        manager.disconnect(
            run_id
        )