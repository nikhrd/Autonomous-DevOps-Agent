from pydantic import BaseModel


class CodeError(BaseModel):

    file: str

    line: int

    bug_type: str

    description: str

    severity: str

    raw_message: str