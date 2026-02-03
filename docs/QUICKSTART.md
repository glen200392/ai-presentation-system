# Quick Start Guide

Get your AI Presentation System up and running in 5 minutes.

---

## Prerequisites

- Python 3.10 or higher
- Git
- API access (if using external services)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/glen200392/ai-presentation-system.git
cd ai-presentation-system
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```
# API Keys (if needed)
OPENAI_API_KEY=your_api_key_here
NEBULA_API_KEY=your_nebula_key_here

# System Settings
QUALITY_THRESHOLD=90
MAX_AGENTS=8
```

---

## Basic Usage

### Generate Your First Presentation

```python
from ai_presentation_system import PresentationGenerator

# Initialize the system
generator = PresentationGenerator()

# Define your presentation request
request = {
    "topic": "AI in Healthcare",
    "audience": "Medical professionals",
    "duration": 15,  # minutes
    "style": "business_professional"
}

# Generate presentation
result = generator.create_presentation(request)

# Download the file
result.download("output/my_presentation.pptx")
```

### Command Line Interface

```bash
# Basic generation
python -m ai_presentation generate \
  --topic "Digital Transformation" \
  --audience "Executives" \
  --style business_professional

# With custom options
python -m ai_presentation generate \
  --topic "Product Launch" \
  --audience "Investors" \
  --slides 20 \
  --duration 30 \
  --output ./presentations/launch.pptx
```

---

## Agent System Overview

The system uses 8 specialized agents:

1. **Scenario Intelligence** - Analyzes requirements and recommends structure
2. **Content Strategist** - Develops narrative and key messages
3. **Visual Designer** - Creates consistent visual themes
4. **Chart Designer** - Generates data visualizations
5. **Narrative Optimizer** - Refines story flow and engagement
6. **Citation Manager** - Handles references and sources
7. **Quality Assurance** - Validates content and accessibility
8. **PowerPoint Generator** - Produces final PPTX file

---

## Example Workflows

### Business Pitch Deck

```python
request = {
    "scenario": "pitch_deck",
    "company": "TechStartup Inc.",
    "audience": "Series A investors",
    "duration": 10,
    "key_points": [
        "Market opportunity",
        "Product demo",
        "Business model",
        "Traction metrics"
    ]
}

presentation = generator.create_presentation(request)
```

### Training Workshop

```python
request = {
    "scenario": "training",
    "topic": "Cloud Security Best Practices",
    "audience": "IT professionals",
    "duration": 60,
    "interactive_elements": True,
    "include_exercises": True
}

presentation = generator.create_presentation(request)
```

### Executive Report

```python
request = {
    "scenario": "board_report",
    "quarter": "Q4 2025",
    "audience": "Board of directors",
    "data_sources": ["sales.csv", "metrics.json"],
    "style": "minimal_modern"
}

presentation = generator.create_presentation(request)
```

---

## Customization

### Design Styles

Choose from 5 predefined styles:

- `business_professional` - Corporate presentations
- `tech_innovation` - Technology and startups
- `creative_energy` - Marketing and creative
- `academic_research` - Educational and research
- `minimal_modern` - Clean and minimalist

### Narrative Frameworks

Select the storytelling approach:

- `problem_solution` - Problem-focused narratives
- `hero_journey` - Transformation stories
- `data_driven` - Analytics and insights
- `before_after_bridge` - Change narratives
- `what_so_what_now_what` - Action-oriented

---

## Troubleshooting

### Common Issues

**Issue**: Agent initialization fails
```bash
# Check Python version
python --version  # Should be 3.10+

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

**Issue**: API rate limits
```python
# Configure rate limiting
generator = PresentationGenerator(
    rate_limit_delay=2.0,  # seconds between calls
    max_retries=3
)
```

**Issue**: Quality score below threshold
```python
# Enable quality monitoring
generator.config.quality_threshold = 95
generator.config.enable_qa_agent = True
```

---

## Next Steps

- Read the [Full Documentation](./docs/DOCUMENTATION_INDEX.md)
- Explore [Agent Configuration](./docs/AGENT_CONFIGURATION.md)
- Check [API Reference](./docs/API_REFERENCE.md)
- View [Examples](./examples/)

---

## Getting Help

- GitHub Issues: [Report bugs or request features](https://github.com/glen200392/ai-presentation-system/issues)
- Documentation: [Full docs](./docs/)
- Email: glen200392@gmail.com

---

**Ready to create amazing presentations? Let's go!** 🚀
