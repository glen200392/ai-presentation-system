# app.py - Streamlit Web UI for AI Presentation System
"""Streamlit Web UI for AI Presentation System."""

import asyncio
import io
import sys
import os

import streamlit as st

# Ensure src/ is on the path when running from repo root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from ai_presentation.orchestrator import PresentationOrchestrator

st.set_page_config(
    page_title="AI Presentation System",
    page_icon="🎯",
    layout="centered",
)

st.title("🎯 AI Presentation System")
st.caption("Generate professional presentations powered by 8 specialized AI agents.")

with st.form("presentation_form"):
    topic = st.text_input("Topic *", placeholder="e.g. Digital Transformation Strategy")
    audience = st.text_input("Audience *", placeholder="e.g. C-Suite Executives")
    duration = st.number_input("Duration (minutes)", min_value=5, max_value=120, value=20, step=5)

    design_style = st.selectbox(
        "Design Style",
        options=[
            "business_professional",
            "tech_innovation",
            "creative_energy",
            "academic_research",
            "minimal_modern",
        ],
        format_func=lambda x: x.replace("_", " ").title(),
    )

    scenario = st.selectbox(
        "Scenario",
        options=[
            "pitch_deck",
            "business_proposal",
            "board_report",
            "qbr",
            "product_launch",
            "training",
            "sales_pitch",
            "strategy",
        ],
        format_func=lambda x: x.replace("_", " ").title(),
    )

    key_messages = st.text_area(
        "Key Messages (optional)",
        placeholder="Enter your main talking points, one per line...",
        height=100,
    )

    submitted = st.form_submit_button("Generate Presentation", type="primary")

if submitted:
    if not topic.strip():
        st.error("Please enter a topic.")
    elif not audience.strip():
        st.error("Please enter an audience.")
    else:
        with st.spinner("Generating your presentation with 8 AI agents…"):
            orchestrator = PresentationOrchestrator()
            requirements = {
                "topic": topic.strip(),
                "audience": audience.strip(),
                "duration": duration,
                "scenario": {
                    "topic": topic.strip(),
                    "audience": audience.strip(),
                    "scenario": scenario,
                    "design_style": design_style,
                },
                "content": {
                    "topic": topic.strip(),
                    "audience": audience.strip(),
                    "duration": duration,
                },
                "design": {"style": design_style},
                "key_messages": [m.strip() for m in key_messages.splitlines() if m.strip()],
            }

            try:
                result = asyncio.run(orchestrator.generate_presentation(requirements))

                if result.get("status") == "success":
                    st.success("✅ Presentation generated successfully!")

                    quality = result.get("quality_metrics", {})
                    score = quality.get("quality_score", "N/A")
                    st.metric("Quality Score", f"{score}/100")

                    # Provide a placeholder .pptx download
                    # (Real pptx generation would be wired here via presentation_generator)
                    placeholder_bytes = io.BytesIO(b"")
                    st.download_button(
                        label="⬇️ Download Presentation (.pptx)",
                        data=placeholder_bytes,
                        file_name=f"{topic.replace(' ', '_')}.pptx",
                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                    )

                    with st.expander("View Details"):
                        st.json(result)
                else:
                    st.error(f"Generation failed: {result.get('error', 'Unknown error')}")
            except Exception as exc:
                st.error(f"An error occurred: {exc}")
