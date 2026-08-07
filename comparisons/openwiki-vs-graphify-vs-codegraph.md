---
title: OpenWiki vs Graphify vs CodeGraph
created: 2026-08-07
updated: 2026-08-07
type: comparison
tags: [openwiki, graphify, codegraph]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-20-cosmic-harbor.md, raw/session-history/2026-07-23-mighty-star.md]
confidence: high
---

# OpenWiki vs Graphify vs CodeGraph

三个"agent 理解代码库"工具的核心对比。三个哲学：

```
OpenWiki:   Agent 需要读文档 → 我生成 Wiki
Graphify:   Agent 需要查代码 → 我建知识图谱
CodeGraph:  Agent 需要精确上下文 → 我给 Surgical Context
```

## 核心理念对比

| 维度 | OpenWiki | Graphify | CodeGraph |
|---|---|---|---|
| 作者 | LangChain AI | Graphify Labs (YC S26) | Colby McHenry |
| 语言 | TypeScript | Python | **Rust 内核 + TS CLI** |
| 给 Agent 什么 | 自然语言文档 | 图结构（节点+边） | **源代码 + 调用路径** |
| 读取方式 | Agent 读 .md | `query/path/explain` 图遍历 | `codegraph_explore` 返回源+行号 |
| 确定性 | 低（LLM 生成） | 高（tree-sitter）+ LLM/media | **最高（Rust AST + 逐字节校验）** |
| 存储 | Markdown Wiki | JSON 图文件 | **SQLite (FTS5)** |
| 更新 | LLM 全量重生成 | 增量 patch ~0.8s | **OS 事件自动同步 ~0.3s** |
| 视觉化 | ❌ | ✅ 力导向 HTML + 社区着色 | 无（Agent 优先） |
| 外部数据源 | Gmail/Notion/X/WEB | PDF/图片/视频/论文 | —（纯代码） |
| 基准 | N/A | LOCOMO recall@10 0.497 | **89% 少工具调用、69% 少 tokens** |
| stars | ~13k | ~94k | ~62k |

## 关键分水岭

**CodeGraph 返回源代码片段（带行号），不是图数据**——agent 可直接使用，相当于把 Read 结果缓存，最省上下文。Graphify 返回图路径，还需再 Read。OpenWiki 返回 LLM 重写的自然语言，信息有损。

## 更新机制

| | OpenWiki | Graphify | CodeGraph |
|---|---|---|---|
| 首次构建 | 分钟级（LLM） | 秒级 | 秒-12 分钟看机器 |
| 增量 | 全重生成 | patch ~0.8s | 监听 ~0.3s |
| 自动监听 | ❌ | ⚠️ watch | ✅ FSEvents/inotify |
| CI | ✅ 三平台 | ✅ | 纯本地 |

## 选型

- 要**广播性文档**（给人/agent 读的架构说明）→ OpenWiki
- 要**多模态**（代码+文档+媒体混图）→ Graphify
- 要**给 Agent 最省 token 的精确源码上下文**（编码日常）→ CodeGraph

## 相关

- 实体：[[openwiki]]、[[graphify]]、[[codegraph]]
- 概念：[[llm-wiki-ecosystem]]、[[tree-sitter]]