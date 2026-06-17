import { create } from "zustand";

interface AgentStore {

  runId: string;

  setRunId: (
    id: string
  ) => void;

  logs: string[];

  addLog: (
    log: string
  ) => void;
}

export const useAgentStore =
  create<AgentStore>(
    (set) => ({
      runId: "",

      logs: [],

      setRunId: (
        id
      ) =>
        set({
          runId: id
        }),

      addLog: (
        log
      ) =>
        set(
          (
            state
          ) => ({
            logs: [
              ...state.logs,
              log,
            ],
          })
        ),
    })
  );