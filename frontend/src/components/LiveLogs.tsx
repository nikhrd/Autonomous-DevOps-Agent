import {
  useAgentStore,
} from "../store/agentStore";

export default function LiveLogs() {

  const logs =
    useAgentStore(
      (s) => s.logs
    );

  return (

    <div
      className="
      border
      rounded
      p-4
      h-64
      overflow-auto"
    >

      <h2
        className="font-bold mb-2"
      >
        Live Logs
      </h2>

      {logs.map(
        (
          log,
          index
        ) => (

          <div
            key={index}
            className="
            text-sm
            border-b
            py-1"
          >
            {log}
          </div>

        )
      )}

    </div>

  );
}