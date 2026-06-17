from pydantic import BaseModel


class CICDRun(
    BaseModel
):

    iteration: int

    status: str

    timestamp: str