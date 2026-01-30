# Contributing to AI Presentation System

First off, thank you for considering contributing to AI Presentation System! 🎉

This project aims to create a comprehensive, enterprise-grade AI presentation generation system. Your contributions help make it better for everyone.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

---

## 🤝 Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow:

- **Be respectful** - Treat everyone with respect and consideration
- **Be collaborative** - Work together constructively
- **Be professional** - Keep discussions focused and productive
- **Be inclusive** - Welcome contributors of all backgrounds and skill levels

---

## 🎯 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title** - Describe the issue concisely
- **Steps to reproduce** - Detailed steps to recreate the bug
- **Expected behavior** - What you expected to happen
- **Actual behavior** - What actually happened
- **Environment** - Python version, OS, Nebula platform version
- **Screenshots** - If applicable

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- **Use case** - Why is this enhancement valuable?
- **Proposed solution** - How should it work?
- **Alternatives** - Other approaches you've considered
- **Impact** - Who benefits and how?

### Contributing Code

We welcome contributions in these areas:

#### 🎨 Design & Visual
- New design styles beyond the current 5
- Additional color palettes
- Layout templates for specific industries
- Brand template integration

#### 📊 Data & Charts
- New chart types (waterfall, funnel, etc.)
- Data processing improvements
- Statistical analysis features
- Real-time data integration

#### 🤖 Agent Capabilities
- Enhanced agent prompts
- New specialized agents
- Workflow optimizations
- Error handling improvements

#### 🌐 Internationalization
- Translations (Chinese, Japanese, Spanish, etc.)
- Locale-specific formatting
- Cultural adaptation for presentations

#### 📚 Documentation
- Tutorial improvements
- Code examples
- API documentation
- Best practices guides

---

## 🛠️ Development Setup

### Prerequisites

```bash
# Ensure you have Python 3.8+
python --version

# Nebula AI platform access
# GitHub account for OAuth (optional)
```

### Setup Steps

```bash
# 1. Fork the repository
# Click "Fork" on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/ai-presentation-system.git
cd ai-presentation-system

# 3. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt  # If available

# 5. Create agents
python code/agents/create_agents.py --dry-run

# 6. Create a feature branch
git checkout -b feature/your-feature-name
```

---

## 📝 Coding Standards

### Python Style Guide

Follow [PEP 8](https://pep8.org/) with these specifics:

- **Indentation**: 4 spaces (no tabs)
- **Line length**: Max 100 characters
- **Imports**: Grouped (standard library, third-party, local)
- **Docstrings**: Google style for functions and classes

Example:

```python
def generate_slide(title: str, content: list, style: str = "professional") -> dict:
    """
    Generate a presentation slide with specified content.
    
    Args:
        title: Slide title text
        content: List of content items to include
        style: Design style (professional, creative, minimal)
    
    Returns:
        Dictionary containing slide configuration
    
    Raises:
        ValueError: If style is not recognized
    """
    if style not in ["professional", "creative", "minimal"]:
        raise ValueError(f"Unknown style: {style}")
    
    return {
        "title": title,
        "content": content,
        "style": style
    }
```

### YAML Configuration

- **Indentation**: 2 spaces
- **Comments**: Use for complex sections
- **Structure**: Match existing agent configs

Example:

```yaml
agent:
  name: "Example Agent"
  description: |
    Multi-line description
    of agent purpose
  
  capabilities:
    - capability_one
    - capability_two
  
  tools:
    - name: "tool_name"
      required: true
```

### Documentation

- **README updates**: For new features or breaking changes
- **Inline comments**: For complex logic only
- **Docstrings**: For all public functions/classes
- **Examples**: Include usage examples for new features

---

## 💬 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

#### Examples

```bash
feat(chart-designer): Add waterfall chart support

- Implement waterfall chart generation
- Add color coding for positive/negative values
- Include data validation for waterfall format

Closes #42

---

fix(orchestrator): Handle empty presentation requests

Previously crashed when description was empty.
Now returns helpful error message.

Fixes #38

---

docs(readme): Update installation instructions

- Add Python version requirement
- Clarify Nebula platform setup
- Fix broken links
```

---

## 🔄 Pull Request Process

### Before Submitting

1. **Test your changes** - Ensure everything works
2. **Update documentation** - Reflect your changes in docs
3. **Follow style guide** - Code matches project standards
4. **Commit message** - Clear and descriptive
5. **Rebase on main** - Ensure clean history

### Submission Steps

```bash
# 1. Ensure you're on your feature branch
git checkout feature/your-feature-name

# 2. Pull latest changes from upstream
git fetch upstream
git rebase upstream/main

# 3. Push to your fork
git push origin feature/your-feature-name

# 4. Create Pull Request on GitHub
# - Clear title describing the change
# - Description explaining what and why
# - Link to related issues
```

### PR Template

Your PR description should include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How was this tested?

## Checklist
- [ ] Code follows style guide
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass
```

### Review Process

1. **Automated checks** - GitHub Actions must pass
2. **Maintainer review** - At least one approval required
3. **Discussion** - Address feedback and questions
4. **Approval** - Maintainer approves changes
5. **Merge** - Squash and merge to main

---

## 🎓 Learning Resources

### Project Architecture
- [Agent Design Guide](./code/agents/implementation-guide.md)
- [Usage Examples](./code/agents/usage-examples.md)
- [Quality Framework](./docs/quality-assurance.md)

### Nebula Platform
- [Nebula Documentation](https://docs.nebula.gg)
- [Multi-Agent Systems](https://docs.nebula.gg/agents)
- [API Reference](https://docs.nebula.gg/api)

### Python-pptx
- [Official Docs](https://python-pptx.readthedocs.io/)
- [Tutorial](https://python-pptx.readthedocs.io/en/latest/user/quickstart.html)

---

## ❓ Questions?

- **GitHub Issues** - For bugs and feature requests
- **Discussions** - For questions and ideas
- **Email** - glen200392@gmail.com for private inquiries

---

## 🙏 Thank You!

Your contributions make this project better for everyone. Whether it's:

- 🐛 Reporting a bug
- 💡 Suggesting an enhancement
- 📝 Improving documentation
- 💻 Contributing code

Every contribution is valued and appreciated! ⭐

---

*Happy Contributing!* 🚀
