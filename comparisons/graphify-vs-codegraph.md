---
title: Graphify vs CodeGraph
created: 2026-08-07
updated: 2026-08-07
type: comparison
tags: [graphify, codegraph]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-23-mighty-star.md]
confidence: high
---

# Graphify vs CodeGraph

两者都在"把代码索引为 AI Agent 可查询的知识图"这一生态位，但技术路线和侧重点差异明显。@^[raw/session-history/2026-07-18-misty-river.md]

## 详细对比

| 维度 | CodeGraph (colbymchenry) | Graphify (Graphify-Labs) |
|---|---|---|
| 解析引擎 | **Rust 原生**（20 语言，逐文件校验一致性） | **Python** + tree-sitter（40+ 语法） |
| 同步方式 | 原生文件监听，自动增量同步（<1s） | git hook 触发，CI/--watch 重建 |
| 跨语言桥接 | iOS/RN/Expo 跨语言边界（Swift↔ObjC, JS↔Native） | 弱（多语言审计较弱） |
| 存储 | SQLite (FTS5) | graph.json + HTML + report |
| 给 agent 的返回 | 源片段 + 行号 + 影响半径 | 图路径/社区/神节点 |
| 多模态 | ❌ 纯代码 | ✅ 文档/PDF/图片/视频 |
| 影响力分析 | 调用者/被调者/完整半径 | 神节点 + 惊喜连接 |
| Stars | ~62k | ~94k |
| 安装 | npx/@native binary | `uv tool install graphifyy` |

## 一句话总结

- **CodeGraph**：工程上更"外科手术式"——给 agent **精确的源码上下文**，自动监听永不 stale，省 token 王
- **Graphify**：更"全景观"——多模态入图 + Leiden 社区 + 神节点分析 + 可交互 HTML，既有代码也有文档/媒体的场景

## 选型

- 纯代码库、日常编码 Agent 协作用 → CodeGraph
- 代码+文档+图片+视频混合、要可视化图谱 → Graphify

## 相关

- 实体：[[codegraph]]、[[graphify]]
- 对比总表：[[openwiki-vs-graphify-vs-codegraph]]
- 概念：[[leiden-community-detection]]、[[god-node-analysis]]、[[tree-sitter]]