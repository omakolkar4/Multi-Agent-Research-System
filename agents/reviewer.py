import re
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5:3b", temperature=0)


def reviewer_agent(state):
    topic = state["topic"]
    draft = state["draft"]
    revision_count = state["revision_count"]

    # Deterministic structural check.
    has_conclusion = bool(
        re.search(r"(?im)^\s*#{0,6}\s*Conclusion\s*$", draft)
    )

    if not has_conclusion:
        status = "revise"
        feedback = (
            "VERDICT: REVISE\n"
            "FEEDBACK: The report is missing its Conclusion section. "
            "Please add a clear conclusion summarizing the main findings."
        )

        print("\n[REVIEWER AGENT] Verdict: REVISE")
        print("[REVIEWER AGENT] Missing Conclusion detected.")

    else:
        prompt = f"""
        You are the Reviewer Agent.

        Review this report about: {topic}

        Check:
        1. Does it address the given topic?
        2. Is it properly structured?
        3. Are explanations clear?
        4. Are there unsupported statistics or references?
        5. Is there a proper conclusion?

        Report:
        {draft}

        Return your response in this exact format:

        VERDICT: APPROVED
        FEEDBACK: The report meets the requirements.

        OR

        VERDICT: REVISE
        FEEDBACK: Explain the specific improvements required.

        Do not claim that facts are externally verified.
        """

        response = llm.invoke(prompt)
        feedback = response.content.strip()

        match = re.search(
            r"(?im)^\s*VERDICT:\s*(APPROVED|REVISE)\b",
            feedback
        )

        status = match.group(1).lower() if match else "revise"

        if not match:
            feedback = (
                "VERDICT: REVISE\n"
                "FEEDBACK: The review response did not contain a valid verdict. "
                "Please check and revise the report."
            )

        print(f"\n[REVIEWER AGENT] Verdict: {status.upper()}")

    return {
        "review_status": status,
        "feedback": feedback,
        "revision_count": revision_count + 1,
        "final_report": draft if status == "approved" else "",
        "trace": state["trace"] + [
            f"Reviewer Agent: {status.upper()} - {feedback}"
        ]
    }