"""AI Presentation System — 8-agent collaborative presentation generation."""

from .agents.document_ingestion_agent import DocumentIngestionAgent
from .content_generator import ContentGenerator
from .orchestrator import PresentationOrchestrator

__version__ = "2.0.0"
__all__ = ["PresentationOrchestrator", "ContentGenerator", "DocumentIngestionAgent"]
