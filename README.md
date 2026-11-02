# AI Multi-Agent Research and Report Generation System

## 1. Project Overview

The AI Multi-Agent Research and Report Generation System is a Python-based application in which three AI agents collaborate to generate a structured research report.

The system uses **LangGraph** to manage communication and task handoffs between the agents. A locally hosted Qwen 2.5 3B model, through Ollama, powers the agents.

The three agents are:

- **Research Agent:** Collects and organizes information about the given topic.
- **Writer Agent:** Converts the research notes into a structured report.
- **Reviewer Agent:** Checks the report, identifies missing sections, and provides feedback for improvements.

## 2. Project Objectives

- Understand how multiple AI agents collaborate on a shared task.
- Assign separate responsibilities to individual agents.
- Implement communication and handoffs using LangGraph.
- Generate structured research reports.
- Detect errors through a review process.
- Demonstrate feedback-based revision and recovery.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| LangGraph | Agent workflow and coordination |
| LangChain | LLM integration |
| Ollama | Local model execution |
| Qwen 2.5 3B | Language model |
| Streamlit | Web application interface |

## 4. System Architecture

The system follows this workflow:

1. The user enters a research topic.
2. The Research Agent collects and organizes information.
3. The Writer Agent prepares a structured report.
4. The Reviewer Agent checks the report.
5. If improvements are required, feedback is sent to the Writer Agent.
6. The Writer Agent revises the report.
7. The Reviewer Agent checks the revised report and provides the final verdict.

**Workflow:** User → Research Agent → Writer Agent → Reviewer Agent → Writer Agent (if revision is needed) → Reviewer Agent → Final Report.

The workflow allows a maximum of two review attempts.

## 5. Failure and Recovery Demonstration

The project includes a controlled failure simulation.

During this test, the first report draft is deliberately generated without a Conclusion section.

The Reviewer Agent detects the missing section and returns a REVISE verdict. The Writer Agent receives the feedback, updates the report, and adds the missing conclusion. The Reviewer Agent then reviews the revised report and approves it.

This demonstrates how feedback and collaboration between agents can help identify and correct errors.

## 6. Project Structure

```text
Multi_Agent_Research_System/
│
├── agents/
│   ├── researcher.py
│   ├── writer.py
│   └── reviewer.py
│
├── graph/
│   ├── state.py
│   └── workflow.py
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 7. Installation and Execution

### Prerequisites

- Python installed
- Ollama installed
- Qwen 2.5 3B model downloaded

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Multi_Agent_Research_System
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Download the model

```bash
ollama pull qwen2.5:3b
```

Ensure the Ollama service is running.

### Step 6: Run the terminal application

```bash
python main.py
```

### Step 7: Run the Streamlit application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## 8. Example Research Topic

```text
Impact of Artificial Intelligence on Education
```

The system generates research notes, prepares a report, and reviews the report before presenting the final output.

## 9. Limitations

- The system uses a locally hosted language model.
- Research is generated from the model's internal knowledge and supplied prompts; live web research is not implemented.
- References and statistics are not independently verified against external sources.
- Output quality depends on the language model.

## 10. Conclusion

This project demonstrates how multiple AI agents can work together to complete a shared task. By separating research, writing, and reviewing responsibilities, the system creates a structured workflow. The failure simulation also demonstrates how agents can use feedback to identify and correct an incomplete report.

