from pydantic import BaseModel


class RunRequest(BaseModel):
    repo_url: str
    team_name: str
    leader_name: str