from app.agents.repo_cloner import RepoCloner

cloner = RepoCloner()

repo_path = cloner.clone_repository(
    "https://github.com/pallets/flask.git",
    "test_run"
)

metadata = cloner.get_repo_metadata(
    repo_path
)

print(metadata)