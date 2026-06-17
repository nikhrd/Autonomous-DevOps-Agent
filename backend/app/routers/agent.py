import json
import uuid

from datetime import datetime

from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.models.session import (
    get_db
)

from app.models.schemas import (
    AgentRun
)

from app.utils.result_builder import (
    ResultBuilder
)

from app.utils.results_writer import (
    ResultsWriter
)
from app.models.request_models import RunRequest

router = APIRouter()


@router.post("/run-agent")
def run_agent(
    payload: RunRequest,
    db: Session = Depends(
        get_db
    )
):

    run_id = str(
        uuid.uuid4()
    )

    start_time = (
        datetime.utcnow()
    )

    run = AgentRun(
        run_id=run_id,
        repo_url=payload.repo_url,
        team_name=payload.team_name,
        leader_name=payload.leader_name,
        status="RUNNING"
    )

    db.add(run)

    db.commit()

    # -------------------------------------------------
    # Execute workflow here
    # -------------------------------------------------

    # Example placeholders
    branch_name = (
        "AI_FIX_BRANCH"
    )

    end_time = (
        datetime.utcnow()
    )

    fixes = [
        {
            "file": "app.py",
            "bug_type": "SYNTAX",
            "line": 10,
            "commit_message":
                "[AI-AGENT] Fix SYNTAX",
            "status": "FIXED"
        }
    ]

    cicd_runs = [
        {
            "iteration": 1,
            "status": "PASSED",
            "timestamp":
                datetime.utcnow()
                .isoformat()
        }
    ]

    commit_count = 1

    tests_passed = True

    # -------------------------------------------------
    # Phase 8 Step 7
    # -------------------------------------------------

    builder = ResultBuilder()

    writer = ResultsWriter()

    results = builder.build(
        run_id=run_id,

        repo_url=
            payload.repo_url,

        team_name=
            payload.team_name,

        leader_name=
            payload.leader_name,

        branch_name=
            branch_name,

        start_time=
            start_time,

        end_time=
            end_time,

        fixes=
            fixes,

        cicd_runs=
            cicd_runs,

        commit_count=
            commit_count,

        tests_passed=
            tests_passed
    )

    writer.save(
        run_id,
        results
    )

    # -------------------------------------------------
    # Phase 8 Step 8
    # -------------------------------------------------

    run.results_json = (
        json.dumps(
            results
        )
    )

    run.score = (
        results["score"]
        ["total"]
    )

    run.status = (
        "COMPLETED"
    )

    db.commit()

    return {
        "run_id": run_id,
        "status": "COMPLETED"
    }