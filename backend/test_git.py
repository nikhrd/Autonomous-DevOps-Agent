from pathlib import Path

from app.agents.git_agent import GitAgent

from app.utils.branch_namer import (
    make_branch_name
)

repo_path = Path(
    "workspace/test_run"
)

branch = make_branch_name(
    "buggyBrains",
    "Nikhitha Dsouza"
)

agent = GitAgent()

agent.create_branch(
    repo_path,
    branch
)

print("Branch Created")