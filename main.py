
from graph.workflow import build_workflow


def main():
    print("=" * 60)
    print("AI MULTI-AGENT RESEARCH AND REPORT GENERATION SYSTEM")
    print("=" * 60)

    topic = input("\nEnter your research topic: ").strip()

    if not topic:
        print("Please enter a valid topic.")
        return

    app = build_workflow()

    initial_state = {
    "topic": topic,
    "research": "",
    "draft": "",
    "feedback": "",
    "review_status": "",
    "revision_count": 0,
    "trace": [],
    "final_report": "",
    "simulate_failure": True,
    "failure_injected": False
}
    

    print("\nStarting multi-agent collaboration...\n")

    result = app.invoke(initial_state)

    print("\n" + "=" * 60)
    print("AGENT EXECUTION TRACE")
    print("=" * 60)

    for step in result["trace"]:
        print("\n- " + step)

    print("\n" + "=" * 60)
    print("FINAL REPORT")
    print("=" * 60)

    report = result["final_report"] or result["draft"]
    print(report)

    print("\n" + "=" * 60)
    print("EXECUTION SUMMARY")
    print("=" * 60)

    print("Topic:", topic)
    print("Review status:", result["review_status"])
    print("Review attempts:", result["revision_count"])


if __name__ == "__main__":
    main()
