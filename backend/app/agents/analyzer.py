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

    def analyze_repository(self, repo_path):

        self.errors = []

        self.run_syntax_checks(repo_path)
        self.run_flake8_checks(repo_path)
        self.run_mypy_checks(repo_path)
        self.run_pylint_checks(repo_path)

        # Remove duplicates
        seen = set()
        unique_errors = []

        for error in self.errors:

            key = (
                error["file"],
                error["line"],
                error["description"]
            )

            if key not in seen:
                seen.add(key)
                unique_errors.append(error)

        self.errors = unique_errors

        return {
            "errors": self.errors
        }

    def run_syntax_checks(self, repo_path):

        for file in Path(repo_path).rglob("*.py"):

            result = check_syntax(file)

            if result:

                self.errors.append(
                    {
                        "file": str(Path(file).resolve()),
                        "line": result["line"],
                        "bug_type": "SYNTAX",
                        "description": result["message"],
                        "severity": "error",
                        "raw_message": result["message"]
                    }
                )

    def run_flake8_checks(self, repo_path):

        output = run_flake8(repo_path)

        for line in output:

            try:

                # Example:
                # test_repo/broken.py:1:1: F401 'os' imported but unused

                parts = line.split(":", 3)

                if len(parts) < 4:
                    continue

                file_path = parts[0]
                line_no = int(parts[1])

                message = parts[3].strip()

                self.errors.append(
                    {
                        "file": str(Path(file_path).resolve()),
                        "line": line_no,
                        "bug_type": "LINTING",
                        "description": message,
                        "severity": "warning",
                        "raw_message": line
                    }
                )

            except Exception:
                continue

    def run_mypy_checks(self, repo_path):

        output = run_mypy(repo_path)

        for line in output:

            if not line.strip():
                continue

            if line.startswith("Success"):
                continue

            try:

                # Example:
                # test_repo/file.py:10: error: Incompatible types ...

                parts = line.split(":", 3)

                if len(parts) < 4:
                    continue

                file_path = parts[0]
                line_no = int(parts[1])

                message = parts[3].strip()

                self.errors.append(
                    {
                        "file": str(Path(file_path).resolve()),
                        "line": line_no,
                        "bug_type": "TYPE_ERROR",
                        "description": message,
                        "severity": "warning",
                        "raw_message": line
                    }
                )

            except Exception:
                continue

    def run_pylint_checks(self, repo_path):

        output = run_pylint(repo_path)

        for line in output:

            if not line.strip():
                continue

            # Skip pylint banners
            if line.startswith("*************"):
                continue

            if "rated at" in line:
                continue

            if "-----" in line:
                continue

            try:

                # Example:
                # test_repo/broken.py:1:0: W0611: Unused import os (unused-import)

                parts = line.split(":", 4)

                if len(parts) < 5:
                    continue

                file_path = parts[0]
                line_no = int(parts[1])

                message = parts[4].strip()

                self.errors.append(
                    {
                        "file": str(Path(file_path).resolve()),
                        "line": line_no,
                        "bug_type": "LOGIC",
                        "description": message,
                        "severity": "warning",
                        "raw_message": line
                    }
                )

            except Exception:
                continue