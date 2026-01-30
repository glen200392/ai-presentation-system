# 📁 AI Presentation System - Directory Structure

> Complete repository organization and file reference guide

---

## 🗂️ Current Repository Structure

```
ai-presentation-system/
├── .gitignore                          # Git ignore patterns
├── LICENSE                             # MIT License
├── README.md                           # Main project documentation (10.5 KB)
├── CONTRIBUTING.md                     # Contribution guidelines (8.1 KB)
│
└── code/
    └── agents/                         # AI Agent configurations
        ├── README.md                   # Agent overview (6.9 KB)
        ├── Agent實作指南.md             # Complete implementation guide (19.8 KB)
        ├── 使用範例.md                   # Real-world usage scenarios (15.5 KB)
        ├── create_agents.py            # Batch agent creation script (10.7 KB)
        │
        ├── agent_orchestrator_config.yaml              # Main coordinator (4.4 KB)
        ├── agent_scenario_intelligence_config.yaml     # Context analyzer (6.2 KB)
        ├── agent_content_strategist_config.yaml        # Narrative designer (7.5 KB)
        ├── agent_research_analyst_config.yaml          # Data gatherer (7.4 KB)
        ├── agent_visual_designer_config.yaml           # Aesthetic creator (12.1 KB)
        ├── agent_chart_designer_config.yaml            # Visualization builder (10.7 KB)
        └── agent_quality_assurance_config.yaml         # Output validator (10.5 KB)
```

**Total Files**: 15  
**Total Size**: ~132 KB  
**Languages**: YAML (7), Markdown (4), Python (1), Config (3)

---

## 📚 File Descriptions

### Root Level

#### `.gitignore` (817 bytes)
Git ignore patterns for Python, virtual environments, IDE files, generated outputs, and temporary files.

**Key Exclusions**:
- Python cache and build artifacts
- Virtual environments (venv/, env/)
- IDE files (.vscode/, .idea/)
- Generated presentations (*.pptx)
- Data files (*.csv, *.xlsx)

#### `LICENSE` (1.1 KB)
MIT License - permits free use, modification, and distribution with attribution.

#### `README.md` (10.5 KB)
Main project documentation including:
- Project overview and key features
- Multi-agent architecture diagram
- Quick start guide
- Documentation links
- Use cases and quality metrics
- Technology stack
- Roadmap and contribution info

#### `CONTRIBUTING.md` (8.1 KB)
Comprehensive contribution guidelines covering:
- Code of conduct
- Bug reporting and feature requests
- Development setup
- Coding standards (Python, YAML)
- Commit message format
- Pull request process

---

### `code/agents/` - Agent Configuration Directory

#### Documentation Files

**`README.md`** (6.9 KB)
- Agent configuration overview
- Quick reference table
- File structure explanation
- Usage instructions

**`implementation-guide.md`** (19.8 KB)
- Complete implementation walkthrough
- Agent-by-agent detailed specs
- YAML structure documentation
- Customization guide
- Troubleshooting section
- Best practices

**`usage-examples.md`** (15.5 KB)
- 4 complete real-world scenarios
- Code examples for each use case
- Multi-agent workflows
- Advanced techniques
- Performance optimization tips

#### Automation Scripts

**`create_agents.py`** (10.7 KB)
Python script for batch agent creation from YAML configs.

**Features**:
- Reads all 7 YAML configurations
- Creates agents via Nebula API
- Validates configurations
- Dry-run mode for testing
- Progress reporting

**Usage**:
```bash
# Create all agents
python create_agents.py

# Dry run (validate only)
python create_agents.py --dry-run

# Custom config directory
python create_agents.py --config-dir ./custom/path
```

#### Agent Configuration Files (YAML)

Each YAML file defines a complete agent specification:

| File | Agent | Size | Purpose |
|------|-------|------|---------|
| `agent_orchestrator_config.yaml` | PowerPoint 簡報生成器 | 4.4 KB | Coordinates all agents, manages workflow |
| `agent_scenario_intelligence_config.yaml` | Presentation Scenario Intelligence | 6.2 KB | Analyzes context, recommends structure |
| `agent_content_strategist_config.yaml` | Presentation Content Strategist | 7.5 KB | Designs narrative, creates outlines |
| `agent_research_analyst_config.yaml` | 簡報研究分析員 | 7.4 KB | Gathers data, validates facts |
| `agent_visual_designer_config.yaml` | Presentation Visual Designer | 12.1 KB | Creates design styles, ensures consistency |
| `agent_chart_designer_config.yaml` | Presentation Chart Designer | 10.7 KB | Generates data visualizations |
| `agent_quality_assurance_config.yaml` | Presentation Quality Assurance | 10.5 KB | Validates output quality |

**YAML Structure**:
```yaml
agent:
  name: "Agent Name"
  description: "Agent purpose and capabilities"
  
  prompt_sections:
    identity: "Who is this agent"
    purpose: "What problem it solves"
    capabilities:
      - capability_one
      - capability_two
    workflow: "Step-by-step process"
    best_practices:
      - practice_one
      - practice_two
  
  selected_toolkits:
    - toolkit_name
  
  tool_ids:
    - tool_id_1
    - tool_id_2
```

---

## 🎯 Agent Interaction Flow

