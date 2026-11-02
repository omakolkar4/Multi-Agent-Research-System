import re
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5:3b", temperature=0.4)


def writer_agent(state):
    topic = state["topic"]
    research = state["research"]
    feedback = state.get("feedback", "")

    prompt = f"""
    You are the Writer Agent in a multi-agent research system.

    Write a complete report about: {topic}

    Use these research notes:
    {research}

    Reviewer feedback:
    {feedback if feedback else "Create the first draft."}

    Requirements:
    - Include an Introduction.
    - Include clear main sections.
    - Include a Conclusion.
    - Address the reviewer's feedback.
    - Do not invent statistics or references.
    - Use simple and understandable language.
    """

    response = llm.invoke(prompt)
    draft = response.content.strip()

    failure_injected = state.get("failure_injected", False)

    # Controlled test: deliberately remove the conclusion from the first draft.
    if state.get("simulate_failure", False) and not failure_injected:
        draft = re.split(
            r"(?im)^\s*#{0,6}\s*Conclusion\s*$",
            draft,
            maxsplit=1
        )[0].strip()

        failure_injected = True

        print("\n[WRITER AGENT] Test failure injected: Conclusion removed.")

        trace_message = (
            "Writer Agent: Created the first draft with a deliberately "
            "missing conclusion for failure testing."
        )

    else:
        # Ensure the revised draft contains a conclusion.
        if not re.search(r"(?im)^\s*#{0,6}\s*Conclusion\s*$", draft):
            draft += (
                "\n\n## Conclusion\n\n"
                f"In conclusion, {topic} requires careful consideration. "
                "The key findings should be applied thoughtfully, while "
                "addressing the challenges and limitations identified "
                "in the research."
            )

        print("\n[WRITER AGENT] Report draft created or revised.")

        trace_message = (
            "Writer Agent: Prepared or revised the report using reviewer feedback."
        )

    return {
        "draft": draft,
        "failure_injected": failure_injected,
        "trace": state["trace"] + [trace_message]
    }