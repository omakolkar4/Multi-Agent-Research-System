
import streamlit as st
from graph.workflow import build_workflow


# Page configuration
st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🤖",
    layout="wide"
)

# Application heading
st.title("🤖 AI Multi-Agent Research System")

st.write(
    "Three AI agents collaborate to research, write, "
    "and review a report using LangGraph."
)

st.divider()

# Research topic input
st.subheader("Enter Your Research Topic")

topic = st.text_area(
    "Research topic",
    placeholder="Example: Impact of Artificial Intelligence on Education",
    height=100
)

# Failure simulation option
st.subheader("Testing Options")

simulate_failure = st.checkbox(
    "Enable failure and recovery demonstration",
    value=False,
    help=(
        "The first draft will deliberately miss its conclusion. "
        "The Reviewer Agent should detect the issue and send it "
        "back to the Writer Agent for revision."
    )
)

if simulate_failure:
    st.info(
        "Failure simulation is enabled. "
        "The first draft will be created without a conclusion."
    )

st.divider()

# Generate report
if st.button("Generate Research Report", type="primary"):

    if not topic.strip():
        st.warning("Please enter a research topic.")

    else:

        # Initial workflow state
        initial_state = {
            "topic": topic.strip(),
            "research": "",
            "draft": "",
            "feedback": "",
            "review_status": "",
            "revision_count": 0,
            "trace": [],
            "final_report": "",
            "simulate_failure": simulate_failure,
            "failure_injected": False
        }

        try:
            with st.spinner(
                "Researcher, Writer, and Reviewer Agents are collaborating..."
            ):
                workflow = build_workflow()
                result = workflow.invoke(initial_state)

            st.success("Multi-agent execution completed!")

            # Agent execution trace
            st.subheader("🔄 Agent Execution Trace")

            for index, step in enumerate(result["trace"], 1):
                st.write(f"**{index}.** {step}")

            st.divider()

            # Final report
            st.subheader("📄 Final Research Report")

            report = result["final_report"] or result["draft"]

            st.markdown(report)

            # Download report
            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name="research_report.txt",
                mime="text/plain"
            )

            st.divider()

            # Execution summary
            st.subheader("📊 Execution Summary")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Review Attempts",
                result["revision_count"]
            )

            col2.metric(
                "Review Status",
                result["review_status"].upper()
            )

            col3.metric(
                "Failure Simulation",
                "Enabled" if simulate_failure else "Disabled"
            )

            # Failure and recovery result
            if simulate_failure:

                st.divider()
                st.subheader("🛠️ Failure and Recovery Result")

                if (
                    result.get("failure_injected")
                    and result["revision_count"] >= 2
                    and result["review_status"] == "approved"
                ):
                    st.success(
                        "Failure detected and successfully recovered! "
                        "The Reviewer Agent rejected the incomplete draft, "
                        "and the Writer Agent corrected it."
                    )

                elif result["review_status"] == "approved":
                    st.info(
                        "The report was approved. Check the execution trace "
                        "to confirm that the missing conclusion was detected "
                        "and corrected."
                    )

                else:
                    st.warning(
                        "The report was not approved within the configured "
                        "review attempts. Check the execution trace."
                    )

        except Exception as error:
            st.error(f"An error occurred: {error}")
