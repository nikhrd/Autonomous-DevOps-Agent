import {
  useEffect,
} from "react";

import {
  useAgentStore,
} from "../store/agentStore";

export function useWebSocket(
  runId: string
) {

  const addLog =
    useAgentStore(
      (s) => s.addLog
    );

  useEffect(() => {

    if (!runId)
      return;

    const ws =
      new WebSocket(
        `ws://localhost:8000/ws/${runId}`
      );

    ws.onmessage =
      (event) => {

        try {

          const data =
            JSON.parse(
              event.data
            );

          addLog(
            data.message
          );

        } catch {

          addLog(
            event.data
          );
        }
      };

    ws.onerror =
      () => {

        addLog(
          "WebSocket Error"
        );
      };

    return () =>
      ws.close();

  }, [
    runId,
    addLog,
  ]);
}