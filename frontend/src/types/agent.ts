export interface Fix {
  file: string;
  bug_type: string;
  line: number;
  commit_message: string;
  status: string;
}

export interface CICDRun {
  iteration: number;
  status: string;
  timestamp: string;
}

export interface Score {
  base: number;
  speed_bonus: number;
  efficiency_penalty: number;
  total: number;
}

export interface AgentResult {
  run_id: string;
  repo_url: string;

  team_name: string;

  leader_name: string;

  branch: string;

  total_failures: number;

  total_fixes: number;

  cicd_status: string;

  score: Score;

  fixes: Fix[];

  cicd_runs: CICDRun[];
}