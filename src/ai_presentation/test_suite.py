"""Comprehensive test suite for AI Presentation System."""

import sys
import os
import pytest
import asyncio
from unittest.mock import Mock, AsyncMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from ai_presentation.orchestrator import PresentationOrchestrator
from ai_presentation.agents import BaseAgent, ScenarioIntelligenceAgent
from ai_presentation.content_generator import ContentGenerator


class TestPresentationOrchestrator:
    """Test PresentationOrchestrator class."""

    @pytest.fixture
    def orchestrator(self):
        """Create orchestrator instance."""
        return PresentationOrchestrator()

    @pytest.mark.asyncio
    async def test_orchestrator_initialization(self, orchestrator):
        """Test orchestrator initializes correctly."""
        assert orchestrator is not None
        assert hasattr(orchestrator, "scenario_agent")

    @pytest.mark.asyncio
    async def test_generate_presentation(self, orchestrator):
        """Test presentation generation."""
        requirements = {
            "topic": "Test Topic",
            "scenario": {},
            "content": {},
        }
        result = await orchestrator.generate_presentation(requirements)
        assert result["status"] == "success"


class TestAgents:
    """Test agent classes."""

    def test_base_agent_creation(self):
        """Test BaseAgent can be extended."""
        agent = ScenarioIntelligenceAgent()
        assert agent.name == "ScenarioIntelligence"


class TestContentGenerator:
    """Test ContentGenerator class."""

    def test_content_generator_init(self):
        """Test generator initialization."""
        gen = ContentGenerator()
        assert gen is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
