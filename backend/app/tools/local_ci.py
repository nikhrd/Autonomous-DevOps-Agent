from app.tools.test_runner import (
    TestRunner
)


class LocalCI:

    def __init__(self):

        self.runner = TestRunner()

    def execute(
        self,
        repo_path
    ):

        results = self.runner.run_tests(
            repo_path
        )

        return {
            "status":
                "LOCAL_PASS"
                if results["success"]
                else "LOCAL_FAIL",

            "exit_code":
                results["exit_code"],

            "stdout":
                results["stdout"],

            "stderr":
                results["stderr"]
        }