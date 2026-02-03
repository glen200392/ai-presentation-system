"""Base Agent - Abstract base class for all agents"""
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
      """Abstract base class for all AI agents"""

    def __init__(self, name: str = None, config: dict = None):
              """Initialize base agent"""
              self.name = name or self.__class__.__name__
              self.config = config or {}
              logger.debug(f"Initializing agent: {self.name}")

    @abstractmethod
    def process(self, *args, **kwargs):
              """Main processing method - must be implemented by subclasses"""
              raise NotImplementedError("Subclass must implement process() method")

    def validate_input(self, data: dict) -> bool:
              """Validate input data"""
              return data is not None and isinstance(data, dict)

    def log_info(self, message: str):
              """Log info message"""
              logger.info(f"[{self.name}] {message}")

    def log_error(self, message: str):
              """Log error message"""
              logger.error(f"[{self.name}] {message}")
