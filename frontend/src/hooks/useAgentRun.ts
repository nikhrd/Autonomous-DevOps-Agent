import {
  useQuery,
} from "@tanstack/react-query";

import {
  getResult,
} from "../api/agentApi";

export function useAgentRun(
  runId: string
) {

  return useQuery({
    queryKey: [
      "run",
      runId,
    ],

    queryFn: () =>
      getResult(runId),

    enabled:
      !!runId,

    refetchInterval:
      3000,
  });
}