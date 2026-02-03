# Contributing to AI Presentation System

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the AI Presentation System.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [Agent Development Guidelines](#agent-development-guidelines)

---

## 📜 Code of Conduct

This project adheres to a code of conduct that we expect all contributors to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

**In summary:**
- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect differing viewpoints and experiences

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- GitHub account
- Nebula AI Platform account (for agent testing)

### First-Time Setup

1. **Fork the repository**
   ```bash
   # Click the "Fork" button on GitHub
   # Then clone your fork
   git clone https://github.com/YOUR_USERNAME/ai-presentation-system.git
   cd ai-presentation-system
   ```

2. **Add upstream remote**
   ```bash
   git remote add upstream https://github.com/glen200392/ai-presentation-system.git
   ```

3. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

---

## 💻 Development Setup

### Virtual Environment

We recommend using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
```

### Environment Variables

Create a `.env` file in the project root:

```bash
# Nebula AI Configuration
NEBULA_API_KEY=your_api_key_here

# SlidesGo API (for PowerPoint generation)
SLIDESGO_API_KEY=your_key_here

# Optional: Testing configuration
TEST_MODE=development
LOG_LEVEL=DEBUG
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=ai_presentation_system --cov-report=html

# Run specific test file
pytest tests/test_agents/test_scenario_intelligence.py

# Run with verbose output
pytest -v
```

---

## 🤝 How to Contribute

### Types of Contributions

We welcome several types of contributions:

1. **Bug Reports** 🐛
   - Use GitHub Issues with the "bug" label
   - Include reproduction steps
   - Provide system information

2. **Feature Requests** 💡
   - Use GitHub Issues with the "enhancement" label
   - Describe the use case clearly
   - Explain expected behavior

3. **Code Contributions** 💻
   - Bug fixes
   - New features
   - Performance improvements
   - Documentation updates

4. **Documentation** 📚
   - Fix typos or unclear instructions
   - Add examples and tutorials
   - Improve API documentation

5. **Agent Development** 🤖
   - New specialized agents
   - Improvements to existing agents
   - Custom workflow patterns

---

## 📝 Coding Standards

### Python Style Guide

We follow **PEP 8** with some modifications:

```python
# Good: Clear function names with type hints
def generate_slide_outline(
    topic: str,
    audience: str,
    duration: int
) -> dict[str, Any]:
    """
    Generate a structured outline for presentation slides.
    
    Args:
        topic: Main presentation topic
        audience: Target audience description
        duration: Presentation duration in minutes
        
    Returns:
        Dictionary containing slide structure and timing
        
    Raises:
        ValueError: If duration is negative or zero
    """
    pass

# Bad: Unclear names, no type hints, no docstring
def gen(t, a, d):
    pass
```

### Code Formatting

We use automated formatters:

- **Black** for code formatting
- **isort** for import sorting
- **Flake8** for linting
- **mypy** for type checking

```bash
# Format code automatically
black ai_presentation_system/
isort ai_presentation_system/

# Check for issues
flake8 ai_presentation_system/
mypy ai_presentation_system/
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Classes | PascalCase | `ContentStrategist`, `ChartDesigner` |
| Functions | snake_case | `generate_outline()`, `validate_config()` |
| Constants | UPPER_SNAKE_CASE | `MAX_SLIDES`, `DEFAULT_STYLE` |
| Private methods | _leading_underscore | `_internal_helper()` |
| Agents | Agent suffix | `ScenarioIntelligenceAgent` |

---

## 🧪 Testing Requirements

### Test Structure

```
tests/
├── test_agents/
│   ├── test_scenario_intelligence.py
│   ├── test_content_strategist.py
│   └── ...
├── test_workflows/
│   ├── test_standard_workflow.py
│   └── test_fast_workflow.py
├── test_integration/
│   └── test_end_to_end.py
└── fixtures/
    └── sample_presentations.py
```

### Writing Tests

```python
import pytest
from ai_presentation_system.agents import ContentStrategist

class TestContentStrategist:
    """Test suite for Content Strategist agent."""
    
    @pytest.fixture
    def agent(self):
        """Create agent instance for testing."""
        return ContentStrategist(config={"style": "business"})
    
    def test_outline_generation(self, agent):
        """Test basic outline generation."""
        result = agent.generate_outline(
            topic="Digital Transformation",
            audience="Executives",
            duration=30
        )
        
        assert "slides" in result
        assert len(result["slides"]) > 0
        assert result["total_duration"] <= 30
    
    def test_invalid_duration_raises_error(self, agent):
        """Test that negative duration raises ValueError."""
        with pytest.raises(ValueError):
            agent.generate_outline(
                topic="Test",
                audience="Test",
                duration=-5
            )
```

### Test Coverage Requirements

- **Minimum coverage**: 80% for new code
- **Critical paths**: 100% coverage required
- **Agent implementations**: Each agent must have dedicated test suite

---

## 🔄 Pull Request Process

### 1. Create a Feature Branch

```bash
# Update your local main branch
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/your-feature-name
```

### Branch Naming Convention

- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test improvements

Examples:
- `feature/add-video-support`
- `fix/citation-formatting-bug`
- `docs/update-quickstart-guide`

### 2. Make Your Changes

```bash
# Make changes
# Add tests
# Update documentation

# Run tests locally
pytest

# Run linters
black .
flake8 .
```

### 3. Commit Your Changes

Use clear, descriptive commit messages:

```bash
# Good commit messages
git commit -m "feat: Add video integration to PowerPoint Generator"
git commit -m "fix: Correct citation formatting in APA style"
git commit -m "docs: Update API reference for Chart Designer"

# Bad commit messages
git commit -m "updates"
git commit -m "fix bug"
git commit -m "changes"
```

**Commit Message Format:**
```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Tests
- `chore`: Maintenance

### 4. Push and Create PR

```bash
# Push to your fork
git push origin feature/your-feature-name

# Go to GitHub and create Pull Request
```

### 5. PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

## Testing
Describe the tests you ran and how to reproduce them.

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or feature works
- [ ] New and existing unit tests pass locally
- [ ] Any dependent changes have been merged

## Screenshots (if applicable)
Add screenshots to help explain your changes.

## Related Issues
Closes #123
Related to #456
```

### 6. Review Process

- Maintainers will review your PR within 3-5 business days
- Address any requested changes
- Keep your branch up to date with main
- Be responsive to feedback

---

## 🤖 Agent Development Guidelines

### Creating a New Agent

1. **Define Agent Purpose**
   ```yaml
   # agents_config.yaml
   - id: "your-new-agent"
     name: "Your New Agent Name"
     role: "Specific role description"
     expertise:
       - "Capability 1"
       - "Capability 2"
   ```

2. **Implement Agent Class**
   ```python
   # ai_presentation_system/agents/your_new_agent.py
   
   from .base_agent import BaseAgent
   
   class YourNewAgent(BaseAgent):
       """
       Your agent description.
       
       This agent specializes in [specific task] by [methodology].
       """
       
       def __init__(self, config: dict):
           super().__init__(config)
           self.setup_capabilities()
       
       def process(self, input_data: dict) -> dict:
           """Main processing method."""
           pass
   ```

3. **Add Tests**
   ```python
   # tests/test_agents/test_your_new_agent.py
   
   def test_your_new_agent():
       agent = YourNewAgent(config={})
       result = agent.process({"test": "data"})
       assert result["status"] == "success"
   ```

4. **Document the Agent**
   ```markdown
   # docs/agents/your_new_agent.md
   
   # Your New Agent
   
   ## Overview
   ## Capabilities
   ## API Reference
   ## Examples
   ```

### Agent Quality Checklist

- [ ] Clear, single-responsibility purpose
- [ ] Comprehensive docstrings
- [ ] Type hints for all methods
- [ ] Error handling with meaningful messages
- [ ] Unit tests covering main scenarios
- [ ] Integration tests with other agents
- [ ] Documentation with examples
- [ ] Performance benchmarks

---

## 📚 Documentation Standards

### Docstring Format (Google Style)

```python
def generate_presentation(
    topic: str,
    audience: str,
    style: str = "business_professional",
    duration: int = 30
) -> PresentationResult:
    """
    Generate a complete presentation from requirements.
    
    This function orchestrates all agents to create a presentation
    that meets the specified requirements and quality standards.
    
    Args:
        topic: Main presentation topic or title
        audience: Target audience description (e.g., "C-Suite Executives")
        style: Design style to apply, defaults to "business_professional"
        duration: Target duration in minutes, defaults to 30
        
    Returns:
        PresentationResult object containing:
            - pptx_file: Path to generated .pptx file
            - quality_score: Overall quality score (0-100)
            - metadata: Generation metadata and statistics
            
    Raises:
        ValueError: If duration is negative or style is invalid
        GenerationError: If presentation generation fails
        
    Example:
        >>> result = generate_presentation(
        ...     topic="Digital Strategy 2026",
        ...     audience="Board of Directors",
        ...     duration=45
        ... )
        >>> print(f"Quality: {result.quality_score}/100")
        Quality: 98/100
    """
    pass
```

---

## ❓ Questions or Need Help?

- **General questions**: [GitHub Discussions](https://github.com/glen200392/ai-presentation-system/discussions)
- **Bug reports**: [GitHub Issues](https://github.com/glen200392/ai-presentation-system/issues)
- **Direct contact**: glen200392@gmail.com

---

## 🎉 Recognition

Contributors will be:
- Listed in [CONTRIBUTORS.md](CONTRIBUTORS.md)
- Mentioned in release notes
- Credited in documentation they create

---

Thank you for contributing to AI Presentation System! 🙏

*Last Updated: 2026-02-02*