```
User Request
    ↓
┌─────────────────────────────────────┐
│   PowerPoint 簡報生成器 (Orchestrator)  │
│   • Analyzes request                │
│   • Delegates to specialists        │
│   • Coordinates workflow            │
└──────────────┬──────────────────────┘
               ↓
    ┌──────────┴──────────┐
    ↓                     ↓
┌──────────────────┐  ┌──────────────────┐
│ Scenario         │  │ Content          │
│ Intelligence     │  │ Strategist       │
│ • Context        │  │ • Narrative      │
│ • Audience       │  │ • Outline        │
└──────────────────┘  └──────────────────┘
    ↓                     ↓
┌──────────────────┐  ┌──────────────────┐
│ Research         │  │ Visual           │
│ Analyst          │  │ Designer         │
│ • Data           │  │ • Styles         │
│ • Facts          │  │ • Colors         │
└──────────────────┘  └──────────────────┘
    ↓                     ↓
┌──────────────────┐  ┌──────────────────┐
│ Chart            │  │ Quality          │
│ Designer         │  │ Assurance        │
│ • Visuals        │  │ • Validation     │
│ • Graphs         │  │ • Final Check    │
└──────────────────┘  └──────────────────┘
               ↓
        Final Presentation
         (.pptx file)
```

---

## 📊 File Statistics

### By File Type

| Type | Count | Total Size | Avg Size |
|------|-------|------------|----------|
| YAML | 7 | 59.4 KB | 8.5 KB |
| Markdown | 4 | 52.3 KB | 13.1 KB |
| Python | 1 | 10.7 KB | 10.7 KB |
| Config | 3 | 10.0 KB | 3.3 KB |

### By Directory

| Directory | Files | Size | Purpose |
|-----------|-------|------|---------|
| `/` (root) | 4 | 20.4 KB | Project docs & config |
| `/code/agents/` | 11 | 111.8 KB | Agent configurations |

### Top 5 Largest Files

1. `implementation-guide.md` - 19.8 KB
2. `usage-examples.md` - 15.5 KB
3. `agent_visual_designer_config.yaml` - 12.1 KB
4. `agent_chart_designer_config.yaml` - 10.7 KB
5. `create_agents.py` - 10.7 KB

---

## 🔧 Configuration Management

### Adding a New Agent

1. Create YAML configuration in `code/agents/`
2. Follow existing naming convention: `agent_{name}_config.yaml`
3. Define all required sections (see YAML Structure above)
4. Update `create_agents.py` to include new agent
5. Add documentation to `implementation-guide.md`
6. Add usage examples to `usage-examples.md`
7. Update `README.md` agent count and descriptions

### Modifying Existing Agents

1. Edit the corresponding YAML file
2. Validate YAML syntax: `python create_agents.py --dry-run`
3. Test changes: `python create_agents.py`
4. Update documentation if capabilities changed
5. Commit with clear description of changes

### Version Control

- All configurations are version-controlled in Git
- Use semantic versioning for major changes
- Tag releases: `v1.0.0`, `v1.1.0`, etc.
- Maintain CHANGELOG.md for tracking changes

---

## 🚀 Quick Reference

### Clone Repository
```bash
git clone https://github.com/glen200392/ai-presentation-system.git
cd ai-presentation-system
```

### Setup Agents
```bash
python code/agents/create_agents.py
```

### Generate Presentation
```python
from nebula import delegate

result = delegate(
    agent_id='agt_0697a0226eaf7dc1800093eb8943c2da',
    description="Create [scenario] presentation on [topic]"
)
```

### Update Agent Config
```bash
# Edit YAML file
vim code/agents/agent_orchestrator_config.yaml

# Validate
python code/agents/create_agents.py --dry-run

# Apply changes
python code/agents/create_agents.py
```

---

## 📖 Documentation Hierarchy

```
README.md (Start here)
    ├── Quick Start
    ├── Architecture Overview
    └── Links to detailed docs
        │
        ├── code/agents/README.md (Agent overview)
        │   └── Brief descriptions
        │
        ├── implementation-guide.md (Technical details)
        │   ├── Complete agent specs
        │   ├── YAML structure
        │   └── Customization guide
        │
        ├── usage-examples.md (Practical usage)
        │   ├── Real scenarios
        │   ├── Code examples
        │   └── Best practices
        │
        └── CONTRIBUTING.md (For contributors)
            ├── Setup instructions
            ├── Coding standards
            └── PR process
```

---

## 🎓 Learning Path

### For New Users
1. Read `README.md` - Understand project overview
2. Follow Quick Start - Set up and run first presentation
3. Read `usage-examples.md` - See real-world scenarios
4. Explore `code/agents/README.md` - Learn about agents

### For Developers
1. Read `CONTRIBUTING.md` - Setup dev environment
2. Study `implementation-guide.md` - Technical architecture
3. Review YAML configs - Understand agent structure
4. Examine `create_agents.py` - Learn automation scripts

### For Contributors
1. Review `CONTRIBUTING.md` - Guidelines and standards
2. Check existing issues - Find contribution opportunities
3. Read documentation - Understand current state
4. Submit PRs - Follow contribution process

---

## 🔗 External Links

- **GitHub**: https://github.com/glen200392/ai-presentation-system
- **Issues**: https://github.com/glen200392/ai-presentation-system/issues
- **Nebula Platform**: https://nebula.gg
- **Python-pptx**: https://python-pptx.readthedocs.io/

---

## 📝 Maintenance Notes

### File Updates Required When:

**Adding New Agent**:
- [ ] Create new YAML config
- [ ] Update `create_agents.py`
- [ ] Update `README.md` (agent count, table)
- [ ] Update `implementation-guide.md` (specs)
- [ ] Update `usage-examples.md` (examples)
- [ ] Update this `STRUCTURE.md`

**Changing Agent Capabilities**:
- [ ] Modify YAML config
- [ ] Update `implementation-guide.md`
- [ ] Update `usage-examples.md` if needed
- [ ] Validate with `--dry-run`

**Adding Documentation**:
- [ ] Create new .md file
- [ ] Update `README.md` links
- [ ] Update this `STRUCTURE.md`
- [ ] Update documentation hierarchy diagram

---

*Last Updated: 2026-01-30*  
*Repository: https://github.com/glen200392/ai-presentation-system*
