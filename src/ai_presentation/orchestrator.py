"""Main Orchestrator for coordinating presentation generation workflow."""

import logging
import asyncio
from typing import Dict, Any, Optional
from .agents import (
    ScenarioIntelligenceAgent,
    ContentStrategistAgent,
    ResearchAnalystAgent,
    VisualDesignerAgent,
    ChartDesignerAgent,
    QualityAssuranceAgent,
)

logger = logging.getLogger(__name__)

AGENT_TIMEOUT = 60
MAX_RETRIES = 2

DEFAULT_VISUAL_RESULT = {
    "style": "business_professional",
    "color_palette": ["#1E3A8A", "#3B82F6", "#FFFFFF"],
    "typography": {"heading": "Calibri", "body": "Calibri"},
    "layout_templates": [],
}

DEFAULT_CHART_RESULT = {
    "charts": [],
}

DEFAULT_CITATION_RESULT = {
    "citations": [],
    "formatted": [],
}


async def _run_with_retry(coro_fn, max_retries: int = MAX_RETRIES, timeout: int = AGENT_TIMEOUT):
    """Run a coroutine with retry and timeout logic."""
    last_error = None
    for attempt in range(max_retries + 1):
        try:
            return await asyncio.wait_for(coro_fn(), timeout=timeout)
        except asyncio.TimeoutError as e:
            last_error = e
            logger.warning(f"Agent timed out (attempt {attempt + 1}/{max_retries + 1})")
        except Exception as e:
            last_error = e
            logger.warning(f"Agent failed (attempt {attempt + 1}/{max_retries + 1}): {e}")
        if attempt < max_retries:
            await asyncio.sleep(2 ** attempt)
    raise last_error


class PresentationOrchestrator:
    """
    Main orchestrator that coordinates all agents in the presentation generation workflow.
    Manages agent execution, data flow, and overall presentation assembly.
    """

    def __init__(self):
        """Initialize orchestrator with all required agents."""
        self.scenario_agent = ScenarioIntelligenceAgent()
        self.strategy_agent = ContentStrategistAgent()
        self.research_agent = ResearchAnalystAgent()
        self.visual_agent = VisualDesignerAgent()
        self.chart_agent = ChartDesignerAgent()
        self.qa_agent = QualityAssuranceAgent()
        logger.info("PresentationOrchestrator initialized with 8 agents")

    async def generate_presentation(
        self,
        requirements: Dict[str, Any],
        document_path: Optional[str] = None,
        document_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Generate complete presentation from user requirements.

        Args:
            requirements: User requirements and input data
            document_path: Optional path to a document for ingestion
            document_url: Optional URL for document ingestion

        Returns:
            Complete presentation object
        """
        logger.info("Starting presentation generation workflow")

        # Optional document ingestion
        if document_path or document_url:
            try:
                from .agents.document_ingestion_agent import DocumentIngestionAgent
                ingestion_agent = DocumentIngestionAgent()
                source = document_path or document_url
                ingestion_result = await _run_with_retry(
                    lambda: ingestion_agent.ingest(source)
                )
                requirements["raw_text"] = ingestion_result.get("raw_text", "")
                logger.info("Document ingestion completed")
            except Exception as e:
                logger.warning(f"Document ingestion failed, continuing without it: {e}")

        try:
            # Step 1: Analyze scenario (critical)
            scenario = await _run_with_retry(
                lambda: self.scenario_agent.analyze_scenario(
                    requirements.get("scenario", {})
                )
            )
            logger.info("Scenario analysis completed")

            # Step 2: Develop content strategy (critical)
            strategy = await _run_with_retry(
                lambda: self.strategy_agent.develop_strategy(
                    requirements.get("content", {})
                )
            )
            logger.info("Content strategy developed")

            # Step 3: Conduct research (critical)
            research = await _run_with_retry(
                lambda: self.research_agent.conduct_research(
                    requirements.get("topic", ""),
                    requirements.get("research_requirements", {}),
                )
            )
            logger.info("Research completed")

            # Step 4: Design visuals (non-critical - graceful degradation)
            try:
                design = await _run_with_retry(
                    lambda: self.visual_agent.design_presentation(
                        requirements.get("design", {})
                    )
                )
                logger.info("Visual design completed")
            except Exception as e:
                logger.warning(f"Visual design failed after retries, using defaults: {e}")
                design = DEFAULT_VISUAL_RESULT

            # Step 5: Create charts (non-critical - graceful degradation)
            try:
                charts = await _run_with_retry(
                    lambda: self.chart_agent.create_charts(
                        requirements.get("data", {})
                    )
                )
                logger.info("Charts created")
            except Exception as e:
                logger.warning(f"Chart creation failed after retries, using defaults: {e}")
                charts = DEFAULT_CHART_RESULT

            # Step 6: Quality assurance (critical)
            presentation = {
                "scenario": scenario,
                "strategy": strategy,
                "research": research,
                "design": design,
                "charts": charts,
            }

            qa_result = await _run_with_retry(
                lambda: self.qa_agent.review_presentation(presentation)
            )
            logger.info("Quality assurance completed")

            return {
                "status": "success",
                "presentation": presentation,
                "quality_metrics": qa_result,
            }

        except Exception as e:
            logger.error(f"Error during presentation generation: {e}")
            return {
                "status": "error",
                "error": str(e),
                "partial_results": {},
            }

    async def execute(self) -> Dict[str, Any]:
        """Execute orchestrator."""
        return {"status": "ready", "orchestrator": "PresentationOrchestrator"}
