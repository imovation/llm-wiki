---
title: OpenWiki 使用说明
created: 2026-08-08
updated: 2026-08-08
type: query
tags: [openwiki, knowledge-base, workflow]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-23-mighty-star.md, raw/releases/openwiki-changelog-2026-08.md, raw/articles/openwiki-readme.md]
confidence: high
---

# OpenWiki 使用说明

## 问题

OpenWiki（LangChain 的 agent 文档 CLI）怎么用？查询安装、命令、两种模式、CI 集成与自定义项。

## 安装

- `npm install -g openwiki`（Node ≥ 22）；Windows 用 npm/pnpm 装（`bun` 可能触发 better-sqlite3 原生编译，需要 VS Build Tools）

## 命令一览

| 命令 | 用途 |
|---|---|
| `openwiki` / `openwiki personal` | 交互式会话（默认 code 模式；`--mode personal` 亦可） |
| `openwiki "generate docs"` / `-p "..."` | 带初始指令进入 / 一次性打印退出（`--print`） |
| `openwiki --init` | 向导配置 provider/key/模型（默认 OpenAI `gpt-5.6-terra`）后生成 `openwiki/` |
| `openwiki --update` | 增量更新；文档不存在时自动创建（CI 可直接用，交互终端成功自动退出） |
| `openwiki personal --init/--update` | Personal 模式 → `~/.openwiki/wiki/` |
| `openwiki visualize [dir] [--port N] [--no-open]` | 交互式节点图 + 侧边 Markdown 阅读器（loopback 127.0.0.1:4321） |
| `openwiki auth <provider>\|configure\|tools` | 本地浏览器 OAuth / 进阶重试命令 |
| `openwiki ingest all\|<connector>` | 手动运行一个或多个已配置源 |
| `openwiki ngrok start [domain]` | 为 Slack OAuth 建反向隧道 |
| `openwiki --help` | 完整帮助 |

聊天内命令：`/api-key` 更新 provider key、`/langsmith-key` 更新/清除 LangSmith 追踪。

## Code 模式工作流

1. `--init` 向导 → 生成仓库根 `openwiki/` 文档
2. 每次运行维护 `AGENTS.md`/`CLAUDE.md` 的 `<!-- OPENWIKI:START -->` 块：**只重写该块**，保留你的内容
3. `openwiki/INSTRUCTIONS.md`：你的 wiki 指令（scope/priorities），生成时读取但**不覆写**
4. CI：GitHub Actions `openwiki code --update --print`；GitLab CI 自动建 MR；Bitbucket Pipeline 自定义调度
5. **no-op 免费**：快照 `openwiki/` 目录，无实际变更不写新元数据，调度 CI 不空转

## Personal 模式

- 连接器：`git-repo`/`hackernews`（免认证）、`x`/`notion`/`google`/`slack`（OAuth；Slack 需 `openwiki ngrok start` 隧道 + 应用注册，Gmail 需自建 OAuth 应用）、`web-search`（需 `TAVILY_API_KEY`）
- 同一连接器可多实例（`web-search-1`/`web-search-2`），原始数据落 `~/.openwiki/connectors/<name>/raw/`
- token 与配置存 `~/.openwiki/.env`（本地私有；配置文件只引用 env 变量名，不含明文密钥）
- macOS 支持 LaunchAgent 定时调度，日志落 `~/.openwiki/logs/`
- `.openwikiignore`（仓库根）：gitignore 语法；**读边界**——忽略路径永不读取/扫描/复现（但不保证不提及）

## 模型与调试

- 12 个 provider：OpenAI（API key 或 ChatGPT 登录走 Codex）、Anthropic、Gemini、Vertex（Model Garden/ADC）、Bedrock（IAM）、GitHub Copilot（`COPILOT_API_KEY` 需 OAuth token，PAT 被拒）、OpenRouter（可 `OPENWIKI_OPENROUTER_PROVIDER_ONLY` 上游 pinning）、NVIDIA NIM、Ollama 等 OpenAI 兼容端点
- base URL 族：`ANTHROPIC_BASE_URL`/`OPENAI_BASE_URL` 等；重试 `OPENWIKI_PROVIDER_RETRY_ATTEMPTS`（默认 3）
- LangSmith：code 模式配置直接在 `--init` 向导选；写入 `openwiki/.langsmith.json`（不含 key），key 取 `OPENWIKI_LANGSMITH_API_KEY`（多 workspace 用 `_2`/`_3` 后缀）
- 多语言：`--language <locale>`
- 遥测：PostHog 仅收集命令类型与成败；`OPENWIKI_TELEMETRY_DISABLED=1` 或 `DO_NOT_TRACK=1` 关闭；`--telemetry-file=<path>` 查看将上报内容

## 局限

文档质量取决于 LLM 能力；OAuth 连接器需应用注册；LaunchAgent 仅 macOS；可视化页面依赖公共 CDN（需联网）；wiki 面向 agent 优化，人类可读性一般。

## 相关

- [[openwiki]]（实体页：特性/版本表/架构）、[[okf]]（输出格式）、[[llm-wiki-ecosystem]]（生态定位）
- 更新机制：定时重跑 + PR，与本 wiki 的感知触发不同（见 [[openwiki]] 对比表）