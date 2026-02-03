# API Reference

Complete API documentation for the AI Presentation System.

---

## Table of Contents

- [Core Classes](#core-classes)
- [Agent APIs](#agent-apis)
- [Utility Functions](#utility-functions)
- [Configuration](#configuration)
- [Error Handling](#error-handling)

---

## Core Classes

### PresentationGenerator

Main entry point for generating presentations.

```python
class PresentationGenerator:
    """
    Orchestrates the multi-agent system to generate presentations.
    
    Attributes:
        config (SystemConfig): System configuration
        agents (dict): Dictionary of initialized agents
        quality_threshold (float): Minimum quality score (default: 90)
    """
    
    def __init__(self, config: Optional[SystemConfig] = None):
        """
        Initialize the presentation generator.
        
        Args:
            config: Optional system configuration object
        """
        
    def create_presentation(
        self,
        request: PresentationRequest
    ) -> PresentationResult:
        """
        Generate a complete presentation from a request.
        
        Args:
            request: Presentation request with topic, audience, style, etc.
            
        Returns:
            PresentationResult: Generated presentation with metadata
            
        Raises:
            ValidationError: Invalid request parameters
            QualityError: Quality score below threshold
            GenerationError: Presentation generation failed
        """
        
    def get_agent_status(self) -> Dict[str, AgentStatus]:
        """
        Get current status of all agents.
        
        Returns:
            Dictionary mapping agent names to their status
        """
```

**Usage Example:**

```python
from ai_presentation_system import PresentationGenerator

generator = PresentationGenerator()

request = {
    "topic": "Cloud Migration Strategy",
    "audience": "IT Leadership",
    "duration": 30,
    "style": "business_professional",
    "data_sources": ["migration_metrics.csv"]
}

result = generator.create_presentation(request)
print(f"Quality Score: {result.quality_score}/100")
result.download("output/cloud_migration.pptx")
```

---

### PresentationRequest

Request object for presentation generation.

```python
class PresentationRequest:
    """
    Structured request for presentation generation.
    
    Attributes:
        topic (str): Presentation topic or title
        audience (str): Target audience description
        duration (int): Presentation duration in minutes
        style (str): Design style (business_professional, tech_innovation, etc.)
        scenario (str): Presentation scenario (pitch_deck, board_report, etc.)
        slide_count (int): Approximate number of slides
        narrative_framework (str): Storytelling approach
        data_sources (List[str]): Paths to data files
        key_messages (List[str]): Core messages to convey
        interactive_elements (bool): Include interactive components
        include_qa (bool): Include Q&A preparation
        accessibility_level (str): Accessibility compliance level
    """
    
    def __init__(
        self,
        topic: str,
        audience: str,
        duration: int = 15,
        style: str = "business_professional",
        **kwargs
    ):
        """
        Create a presentation request.
        
        Args:
            topic: Presentation topic
            audience: Target audience
            duration: Duration in minutes (default: 15)
            style: Design style (default: business_professional)
            **kwargs: Additional optional parameters
        """
        
    def validate(self) -> bool:
        """
        Validate request parameters.
        
        Returns:
            True if valid
            
        Raises:
            ValidationError: Invalid parameters
        """
```

**Validation Rules:**

- `topic`: Non-empty string, max 200 characters
- `audience`: Non-empty string, max 200 characters
- `duration`: Integer between 5 and 120 minutes
- `style`: One of 5 predefined styles
- `slide_count`: Integer between 5 and 100 (if specified)

---

### PresentationResult

Result object containing generated presentation and metadata.

```python
class PresentationResult:
    """
    Result of presentation generation.
    
    Attributes:
        presentation_id (str): Unique identifier
        file_path (str): Path to generated PPTX file
        quality_score (float): Overall quality score (0-100)
        agent_metrics (Dict): Performance metrics per agent
        slide_count (int): Number of slides generated
        generation_time (float): Total generation time in seconds
        metadata (Dict): Additional metadata
        warnings (List[str]): Any warnings during generation
    """
    
    def download(self, destination: str) -> str:
        """
        Download presentation to specified location.
        
        Args:
            destination: Target file path
            
        Returns:
            Path to downloaded file
        """
        
    def get_embed_url(self) -> str:
        """
        Get embeddable URL for online viewing.
        
        Returns:
            URL string for embedding
        """
        
    def get_quality_report(self) -> QualityReport:
        """
        Get detailed quality assessment report.
        
        Returns:
            QualityReport object with detailed metrics
        """
```

---

## Agent APIs

### ScenarioIntelligenceAgent

Analyzes requirements and recommends presentation structure.

```python
class ScenarioIntelligenceAgent:
    """
    Analyzes user requirements and classifies presentation scenario.
    """
    
    def analyze_request(
        self,
        request: PresentationRequest
    ) -> ScenarioAnalysis:
        """
        Analyze request and recommend structure.
        
        Args:
            request: Presentation request
            
        Returns:
            ScenarioAnalysis with recommended structure
        """
        
    def recommend_slide_sequence(
        self,
        scenario: str,
        duration: int
    ) -> List[SlideBlueprint]:
        """
        Recommend optimal slide sequence.
        
        Args:
            scenario: Presentation scenario type
            duration: Duration in minutes
            
        Returns:
            List of slide blueprints
        """
```

**Scenario Types:**

- `pitch_deck`: Investor pitches
- `business_proposal`: Business proposals
- `board_report`: Executive reports
- `qbr`: Quarterly business reviews
- `product_launch`: Product announcements
- `training`: Training workshops
- `sales_pitch`: Sales presentations
- `strategy`: Strategic planning

---

### ContentStrategistAgent

Develops narrative structure and key messages.

```python
class ContentStrategistAgent:
    """
    Creates narrative structure and speech scripts.
    """
    
    def develop_narrative(
        self,
        topic: str,
        audience: str,
        framework: str = "problem_solution"
    ) -> NarrativeStructure:
        """
        Develop narrative structure.
        
        Args:
            topic: Presentation topic
            audience: Target audience
            framework: Narrative framework to use
            
        Returns:
            NarrativeStructure object
        """
        
    def generate_speech_script(
        self,
        slides: List[Slide],
        duration: int
    ) -> SpeechScript:
        """
        Generate speaker notes and timing.
        
        Args:
            slides: List of slide objects
            duration: Total duration in minutes
            
        Returns:
            SpeechScript with timing and notes
        """
```

**Narrative Frameworks:**

- `problem_solution`: Problem-focused narratives
- `hero_journey`: Transformation stories
- `data_driven`: Data and insights
- `before_after_bridge`: Change narratives
- `what_so_what_now_what`: Action-oriented

---

### VisualDesignerAgent

Creates consistent visual themes and generates images.

```python
class VisualDesignerAgent:
    """
    Designs visual themes and generates custom imagery.
    """
    
    def create_visual_theme(
        self,
        style: str,
        brand_colors: Optional[List[str]] = None
    ) -> VisualTheme:
        """
        Create complete visual theme.
        
        Args:
            style: Design style name
            brand_colors: Optional brand color palette
            
        Returns:
            VisualTheme with colors, fonts, layouts
        """
        
    def generate_slide_image(
        self,
        prompt: str,
        style: str,
        aspect_ratio: str = "16:9"
    ) -> str:
        """
        Generate custom slide image.
        
        Args:
            prompt: Image description
            style: Visual style to match
            aspect_ratio: Image aspect ratio
            
        Returns:
            Path to generated image file
        """
        
    def validate_accessibility(
        self,
        theme: VisualTheme
    ) -> AccessibilityReport:
        """
        Validate WCAG compliance.
        
        Args:
            theme: Visual theme to validate
            
        Returns:
            AccessibilityReport with compliance details
        """
```

**Design Styles:**

- `business_professional`: Corporate presentations
- `tech_innovation`: Technology and startups
- `creative_energy`: Marketing and creative
- `academic_research`: Educational content
- `minimal_modern`: Clean and minimal

---

### ChartDesignerAgent

Generates data visualizations for slides.

```python
class ChartDesignerAgent:
    """
    Creates publication-ready charts from data.
    """
    
    def create_chart(
        self,
        data: pd.DataFrame,
        chart_type: str,
        style: str,
        title: str,
        **options
    ) -> Chart:
        """
        Create a chart from data.
        
        Args:
            data: DataFrame with chart data
            chart_type: Type of chart (bar, line, pie, etc.)
            style: Visual style to match
            title: Chart title
            **options: Additional chart options
            
        Returns:
            Chart object with image and metadata
        """
        
    def recommend_chart_type(
        self,
        data: pd.DataFrame,
        purpose: str
    ) -> str:
        """
        Recommend optimal chart type.
        
        Args:
            data: DataFrame to visualize
            purpose: Visualization purpose
            
        Returns:
            Recommended chart type
        """
```

**Chart Types:**

- `bar`: Bar charts (comparison)
- `line`: Line charts (trends)
- `pie`: Pie/donut charts (composition)
- `scatter`: Scatter plots (correlation)
- `heatmap`: Heatmaps (patterns)
- `treemap`: Treemaps (hierarchy)
- `waterfall`: Waterfall charts (change)
- `combo`: Combination charts

---

### QualityAssuranceAgent

Validates presentation quality before delivery.

```python
class QualityAssuranceAgent:
    """
    Performs comprehensive quality checks.
    """
    
    def validate_presentation(
        self,
        presentation: Presentation
    ) -> QualityReport:
        """
        Comprehensive quality validation.
        
        Args:
            presentation: Presentation to validate
            
        Returns:
            QualityReport with detailed findings
        """
        
    def check_data_accuracy(
        self,
        slides: List[Slide],
        sources: List[str]
    ) -> DataValidationReport:
        """
        Verify data accuracy against sources.
        
        Args:
            slides: Slides with data
            sources: Original data sources
            
        Returns:
            DataValidationReport with verification results
        """
```

**Quality Dimensions:**

- Data accuracy (40% weight)
- Visual consistency (20% weight)
- Content completeness (20% weight)
- Accessibility compliance (10% weight)
- Brand conformity (10% weight)

---

## Utility Functions

### Validation Utilities

```python
def validate_presentation_request(
    request: Dict
) -> Tuple[bool, List[str]]:
    """
    Validate presentation request dictionary.
    
    Args:
        request: Request dictionary
        
    Returns:
        Tuple of (is_valid, error_messages)
    """
    
def validate_file_path(path: str, extensions: List[str]) -> bool:
    """
    Validate file path and extension.
    
    Args:
        path: File path to validate
        extensions: Allowed file extensions
        
    Returns:
        True if valid
    """
```

### Data Processing

```python
def load_data_source(
    file_path: str
) -> pd.DataFrame:
    """
    Load data from various file formats.
    
    Supports: CSV, Excel, JSON, Parquet
    
    Args:
        file_path: Path to data file
        
    Returns:
        DataFrame with loaded data
    """
    
def clean_dataset(
    df: pd.DataFrame,
    strategy: str = "auto"
) -> pd.DataFrame:
    """
    Clean dataset for visualization.
    
    Args:
        df: Input DataFrame
        strategy: Cleaning strategy (auto, strict, lenient)
        
    Returns:
        Cleaned DataFrame
    """
```

### Export Utilities

```python
def export_presentation(
    presentation: Presentation,
    format: str = "pptx",
    destination: str = None
) -> str:
    """
    Export presentation to file.
    
    Args:
        presentation: Presentation object
        format: Export format (pptx, pdf)
        destination: Optional destination path
        
    Returns:
        Path to exported file
    """
```

---

## Configuration

### SystemConfig

```python
class SystemConfig:
    """
    System-wide configuration.
    
    Attributes:
        quality_threshold (float): Minimum quality score (0-100)
        max_agents (int): Maximum concurrent agents
        enable_caching (bool): Enable result caching
        cache_ttl (int): Cache time-to-live in seconds
        api_timeout (int): API request timeout in seconds
        max_retries (int): Maximum retry attempts
        log_level (str): Logging level
    """
    
    @classmethod
    def from_env(cls) -> 'SystemConfig':
        """Load configuration from environment variables."""
        
    @classmethod
    def from_file(cls, path: str) -> 'SystemConfig':
        """Load configuration from YAML/JSON file."""
```

**Environment Variables:**

```bash
# Core Settings
AI_PRESENTATION_QUALITY_THRESHOLD=90
AI_PRESENTATION_MAX_AGENTS=8
AI_PRESENTATION_ENABLE_CACHING=true

# API Settings
AI_PRESENTATION_API_TIMEOUT=60
AI_PRESENTATION_MAX_RETRIES=3
AI_PRESENTATION_RATE_LIMIT=100

# Logging
AI_PRESENTATION_LOG_LEVEL=INFO
AI_PRESENTATION_LOG_FILE=/var/log/ai-presentation.log
```

---

## Error Handling

### Exception Hierarchy

```python
class PresentationError(Exception):
    """Base exception for all presentation errors."""
    
class ValidationError(PresentationError):
    """Invalid request parameters."""
    
class QualityError(PresentationError):
    """Quality score below threshold."""
    
class GenerationError(PresentationError):
    """Presentation generation failed."""
    
class AgentError(PresentationError):
    """Agent execution error."""
    
class DataError(PresentationError):
    """Data processing error."""
```

### Error Handling Example

```python
from ai_presentation_system import (
    PresentationGenerator,
    ValidationError,
    QualityError
)

generator = PresentationGenerator()

try:
    result = generator.create_presentation(request)
except ValidationError as e:
    print(f"Invalid request: {e.message}")
    print(f"Errors: {e.validation_errors}")
except QualityError as e:
    print(f"Quality too low: {e.score}/100")
    print(f"Issues: {e.quality_issues}")
except GenerationError as e:
    print(f"Generation failed: {e.message}")
    print(f"Agent: {e.failed_agent}")
```

---

## Response Formats

### Quality Report

```json
{
  "overall_score": 98,
  "dimensions": {
    "data_accuracy": {
      "score": 100,
      "checks_passed": 15,
      "checks_failed": 0
    },
    "visual_consistency": {
      "score": 95,
      "issues": ["Font size variation on slide 8"]
    },
    "content_completeness": {
      "score": 98,
      "missing_elements": []
    },
    "accessibility": {
      "score": 97,
      "wcag_level": "AA",
      "violations": []
    },
    "brand_conformity": {
      "score": 100,
      "compliant": true
    }
  },
  "recommendations": [
    "Standardize font sizes across all slides"
  ]
}
```

### Agent Metrics

```json
{
  "scenario_intelligence": {
    "execution_time": 2.3,
    "success": true,
    "output_quality": 98
  },
  "content_strategist": {
    "execution_time": 8.5,
    "success": true,
    "output_quality": 96
  },
  "visual_designer": {
    "execution_time": 15.2,
    "success": true,
    "images_generated": 5,
    "output_quality": 97
  }
}
```

---

## Rate Limits and Performance

### Default Limits

- **API Calls**: 100 requests/minute per agent
- **Concurrent Generations**: 5 presentations
- **Max Slides**: 100 per presentation
- **Max File Size**: 50MB for data sources
- **Cache Duration**: 24 hours

### Performance Optimization

```python
# Enable caching for repeated requests
generator = PresentationGenerator(
    config=SystemConfig(
        enable_caching=True,
        cache_ttl=3600
    )
)

# Batch processing
requests = [request1, request2, request3]
results = generator.batch_create(requests, parallel=True)
```

---

## Support

For API questions:
- GitHub Issues: https://github.com/glen200392/ai-presentation-system/issues
- Email: glen200392@gmail.com
- Documentation: [DOCUMENTATION_INDEX.md](./DOCUMENTATION_INDEX.md)
