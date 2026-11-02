
from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.3
)


def researcher_agent(state):
    topic = state["topic"]

    prompt = f"""
    You are the Research Agent in a multi-agent system.

    Your responsibility:
    - Research the given topic.
    - Identify important concepts.
    - Explain key points in simple language.
    - Provide useful examples.
    - Organize the findings into clear sections.

    Rules:
    - Do not invent statistics or references.
    - If you are uncertain about a fact, clearly mention it.
    - Do not write the final report.

    Research Topic: {topic}

    Prepare structured research notes for the Writer Agent.
    """

    response = llm.invoke(prompt)

    research = response.content

    print("\n[RESEARCH AGENT] Research completed.")

    return {
        "research": research,
        "trace": state["trace"] + [
            "Research Agent: Collected and organized topic information."
        ]
    }
