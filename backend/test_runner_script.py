from app.tools.test_runner import (
    TestRunner
)

runner = TestRunner()

results = runner.run_tests(
    "test_repo"
)

print(results)