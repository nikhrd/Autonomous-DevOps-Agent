from pathlib import Path

from app.tools.linters import (
    run_flake8,
    run_mypy,
    run_pylint
)

from app.tools.syntax_checker import (
    check_syntax
)


class Analyzer:

    def __init__(self):

        self.errors = []

    def analyze_repository(
        self,
        repo_path
    ):

        self.errors = []

        self.run_syntax_checks(
            repo_path
        )

        self.run_flake8_checks(
            repo_path
        )

        self.run_mypy_checks(
            repo_path
        )

        self.run_pylint_checks(
            repo_path
        )

        return {
            "errors": self.errors
        }

    def run_syntax_checks(
        self,
        repo_path
    ):

        for file in Path(repo_path).rglob("*.py"):

            result = check_syntax(file)

            if result:

                self.errors.append(
                    {
                        "file": str(file),
                        "line": result["line"],
                        "bug_type": "SYNTAX",
                        "description": result["message"],
                        "severity": "error",
                        "raw_message": result["message"]
                    }
                )

    def run_flake8_checks(
        self,
        repo_path
    ):

        output = run_flake8(
            repo_path
        )

        for line in output:

            self.errors.append(
                {
                    "file": line,
                    "line": 0,
                    "bug_type": "LINTING",
                    "description": line,
                    "severity": "warning",
                    "raw_message": line
                }
            )

    def run_mypy_checks(
        self,
        repo_path
    ):

        output = run_mypy(
            repo_path
        )

        for line in output:

            self.errors.append(
                {
                    "file": line,
                    "line": 0,
                    "bug_type": "TYPE_ERROR",
                    "description": line,
                    "severity": "warning",
                    "raw_message": line
                }
            )

    def run_pylint_checks(
        self,
        repo_path
    ):

        output = run_pylint(
            repo_path
        )

        for line in output:

            self.errors.append(
                {
                    "file": line,
                    "line": 0,
                    "bug_type": "LOGIC",
                    "description": line,
                    "severity": "warning",
                    "raw_message": line
                }
            )