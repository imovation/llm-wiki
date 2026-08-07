---
title: LLM Wiki 生态
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [llm-wiki, knowledge-base, ecosystem]
sources: [raw/articles/llm-wiki.md, raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-23-mighty-star.md]
confidence: medium
---

# LLM Wiki 生态

围绕 [[llm-wiki-模式]] 衍生出的工具、规范、变体全景图。本概念页梳理它们的定位关系。

## 五项目定位对比（源自 07-18 会话）

| | Karpathy 原文 | Hermes Skill | OpenWiki | llm-wiki-compiler | OKF v0.1 |
|---|---|---|---|---|---|
| **性质** | 抽象模式 | 内置技能（Agent 指导） | CLI（知识源→wiki） | **CLI/SDK 编译器**（raw→Page） | 数据交换规范 |
| **语言** | Markdown | Markdown | TypeScript (CLI) | TypeScript (CLI+SDK+MCP) | — |
| **输出** | 概念.md | 概念/实体/对比.md | OKF 格式 bundle | 类型化页面 + OKF | 无实现 |
| **模式** | 手动喂给 agent | agent 自己执行 | 代码/个人 | 领域模板（autosci/newsroom） | 仅格式定义 |

## 知识管理生态全图（三工具流水线）

```
Graphify（理解）→ OpenWiki（记录）→ Comet（执行+评估）
   知识图谱        项目文档         工作流编排 & 科学评测
```

- AI 编程中三者互补：**graphify/codegraph 先理解，openwiki 记录，comet 执行与评测**
- 三者生态位有重叠：OpenWiki ↔ Graphify（"理解代码库"层最大重叠），但分别走**叙事文档**与**结构化图谱**两条路

## 更完整的生态网

- 桌面端产品化：[[nashsu-llm-wiki]]（最完整：两阶段 CoT + 知识图谱 + Louvain）
- 编译路线：[[llm-wiki-compiler]]（批量、生命周期门控）
- 代码图谱路线：[[codegraph]]、[[graphify]]
- 搜索：[[qmd]]
- 规范层：[[okf]]
- 流程指令层：[[openspec]]（spec）、[[comet]]（执行编排）
- 观测：[[langsmith]]

## 应用场景

- AI 原生软件工程文档体系（哪些传统文档进 Spec、哪些进 Wiki，见 [[spec-vs-wiki]]）
- 离职交接方案（Cookie 图谱冻结 + Spec 补齐 + Wiki 编译 + 搜索就绪）
- 个人知识库：Obsidian + agent skill 场景化

## 相关

- 核心概念：[[llm-wiki-模式]]、[[okf]]、[[spec-vs-wiki]]、[[三层架构]]
- 对比：[[openwiki-vs-graphify-vs-codegraph]]