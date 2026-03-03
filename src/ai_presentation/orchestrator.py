"""Main Orchestrator for coordinating presentation generation workflow."""

import asyncio
import logging
from typing import Any, Dict, Optional

from .agents import (
    ChartDesignerAgent,
    ContentStrategistAgent,
    QualityAssuranceAgent,
    ResearchAnalystAgent,
    ScenarioIntelligenceAgent,
    VisualDesignerAgent,
)

logger = logging.getLogger(__name__)

AGENT_TIMEOUT = 60
MAX_RETRIES = 2

DEFAULT_VISUAL_RESULT = {
    "layout": {"slide_count": 10, "layout_types": ["Title", "Content"]},
    "colors": {"primary": ["#1f77b4"], "secondary": ["#ff7f0e"]},
    "typography": {"heading_font": "Arial Bold", "body_font": "Arial"},
    "visual_hierarchy": ["Title prominence", "Content organization"],
}

DEFAULT_CHART_RESULT = {
    "analysis": {"data_type": "numeric", "dimensions": 2, "data_points": 0},
    "charts": ["Bar Chart"],
    "visualizations": {"style": "modern"},
    "interactivity": {"hover": True},
}

DEFAULT_CITATION_RESULT = {
    "citations": [],
    "formatted_references": [],
}


async def _run_with_retry(coro_func, *args, retries: int = MAX_RETRIES, timeout: int = AGENT_TIMEOUT, **kwargs):
    """Run a coroutine with retry and timeout logic."""
    last_exc = None
    for attempt in range(retries + 1):
        try:
            return await asyncio.wait_for(coro_func(*args, **kwargs), timeout=timeout)
        except asyncio.TimeoutError as e:
            last_exc = e
            logger.warning(f"Agent timed out (attempt {attempt + 1}/{retries + 1})")
        except Exception as e:
            last_exc = e
            logger.warning(f"Agent failed (attempt {attempt + 1}/{retries + 1}): {e}")
        if attempt < retries:
            await asyncio.sleep(2 ** attempt)
    raise last_exc


class PresentationOrchestrator:
    """Main orchestrator that coordinates all agents in the presentation generation workflow."""

    def __init__(self):
        """Initialize orchestrator with all required agents."""
        self.scenario_agent = ScenarioIntelligenceAgent()
        self.strategy_agent = ContentStrategistAgent()
        self.research_agent = ResearchAnalystAgent()
        self.visual_agent = VisualDesignerAgent()
        self.chart_agent = ChartDesignerAgent()
        self.qa_agent = QualityAssuranceAgent()
        logger.info("PresentationOrchestrator initialized with 6 core agents")

    async def generate_presentation(
        self,
        requirements: Dict[str, Any],
        document_path: Optional[str] = None,
        document_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generate complete presentation from user requirements.

        Args:
            requirements: User requirements and input data
            document_path: Optional path to a source document (PDF/DOCX/TXT)
            document_url: Optional URL to ingest content from

        Returns:
            Complete presentation object
        """
        logger.info("Starting presentation generation workflow")

        if document_path or document_url:
            try:
                from .agents.document_ingestion_agent import DocumentIngestionAgent
                ingestion_agent = DocumentIngestionAgent()
                source = document_path or document_url
                ingested = await _run_with_retry(ingestion_agent.ingest, source)
                requirements["raw_text"] = ingested.get("raw_text", "")
                logger.info("Document ingestion completed")
            except Exception as e:
                logger.warning(f"Document ingestion failed, continuing without it: {e}")

        partial_results: Dict[str, Any] = {}
        try:
            # Step 1: Analyze scenario (critical)
            scenario = await _run_with_retry(
                self.scenario_agent.analyze_scenario,
                requirements.get("scenario", {}),
            )
            partial_results["scenario"] = scenario
            logger.info("Scenario analysis completed")

            # Step 2: Develop content strategy (critical)
            strategy = await _run_with_retry(
                self.strategy_agent.develop_strategy,
                requirements.get("content", {}),
            )
            partial_results["strategy"] = strategy
            logger.info("Content strategy developed")

            # Step 3: Conduct research (critical)
            research = await _run_with_retry(
                self.research_agent.conduct_research,
                requirements.get("topic", ""),
                requirements.get("research_requirements", {}),
            )
            partial_results["research"] = research
            logger.info("Research completed")

        except Exception as e:
            logger.error(f"Critical agent failed: {e}")
            return {"status": "error", "error": str(e), "partial_results": partial_results}

        # Step 4: Design visuals (non-critical)
        try:
            design = await _run_with_retry(
                self.visual_agent.design_presentation,
                requirements.get("design", {}),
            )
            logger.info("Visual design completed")
        except Exception as e:
            logger.warning(f"Visual agent failed, using default: {e}")
            design = DEFAULT_VISUAL_RESULT

        # Step 5: Create charts (non-critical)
        try:
            charts = await _run_with_retry(
                self.chart_agent.create_charts,
                requirements.get("data", {}),
            )
            logger.info("Charts created")
        except Exception as e:
            logger.warning(f"Chart agent failed, using default: {e}")
            charts = DEFAULT_CHART_RESULT

        presentation = {
            "scenario": partial_results["scenario"],
            "strategy": partial_results["strategy"],
            "research": partial_results["research"],
            "design": design,
            "charts": charts,
        }

        # Step 6: Quality assurance (critical)
        try:
            qa_result = await _run_with_retry(
                self.qa_agent.review_presentation,
                presentation,
            )
            logger.info("Quality assurance completed")
        except Exception as e:
            logger.error(f"QA agent failed: {e}")
            return {"status": "error", "error": str(e), "partial_results": presentation}

        return {
            "status": "success",
            "presentation": presentation,
            "quality_metrics": qa_result,
        }

    async def execute(self) -> Dict[str, Any]:
        """Execute orchestrator."""
        return {"status": "ready", "orchestrator": "PresentationOrchestrator"}
