---
title: OpenWiki 使用说明
created: 2026-08-08
updated: 2026-08-08
type: query
tags: [openwiki, cli, workflow]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-23-mighty-star.md, raw/releases/openwiki-changelog-2026-08.md]
confidence: high
---

# OpenWiki 使用说明

## 问题

OpenWiki（LangChain 的 agent 文档 CLI）怎么用？含安装、命令、两种模式、CI 集成与调试。

## 安装与命令

- 安装：`npm install -g openwiki`（Node ≥ 22）^[raw/session-history/2026-07-23-mighty-star.md]

| 命令 | 用途 |
|---|---|
| `openwiki --init` | 向导配置 provider/API key/模型（默认 OpenAI `gpt-5.6-terra`） |
| `openwiki --update` | Code 模式生成/增量更新（文档不存在时自动创建，CI 里可直接用） |
| `openwiki personal --init/--update` | Personal 模式 → `~/.openwiki/wiki/` |
| `openwiki auth <provider>` | OAuth 登录（Gmail/Slack/X/Notion） |

## Code 模式工作流

1. `--init` 向导 → 生成仓库根 `openwiki/` 文档
2. 每次运行维护 `AGENTS.md`/`CLAUDE.md` 的 `<!-- OPENWIKI:START -->` 块：**只重写该区块**，保留用户自定义内容 ^[raw/session-history/2026-07-23-mighty-star.md]
3. `openwiki/INSTRUCTIONS.md`：用户编写的 wiki 指令（scope/priorities），生成时读取但不覆写
4. CI：GitHub Actions `openwiki code --update --print`；GitLab CI 自动建 MR；Bitbucket Pipeline 自定义调度

## Personal 模式

- 连接器：`git-repo`/`hackernews`（免认证）、`x`/`notion`/`google`/`slack`（OAuth；Slack 需 ngrok，Gmail/Slack 需自建 OAuth 应用）、`web-search`（需 `TAVILY_API_KEY`）
- 同一连接器可多实例（`web-search-1`/`web-search-2`），原始数据落 `~/.openwiki/connectors/<name>/raw/`
- macOS 支持 LaunchAgent 定时调度，日志落 `~/.openwiki/logs/`

## 模型与调试

- 多 provider：OpenAI（API key 或 ChatGPT 登录）、Anthropic、Gemini/Vertex（Google ADC）、Bedrock（IAM）、OpenRouter、NVIDIA NIM、Nebius、任意 OpenAI 兼容端点（Ollama/LiteLLM）；支持自定义 BASE_URL
- 配置 `LANGSMITH_API_KEY` 可追踪每次运行的 LLM 调用链（调试/成本分析）
- 遥测：PostHog 仅收集命令类型与成败状态；`OPENWIKI_TELEMETRY_DISABLED=1` 或 `DO_NOT_TRACK=1` 关闭

## 局限

文档质量取决于 LLM 能力；OAuth 连接器需应用注册；LaunchAgent 仅 macOS；wiki 面向 agent 优化，人类可读性一般。

## 相关

- [[openwiki]]（实体页：特性/版本表/架构）、[[okf]]（输出格式）、[[llm-wiki-ecosystem]]（生态定位）
- 更新机制：定时重跑 + PR，与本 wiki 的感知触发不同（见 [[openwiki]] 对比表）