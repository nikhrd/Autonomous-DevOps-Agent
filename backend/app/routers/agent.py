import uuid

from fastapi import APIRouter

from app.models.run_request import (
    RunRequest
)

router = APIRouter()


@router.post("/run-agent")
def run_agent(
    payload: RunRequest
):

    run_id = str(
        uuid.uuid4()
    )

    return {
        "run_id": run_id,
        "repo_url": payload.repo_url,
        "team_name": payload.team_name,
        "leader_name": payload.leader_name
    }