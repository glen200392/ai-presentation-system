"""Base agent class for all AI Presentation System agents."""

import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Any, Dict

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """Abstract base class for all AI agents."""

    def __init__(self, name: str = None, config: dict = None):
        """Initialize base agent."""
        self.name = name or self.__class__.__name__
        self.config = config or {}
        logger.debug(f"Initializing agent: {self.name}")

    @abstractmethod
    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Main async execution method - must be implemented by subclasses."""
        raise NotImplementedError("Subclass must implement execute() method")

    async def execute_with_retry(
        self, input_data: Dict[str, Any], max_retries: int = 3
    ) -> Dict[str, Any]:
        """Execute with exponential backoff retry logic."""
        last_error = None
        for attempt in range(max_retries):
            try:
                return await self.execute(input_data)
            except Exception as e:
                last_error = e
                wait = 2 ** attempt
                logger.warning(
                    f"[{self.name}] attempt {attempt + 1}/{max_retries} failed: {e}; "
                    f"retrying in {wait}s"
                )
                if attempt < max_retries - 1:
                    await asyncio.sleep(wait)
        raise last_error

    def validate_input(self, data: dict) -> bool:
        """Validate input data."""
        return data is not None and isinstance(data, dict)

    def log_info(self, message: str):
        """Log info message."""
        logger.info(f"[{self.name}] {message}")

    def log_error(self, message: str):
        """Log error message."""
        logger.error(f"[{self.name}] {message}")

    # Legacy sync stub for backward compatibility
    def process(self, *args, **kwargs):
        """Legacy processing method - prefer execute()."""
        raise NotImplementedError("Subclass must implement process() method")
