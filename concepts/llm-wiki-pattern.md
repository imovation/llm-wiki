---
title: LLM Wiki 模式
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [llm-wiki, rag-alternative, knowledge-base, three-layer]
sources: [raw/articles/llm-wiki.md, raw/articles/SKILL.md]
confidence: high
---

# LLM Wiki 模式

Andrej Karpathy 的 **LLM Wiki** 模式（2026-04）：不是 RAG，而是让 LLM **增量构建并维护一个持久 wiki**——位于你和原始来源之间的结构化互链 Markdown 集合。原始文档：`raw/articles/llm-wiki.md`。

## 核心：vs RAG

传统 RAG 每次查询时检索片段临时拼凑答案：LLM 每次从头**重新发现**知识，无积累、无结构、不持久。^[raw/articles/llm-wiki.md]

LLM Wiki 不同：
- 知识**一次性编译，持续保持最新**（不每次重新推导）
- 交叉引用**已经建好**、矛盾**已经标记**、综合**已反映所有已读材料**
- **复利效应**：每加一个来源、每问一个问题就变丰富

## 三层架构

1. **raw/ 原始来源**——不可变，LLM 只读不改。事实来源（source of truth）
2. **wiki**——LLM 完全拥有的 Markdown 层：摘要、实体页、概念页、对比、概览、综合。LLM 写，人类读
3. **schema**——告诉 LLM 如何组织的文档（SCHEMA.md / AGENTS.md）：约定、分解、工作流。人类与 LLM 不断共同调整

类比：**Obsidian 是 IDE，LLM 是程序员，wiki 是代码库。**

## 三个操作

- **Ingest**：新源 → 读 → 讨论 → 写摘要页 → 更新索引/实体/概念页 → 记 log。单源可触及 10-15 页
- **Query**：索引 → 找页 → 综合答案带引用。**好答案归档回 wiki（queries/）长期积累**
- **Lint**：健康检查——矛盾、被取代主张、孤儿、缺页、缺链、数据缺口

## 两个特殊文件

- **index.md**：内容目录（逐页一行链接+摘要），避免 embedding RAG。中等规模（~100 源/数百页）够用
- **log.md**：时间顺序、仅追加。前缀 `## [YYYY-MM-DD] action | subject` 可用 unix 工具解析

## 为什么可行

维护知识库的瓶颈是**记账**（交叉引用、保持更新、记录矛盾、一致性），人类因维护成本增长而放弃，LLM 不会厌倦/忘记，一次可触及 15 文件，**维护成本趋近零**。与 Vannevar Bush 的 Memex（1945）精神相通。

## 可选工具

- 搜索（wiki 变大后）：[[qmd]]
- Obsidian Web Clipper 剪藏；本地下载图片；图谱视图；Marp 幻灯片；Dataview
- 本模式的各种实现见 [[llm-wiki-ecosystem]]

## 相关

- 概念：[[llm-wiki-ecosystem]]、[[okf]]、[[spec-vs-wiki]]、[[three-layer-architecture]]
- 工具：[[llm-wiki-skill]]（agent 操作手册）、[[nashsu-llm-wiki]]