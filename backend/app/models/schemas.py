from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from .database import Base


class AgentRun(Base):
    __tablename__ = "agent_runs"

    id = Column(Integer, primary_key=True, index=True)

    run_id = Column(String, unique=True)

    repo_url = Column(String)

    team_name = Column(String)

    leader_name = Column(String)

    status = Column(String, default="PENDING")

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )