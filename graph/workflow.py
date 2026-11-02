
from langgraph.graph import StateGraph, START, END

from graph.state import ResearchState
from agents.researcher import researcher_agent
from agents.writer import writer_agent
from agents.reviewer import reviewer_agent


MAX_REVISIONS = 2


def route_after_review(state: ResearchState):
    if state["review_status"] == "approved":
        return END

    if state["revision_count"] >= MAX_REVISIONS:
        return END

    return "writer"


def build_workflow():
    workflow = StateGraph(ResearchState)

    workflow.add_node("researcher", researcher_agent)
    workflow.add_node("writer", writer_agent)
    workflow.add_node("reviewer", reviewer_agent)

    workflow.add_edge(START, "researcher")
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", "reviewer")

    workflow.add_conditional_edges(
        "reviewer",
        route_after_review,
        {
            "writer": "writer",
            END: END
        }
    )

    return workflow.compile()
