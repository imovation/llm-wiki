---
title: OpenSpec
created: 2026-08-07
updated: 2026-08-20
type: entity
tags: [openspec, spec-driven, ai-coding]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/releases/tool-updates-2026-08.md, raw/releases/updates-2026-08-14.md, raw/releases/updates-2026-08-20.md]
confidence: high
---

# OpenSpec

[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)（约 65.5k star，MIT，TypeScript CLI）。**规范驱动开发（SDD）框架**——在写代码之前，人类和 AI 先在规范上达成一致。npm 最新 v1.10.0（2026-08-19；v1.9.0 2026-08-13）。

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

- **v1.10.0（2026-08-19，Zed support & quieter installs）**：新增 **Zed Agent**——`openspec init --tools zed` 把工作流 skills 装进 `.agents/skills/`，以 `/openspec-propose` 斜杠命令调用（skills-only，需 Zed v1.4.2+）；**非英语产物**——`openspec init --language <language>` 不经手改 `config.yaml` 设置生成产物语言，OpenSpec 标题与 `SHALL`/`MUST` 保持英语、规范仍可校验；**更安静安装**——发布包声明零 install scripts，`npm install -g` 不再弹像打包缺陷的 `allow-scripts` 告警（且其建议的 `npm approve-scripts` 对全局安装本就无效），shell 补全提示改由 CLI 自己经 stderr 发一次、仅当有人在读；**任务计划**——生成任务必须写明"如何知道做完了"（测试/命令/可观察结果/交付物），"Implement the thing" 不再算计划；**提示库**——多选 picker 展示完整按键帮助，导航/全选/反选不再靠口耳相传；修复：`openspec feedback` 不再把整份报告当 issue 标题、正文只剩元数据，改保留报告文本、标题可控长度；归档淘汰能力若规范里还有合并无法处理的内容会死路于无引导的 `Spec must have at least one requirement`，现中止时明确指出是什么挡路；`specs` 指令此前从相对工作目录的路径读主规范——store 缺规范或静默返回同名不同能力时现纠正；自定义 profile 可只选 archive 不选 sync 导致归档调一个从未安装的工作流；OpenCode `/opsx-propose add-auth` 此前在进入工作流前丢掉了 `add-auth`；无 spec 产物的 schema 变体创建即校验失败、要求一个 schema 永远产不出的 delta；首启 telemetry 提示从 stdout 移到 stderr——`openspec spec show auth > auth.md` 不再把提示写进文件；`openspec update` 不再建议 Claude Code/Codex 等 CLI 工具重启它们没有的 IDE。^[raw/releases/updates-2026-08-20.md]

## 相关

- 概念：[[spec-vs-wiki]]、[[okf]]
- 工具：[[comet]]（组合 OpenSpec + Superpowers）