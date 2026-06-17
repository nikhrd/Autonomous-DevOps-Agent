from app.agents.cicd_monitor import (
    CICDMonitor
)

from app.tools.local_ci import (
    LocalCI
)

from app.utils.github_parser import (
    parse_repo_name
)


class CIExecutor:

    def __init__(self):

        self.monitor = CICDMonitor()

        self.local_ci = LocalCI()

    def execute(
        self,
        repo_url,
        repo_path
    ):

        repo_name = parse_repo_name(
            repo_url
        )

        has_workflow = (
            self.monitor.has_workflows(
                repo_name
            )
        )

        if not has_workflow:

            return self.local_ci.execute(
                repo_path
            )

        return self.monitor.wait_for_completion(
            repo_name
        )