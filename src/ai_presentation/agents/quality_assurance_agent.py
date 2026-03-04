"""Quality Assurance Agent for validating presentation quality."""

import logging
from typing import Any, Dict, List, Optional
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)


class QualityAssuranceAgent(BaseAgent):
    """Reviews presentation and produces quality report."""

    name = "QualityAssurance"

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(self.name, config or {})
        logger.info("QualityAssuranceAgent initialized")

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute quality review."""
        return await self.review_presentation(input_data)

    async def review_presentation(self, presentation: Dict[str, Any]) -> Dict[str, Any]:
        """
        Review presentation quality.

        Returns:
            dict with keys: quality_score (0-100), issues, passed
        """
        issues: List[Dict[str, Any]] = []
        score = 90

        if not presentation.get("scenario"):
            issues.append({"severity": "high", "message": "Missing scenario analysis"})
            score -= 20
        if not presentation.get("strategy"):
            issues.append({"severity": "high", "message": "Missing content strategy"})
            score -= 20
        if not presentation.get("design"):
            issues.append({"severity": "medium", "message": "Missing visual design"})
            score -= 10
        if not presentation.get("charts"):
            issues.append({"severity": "low", "message": "No charts provided"})
            score -= 5

        score = max(0, score)
        passed = score >= 70

        self.log_info(f"QA review complete: score={score}, passed={passed}")

        return {
            "quality_score": score,
            "issues": issues,
            "passed": passed,
        }
