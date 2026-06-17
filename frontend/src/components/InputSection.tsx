import { useState } from "react";

import api from "../api/agentApi";

import { useAgentStore } from "../store/agentStore";
import {
  runAgent,
} from "../api/agentApi";

export default function InputSection() {

  const { setRunId } =
    useAgentStore();

  const [repoUrl, setRepoUrl] =
    useState("");

  const [teamName, setTeamName] =
    useState("");

  const [leaderName, setLeaderName] =
    useState("");

  const runAgentHandler =
  async () => {

    try {

      const response =
        await runAgent({
          repo_url:
            repoUrl,

          team_name:
            teamName,

          leader_name:
            leaderName,
        });

      setRunId(
        response.run_id
      );

    } catch (
      error
    ) {

      console.error(
        error
      );
    }
  };

  return (
    <div className="border p-4 rounded">

      <input
        className="border p-2 w-full mb-2"
        placeholder="Repository URL"
        value={repoUrl}
        onChange={(e) =>
          setRepoUrl(
            e.target.value
          )
        }
      />

      <input
        className="border p-2 w-full mb-2"
        placeholder="Team Name"
        value={teamName}
        onChange={(e) =>
          setTeamName(
            e.target.value
          )
        }
      />

      <input
        className="border p-2 w-full mb-2"
        placeholder="Leader Name"
        value={leaderName}
        onChange={(e) =>
          setLeaderName(
            e.target.value
          )
        }
      />

      <button
        onClick={runAgentHandler}
        className="bg-black text-white px-4 py-2"
      >
        Run Agent
      </button>

    </div>
  );
}