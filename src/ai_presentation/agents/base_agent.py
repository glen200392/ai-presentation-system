"""Base agent class for all AI Presentation System agents."""

import asyncio
import logging
from abc import ABC, abstractmethod
from functools import wraps
from typing import Any, Dict

logger = logging.getLogger(__name__)


def retry(max_retries: int = 3, backoff: float = 1.0):
    """Decorator that retries an async function with exponential backoff."""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(max_retries):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    if attempt < max_retries - 1:
                        wait = backoff * (2 ** attempt)
                        logger.warning(
                            f"Attempt {attempt + 1}/{max_retries} failed: {e}. "
                            f"Retrying in {wait}s…"
                        )
                        await asyncio.sleep(wait)
            raise last_exc
        return wrapper
    return decorator


class BaseAgent(ABC):
    """Abstract base class for all AI agents."""

    def __init__(self, name: str = None, config: dict = None):
        """Initialize base agent."""
        self.name = name or self.__class__.__name__
        self.config = config or {}
        logger.debug(f"Initializing agent: {self.name}")

    @abstractmethod
    def process(self, *args, **kwargs):
        """Main processing method - must be implemented by subclasses."""
        raise NotImplementedError("Subclass must implement process() method")

    @retry(max_retries=3)
    async def execute_with_retry(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the agent with retry logic."""
        return await self.execute(input_data)

    async def execute(self, input_data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute the agent task."""
        return {"status": "ready", "agent": self.name}

    def validate_input(self, data: dict) -> bool:
        """Validate input data."""
        return data is not None and isinstance(data, dict)

    def log_info(self, message: str):
        """Log info message."""
        logger.info(f"[{self.name}] {message}")

    def log_error(self, message: str):
        """Log error message."""
        logger.error(f"[{self.name}] {message}")
