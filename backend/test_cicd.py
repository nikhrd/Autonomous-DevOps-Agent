from app.agents.ci_executor import (
    CIExecutor
)

executor = CIExecutor()

result = executor.execute(
    repo_url="https://github.com/pallets/flask",
    repo_path="workspace/test_run"
)

print(result)