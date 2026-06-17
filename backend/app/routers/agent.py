import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.run_request import RunRequest
from app.models.session import get_db
from app.models.schemas import AgentRun

router = APIRouter()


@router.post("/run-agent")
def run_agent(
    payload: RunRequest,
    db: Session = Depends(get_db)
):
    # Generate run ID first
    run_id = str(uuid.uuid4())

    run = AgentRun(
        run_id=run_id,
        repo_url=payload.repo_url,
        team_name=payload.team_name,
        leader_name=payload.leader_name,
        status="RUNNING"
    )

    db.add(run)
    db.commit()
    db.refresh(run)

    return {
        "run_id": run_id,
        "repo_url": payload.repo_url,
        "team_name": payload.team_name,
        "leader_name": payload.leader_name
    }