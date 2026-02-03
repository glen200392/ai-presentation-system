# Repository Structure

Complete directory structure for the AI Presentation System following Python best practices.

---

## Overview

```
ai-presentation-system/
├── .github/                      # GitHub configurations
│   ├── workflows/               # CI/CD workflows
│   │   ├── tests.yml           # Automated testing
│   │   ├── lint.yml            # Code quality checks
│   │   └── release.yml         # Release automation
│   ├── ISSUE_TEMPLATE/         # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                        # Documentation
│   ├── api/                    # API documentation
│   ├── guides/                 # User guides
│   ├── architecture/           # System architecture
│   └── examples/               # Usage examples
├── src/                        # Source code
│   └── ai_presentation/        # Main package
│       ├── agents/             # Agent implementations
│       ├── core/               # Core functionality
│       ├── utils/              # Utility functions
│       ├── config/             # Configuration
│       └── __init__.py
├── tests/                      # Test suite
│   ├── unit/                   # Unit tests
│   ├── integration/            # Integration tests
│   └── fixtures/               # Test fixtures
├── examples/                   # Example scripts
├── scripts/                    # Utility scripts
├── configs/                    # Configuration files
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
├── README.md                  # Project overview
├── CONTRIBUTING.md            # Contribution guidelines
├── LICENSE                    # License file
├── setup.py                   # Package setup
├── requirements.txt           # Dependencies
├── requirements-dev.txt       # Dev dependencies
└── pyproject.toml            # Project metadata
```

---

## Detailed Structure

### Root Level Files

```
├── README.md                   # Project overview, badges, quick start
├── CONTRIBUTING.md             # How to contribute
├── LICENSE                     # MIT License
├── CODE_OF_CONDUCT.md         # Community guidelines
├── CHANGELOG.md               # Version history
├── .gitignore                 # Git ignore patterns
├── .env.example               # Environment variables template
├── setup.py                   # Package installation script
├── pyproject.toml             # Modern Python project config
├── requirements.txt           # Production dependencies
├── requirements-dev.txt       # Development dependencies
└── Makefile                   # Common commands
```

### .github/ - GitHub Configuration

```
.github/
├── workflows/
│   ├── tests.yml              # Run tests on PR/push
│   ├── lint.yml               # Code quality checks
│   ├── release.yml            # Automated releases
│   └── docs.yml               # Documentation builds
├── ISSUE_TEMPLATE/
│   ├── bug_report.md          # Bug report template
│   ├── feature_request.md     # Feature request template
│   └── question.md            # Question template
├── PULL_REQUEST_TEMPLATE.md   # PR template
└── dependabot.yml             # Dependency updates
```

### docs/ - Documentation

```
docs/
├── index.md                   # Documentation home
├── QUICKSTART.md             # Quick start guide
├── DEPLOYMENT.md             # Deployment guide
├── API_REFERENCE.md          # Complete API docs
├── guides/
│   ├── installation.md       # Installation guide
│   ├── configuration.md      # Configuration guide
│   ├── usage.md              # Usage examples
│   └── troubleshooting.md    # Common issues
├── architecture/
│   ├── overview.md           # System overview
│   ├── agents.md             # Agent architecture
│   ├── workflows.md          # Workflow diagrams
│   └── decisions.md          # Architecture decisions
├── examples/
│   ├── basic_usage.md        # Basic examples
│   ├── advanced_usage.md     # Advanced examples
│   └── custom_agents.md      # Custom agent creation
└── api/
    ├── core.md               # Core API
    ├── agents.md             # Agent APIs
    └── utils.md              # Utility APIs
```

### src/ai_presentation/ - Main Package

```
src/ai_presentation/
├── __init__.py                # Package initialization
├── __version__.py             # Version information
├── main.py                    # Main entry point
├── cli.py                     # Command-line interface
├── agents/                    # Agent implementations
│   ├── __init__.py
│   ├── base.py               # Base agent class
│   ├── scenario_intelligence.py
│   ├── content_strategist.py
│   ├── visual_designer.py
│   ├── chart_designer.py
│   ├── narrative_optimizer.py
│   ├── citation_manager.py
│   ├── quality_assurance.py
│   └── pptx_generator.py
├── core/                      # Core functionality
│   ├── __init__.py
│   ├── generator.py          # Main generator
│   ├── orchestrator.py       # Agent orchestrator
│   ├── request.py            # Request models
│   ├── result.py             # Result models
│   └── exceptions.py         # Custom exceptions
├── utils/                     # Utility functions
│   ├── __init__.py
│   ├── validation.py         # Validation utilities
│   ├── data_processing.py    # Data utilities
│   ├── file_handling.py      # File utilities
│   ├── logging.py            # Logging setup
│   └── metrics.py            # Metrics tracking
├── config/                    # Configuration
│   ├── __init__.py
│   ├── settings.py           # Settings management
│   ├── agents_config.yaml    # Agent configurations
│   └── defaults.py           # Default values
└── templates/                 # Templates
    ├── styles/               # Visual styles
    └── prompts/              # Agent prompts
```

### tests/ - Test Suite

