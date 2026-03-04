"""
AI Presentation System package.

Orchestrates 8 specialized AI agents to generate professional presentations:
Scenario Intelligence, Content Strategist, Narrative Optimizer, Visual Designer,
Chart Designer, Citation Manager, Quality Assurance, PowerPoint Generator.
"""

from .orchestrator import PresentationOrchestrator
from .content_generator import ContentGenerator
from .agents.document_ingestion_agent import DocumentIngestionAgent

__version__ = "2.0.0"
__all__ = ["PresentationOrchestrator", "ContentGenerator", "DocumentIngestionAgent"]
