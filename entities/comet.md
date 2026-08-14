---
title: Comet
created: 2026-08-07
updated: 2026-08-14
type: entity
tags: [comet, ai-coding, workflow]
sources: [raw/session-history/2026-07-20-cosmic-harbor.md, raw/releases/tool-updates-2026-08.md, raw/releases/updates-2026-08-11.md, raw/releases/updates-2026-08-14.md]
confidence: medium
---

# Comet

[rpamis/comet](https://github.com/rpamis/comet)（约 2.7k star，MIT）。**Agent Skill 平台 + 可恢复的长任务工作流引擎**。将 OpenSpec artifacts 和 Superpowers 执行方法论组合为五阶段工作流。当前 0.4.0-beta 系列（2026-07 起），最新 0.4.0-beta.18（2026-08-13）。@^[raw/session-history/2026-07-20-cosmic-harbor.md] ^[raw/releases/tool-updates-2026-08.md] ^[raw/releases/updates-2026-08-11.md] ^[raw/releases/updates-2026-08-14.md]

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

## 版本动态

- **0.4.0-beta.18（2026-08-13）**：`comet eval` 支持独立 Skill 评估——不再依赖 `comet-any`，接受项目自写或自动生成任务、离线 `--collect`，subject 与 LLM-as-judge 独立模型/API 路由；评估 agent 可选用 Claude Code/Codex/Qoder/CodeBuddy（CLI 或 eval manifest 指定，Claude Code 仍默认）；Skill 可内联确定性任务或复用 `comet/eval.yaml` 的 `evaluation.tasks` 包级定义；无任务 Skill 首次正常运行自动生成有界、hash 缓存任务集（`--quick`/纯缓存 `--collect` 保留）；新增 Langfuse 评估套件（`comet eval --suite langfuse`，上报任务 trace/rubric 分/pass 指标/实验摘要，隔离缓存自动装 pin 版本官方 Claude Code/Codex 插件，捕获 Qoder/CodeBuddy 转录不改本地评分）；Native 新增 Supervisor Change 模式（识别需独立验收的大请求、确认时提出具名子图、串行兜底自动派发就绪子任务、按序并入 Supervisor 分支、按验收标准终验集成结果）；Dashboard 感知全部注册 Git worktree（Classic/Native 变更独立成根条目、显式子变更归组到可展开 Supervisor Change）；新增 WorkBuddy 平台支持（`comet init/update` 装/刷新 `.workbuddy/skills/`，项目安装合并 Hook 到 `.workbuddy/settings.json`）；用户级 Eval 配置 `~/.comet/eval/.env`（Bench 与 judge 凭据/endpoint/模型分离，缺失自动生成注释模板、绝不覆盖）；项目级 Hook 写入白名单 `hook.allow_paths`（`.comet/config.yaml`，共享规则/笔记可写，Runtime/workflow 产物仍受保护）；Classic 工作区路由（Open 时选/备当前分支或 Worktree）、Native 并行变更复用既有 Worktree；修复 macOS 打包 Hook Router 临时路径（含 `/var` 符号链接）执行、Classic 从嵌套目录发现 project root、Classic OpenSpec 版本透传、Codex OpenSpec skills 刷新（读 1.8 的 `.agents` Codex skill 输出，1.7 及更早回退 `.codex`，缺失/空 staged 输出明确失败）；安全：DOMPurify/Mermaid/Nanoid 依赖补丁（XSS/DoS/原型污染/CSS 注入/资源耗尽）。^[raw/releases/updates-2026-08-14.md]
- **0.4.0-beta.17（2026-08-10）**：独立 Native 验证（Builder 提交候选后，Comet 运行声明的本地检查、协调只读 Verifier 复核所有验收项，失败项经有界循环回到 Build）；新增 Trae / Trae CN 的 Hook Router 支持（`comet init/update/doctor/uninstall`，写官方 `hooks.json` 并保留用户配置）；Native 完成循环提速（Verify/Archive 不再扫描指纹、逐项重查，stdout/stderr 流到本地日志，长 Maven/Gradle/npm/Python 输出不再误判）；便携式 Native 恢复（`comet-state.yaml` 记录阶段/循环/handoff/阻断/检查/验证摘要，跨设备新 Agent 零上下文恢复；`verification.md` 可重建）；Native dashboard 工作流视图与 artifact 预览（展示可移植状态，机器专属 runtime 文件不进 artifact 列表）；批量 clarification 成为新项目默认、工作树/分支跟踪结构化的创建/发现/恢复/授权收尾；跨平台 Native 检查（Windows 上 npm/pnpm shim 不再 shell 特定失败，超时检查按进程树停止）；`comet doctor` 识别 Claude Code plugin 管理的 Superpowers 安装（不再误报安装警告）；移除旧 Native 验证簿记（项目级扫描设置与公共 checkpoint/check/evidence/receipt 命令链），旧 active changes 保守迁移、archived 只读。^[raw/releases/updates-2026-08-11.md]

## 相关

- 概念：[[spec-vs-wiki]]、[[openspec]]
- 工具：[[openwiki]]、[[graphify]]、[[langsmith]]