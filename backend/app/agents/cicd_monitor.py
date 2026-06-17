import os
import time

from github import Github

from dotenv import load_dotenv

load_dotenv()


class CICDMonitor:

    def __init__(self):

        self.github = Github(
            os.getenv("GITHUB_TOKEN")
        )

        self.poll_interval = int(
            os.getenv(
                "CI_POLL_INTERVAL",
                10
            )
        )

    def get_repo(
        self,
        repo_full_name
    ):

        return self.github.get_repo(
            repo_full_name
        )

    def has_workflows(
        self,
        repo_full_name
    ):

        repo = self.get_repo(
            repo_full_name
        )

        workflows = repo.get_workflows()

        return workflows.totalCount > 0

    def get_latest_run(
        self,
        repo_full_name
    ):

        repo = self.get_repo(
            repo_full_name
        )

        runs = repo.get_workflow_runs()

        if runs.totalCount == 0:
            return None

        return runs[0]

    def wait_for_completion(
        self,
        repo_full_name
    ):

        while True:

            run = self.get_latest_run(
                repo_full_name
            )

            if not run:
                return None

            print(
                f"Status: {run.status}"
            )

            if run.status == "completed":

                return {
                    "run_id": run.id,
                    "status": run.conclusion,
                    "created_at": str(
                        run.created_at
                    ),
                    "updated_at": str(
                        run.updated_at
                    )
                }

            time.sleep(
                self.poll_interval
            )