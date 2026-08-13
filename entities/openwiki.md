---
title: OpenWiki
created: 2026-08-07
updated: 2026-08-13
type: entity
tags: [openwiki, knowledge-base, cli]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-20-cosmic-harbor.md, raw/session-history/2026-07-23-mighty-star.md, raw/releases/openwiki-changelog-2026-08.md, raw/articles/openwiki-readme.md, raw/releases/updates-2026-08-13.md]
confidence: high
---

# OpenWiki

LangChain（[langchain-ai](https://github.com/langchain-ai/openwiki)）开源的 **Agent 文档 CLI**，自动生成并持续维护代码库或个人知识源的 wiki。TypeScript，MIT，约 15k star（2026-08）。^[raw/session-history/2026-07-18-misty-river.md] ^[raw/releases/openwiki-changelog-2026-08.md]

## 是什么

一句话：**为代码库或个人知识源自动编写并持续维护 agent 可读的 Markdown wiki。**

## 两种模式

| 模式 | 命令 | 输出位置 | 用途 |
|---|---|---|---|
| **Code 模式**（默认） | `openwiki --init/--update` | 仓库根 `openwiki/` | 当前代码库架构/模块文档 |
| **Personal 模式** | `openwiki personal --init/--update` | `~/.openwiki/wiki/` | 个人"第二大脑"，聚合多来源 |

## 关键特性

- **Agent-first**：维护 `AGENTS.md`/`CLAUDE.md` 中的 `<!-- OPENWIKI:START -->` 块（只重写该块）；`openwiki/INSTRUCTIONS.md` 用户指令只读取不覆写（v0.3.0 起 agent 提示可选/按需）
- **双向同步/CI**：GitHub Actions、GitLab CI、Bitbucket Pipeline 自动跑更新并提 PR；**no-op 免费**——每次运行快照 `openwiki/` 目录，仅在真有变更时记录新元数据，调度 CI 不空转
- **Mermaid 原生支持**（v0.2.3）：序列/ER/状态/流程图；默认零依赖轻量校验，可 `npm install mermaid jsdom` 权威校验（与 GitHub 渲染一致）；失败降级为 text fence+注释，下次 `--update` 修复
- **原生 wiki 可视化器**（v0.2.5）：`openwiki visualize` 把 wiki 变成交互式节点图 + 侧边 Markdown 阅读器；loopback 127.0.0.1（默认端口 4321 自增，`--port`/`--no-open`）；图谱/Markdown 库走公共 CDN（需联网）
- **`.openwikiignore`**（v0.2.5）：gitignore 风格（注释/`*`/`**`/目录/`!` 否定）；语义是**读边界**——忽略路径永不读取/扫描/复现（不保证不提及）
- **内部链接验证**（v0.3.0）：生成后校验 wiki 内部链接，v0.3.1 修复误报
- **输出兼容 [[okf]] v0.1 规范**（v0.2.0）：frontmatter 仅 `type` 必填；根 index 声明 `okf_version: "0.1"`；合法 timestamp/扩展字段跨更新与迁移保留
- **`log.md` 更新日志**：每次运行生成，记录变更文件与位置（v0.2.0 OKF 化）
- **匿名 telemetry**（v0.2.0）：单 `openwiki_run` 事件（命令/成败/粗粒度错误类）；从不收集文件内容/凭据/提示词/输出/IP；`OPENWIKI_TELEMETRY_DISABLED=1` 或 `DO_NOT_TRACK=1` 关闭；`--telemetry-file=` 查看将上报内容；对话/CI 不计作品安装
- **Built-in 连接器**（Personal 模式）：git-repo、Gmail、Notion、X、Web Search（Tavily）、Hackernews、Slack、MCP；同一连接器可配多实例（`web-search-1/2`），原始数据落 `~/.openwiki/connectors/<name>/raw/`；`openwiki auth <provider>` 本地浏览器 OAuth（token 存 `~/.openwiki/.env`）、`auth configure/tools` 进阶重试、`openwiki ngrok start` 为 Slack OAuth 开隧道（自动写 `OPENWIKI_HTTPS_OAUTH_REDIRECT_URI`）
- **LangSmith connector**（v0.2.4，**code 模式**）：拉近期 trace（工具调用/结果/延迟）入代码 wiki，文档反映真实运行时行为；配置写入提交版 `openwiki/.langsmith.json`（只含 workspace/project 名，不含 key）；key 从 `OPENWIKI_LANGSMITH_API_KEY` 读，多 workspace 用 `_2`/`_3` 后缀，仅官方 US/EU 端点
- **12 个模型供应商**：OpenAI（`gpt-5.6-terra` 默认）/ChatGPT 登录（`openai-chatgpt` 走 Codex 后端，用订阅额度）/Anthropic/Gemini/Vertex（Model Garden 含 Claude 与伙伴模型，ADC 免 key）/Bedrock（IAM）/GitHub Copilot（`COPILOT_API_KEY` 需 OAuth token，PAT 被拒）/OpenRouter（`OPENWIKI_OPENROUTER_PROVIDER_ONLY` 可 pin 上游）/Nebius/NVIDIA NIM/OpenAI 兼容（Ollama 等）；base URL 族 env（`ANTHROPIC_BASE_URL` 等）+ 重试次数 `OPENWIKI_PROVIDER_RETRY_ATTEMPTS`（默认 3）
- **多语言输出**（v0.2.4）：`--language <locale>` 生成指定语言，代码/标识符保持规范
- **交互聊天**：运行后保持对话（`/api-key`、`/langsmith-key` 命令）；`-p`/`--print` 一次性打印退出；`--init`/`--update` 交互终端下成功自动退出

## 版本（截至 2026-08）

| 版本 | 日期 | 要点 |
|---|---|---|
| v0.3.2 | 2026-08-11 | latest；安全与结构：pin 补丁版 js-yaml/undici（pnpm overrides）、Windows stdio MCP 子进程注入 `APPDATA`/`LOCALAPPDATA`、`dist/cli.js` exec bit 保留、CLI/仓库按领域模块重构 + 测试覆盖、错误分类与运行记账加固、credentials 纯逻辑拆分 |
| v0.3.1 | 2026-08-05 | 内部链接验证误报修复 |
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

Personal 模式另有 LaunchAgent 定时调度（日志落 `~/.openwiki/logs/`）。两种机制可互补：本 wiki 用感知触发避免盲跑噪声。补充：no-op 快照机制让 OpenWiki 的盲跑不产生 git 噪音（见上「关键特性」）。

## 命令快览

| 命令 | 说明 |
|---|---|
| `openwiki` / `openwiki personal` | 交互聊天会话（code/personal） |
| `openwiki "generate docs"` | 带初始指令进入 |
| `openwiki -p "what can you do?"` | 一次性会话，打印后退出（`--print`） |
| `openwiki --init/--update` | code 模式初始化/更新（personal 加 positional） |
| `openwiki visualize [dir] --port N --no-open` | 可视化节点图 |
| `openwiki auth <provider>\|configure\|tools` | 连接器认证（浏览器 OAuth）与进阶重试 |
| `openwiki ingest all\|<connector>` | 手动运行连接器摄取 |
| `openwiki ngrok start [domain]` | Slack OAuth 反向隧道 |
| `openwiki --help` | 完整帮助 |

## 与同类的关系

见 [[openwiki-vs-graphify-vs-codegraph]]。核心：OpenWiki 是**叙事型文档**（LLM 写 .md），而 [[codegraph]]/[[graphify]] 是**结构化图谱**。

## 相关

- 概念：[[llm-wiki-ecosystem]]、[[okf]]、[[spec-vs-wiki]]
- 工具：[[graphify]]、[[codegraph]]