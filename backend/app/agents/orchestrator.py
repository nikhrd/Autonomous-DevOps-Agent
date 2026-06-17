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

MAX_RETRIES = int(
    os.getenv(
        "MAX_RETRIES",
        5
    )
)
analyzer = Analyzer()
fixer = FixGenerator()
runner = TestRunner()

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

graph.add_conditional_edges(
    "test",
    route_result,
    {
        "retry": "analyze",
        "done": END
    }
)

workflow = graph.compile()