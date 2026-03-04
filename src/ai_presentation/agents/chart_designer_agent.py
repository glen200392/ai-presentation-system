"""Chart Designer Agent for creating data visualizations."""

import logging
from typing import Any, Dict, List, Optional
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)


class ChartDesignerAgent(BaseAgent):
    """Creates charts and data visualizations for presentations."""

    name = "ChartDesigner"

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(self.name, config or {})
        logger.info("ChartDesignerAgent initialized")

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute chart creation."""
        return await self.create_charts(input_data)

    async def create_charts(self, data_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create charts from input data.

        Returns:
            dict with key: charts (list of chart specs)
        """
        raw_charts: List[Dict[str, Any]] = data_input.get("charts", [])
        charts: List[Dict[str, Any]] = []

        for spec in raw_charts:
            charts.append(
                {
                    "type": spec.get("type", "bar"),
                    "title": spec.get("title", "Chart"),
                    "data": spec.get("data", {}),
                    "style": spec.get("style", "business_professional"),
                }
            )

        if not charts:
            charts = [
                {
                    "type": "bar",
                    "title": "Overview",
                    "data": {},
                    "style": "business_professional",
                }
            ]

        self.log_info(f"Created {len(charts)} chart(s)")
        return {"charts": charts}
