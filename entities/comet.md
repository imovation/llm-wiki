---
title: Comet
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [comet, ai-coding, workflow]
sources: [raw/session-history/2026-07-20-cosmic-harbor.md]
confidence: medium
---

# Comet

[rpamis/comet](https://github.com/rpamis/comet)（约 2.4k star，MIT）。**Agent Skill 平台 + 可恢复的长任务工作流引擎**。将 OpenSpec artifacts 和 Superpowers 执行方法论组合为五阶段工作流。@^[raw/session-history/2026-07-20-cosmic-harbor.md]

## 关键特性

- **状态机 + 阶段守卫（phase guards）**：确保 agent 只在当前阶段做允许的事。例如在 Claude Code 上用 PreToolUse 阻止非当前阶段文件写入
- **可中断恢复**：`.comet.yaml` 记录进度，跨设备零上下文恢复
- **`/comet-any`**：把任意 Skill 组合为可分发的 Bundle
- **`comet eval`**：基于 Rubric / Pass@k / Pass^k 科学化评估，对接 [[langsmith]]
- 支持 33+ AI 编码平台，纯 Node.js；Dashboard 可视化跟踪

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