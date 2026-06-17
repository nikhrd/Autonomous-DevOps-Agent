from datetime import datetime

from app.utils.scoring import (
    calculate_score
)


class ResultBuilder:

    def build(
        self,
        run_id,
        repo_url,
        team_name,
        leader_name,
        branch_name,
        start_time,
        end_time,
        fixes,
        cicd_runs,
        commit_count,
        tests_passed
    ):

        score = calculate_score(
            start_time,
            end_time,
            commit_count,
            tests_passed
        )

        return {

            "run_id": run_id,

            "team_name": team_name,

            "leader_name": leader_name,

            "repo_url": repo_url,

            "branch": branch_name,

            "start_time":
                start_time.isoformat(),

            "end_time":
                end_time.isoformat(),

            "total_time_seconds":
                int(
                    (
                        end_time
                        - start_time
                    ).total_seconds()
                ),

            "total_failures":
                len(fixes),

            "total_fixes":
                len(
                    [
                        x
                        for x in fixes
                        if x["status"]
                        == "FIXED"
                    ]
                ),

            "commit_count":
                commit_count,

            "cicd_status":
                cicd_runs[-1]["status"]
                if cicd_runs
                else "UNKNOWN",

            "score":
                score,

            "fixes":
                fixes,

            "cicd_runs":
                cicd_runs
        }