# Agent Configuration Documentation

This folder contains complete configuration files for all 7 AI agents in the presentation generation system.

## 📁 Files Overview

| File | Agent | Role |
|------|-------|------|
| `agent_orchestrator_config.yaml` | PowerPoint 簡報生成器 | 主控協調器 |
| `agent_scenario_intelligence_config.yaml` | Scenario Intelligence | 場景分析與受眾分析 |
| `agent_content_strategist_config.yaml` | Content Strategist | 內容策略與大綱生成 |
| `agent_research_analyst_config.yaml` | 簡報研究分析員 | 數據研究與事實檢查 |
| `agent_visual_designer_config.yaml` | Visual Designer | 視覺設計與風格指南 |
| `agent_chart_designer_config.yaml` | Chart Designer | 圖表設計與數據視覺化 |
| `agent_quality_assurance_config.yaml` | Quality Assurance | 品質檢查與驗證 |

## 🎯 Configuration Format

Each YAML file contains:

- **agent_metadata**: Basic information (name, version, type, role)
- **core_capabilities**: Detailed capability descriptions
- **workflow**: Step-by-step process
- **output_format**: Expected output structure
- **quality_standards**: Quality targets and thresholds
- **available_tools**: Tools and packages used
- **prompt_template**: Complete system prompt

## 🔧 How to Use

### 1. Import Configuration

```python
import yaml

with open('agent_orchestrator_config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
    
agent_name = config['agent_metadata']['name']
capabilities = config['core_capabilities']
```

### 2. Create Agent from Config

```python
from nebula import manage_agents

# Extract prompt from config
prompt = config['prompt_template']
tools = [tool['tool_name'] for tool in config['available_tools']]

# Create agent
agent = manage_agents(
    action='create',
    name=config['agent_metadata']['name'],
    description=config['agent_metadata']['description'],
    prompt_sections={
        'identity': config['agent_metadata']['role'],
        'capabilities': config['core_capabilities'],
        'workflow': config['workflow']
    },
    selected_toolkits=tools
)
```

### 3. Validate Configuration

```python
def validate_config(config):
    """Validate agent configuration completeness."""
    required_keys = [
        'agent_metadata',
        'core_capabilities',
        'workflow',
        'output_format',
        'quality_standards',
        'prompt_template'
    ]
    
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required key: {key}")
    
    return True
```

## 🏗️ Agent Architecture

```
┌─────────────────────────────────────────┐
│   PowerPoint 簡報生成器 (Orchestrator)   │
│   • 協調所有子 Agent                      │
│   • 整合輸出結果                          │
│   • 生成最終 .pptx 檔案                   │
└──────────────┬──────────────────────────┘
               │
    ┌──────────┴───────────┐
    │                      │
┌───▼──────┐        ┌──────▼────┐
│ Scenario │        │  Content  │
│Intelligence│      │ Strategist │
│          │        │           │
│ 場景分析  │        │ 內容策略   │
└──────────┘        └───────────┘
    │                      │
    │                      │
┌───▼──────┐        ┌──────▼────┐
│ Research │        │  Visual   │
│ Analyst  │        │ Designer  │
│          │        │           │
│ 研究分析  │        │ 視覺設計   │
└──────────┘        └───────────┘
    │                      │
    │                      │
┌───▼──────┐        ┌──────▼────┐
│  Chart   │        │  Quality  │
│ Designer │        │ Assurance │
│          │        │           │
│ 圖表設計  │        │ 品質保證   │
└──────────┘        └───────────┘
```

## 📊 Configuration Statistics

| Metric | Value |
|--------|-------|
| Total Agents | 7 |
| Total Configuration Lines | ~3,500 |
| Design Styles Supported | 5 |
| Chart Types Supported | 8 |
| Enterprise Scenarios | 8 |
| Quality Dimensions | 5 |
| Narrative Frameworks | 5 |

## 🎨 Design Styles

All agents support these 5 design styles:

1. **Business Professional** - Formal, conservative, blue-gray palette
2. **Tech Innovation** - Modern, dynamic, tech colors
3. **Creative Energy** - Vibrant, bold, colorful
4. **Academic Research** - Rigorous, traditional, academic colors
5. **Minimal Modern** - Clean, minimal, black-white-red

## 🔍 Quality Standards

Each agent has defined quality targets:

| Agent | Primary Metric | Target |
|-------|----------------|--------|
| Orchestrator | Overall Quality | 98/100 |
| Scenario Intelligence | Classification Accuracy | >90% |
| Content Strategist | Narrative Clarity | >95% |
| Research Analyst | Fact-Check Pass Rate | >95% |
| Visual Designer | WCAG Compliance | AA |
| Chart Designer | Visual Clarity | >90 |
| Quality Assurance | Detection Rate | >98% |

## 🚀 Quick Start

```bash
# 1. Load all configurations
python load_configs.py

# 2. Create agents from configs
python create_agents.py

# 3. Test agent system
python test_agents.py

# 4. Generate sample presentation
python generate_sample.py
```

## 📝 Customization

### Modify Workflow

Edit the `workflow` section in any config file:

```yaml
workflow:
  step_1:
    name: "Your Custom Step"
    input: "Input description"
    process: "Process description"
    output: "Output description"
```

### Add New Tools

Update the `available_tools` section:

```yaml
available_tools:
  - tool_name: "new_tool"
    description: "Tool description"
    parameters:
      - name: "param1"
        type: "string"
        required: true
```

### Adjust Quality Targets

Modify `quality_standards`:

```yaml
quality_standards:
  your_metric: "target value"
  another_metric: "≥ 95%"
```

## 🔗 Related Documentation

- [Agent System Architecture](../docs/Agent系統架構.md)
- [Quick Start Guide](../docs/快速開始指南.md)
- [Quality Control System](../docs/持續品質提升系統.md)
- [API Reference](../docs/API參考文檔.md)

## 📄 License

MIT License - See [LICENSE](../LICENSE) for details

## 🤝 Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines

---

**Last Updated**: 2026-01-30  
**Version**: 1.0.0  
**Maintainer**: AI Presentation System Team
