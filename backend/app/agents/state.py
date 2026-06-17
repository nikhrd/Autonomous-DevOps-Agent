from typing import TypedDict


class AgentState(
    TypedDict
):
    repo_path: str
    errors: list
    retries: int
    fixed_count: int
    test_passed: bool
    cicd_runs: list
    cicd_status: str