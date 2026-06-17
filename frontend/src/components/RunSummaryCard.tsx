import type { AgentResult } from "../types/agent";

interface Props {
  result?: AgentResult;
}

export default function RunSummaryCard({
  result
}: Props) {

  if (!result)
    return null;

  return (
    <div className="border p-4 rounded">

      <h2>
        Run Summary
      </h2>

      <p>
        Repo:
        {result.repo_url}
      </p>

      <p>
        Team:
        {result.team_name}
      </p>

      <p>
        Leader:
        {result.leader_name}
      </p>

      <p>
        Fixes:
        {result.total_fixes}
      </p>

      <p>
        Failures:
        {result.total_failures}
      </p>

      <p>
        CI/CD:
        {result.cicd_status}
      </p>

    </div>
  );
}