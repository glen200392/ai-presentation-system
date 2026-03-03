"""Streamlit Web UI for AI Presentation System."""

import asyncio
import io
import logging

import streamlit as st

logger = logging.getLogger(__name__)

DESIGN_STYLES = [
    "business_professional",
    "tech_innovation",
    "creative_energy",
    "academic_research",
    "minimal_modern",
]

SCENARIOS = [
    "pitch_deck",
    "business_proposal",
    "board_report",
    "qbr",
    "product_launch",
    "training",
    "sales_pitch",
    "strategy",
]


def run_generation(requirements: dict) -> dict:
    """Run the async generation pipeline in a sync context."""
    import sys
    import os

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
    from ai_presentation.orchestrator import PresentationOrchestrator

    orchestrator = PresentationOrchestrator()
    return asyncio.run(orchestrator.generate_presentation(requirements))


def main():
    """Main Streamlit application entry point."""
    st.set_page_config(
        page_title="AI Presentation System",
        page_icon="🎯",
        layout="centered",
    )

    st.title("🎯 AI Presentation System")
    st.markdown(
        "Generate professional presentations in minutes using **8 specialized AI agents**."
    )

    with st.form("generation_form"):
        st.subheader("Presentation Details")

        topic = st.text_input(
            "Topic *",
            placeholder="e.g. Digital Transformation Strategy for Q1 2026",
        )
        audience = st.text_input(
            "Audience *",
            placeholder="e.g. C-Suite Executives",
        )
        duration = st.number_input(
            "Duration (minutes)",
            min_value=5,
            max_value=120,
            value=20,
            step=5,
        )
        design_style = st.selectbox("Design Style", DESIGN_STYLES)
        scenario = st.selectbox("Scenario", SCENARIOS)
        key_messages = st.text_area(
            "Key Messages (optional)",
            placeholder="Enter your key messages, one per line…",
            height=100,
        )

        submitted = st.form_submit_button("🚀 Generate Presentation")

    if submitted:
        if not topic.strip():
            st.error("Please enter a topic.")
            return
        if not audience.strip():
            st.error("Please enter an audience.")
            return

        requirements = {
            "topic": topic.strip(),
            "scenario": {
                "topic": topic.strip(),
                "audience": audience.strip(),
                "duration": duration,
                "design_style": design_style,
                "scenario_type": scenario,
            },
            "content": {
                "topic": topic.strip(),
                "key_messages": [m.strip() for m in key_messages.splitlines() if m.strip()],
            },
            "design": {"style": design_style, "slides": max(5, duration // 2)},
        }

        with st.spinner("⏳ Generating your presentation (this may take a moment)…"):
            try:
                result = run_generation(requirements)
            except Exception as exc:
                st.error(f"Generation failed: {exc}")
                logger.exception("Presentation generation error")
                return

        if result.get("status") == "success":
            st.success("✅ Presentation generated successfully!")

            with st.expander("📊 Quality Metrics"):
                metrics = result.get("quality_metrics", {})
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Overall Score", f"{metrics.get('overall_score', 'N/A')}/100")
                with col2:
                    st.metric("Passed QA", "✅ Yes" if metrics.get("passed") else "❌ No")

            # TODO: Replace placeholder with real .pptx bytes once PresentationGenerator
            # (python-pptx integration) is wired up to the orchestrator result.
            placeholder_bytes = io.BytesIO(b"placeholder pptx content")
            st.download_button(
                label="⬇️ Download Presentation (.pptx)",
                data=placeholder_bytes,
                file_name=f"{topic[:40].replace(' ', '_')}.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            )
        else:
            error_msg = result.get("error", "Unknown error")
            st.error(f"❌ Generation failed: {error_msg}")
            if result.get("partial_results"):
                with st.expander("Partial results"):
                    st.json(result["partial_results"])


if __name__ == "__main__":
    main()
