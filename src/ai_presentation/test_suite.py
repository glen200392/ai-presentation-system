"""Comprehensive test suite for AI Presentation System."""

import asyncio

import pytest
from unittest.mock import AsyncMock, Mock

from .agents import BaseAgent, ScenarioIntelligenceAgent
from .content_generator import ContentGenerator
from .orchestrator import PresentationOrchestrator
from .presentation_generator import PresentationGenerator


class TestPresentationOrchestrator:
    """Test PresentationOrchestrator class."""

    @pytest.fixture
    def orchestrator(self):
        """Create orchestrator instance."""
        return PresentationOrchestrator()

    @pytest.mark.asyncio
    async def test_generate_presentation(self, orchestrator):
        """Test presentation generation."""
        requirements = {
            "topic": "Test Topic",
            "scenario": {"topic": "Test Topic"},
            "content": {"topic": "Test Topic"},
        }
        result = await orchestrator.generate_presentation(requirements)
        assert result is not None
        assert "status" in result

    @pytest.mark.asyncio
    async def test_execute(self, orchestrator):
        """Test orchestrator execute method."""
        result = await orchestrator.execute()
        assert result["status"] == "ready"


class TestContentGenerator:
    """Test ContentGenerator class."""

    @pytest.fixture
    def generator(self):
        """Create content generator instance."""
        return ContentGenerator()

    @pytest.mark.asyncio
    async def test_generate_slides(self, generator):
        """Test slide generation."""
        strategy = {
            "outline": [
                {"section": "Intro", "key_points": ["Point 1"]},
            ],
            "content_flow": ["Flow 1"],
        }
        research = {}
        slides = await generator.generate_slides(strategy, research)
        assert len(slides) > 0

    @pytest.mark.asyncio
    async def test_generate_notes(self, generator):
        """Test speaker notes generation."""
        slides = [{"slide_number": 1, "title": "Test Slide"}]
        notes = await generator.generate_notes(slides)
        assert "slide_1" in notes


class TestScenarioIntelligenceAgent:
    """Test ScenarioIntelligenceAgent class."""

    @pytest.fixture
    def agent(self):
        """Create agent instance."""
        return ScenarioIntelligenceAgent()

    @pytest.mark.asyncio
    async def test_analyze_scenario(self, agent):
        """Test scenario analysis."""
        scenario_data = {"topic": "Test", "audience": {}}
        result = await agent.analyze_scenario(scenario_data)
        assert "scenario_type" in result
        assert "objectives" in result
