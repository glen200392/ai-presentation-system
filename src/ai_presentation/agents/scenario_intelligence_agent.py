"""Scenario Intelligence Agent for analyzing presentation scenarios."""

import logging
from typing import Any, Dict, Optional
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

_DEFAULT_STRUCTURES = {
    "pitch_deck": ["Problem", "Solution", "Market", "Business Model", "Team", "Ask"],
    "business_proposal": [
        "Executive Summary",
        "Background",
        "Proposal",
        "Benefits",
        "Timeline",
        "Next Steps",
    ],
    "board_report": [
        "Executive Summary",
        "KPIs",
        "Financials",
        "Strategic Updates",
        "Risks",
        "Recommendations",
    ],
    "qbr": ["Quarter Recap", "KPI Review", "Wins", "Challenges", "Q+1 Plan"],
    "product_launch": [
        "Vision",
        "Product Overview",
        "Features",
        "Market Fit",
        "GTM",
        "Roadmap",
    ],
    "training": [
        "Objectives",
        "Content Modules",
        "Activities",
        "Assessment",
        "Resources",
    ],
    "sales_pitch": ["Hook", "Pain Points", "Solution", "Proof", "Pricing", "CTA"],
    "strategy": [
        "Context",
        "Vision",
        "Goals",
        "Initiatives",
        "Resources",
        "Milestones",
    ],
}


class ScenarioIntelligenceAgent(BaseAgent):
    """Analyzes presentation scenario and recommends optimal structure."""

    name = "ScenarioIntelligence"

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(self.name, config or {})
        logger.info("ScenarioIntelligenceAgent initialized")

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute scenario analysis."""
        return await self.analyze_scenario(input_data)

    async def analyze_scenario(self, requirements: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze presentation scenario and return structured recommendations.

        Returns:
            dict with keys: scenario_type, audience, recommended_structure,
            narrative_recommendation, design_style
        """
        scenario_type = requirements.get("scenario", "strategy")
        audience = requirements.get("audience", "general")
        topic = requirements.get("topic", "")
        design_style = requirements.get("design_style", "business_professional")

        structure = _DEFAULT_STRUCTURES.get(
            scenario_type, _DEFAULT_STRUCTURES["strategy"]
        )

        self.log_info(f"Analyzed scenario: {scenario_type} for topic: {topic}")

        return {
            "scenario_type": scenario_type,
            "audience": audience,
            "recommended_structure": structure,
            "narrative_recommendation": "problem_solution",
            "design_style": design_style,
        }
