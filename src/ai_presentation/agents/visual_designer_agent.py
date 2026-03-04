"""Visual Designer Agent for creating presentation layouts and designs."""

import logging
from typing import Any, Dict, List, Optional
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

_STYLE_PALETTES: Dict[str, List[str]] = {
    "business_professional": ["#1E3A8A", "#3B82F6", "#FFFFFF", "#F1F5F9"],
    "tech_innovation": ["#0F172A", "#6366F1", "#22D3EE", "#F8FAFC"],
    "creative_energy": ["#7C3AED", "#EC4899", "#F59E0B", "#FFFFFF"],
    "academic_research": ["#1E293B", "#475569", "#94A3B8", "#F8FAFC"],
    "minimal_modern": ["#FFFFFF", "#111827", "#6B7280", "#F3F4F6"],
}


class VisualDesignerAgent(BaseAgent):
    """Designs visual framework and style guide for presentations."""

    name = "VisualDesigner"

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(self.name, config or {})
        logger.info("VisualDesignerAgent initialized")

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute visual design."""
        return await self.design_presentation(input_data)

    async def design_presentation(self, design_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Design presentation visual framework.

        Returns:
            dict with keys: style, color_palette, typography, layout_templates
        """
        style = design_input.get("style", "business_professional")
        palette = _STYLE_PALETTES.get(style, _STYLE_PALETTES["business_professional"])

        self.log_info(f"Designing presentation with style: {style}")

        return {
            "style": style,
            "color_palette": palette,
            "typography": {
                "heading": "Calibri Bold",
                "body": "Calibri",
                "accent": "Calibri Light",
            },
            "layout_templates": [
                {"name": "title_slide", "columns": 1},
                {"name": "content_slide", "columns": 2},
                {"name": "data_slide", "columns": 1},
            ],
        }
