---
title: OpenWiki
created: 2026-08-07
updated: 2026-08-08
type: entity
tags: [openwiki, knowledge-base, cli]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-20-cosmic-harbor.md, raw/session-history/2026-07-23-mighty-star.md, raw/releases/openwiki-changelog-2026-08.md]
confidence: high
---

# OpenWiki

LangChain（[langchain-ai](https://github.com/langchain-ai/openwiki)）开源的 **Agent 文档 CLI**，自动生成并持续维护代码库或个人知识源的 wiki。TypeScript，MIT，约 14.6k star（2026-08）。^[raw/session-history/2026-07-18-misty-river.md] ^[raw/releases/openwiki-changelog-2026-08.md]

## 是什么

一句话：**为代码库或个人知识源自动编写并持续维护 agent 可读的 Markdown wiki。**

## 两种模式

| 模式 | 命令 | 输出位置 | 用途 |
|---|---|---|---|
| **Code 模式**（默认） | `openwiki --init/--update` | 仓库根 `openwiki/` | 当前代码库架构/模块文档 |
| **Personal 模式** | `openwiki personal --init/--update` | `~/.openwiki/wiki/` | 个人"第二大脑"，聚合多来源 |

## 关键特性

- **Agent-first**：生成 `AGENTS.md`/`CLAUDE.md` 中的 `# OPENWIKI:START` 块，引导 agent 先查 wiki
- **双向同步/CI**：GitHub Actions、GitLab CI、Bitbucket Pipeline 自动跑更新并提 PR
- **Mermaid 原生支持**：序列图、ER 图、状态图，带验证-降级-修复回路（v0.2.3 起）
- **原生 wiki 可视化器**（v0.2.5）：本地可视化 wiki 结构，无需外挂工具
- **`.openwikiignore`**（v0.2.5）：文档运行时可排除指定路径
- **内部链接验证**（v0.3.0）：生成后校验 wiki 内部链接，v0.3.1 修复误报
- **输出兼容 [[okf]] v0.1 规范**：YAML frontmatter 标记文档类型；frontmatter validator + index.md 中间件（v0.2.0）
- **`log.md` 更新日志**：每次运行生成，记录变更文件与位置（v0.2.0 OKF 化）
- **匿名 CLI telemetry**（v0.2.0）：run 事件遥测，可拒绝/超时上报
- **Built-in 连接器**（Personal 模式）：git-repo、Gmail、Notion、X、Web Search（Tavily）、Hackernews、Slack、MCP；LangSmith connector（v0.2.4)；同一连接器可配多个实例（如多个不同主题的 web-search），原始数据落 `~/.openwiki/connectors/<name>/raw/`
- **多模型供应商**：OpenAI、Anthropic、Gemini（含 Vertex/Gemini Enterprise）、Bedrock、Ollama、OpenRouter、NVIDIA NIM、Nebius、GitHub Copilot 等（v0.2.x 持续扩充）
- **多语言输出**（v0.2.4）：wiki agent 支持非英语输出

## 版本（截至 2026-08）

| 版本 | 日期 | 要点 |
|---|---|---|
| v0.3.1 | 2026-08-05 | latest；内部链接验证误报修复 |
| v0.3.0 | 2026-08-04 | 链接验证、agent 提示改进（guidance 可选/按需）、agent graph factory 导出 |
| v0.2.5 | 2026-07-31 | 原生 wiki 可视化器、`.openwikiignore` |
| 0.2.4 | 2026-07-29 | LangSmith connector、GitHub Copilot provider、多语言输出 |
| 0.2.3 | 2026-07-23 | Mermaid 图表生成、连接器容错（超时/重试/退避） |
| 0.2.2 | 2026-07-21 | Gemini 3.6 flash / 3.5 flash lite providers |
| 0.2.1 | 2026-07-20 | `--init` 向导重构、`OPENAI_BASE_URL`、code-mode 不再污染 `~/.openwiki/wiki` |
| 0.2.0 | 2026-07-16 | OKF 化 + telemetry、Gemini/Bedrock/Vertex 等新 provider |

## 架构

- Agent 框架 `deepagents`；状态管理 LangGraph + SQLite checkpoint（v0.2.4 起老 checkpoint 会被修剪）；终端渲染用 ink + React 18；遥测 posthog。
- **写保护设计**：docs-only write guard 拒绝 `..` 路径穿越（v0.2.3）；managed markers（`# OPENWIKI:START/END`）损坏时仍保留 agent 指令（v0.3.0）；并发环境保存序列化 + 临时文件隔离（v0.3.0）
- **输出卫生**：文件/图片内容块不泄漏进 CLI 输出（v0.2.4）；连接器 HTTP 带 timeout + 429/5xx 重试退避（v0.2.4）；telemetry 上报失败/超时如实报告（v0.3.0）
- **扩展性**：agent graph factory 可导出（v0.3.0）；`OPENAI_BASE_URL`/gateway 路由覆盖（v0.2.1/0.2.5）；模型 id 可含逗号以支持代理路由标识（v0.2.5）

## 自动更新机制

OpenWiki 自带「**定时重跑 + PR**」式更新，与本 wiki 的「**感知触发 + agent 摄取**」思路不同：

| | OpenWiki 内置 | 本 wiki（`scripts/auto_ingest.sh`） |
|---|---|---|
| 触发 | 固定周期（schedule）盲跑 `--update` | 检测上游版本变化才动作 |
| 输出 | 生成 diff 提 PR，人工审核合并 | agent 直接落库，lint 把关 |
| 覆盖 | 单一仓库/个人知识源 | 生态 8 个工具全监控 |
| 保留 | CI 配置（GitHub Actions / GitLab CI / Bitbucket Pipeline） | cron + `tracked-projects.json` |

Personal 模式另有 LaunchAgent 定时调度（日志落 `~/.openwiki/logs/`）。两种机制可互补：本 wiki 用感知触发避免盲跑噪声。

## 与同类的关系

见 [[openwiki-vs-graphify-vs-codegraph]]。核心：OpenWiki 是**叙事型文档**（LLM 写 .md），而 [[codegraph]]/[[graphify]] 是**结构化图谱**。

## 相关

- 概念：[[llm-wiki-ecosystem]]、[[okf]]、[[spec-vs-wiki]]
- 工具：[[graphify]]、[[codegraph]]