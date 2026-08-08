---
title: Comet
created: 2026-08-07
updated: 2026-08-08
type: entity
tags: [comet, ai-coding, workflow]
sources: [raw/session-history/2026-07-20-cosmic-harbor.md, raw/releases/tool-updates-2026-08.md]
confidence: medium
---

# Comet

[rpamis/comet](https://github.com/rpamis/comet)（约 2.4k star，MIT）。**Agent Skill 平台 + 可恢复的长任务工作流引擎**。将 OpenSpec artifacts 和 Superpowers 执行方法论组合为五阶段工作流。当前 0.4.0-beta 系列（2026-07 起），最新 0.4.0-beta.14。@^[raw/session-history/2026-07-20-cosmic-harbor.md] ^[raw/releases/tool-updates-2026-08.md]

## 关键特性

- **状态机 + 阶段守卫（phase guards）**：确保 agent 只在当前阶段做允许的事。例如在 Claude Code 上用 PreToolUse 阻止非当前阶段文件写入
- **可中断恢复**：`.comet.yaml` 记录进度，跨设备零上下文恢复（0.4.0 系列迁移至 `.comet/run-state.json` + 可审计事件流）
- **`/comet-any`**：把任意 Skill 组合为可分发的 Bundle
- **`comet eval`**：基于 Rubric / Pass@k / Pass^k 科学化评估，对接 [[langsmith]]
- **`comet dashboard`**（0.4.0-beta.1 起）：本地只读仪表盘，可视化变更阶段/风险/产物
- 支持 33+ AI 编码平台；0.4.0 起纯 Node 运行时（跨平台、去 Bash/WSL 依赖）
- 0.4.0-beta 新增 **Native 工作流**：与 Classic 并存，官方评测 token -76.8%、pass^3 87.5%

## 五阶段工作流

```
Open → Design → Build → Verify → Archive
```

（此后 Comet 体现成 Graphify/CodeGraph 相同的"注入 AGENTS.md/CLAUDE.md"手法，但目的不同。）

## 生态位重叠

与 [[openwiki]]/[[graphify]]：
- 共用 AGENTS.md / CLAUDE.md 注入（Comet 注入 resume 块、Graphify 注入查询指令），但分隔符不同，可共存
- 共用 Claude Code PreToolUse hook 机制——同机制，不同目的
- Comet 独占：五阶段状态机、SKILL 创建/分发/评估、科学评测、LangSmith 集成

## 相关

- 概念：[[spec-vs-wiki]]、[[openspec]]
- 工具：[[openwiki]]、[[graphify]]、[[langsmith]]