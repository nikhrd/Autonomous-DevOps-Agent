from pydantic import BaseModel


class FixResult(BaseModel):

    file: str

    bug_type: str

    line: int

    commit_message: str

    status: str


class CICDRun(BaseModel):

    iteration: int

    status: str

    timestamp: str