```
tests/
├── __init__.py
├── conftest.py               # Pytest configuration
├── unit/                     # Unit tests
│   ├── __init__.py
│   ├── test_generator.py
│   ├── test_agents/
│   │   ├── test_scenario_intelligence.py
│   │   ├── test_content_strategist.py
│   │   └── ...
│   ├── test_core/
│   │   ├── test_request.py
│   │   └── test_result.py
│   └── test_utils/
│       ├── test_validation.py
│       └── test_data_processing.py
├── integration/              # Integration tests
│   ├── __init__.py
│   ├── test_full_workflow.py
│   ├── test_agent_collaboration.py
│   └── test_quality_pipeline.py
├── fixtures/                 # Test fixtures
│   ├── sample_data/
│   │   ├── test_data.csv
│   │   └── test_metrics.json
│   └── expected_outputs/
│       └── sample_presentation.pptx
└── performance/              # Performance tests
    └── test_benchmarks.py
```

### examples/ - Example Scripts

```
examples/
├── README.md                 # Examples overview
├── basic/
│   ├── simple_presentation.py
│   ├── with_data.py
│   └── custom_style.py
├── advanced/
│   ├── batch_generation.py
│   ├── custom_workflow.py
│   └── integration_example.py
└── notebooks/
    ├── tutorial.ipynb
    └── advanced_features.ipynb
```

### scripts/ - Utility Scripts

```
scripts/
├── setup.sh                  # Initial setup script
├── run_tests.sh             # Test runner
├── build_docs.sh            # Documentation builder
├── deploy.sh                # Deployment script
└── quality_check.sh         # Quality checks
```

### configs/ - Configuration Files

```
configs/
├── agents/
│   ├── scenario_intelligence.yaml
│   ├── content_strategist.yaml
│   └── ...
├── styles/
│   ├── business_professional.yaml
│   ├── tech_innovation.yaml
│   └── ...
└── environments/
    ├── development.yaml
    ├── staging.yaml
    └── production.yaml
```

---

## Key Files Content

### setup.py

```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ai-presentation-system",
    version="2.0.0",
    author="Glen Chen",
    author_email="glen200392@gmail.com",
    description="AI-powered presentation generation system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glen200392/ai-presentation-system",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ai-presentation=ai_presentation.cli:main",
        ],
    },
)
```

### pyproject.toml

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "ai-presentation-system"
version = "2.0.0"
description = "AI-powered presentation generation system"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}
authors = [
    {name = "Glen Chen", email = "glen200392@gmail.com"}
]
keywords = ["ai", "presentation", "powerpoint", "automation"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

[project.urls]
Homepage = "https://github.com/glen200392/ai-presentation-system"
Documentation = "https://github.com/glen200392/ai-presentation-system/docs"
Repository = "https://github.com/glen200392/ai-presentation-system"
Issues = "https://github.com/glen200392/ai-presentation-system/issues"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --cov=ai_presentation --cov-report=html --cov-report=term"

[tool.black]
line-length = 100
target-version = ['py310']
include = '\.pyi?$'

[tool.isort]
profile = "black"
line_length = 100

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

### Makefile

```makefile
.PHONY: install test lint format clean docs

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

install-prod:
	pip install -r requirements.txt

test:
	pytest tests/ -v

test-cov:
	pytest tests/ --cov=ai_presentation --cov-report=html

lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/
	isort src/ tests/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +

docs:
	cd docs && mkdocs build

serve-docs:
	cd docs && mkdocs serve

build:
	python setup.py sdist bdist_wheel

release: clean build
	twine upload dist/*
```

### .gitignore

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Environment
.env
.env.local

# Outputs
output/
cache/
logs/
*.pptx
*.pdf

# OS
.DS_Store
Thumbs.db
```

---

## Best Practices Implemented

### 1. **Separation of Concerns**
- Source code in `src/`
- Tests in `tests/`
- Docs in `docs/`
- Examples separate from source

### 2. **Flat is Better Than Nested**
- Maximum 3-4 levels of nesting
- Clear module boundaries
- Intuitive imports

### 3. **Explicit Package Structure**
- `__init__.py` in every package
- Clear module responsibilities
- Version in dedicated file

### 4. **Testing Infrastructure**
- Unit tests isolated
- Integration tests separate
- Fixtures organized
- Performance tests tracked

### 5. **Documentation**
- API docs auto-generated
- User guides comprehensive
- Examples runnable
- Architecture documented

### 6. **Development Workflow**
- CI/CD automated
- Code quality enforced
- Dependencies managed
- Releases automated

---

## Migration Guide

To reorganize existing code into this structure:

```bash
# 1. Create new structure
mkdir -p src/ai_presentation/{agents,core,utils,config}
mkdir -p tests/{unit,integration,fixtures}
mkdir -p docs/{api,guides,architecture,examples}

# 2. Move source files
mv agents/* src/ai_presentation/agents/
mv core/* src/ai_presentation/core/

# 3. Set up package
touch src/ai_presentation/__init__.py
echo "VERSION = '2.0.0'" > src/ai_presentation/__version__.py

# 4. Install in development mode
pip install -e .

# 5. Run tests to verify
pytest tests/
```

---

## Next Steps

1. Implement core package structure
2. Migrate existing agent code
3. Set up testing infrastructure
4. Configure CI/CD pipelines
5. Build documentation site
6. Publish initial release

---

This structure follows Python packaging best practices (PEP 517/518) and is ready for PyPI distribution.
