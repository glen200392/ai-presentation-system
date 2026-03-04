"""Content Strategist Agent for developing presentation content strategy."""

import logging
from typing import Any, Dict, List, Optional
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)


class ContentStrategistAgent(BaseAgent):
    """Develops content strategy and narrative framework for presentations."""

    name = "ContentStrategist"

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(self.name, config or {})
        logger.info("ContentStrategistAgent initialized")

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute content strategy development."""
        return await self.develop_strategy(input_data)

    async def develop_strategy(self, content_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Develop content strategy based on input.

        Returns:
            dict with keys: narrative_framework, outline, speaker_notes_template,
            qa_questions
        """
        topic = content_input.get("topic", "Presentation Topic")
        audience = content_input.get("audience", "general")
        duration = content_input.get("duration", 20)

        slides_count = max(5, min(20, duration))
        outline: List[Dict[str, Any]] = [
            {
                "slide": i + 1,
                "title": f"Section {i + 1}",
                "content": [],
                "duration_min": 1,
            }
            for i in range(slides_count)
        ]
        if outline:
            outline[0]["title"] = "Introduction"
            outline[-1]["title"] = "Conclusion & Next Steps"

        self.log_info(f"Developed strategy for topic: {topic}, audience: {audience}")

        return {
            "narrative_framework": "problem_solution",
            "outline": outline,
            "speaker_notes_template": f"Speak to {audience} about {topic}.",
            "qa_questions": [
                "What is the main takeaway?",
                "What are the next steps?",
                "What evidence supports this?",
            ],
        }
