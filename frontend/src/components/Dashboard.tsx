import RunSummaryCard
    from "./RunSummaryCard";

import ScoreBreakdown
    from "./ScoreBreakdown";

import FixesTable
    from "./FixesTable";

import CICDTimeline
    from "./CICDTimeline";

import LiveLogs
    from "./LiveLogs";

import {
    useAgentStore,
} from "../store/agentStore";

import {
    useAgentRun,
} from "../hooks/useAgentRun";

import {
    useWebSocket,
} from "../hooks/useWebSocket";



export default function Dashboard() {
    const runId =
        useAgentStore(
            (s) => s.runId
        );
    useWebSocket(runId);
    const {
        data,
        isLoading,
        error,
    } =
        useAgentRun(
            runId
        );

    if (!runId)
        return null;

    if (isLoading)
        return (
            <p>
                Loading...
            </p>
        );

    if (error)
        return (
            <p>
                Error loading
            </p>
        );

    return (

        <div
            className="
      grid
      gap-4"
        >

            <RunSummaryCard
                result={data}
            />

            <ScoreBreakdown
                score={data.score}
            />

            <FixesTable
                fixes={
                    data.fixes || []
                }
            />

            <CICDTimeline
                runs={
                    data.cicd_runs || []
                }
            />

            <LiveLogs />

        </div>

    );
}