import shutil
from pathlib import Path

from git import Repo


class RepoCloner:

    def __init__(self):
        self.workspace = Path("workspace")

        self.workspace.mkdir(
            exist_ok=True
        )

    def clone_repository(
        self,
        repo_url: str,
        run_id: str
    ):

        clone_path = self.workspace / run_id

        if clone_path.exists():
            shutil.rmtree(clone_path)

        Repo.clone_from(
            repo_url,
            clone_path
        )

        return clone_path

    def detect_python_files(
        self,
        repo_path
    ):

        files = []

        for file in repo_path.rglob("*.py"):
            files.append(str(file))

        return files

    def get_repo_metadata(
        self,
        repo_path
    ):

        py_files = self.detect_python_files(
            repo_path
        )

        return {
            "python_files": py_files,
            "file_count": len(py_files)
        }