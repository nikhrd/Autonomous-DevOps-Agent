from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text
)

from datetime import datetime

from app.models.database import Base


class AgentRun(Base):

    __tablename__ = "agent_runs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    run_id = Column(
        String,
        unique=True
    )

    repo_url = Column(String)

    team_name = Column(String)

    leader_name = Column(String)

    branch_name = Column(String)

    status = Column(String)

    score = Column(Integer)

    results_json = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )