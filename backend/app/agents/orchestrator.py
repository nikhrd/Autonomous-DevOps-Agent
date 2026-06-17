import os

from langgraph.graph import (
    StateGraph,
    END
)

from app.agents.analyzer import Analyzer
from app.agents.fix_generator import (
    FixGenerator
)

from app.tools.test_runner import (
    TestRunner
)

from app.agents.state import (
    AgentState
)

from app.agents.ci_executor import (
    CIExecutor
)

MAX_RETRIES = int(
    os.getenv(
        "MAX_RETRIES",
        5
    )
)
analyzer = Analyzer()
fixer = FixGenerator()
runner = TestRunner()
ci_executor = CIExecutor()

def analyze_node(
    state: AgentState
):

    results = analyzer.analyze_repository(
        state["repo_path"]
    )

    state["errors"] = results["errors"]

    return state

def fix_node(
    state: AgentState
):

    for error in state["errors"]:

        fixer.apply_fix(
            error
        )

    return state

def test_node(
    state: AgentState
):

    results = runner.run_tests(
        state["repo_path"]
    )

    state["test_passed"] = results["success"]

    return state

def route_result(
    state: AgentState
):

    if state["test_passed"]:
        return "done"

    if state["retries"] >= MAX_RETRIES:
        return "done"

    state["retries"] += 1

    return "retry"

def cicd_node(
    state
):

    result = ci_executor.execute(
        state["repo_url"],
        state["repo_path"]
    )

    state["cicd_status"] = (
        result["status"]
    )

    state["cicd_runs"].append(
        {
            "iteration":
                state["retries"] + 1,

            "status":
                result["status"],

            "timestamp":
                result.get(
                    "updated_at",
                    "LOCAL"
                )
        }
    )

    return state

graph = StateGraph(
    AgentState
)

graph.add_node(
    "analyze",
    analyze_node
)

graph.add_node(
    "fix",
    fix_node
)

graph.add_node(
    "test",
    test_node
)

graph.add_node(
    "cicd",
    cicd_node
)

graph.set_entry_point(
    "analyze"
)

graph.add_edge(
    "analyze",
    "fix"
)

graph.add_edge(
    "fix",
    "test"
)

graph.add_edge(
    "test",
    "cicd"
)

graph.add_conditional_edges(
    "cicd",
    route_result,
    {
        "retry": "analyze",
        "done": END
    }
)

workflow = graph.compile()