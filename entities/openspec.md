---
title: OpenSpec
created: 2026-08-07
updated: 2026-08-08
type: entity
tags: [openspec, spec-driven, ai-coding]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/releases/tool-updates-2026-08.md]
confidence: high
---

# OpenSpec

[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)（约 61.7k star，MIT，TypeScript CLI）。**规范驱动开发（SDD）框架**——在写代码之前，人类和 AI 先在规范上达成一致。npm 最新 v1.8.0（2026-08-05；v1.7.0 2026-07-29）。

## 一句话

> 用 `/opsx:propose "想法"` 让 AI 把你的需求变成结构化规范（提案→需求→设计→任务），你审核后 `/opsx:apply` 实现，`/opsx:archive` 归档。所有决策以 Markdown 留在仓库，不散落在聊天历史。

## 工作流

```
/opsx:explore  → 不确定怎么做？AI 先读代码讨论
/opsx:propose  → openspec/changes/<name>/ 
                  ├── proposal.md (为什么做)
                  ├── specs/ (需求 + WHEN/THEN 场景)
                  ├── design.md (技术方案)
                  └── tasks.md (实现清单)
/opsx:apply    → 按 tasks.md 逐项实现
/opsx:archive  → 归档，规范更新
```

## 设计哲学

`fluid not rigid` · `iterative not waterfall` · `easy not complex` · **`built for brownfield`**（为既有项目设计）· 纯 Markdown 无特殊语法。

## 与 Spec wiki 的位置

见 [[spec-vs-wiki]]——OpenSpec 是 **spec 层的标准实现**，与 [[llm-wiki-ecosystem]] 的 wiki 层互补。对离职交接场景，它能把"为什么这么做"提炼为决策记录。@^[raw/session-history/2026-07-18-misty-river.md]

## 相关

- 概念：[[spec-vs-wiki]]、[[okf]]
- 工具：[[comet]]（组合 OpenSpec + Superpowers）