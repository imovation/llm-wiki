---
title: OpenSpec
created: 2026-08-07
updated: 2026-08-14
type: entity
tags: [openspec, spec-driven, ai-coding]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/releases/tool-updates-2026-08.md, raw/releases/updates-2026-08-14.md]
confidence: high
---

# OpenSpec

[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)（约 64.8k star，MIT，TypeScript CLI）。**规范驱动开发（SDD）框架**——在写代码之前，人类和 AI 先在规范上达成一致。npm 最新 v1.9.0（2026-08-13；v1.8.0 2026-08-05）。

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

## 版本动态

- **v1.9.0（2026-08-13，Command Code & safer specs）**：新增 Command Code 工具支持——`openspec init --tools command-code` 装工作流 skills，并经 adapter 在 `.commandcode/commands/` 生成 `/opsx-*` 斜杠命令；`openspec validate --archived` 可选校验 `changes/archive/` 中每个 change 的 `tasks.md` 复选框是否全勾选（未完成退出非零，适合 pre-commit/CI 钩子抓未完成归档）；root 解析更诚实——`list`/`validate --all|--changes|--specs`/`schemas` 在 OpenSpec root 外大声失败而非静默解析空 root；创作期场景安全——`validate` 把每个需求下 `####` 子块计为场景，MODIFIED 会丢场景的块在 archive 删除前拦截；`spec-driven` change 校验重复任务 ID 与 `## N.` 组错配（`--strict` 强制）；`archive` 非 TTY 用纯文本提示（CI 日志无转义码）、首次 telemetry 提示不再污染 `--json`；delta 同步保留 `## Requirements` 周围空行、文件以恰一个换行结尾（忠实重建）；`openspec schema fork` 就地编辑 YAML 保留注释/块标量风格/键序；`openspec update` 不再覆盖 vendor-neutral `.agents` skills 树（legacy Codex 升级也不翻转目标）；apply 指引要求 agent 浮出范围外工作而非静默推迟。^[raw/releases/updates-2026-08-14.md]

## 相关

- 概念：[[spec-vs-wiki]]、[[okf]]
- 工具：[[comet]]（组合 OpenSpec + Superpowers）