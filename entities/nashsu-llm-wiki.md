---
title: nashsu llm_wiki
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [nashsu-app, knowledge-base, desktop]
sources: [raw/session-history/2026-07-18-misty-river.md]
confidence: medium
---

# nashsu llm_wiki

[nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)，作者 nash_su。**Karpathy LLM Wiki 模式最完整的桌面端产品化实现**。约 14.9k star，GPL v3，Tauri v2（TypeScript 71% + Rust 25%），当前 v0.6.5。@^[raw/session-history/2026-07-18-misty-river.md]

## 核心定位

**一个构建自身知识库的跨平台桌面应用。** 把文档丢进去，LLM 自动增量构建并维护结构化的互链 wiki。三栏 UI：文件树 + 聊天 + 预览。

## 核心亮点

1. **两阶段 CoT 摄入**（区别于单步）
   - Step 1：LLM 读源 → 结构化分析（提取实体/概念/矛盾）
   - Step 2：基于分析 → 生成 wiki 页面
   - SHA256 增量缓存 + 持久化摄入队列 + 崩溃恢复
2. **知识图谱（最独特）**
   - 4 信号相关模型：直接链接(×3) + 来源重叠(×4) + Adamic-Adar(×1.5) + 类型亲和(×1.0)
   - **Louvain 社区发现**（与 [[graphify]] 的 Leiden 同为社区发现算法，见 [[leiden-community-detection]]）
   - 图谱洞察：自动检测"意外关联"与"知识缺口"，点击触发 Deep Research
   - sigma.js + ForceAtlas2 力导向渲染
3. **多格式文档解析**：PDF（pdf-extract + 可选 MinerU）、DOCX、PPTX、XLSX、EPUB/MOBI、图片、音视频、网页剪藏
4. **向量搜索（可选）**：LanceDB 嵌入式向量库，任意 OpenAI 兼容端点

## 与同类区分

| | nashsu/llm_wiki | llm-wiki skill | llmwiki | OpenWiki |
|---|---|---|---|---|
| 形态 | 桌面 GUI（Tauri） | Agent 内置 skill | CLI+SDK+MCP | CLI |
| 图谱 | 有（sigma.js + Louvain） | 无 | 有(graph 目录+OKF) | 无 |
| 审核 | 异步 Review 队列 | schema 描述 | 运行时门控 | 无 |

## 相关

- 概念：[[llm-wiki-生态]]
- 工具：[[llm-wiki-compiler]]、[[llm-wiki-skill]]、[[openwiki]]、[[graphify]]