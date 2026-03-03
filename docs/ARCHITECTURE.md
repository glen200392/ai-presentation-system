# System Architecture Documentation

**Version**: 2.0  
**Last Updated**: 2026-01-30  
**Status**: Production Ready (90/100)

## 📊 Architecture Diagrams

### 1. System Architecture Diagram
![System Architecture](./images/system_architecture_diagram.png)

**說明**: 完整的系統架構，展示 8 個 Agents 的協作關係、工具包層、輸出層。

**關鍵組件**:
- User Interface Layer
- Orchestrator Agent (PowerPoint 簡報生成器)
- 6 個 Sub-Agents（按 3 個 Phase 組織）
- Toolkit & API Layer
- Output Layer (.pptx + Charts + Logs)

---

### 2. Workflow Diagram
![Workflow Diagram](./images/workflow_diagram.png)

**說明**: 端到端的工作流程，從使用者輸入到最終交付。

**流程步驟** (總時間 ~12 分鐘):
1. User Input (1 min)
2. Scenario Analysis (2 min)
3. Content Strategy (2 min)
4. Research & Data (2 min)
5. Visual Design (1 min)
6. **Chart Generation ★** (3 min) - v2.0 新增
7. Assembly & QA (1 min)

---

### 3. Agent Collaboration Network
![Agent Collaboration](./images/agent_collaboration_diagram.png)

**說明**: 8 個 Agents 的協作網絡拓撲圖。

**協作統計**:
- 8 個 Agents
- 100% 執行覆蓋率
- 12 分鐘總時間
- v2.0 改進：Chart Designer 啟用 (+3 圖表)、Agent 日誌啟用 (100% 透明)

---

## 🏗️ 技術架構

### Multi-Agent 協作模式

系統採用 **Orchestrator-Driven** 架構模式：

```
Orchestrator (主控)
    ├─→ Phase 1: 需求分析 (3 Agents)
    │   ├─ Scenario Intelligence
    │   ├─ Content Strategist
    │   └─ Research Analyst
    ├─→ Phase 2: 視覺設計 (2 Agents)
    │   ├─ Visual Designer
    │   └─ Chart Designer ★ (v2.0 已啟用)
    └─→ Phase 3: 組裝 & QA (1 Agent)
        └─ Quality Assurance
```

### Agent 工具包

每個 Agent 配置特定工具包：

| Agent | 工具包 | 用途 |
|-------|--------|------|
| Orchestrator | Web, Python, File Mgmt, Image Gen, **Agent Delegation** | 統籌所有 Sub-Agents |
| Research Analyst | Web, Python, File Mgmt | 數據研究與驗證 |
| Chart Designer | **Python**, Web | 圖表生成 |
| Visual Designer | Python | 配色與版面設計 |
| Content Strategist | Web | 內容策略與大綱 |
| Scenario Intelligence | (無) | 場景分類 |
| Quality Assurance | Web, Code | 品質檢查 |

---

## 📈 v2.0 架構改進

### 關鍵修復

1. **Chart Designer 啟用**
   - 問題：v1.0 完全未被呼叫
   - 解決：為 Orchestrator 添加 **Agent Delegation** 工具包
   - 成效：成功生成 3 個專業圖表（+15 分）

2. **Agent 協作透明化**
   - 問題：無法驗證 Agents 執行狀態
   - 解決：完整記錄所有 Agent 執行日誌
   - 成效：100% 透明度（+5 分）

3. **演講者備註嵌入**
   - 問題：備註在外部文檔
   - 解決：直接嵌入 .pptx notes 欄位
   - 成效：9/9 投影片都有備註（+2 分）

### 架構優勢

✅ **模組化**: 每個 Agent 專注單一職責  
✅ **可擴展**: 易於添加新 Agents  
✅ **容錯**: Agent 失敗不影響整體流程  
✅ **透明**: 完整執行日誌可追蹤  
✅ **高效**: 12 分鐘完成完整簡報

---

## 🔄 部署架構

### 開發環境
- Python 3.9+
- Nebula Agent Platform
- GitHub Repository

### 生產環境需求
- Agent Runtime（Nebula Platform）
- Python 執行環境
- 網路存取（Web Search, API）
- 文件儲存（.pptx, PNG）

### 擴展性
- 當前：8 個 Agents
- 未來可擴展至 10+ Agents（不同產業模板）
- 支援並行執行（Phase 1 的 3 個 Agents 可並行）

---

## 📚 相關文檔

- [Agents Configuration](../agents/agents_config_v2.json) - 完整 Agent 配置
- [Optimization Test Report](./optimization_test_report_v2.md) - v2.0 測試報告
- [Use Cases](./USE_CASES_DETAILED.md) - 5 個產業應用案例
- [QA Report](./QA_REPORT_v2.md) - 品質保證檢查報告
- [README](../README.md) - 系統概覽

---

**維護者**: AI Presentation System Team  
**最後更新**: 2026-01-30
