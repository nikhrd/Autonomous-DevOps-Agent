from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.models.schemas import (
    AgentRun
)

from app.models.session import (
    get_db
)

router = APIRouter()

@router.get(
    "/results/{run_id}"
)
def get_result(
    run_id: str,
    db: Session = Depends(
        get_db
    )
):

    run = (
        db.query(AgentRun)
        .filter(
            AgentRun.run_id
            == run_id
        )
        .first()
    )

    return run
@router.get("/runs")
def list_runs(
    db: Session = Depends(
        get_db
    )
):

    return (
        db.query(
            AgentRun
        )
        .all()
    )