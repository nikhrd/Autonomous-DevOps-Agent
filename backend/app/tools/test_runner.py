import subprocess
from pathlib import Path


class TestRunner:

    def discover_tests(
        self,
        repo_path
    ):

        tests = []

        for file in Path(repo_path).rglob("test_*.py"):
            tests.append(file)

        for file in Path(repo_path).rglob("*_test.py"):
            tests.append(file)

        return tests

    def run_tests(
        self,
        repo_path
    ):

        cmd = [
            "pytest",
            str(repo_path),
            "-v"
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode
        }