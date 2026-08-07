---
title: CodeGraph
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [codegraph, knowledge-graph, cli]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-20-cosmic-harbor.md, raw/session-history/2026-07-23-mighty-star.md]
confidence: high
---

# CodeGraph

[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)，Colby McHenry 开发的**本地优先代码智能工具**，将代码库化为 AI agent 可直接查询的**预索引知识图谱**（SQLite + FTS5）。TypeScript CLI + **Rust 内核**，MIT，约 61.9k star。@^[raw/session-history/2026-07-23-mighty-star.md]

## 核心定位：Surgical Context

> Agent 不需要读全部代码，它只需要精确的上下文。一次 `codegraph_explore` 调用返回相关符号的源代码、调用路径（含动态分发跳转）、变更影响半径。

关键差异：`codegraph_explore` 返回的是**源代码片段（带行号）**，不是图数据——相当于把 Read 工具结果缓存，消耗最小 agent 上下文。

## 关键特性

- **自动同步**：原生 OS 事件监听（FSEvents/inotify/ReadDirectoryChangesW），保存后 ~0.3s 增量更新，永不 stale
- **框架感知路由**：Django/FastAPI/Express/NestJS/Laravel/Rails/Spring 等 17+ 框架 URL → Handler
- **iOS/RN 跨语言桥接**：Swift↔ObjC、RN Bridge、TurboModules、Expo Modules
- **影响分析**：调用者/被调用者/完整影响半径
- **FTS5 全文搜索**：全代码库即时符号搜索
- **MCP Server**：给 AI agent 输出
- 支持 Claude Code、Cursor、Codex、OpenCode、Gemini、Antigravity 等

## 性能基准

7 个真实开源项目（Claude Opus 4.8，中位数 4次）：

| 指标 | WITH CodeGraph | WITHOUT |
|---|---|---|
| 工具调用 | **2-3** 次 | 10-57 次 |
| Token | 减少 **69%** | — |
| 成本 | 减少 **60%** | — |
| 文件读取 | **0** | 1-24 次 |
| 加速比 | 最大 5× | — |

## 内核：Rust + tree-sitter

20 种语言的 tree-sitter 语法编译为原生代码，每文件一次 FFI 调用，字节级正确性验证；无预编译平台回退 JS/WASM 引擎。100% 本地、无 API Key。^[raw/session-history/2026-07-23-mighty-star.md]

## 相关

- 概念：[[tree-sitter]]、[[cst-vs-ast]]
- 工具：[[graphify]]（最接近竞品）、[[openwiki]]
- 对比：[[openwiki-vs-graphify-vs-codegraph]]