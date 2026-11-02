from typing import TypedDict, List

class ResearchState(TypedDict):
    topic: str
    research: str
    draft: str
    feedback: str
    review_status: str
    revision_count: int
    trace: List[str]
    final_report: str
    simulate_failure: bool
    failure_injected: bool