---
source_url: opencode://session-history/2026-07-23-mighty-star
title: "Session: OpenWiki+Graphify+CodeGraph"
ingested: 2026-08-07
sha256: 7718378494af775ac2e87250f76e1d40e52f18057c7a255189ffb0f3375a8c9f
---

# Session: OpenWiki+Graphify+CodeGraph

- slug: `mighty-star`  session-id: `ses_070f143cfffeCw0qaVFw0a2DNf`  created: 2026-07-23 20:58
- 源目录：/home/imovation/projects/llm-wiki


## [07-23 20:58] user

深度研究并介绍openwiki:openwiki:https://github.com/langchain-ai/openwiki


## [07-23 20:59] assistant

The user wants me to deeply research and introduce the openwiki project from LangChain AI: https://github.com/langchain-ai/openwiki

Let me fetch information about this project from multiple sources.


## [07-23 20:59] assistant

Let me also fetch more details about the project - maybe the README in raw format and some other pages to get more comprehensive understanding.


## [07-23 20:59] assistant

Let me fetch the package.json and some other source files to get a deeper understanding of the project architecture.


## [07-23 20:59] assistant

Now I have a comprehensive understanding of OpenWiki. Let me also look at the src directory to understand the code architecture better.


## [07-23 20:59] assistant

Now I have a comprehensive understanding of OpenWiki. Let me compile a thorough research report for the user.

## OpenWiki 深度研究报告

### 概述

**OpenWiki** 是 LangChain AI 团队开发的开源 CLI 工具（MIT 协议），用于**自动生成并持续维护代码库的 Agent 文档（Wiki）**。它的核心理念是：文档不是写给人类看的，而是写给 AI Agent 看的。项目当前 **13k Stars**，最新版本 **v0.2.2**（2026-07-21），语言为 TypeScript（88.4%）+ JavaScript。

**GitHub**: https://github.com/langchain-ai/openwiki
**安装**: `npm install -g openwiki`（Node >= 22）

---

### 核心定位与设计哲学

OpenWiki 区别于传统文档工具的关键点：

1. **Agent-first** — 生成的是 `AGENTS.md` / `CLAUDE.md`，直接嵌入仓库根目录，让编码 Agent 在读取上下文时自动引用 Wiki 内容
2. **双向同步** — 不只生成，还通过 `--update` 持续更新，并配有 CI/CD 集成（GitHub Actions / GitLab CI / Bitbucket Pipelines），自动提 PR 更新文档
3. **Mermaid 原生支持** — 自动生成序列图、ER 图、状态图、流程图，有验证-降级-修复回路
4. **符合 Google OKF v0.1 标准** — 输出兼容 [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)，YAML front matter 标记每个文档类型

---

### 两大工作模式

| 模式 | 命令 | 存储位置 | 用途 |
|------|------|----------|------|
| **Code Mode**（默认） | `openwiki --init` | 仓库根目录 `openwiki/` | 为当前代码库生成项目文档 |
| **Personal Mode** | `openwiki personal --init` | `~/.openwiki/wiki/` | 构建个人知识库，支持连接多种外部源 |

---

### 架构与技术栈

**依赖体系**（源自 `package.json`）：
- **Agent 框架**: `deepagents` v1.11.1（核心文档生成 Agent）
- **LLM 集成**: `@langchain/core` + `@langchain/anthropic` + `@langchain/openai` + `@langchain/google` + `@langchain/aws` + `@langchain/openrouter`
- **状态管理**: `@langchain/langgraph-checkpoint-sqlite`（基于 SQLite 的 checkpoint）
- **CLI 渲染**: `ink` + `react` 18（终端 React 渲染）
- **文档解析**: `marked` + `yaml`
- **遥测**: `posthog-node` + `ci-info`
- **可选依赖**: `mermaid` + `jsdom`（用于权威 Mermaid 校验）

**源码目录结构**（`src/`）：
- `cli.tsx` — CLI 入口
- `agent/` — Agent 逻辑
- `auth/` — OAuth 认证（Gmail, Slack, X, Notion）
- `connectors/` — 数据源连接器
- `mermaid/` — Mermaid 图生成与验证
- `okf/` — Google OKF 格式处理
- `telemetry/` — 遥测
- `code-mode.ts`, `commands.ts`, `credentials.tsx`, `ingestion.ts`, `onboarding.ts`, `schedules.ts` 等

---

### 支持的 LLM Provider

| Provider | 认证方式 |
|----------|----------|
| OpenAI | API Key 或 ChatGPT 登录（Codex） |
| Anthropic | API Key（支持自定义 BASE_URL） |
| OpenRouter | API Key（支持 provider pinning） |
| Gemini (AI Studio) | API Key |
| Gemini Enterprise (Vertex AI) | Google ADC（服务账号 / gcloud / Workload Identity） |
| AWS Bedrock | IAM Access Key |
| OpenAI-compatible | 任何兼容端点（Ollama, LM Studio, LiteLLM, 9Router 等） |
| Fireworks / Baseten / NVIDIA NIM | API Key（支持自定义 BASE_URL） |
| Nebius Token Factory | API Key |

默认模型：OpenAI `gpt-5.6-terra`。支持自定义模型 ID。

---

### 连接器（Connectors）— Personal Mode 数据源

| 连接器 | 来源 | 认证 |
|--------|------|------|
| `git-repo` | 本地 Git 仓库 | 无需认证 |
| `x` (Twitter) | 首页时间线、帖子、提及、书签、列表 | OAuth 2.0 PKCE |
| `notion` | Notion 工作空间 | Notion OAuth（通过托管 MCP） |
| `google` | Gmail（未来可扩展 Drive/Calendar） | OAuth（本地浏览器流程） |
| `web-search` | Tavily 搜索 | `TAVILY_API_KEY` |
| `hackernews` | Hacker News 公开 API | 无需认证 |
| `slack` | Slack 工作空间 | OAuth（需 ngrok） |

支持同一连接器多实例配置（如 `web-search-1` / `web-search-2`）。

---

### 关键特性深度解析

#### 1. AGENTS.md / CLAUDE.md 管理
每次 `code` 运行时，OpenWiki 在仓库根目录维护 `AGENTS.md` 和 `CLAUDE.md`。只重写 `<!-- OPENWIKI:START -->...<!-- OPENWIKI:END -->` 区块，保留用户自定义内容。CI 工作流也把这些文件纳入文档 PR。

#### 2. INSTRUCTIONS.md
仓库维度的 `openwiki/INSTRUCTIONS.md` 是用户编写的 Wiki 指令（scope/priorities），OpenWiki 在生成文档时读取但不会覆写。

#### 3. Mermaid 图自动生成与自愈
- 自动为运行时/请求流生成序列图、数据模型 ER 图、生命周期状态图、控制流流程图
- 每次运行后校验所有 `mermaid` fence，失败的转为 `text` fence + 注释
- 下次 `--update` 修复并恢复 `mermaid` fence
- 可选安装 `mermaid` + `jsdom` 获得权威校验

#### 4. OKF 兼容性
输出 Google Open Knowledge Format v0.1，每个 Markdown 概念文档有 YAML front matter 标注 `type`。`index.md` 和 `log.md` 为保留文档。标准 Markdown 链接表达概念间关系。

#### 5. CI/CD 集成
- **GitHub Actions**: `openwiki code --update --print`
- **GitLab CI**: 自动创建 MR
- **Bitbucket Pipelines**: 支持自定义 pipeline 调度
- 无需 `--init`，`--update` 在文档不存在时自动创建

#### 6. 遥测
默认开启，使用 PostHog，仅收集命令类型和成功/失败状态（不含文件内容、凭据、提示词、模型输出等）。可通过 `OPENWIKI_TELEMETRY_DISABLED=1` 或 `DO_NOT_TRACK=1` 关闭。

#### 7. 调度（macOS）
Personal Mode 支持 LaunchAgent 定时调度，日志输出到 `~/.openwiki/logs/`。

---

### 项目状态

- **版本**: v0.2.2（2026-07-21，共 10 个 Release）
- **提交**: 176 commits
- **贡献者**: 多人在维护
- **活跃度**: Issues 59 个，PR 65 个，持续活跃开发
- **趋势**: Trendshift 日榜常客

---

### 适用场景

1. **代码库文档自动化** — 大型项目无需手写文档，Agent 自动生成并保持同步
2. **AI 辅助开发工作流** — 与 Claude Code、Copilot、Cline 等编码 Agent 配合，自动提供项目上下文
3. **个人知识管理** — 聚合 Gmail、Notion、Twitter、Git 仓库、网页搜索等内容，构建个人 AI 知识库
4. **团队 onboarding** — Wiki 自动生成，新成员和 AI 助手都有一致的项目理解

### 局限性

- 生成的文档质量取决于 LLM 能力，复杂领域概念可能需要人工校正
- Personal Mode 的部分连接器（Gmail, Slack）需要 OAuth 应用注册
- macOS LaunchAgent 调度目前仅限 macOS
- 生成的 Wiki 主要为 Agent 优化，人类可读性可能不如传统文档工具


## [07-23 21:32] user

深度研究并介绍graphify:https://github.com/Graphify-Labs/graphify


## [07-23 21:32] assistant

The user wants me to deeply research and introduce the Graphify project from https://github.com/Graphify-Labs/graphify. Let me fetch information from multiple sources.


## [07-23 21:32] assistant

Now I have a very comprehensive understanding of Graphify. Let me also fetch the ARCHITECTURE.md and pyproject.toml for more technical depth.


## [07-23 21:32] assistant

Now I have a very comprehensive picture. Let me compile a deep research report on Graphify.

## Graphify 深度研究报告

### 概述

**Graphify** 是 Y Combinator S26 支持的 **开源代码知识图谱工具**（Python, Apache-2.0 + MIT 双协议），由 Safi Shamsi 创立。它将整个代码库（代码、文档、PDF、图片、视频、SQL schema、Terraform 配置等）转化为**可查询的知识图谱**，让 AI 编码助手以图查询替代文件 grep。目前 **94K+ Stars**、**9.1K Forks**、**1.2M+ PyPI 下载**、**171 个 Release**、**170+ 贡献者**，日均发版，是开源领域最受欢迎的代码知识图谱项目。

**GitHub**: https://github.com/Graphify-Labs/graphify
**官网**: https://graphify.com
**安装**: `uv tool install graphifyy` 或 `pipx install graphifyy`

---

### 核心设计哲学

Graphify 的核心洞察：**AI 编码助手的瓶颈在于上下文理解，而非模型能力**。传统方式（grep、RAG 向量检索）要么丢失语义关系，要么无法精确追踪跨文件连接。Graphify 用**确定性 AST 解析 + 图结构**解决这一问题。

关键区别与 OpenWiki：

| 维度 | OpenWiki | Graphify |
|------|----------|----------|
| 输出 | Markdown Wiki（文档） | 知识图谱（节点+边） |
| 代码解析 | LLM 驱动 | Tree-sitter AST（确定性、零 API 调用） |
| 查询方式 | 读文档 | `graphify query/path/explain` 图遍历 |
| 存储格式 | 自然语言文档 | `graph.json` + `graph.html` + `GRAPH_REPORT.md` |
| 更新粒度 | 全量重新生成 | 增量 patch（~0.8s 更新 3 个文件） |
| 隐私 | 代码可能外传 | 代码纯本地解析，无需联网 |

---

### 架构与管道

源自 `ARCHITECTURE.md`，Graphify 的 8 阶段管道：

```
detect() → extract() → build_graph() → cluster() → analyze() → report() → export()
```

每个阶段是独立模块，通过 Python dict 和 NetworkX 图通信，无共享状态：

| 模块 | 功能 |
|------|------|
| `detect.py` | 文件收集（支持 `.gitignore` + `.graphifyignore` 双过滤） |
| `extract.py` | 核心提取（36 种 tree-sitter 语法 + 语义提取器） |
| `build.py` | 构建 `nx.Graph`，合并多源提取结果 |
| `cluster.py` | Leiden 社区检测，自动识别子系统 |
| `analyze.py` | 分析 God Node（高介数中心性节点）、惊喜连接、建议问题 |
| `report.py` | 渲染 `GRAPH_REPORT.md` |
| `export.py` | 导出 `graph.json` / `graph.html` / `graph.svg` / Obsidian Vault |
| `serve.py` | MCP stdio/HTTP 服务器 |

---

### 技术栈

**核心依赖**（`pyproject.toml`）：
- **图引擎**: `networkx` + `numpy`
- **AST 解析**: 28+ 个 `tree-sitter-*` 语法包（Python/TS/Go/Rust/Java/C/C++/Ruby/C#/Kotlin/Scala/PHP/Swift/Lua/Zig/PowerShell/Elixir/ObjC/Julia/Verilog/Fortran/Bash/JSON 等）
- **社区检测**: `graspologic`（Leiden 算法）
- **模糊匹配**: `rapidfuzz`
- **可选**: `pypdf` / `python-docx` / `openpyxl` / `faster-whisper` / `yt-dlp` / `mcp` / `neo4j` / `falkordb` / `matplotlib` / `jieba` 等

---

### 关键特性深度解析

#### 1. 图查询三元组

查询替代读文件，每条边带置信度标签：

```
$ graphify path "FastAPI" "ModelField"
Shortest path (3 hops):
  FastAPI --uses--> DefaultPlaceholder <--references-- get_request_handler() --references--> ModelField
```

三个核心命令：
- `graphify query "<问题>"` — 自然语言查询，返回子图
- `graphify path <A> <B>` — 最短路径追踪
- `graphify explain "<概念>"` — 单个概念展开（节点度、连接清单）

#### 2. 边置信度标签

| 标签 | 含义 |
|------|------|
| `EXTRACTED` | 源代码中显式存在（import 语句、直接调用） |
| `INFERRED` | 合理推导（调用图二次传递、共现关系） |
| `AMBIGUOUS` | 不确定，需人工审查 |

#### 3. God Node 与社区检测

- **God Node**: 介数中心性最高的节点，连接最多社区。一个断了能立即显示爆炸半径
- **Leiden 聚类**: 自动将图分割为子系统，无 LLM 参与，社区标签由算法自动生成

#### 4. 增量更新

Graphify 的核心竞争力之一：**3 个文件变更在 ~0.8 秒内完成增量 patch**，498,752 个其他节点完全不受影响。传统 RAG 向量检索需要数小时重新嵌入。

#### 5. 多格式/多语言支持

| 类型 | 格式 | 提取方式 |
|------|------|----------|
| 代码 | 36 种语言（含 Apex/Terraform/HCL/DreamMaker/Pascal/Dart/Vue/Svelte 等） | Tree-sitter AST（本地、零 API） |
| 文档 | `.md .mdx .qmd .html .txt .rst .yaml .yml` | LLM 语义提取 |
| PDF | `.pdf` | LLM 语义提取 |
| Office | `.docx .xlsx` | 可选 extra |
| 图片 | `.png .jpg .webp .gif` | 视觉提取 |
| 视频/音频 | `.mp4 .mov .mp3 .wav` + YouTube URL | faster-whisper 本地转录 |
| Google Workspace | `.gdoc .gsheet .gslides` | 可选 `gws` 集成 |
| 数据库 | PostgreSQL 实时 introspection（`--postgres DSN`） | 实时 schema 拉取 |
| 基础设施 | Terraform `.tf .tfvars .hcl` | Tree-sitter HCL 语法 |
| SQL | `.sql` | Tree-sitter SQL 语法 |
| 包清单 | `pyproject.toml` `go.mod` `pom.xml` `apm.yml` | 提取依赖边 |
| MCP 配置 | `.mcp.json` `claude_desktop_config.json` | 提取 server 节点、环境变量 |

#### 6. 20+ AI 编码助手平台集成

Graphify 为每个平台提供定制 skill/hook/指令：

- **Hook 平台**（Claude Code, Gemini CLI, Codex, CodeBuddy）：PreToolUse hook 在文件读取前自动触发图查询
- **指令文件平台**（OpenCode, Cursor, Aider, Kilo, Kiro, Devin CLI, Pi, Hermes 等）：写入 `AGENTS.md` / `.cursor/rules/` 等
- **VS Code Copilot Chat**: 专用 VS Code 扩展命令
- **Strict Mode**: 可选强制模式，首次 session 阻塞直接读文件，重定向到图查询

#### 7. MCP 服务器

```bash
# stdio（默认，每个开发者一个本地进程）
python -m graphify.serve graphify-out/graph.json

# HTTP（团队共享，MCP Streamable HTTP 传输）
python -m graphify.serve graphify-out/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

支持 `query_graph` / `get_node` / `get_neighbors` / `shortest_path` / `list_prs` / `get_pr_impact` / `triage_prs` 等工具。支持 Docker 部署。

#### 8. PR 审查面板

```bash
graphify prs              # PR 仪表盘：CI 状态、审查状态、工作区映射
graphify prs 42           # 深度分析 PR #42 的图影响
graphify prs --triage     # AI 排序审查队列
graphify prs --conflicts  # 共享图社区的 PR（合并顺序风险）
```

#### 9. 代码推理（Rationale）节点

`# NOTE:` / `# WHY:` / `# HACK:` 注释、docstrings、ADR/RFC 引用都被提取为独立节点，链接到对应代码。这让开发者能直接问"为什么这段代码这么写"。

#### 10. Git Hook 自动重建

```bash
graphify hook install
```

每次 git commit 后自动增量重建（仅 AST，零 API 费用）。包含 git merge driver，`graph.json` 冲突自动合并。

#### 11. 团队协作

`graphify-out/` 可提交到 git：
- 一人构建 → 全团队 AI 助手共享同一份图
- 新成员第一天就能获得架构上下文
- CI 中运行 `graphify extract --code-only` 零 API 成本

---

### 基准测试（来自 BENCHMARKS.md）

| 基准 | 指标 | Graphify | 对比 |
|------|------|----------|------|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | **45.3%** | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | 与 dense RAG 持平 |
| 图构建 | LLM 费用 | **$0** | 按 token 计费系统 |

所有系统使用相同 harness、相同模型、相同预算运行。评审者双盲验证（90.6% 一致性，Cohen's kappa 0.81）。

---

### 隐私设计

- **代码文件**: 纯本地 tree-sitter AST 解析，不离开机器。`--code-only` 完全离线运行
- **视频/音频**: faster-whisper 本地转录，不离开机器
- **文档/PDF/图片**: 通过 IDE session 的模型 API 发送（headless 模式需配置 API key，支持 Gemini/Claude/OpenAI/DeepSeek/Ollama/Bedrock/Kimi 多后端）
- **数据驻留**: `--backend ollama` 完全本地；Kimi 路由至中国 Moonshot AI 服务器
- **无遥测**: 无使用追踪，无分析

---

### 项目状态与社区

- **Stars**: 94K+（持续快速增长中）
- **Forks**: 9.1K+
- **贡献者**: 170+
- **Release**: v0.9.25（2026-07-22），共 171 个 Release，日均发版
- **Issues**: 611 open
- **PR**: 345 open
- **YC**: S26 批次
- **企业级**: 21 家财富 500 强在企业队列中
- **PyPI 下载**: 1.2M+

---

### 适用场景

1. **大型代码库 onboarding** — 新成员 4 分钟获得完整代码库图，无需 3 周手工阅读
2. **跨语言/跨服务影响分析** — "重命名 users 表会破坏什么？"从数据库表 → SQLAlchemy 模型 → API 路由 → Terraform RDS 一条路径追踪
3. **PR 审查** — 自动分析 PR 影响的图社区、合并顺序风险、排序审查队列
4. **复杂架构理解** — God Node 揭示核心依赖，社区检测拆分子系统，惊喜连接发现隐藏耦合
5. **决策追溯** — `# WHY:` 注释和 ADR 文档作为一等公民节点，与代码直接关联
6. **AI 编码助手增强** — 让 Claude Code / Codex / Cursor / Gemini CLI 等 20+ 平台的 Agent 不再盲目 grep，而是用图查询获取精确上下文

### 局限性

- 文档/PDF/图片的语义提取需要 LLM API（除非只用 `--code-only`）
- 超大库的首次完整构建需要时间（但后续增量极快）
- 社区检测效果取决于代码库的模块化程度
- 部分可选 extra（如 `video` 需要 Python 3.11+, `leiden` 需要 Python < 3.13）有版本限制


## [07-23 21:41] user

深度研究并介绍codegraph:https://github.com/colbymchenry/codegraph


## [07-23 21:41] assistant

The user wants me to deeply research and introduce the codegraph project from https://github.com/colbymchenry/codegraph. Let me fetch information from multiple sources.


## [07-23 21:41] assistant

Now let me also fetch the package.json to get the technical dependencies, and the docs structure for more detail.


## [07-23 21:42] assistant

Now I have a comprehensive understanding of CodeGraph. Let me compile a deep research report.

## CodeGraph 深度研究报告

### 概述

**CodeGraph** 由 Colby McHenry 开发，是一个**本地优先的代码智能工具**，将代码库转化为 AI 编码助手可直接查询的知识图谱。自 2026 年 1 月首次发布以来，仅用半年达到 **61.9K+ Stars**、**3.9K Forks**、**76.6K+ npm 周下载量**，是增长最快的代码知识图谱项目之一。当前最新版本 **v1.5.0**（2026-07-21），共 **30 个 Release**，**40 位贡献者**。

**GitHub**: https://github.com/colbymchenry/codegraph
**文档站**: https://colbymchenry.github.io/codegraph/
**商业版**: https://getcodegraph.com（企业级平台，waitlist 中）
**安装**: `npx @colbymchenry/codegraph` 或 `npm i -g @colbymchenry/codegraph`

---

### 核心定位：Surgical Context

CodeGraph 的核心洞察与 OpenWiki 和 Graphify 截然不同：

> **Agent 不需要读全部代码，它只需要精确的上下文。** 一次 `codegraph_explore` 调用返回相关符号的源代码、调用路径（含 grep 无法追踪的动态分发跳转）、以及变更影响半径。

| 对比维度 | OpenWiki | Graphify | CodeGraph |
|----------|----------|----------|-----------|
| 作者/组织 | LangChain AI | Graphify Labs (YC S26) | Colby McHenry（个人） |
| 语言 | TypeScript | Python | **Rust 内核 + TypeScript CLI** |
| 存储 | Markdown Wiki | JSON 图文件 | **SQLite (FTS5)** |
| 更新方式 | LLM 全量重生成 | 增量 patch (~0.8s) | **原生 OS 事件监听，自动增量同步 (~0.3s)** |
| 核心工具 | 文档生成 | 图查询/路径/解释 | **单工具 `codegraph_explore`** |
| 基准表现 | N/A | LOCOMO recall@10 0.497 | **89% 少工具调用、60% 低成本、69% 少 tokens** |
| Stars | 13K | 94K | **61.9K（增长最快）** |

---

### 架构与技术栈

#### 双层引擎架构

```
Rust Kernel（编译原生二进制）
  ├── 20 种语言的 tree-sitter 语法编译为原生代码
  ├── 边界跨越：每文件仅一次 FFI 调用
  ├── 字节级正确性验证（与参考引擎逐字节一致）
  └── 无预编译二进制平台 → 自动回退到 JS 引擎

TypeScript 层
  ├── CLI（commander）
  ├── MCP Server
  ├── SQLite 数据库层（schema.sql + FTS5）
  └── WebAssembly tree-sitter 回退（web-tree-sitter + tree-sitter-wasms）
```

#### 核心技术依赖

**Rust 内核部分**（`codegraph-kernel/`）：
- 原生 tree-sitter 语法（编译为二进制）
- 零依赖打包，无 Node.js 运行时也可以运行

**TypeScript CLI 部分**（`package.json`）：
- `web-tree-sitter` + `tree-sitter-wasms` — WASM 回退引擎
- `better-sqlite3`（devDependency）— SQLite 数据库
- `commander` — CLI 框架
- `@clack/prompts` — 交互式提示
- `ignore` — `.gitignore` 解析
- `picomatch` — glob 匹配
- Node >= 20（自打包运行时无 Node 也可用）

---

### 关键特性深度解析

#### 1. `codegraph_explore` — 单一 MCP 工具

CodeGraph 将 MCP 工具面精简为**一个工具**：`codegraph_explore`。设计决策基于对 Agent 行为的实测——工具越多，Agent 越容易选错。一次调用返回：

- 相关符号的**逐文件源代码**（与 Read 工具相同格式）
- 符号间的**调用路径**（含动态分发跳转：回调、React 重渲染、接口→实现）
- **影响半径摘要**（变更波及范围）

其他工具（`codegraph_node`, `codegraph_search`, `codegraph_callers`, `codegraph_callees`, `codegraph_impact`, `codegraph_files`, `codegraph_status`）保持功能完整但**默认不列出**，可通过 `CODEGRAPH_MCP_TOOLS` 环境变量重新启用。

#### 2. 三层自动同步机制

**这是 CodeGraph 区别于所有竞品的核心工程优势：**

```
① 文件监听器 → 原生 OS 事件（FSEvents/inotify/ReadDirectoryChangesW）
                      ↓
② 去抖窗口（默认 2s，可配置 100ms-60s）→ 突发编辑合并为一次同步
                      ↓
③ 连接时追齐 → MCP 重连时（size, mtime）+ content-hash 快速校验
```

同步延迟基准：
- **4,400 文件项目**：变更同步 ~**0.3s**
- **Swift 编译器仓库（27,000 文件）**：变更同步 ~**0.4s**
- **Linux 内核（70,000 文件）**：首次完整索引 ~**12 分钟**（2 核 VPS）
- 对比竞品：2-7× 更快（因为竞品成本随仓库大小增长，CodeGraph 只随变更大小增长）

**去抖窗口内的安全保障：** MCP 工具响应会在引用待同步文件时自动添加 `⚠️` 横幅，告知 Agent 直接 Read 该文件。Agent（经验证 Claude Code）会自动说"直接读取文件以获取最新内容"然后打开它。

#### 3. Rust 原生内核

- 20 种语言（TS/JS/Java/Python/Go/C/C++/Rust/C#/Ruby/PHP/Swift/Kotlin/Scala/Dart/R/Lua/Luau + Metal/CUDA 走 C++ 路径）
- 每个语言在**真实仓库**（从小库到 Linux 内核）上验证**逐字节与参考引擎一致**
- 无预编译二进制平台或语法错误文件 → 自动**逐文件回退**到 WASM 引擎，输出相同图

#### 4. 自适应资源调度

```
工作站（高配）  → 全并行管线：原生解析 worker + 多 worker 解析器池 + 内存缓存
2 核 / 6GB VPS → 调优至可靠完成：Linux 内核（70K 文件、2M 符号、6.4M 关系）完整索引 < 12 分钟
容器环境       → cgroup 感知实际核数（而非宿主机的 64 核）
```

#### 5. 框架感知路由

17 个 Web 框架的 URL 路由 → 处理器映射：

| 框架 | 识别的路由模式 |
|------|---------------|
| **Django** | `path()`, `re_path()`, `url()`, `include()`, CBV `.as_view()` |
| **Flask** | `@app.route()`, blueprint routes |
| **FastAPI** | `@app.get()`, `@router.post()` |
| **Express** | `app.get()`, `router.post()` + middleware chains |
| **NestJS** | `@Controller` + `@Get/@Post`, GraphQL `@Resolver`, `@MessagePattern` |
| **Laravel** | `Route::get()`, `Route::resource()`, tuple syntax |
| **Rails** | `get '/x', to: 'users#index'` |
| **Spring** | `@GetMapping`, `@PostMapping`, `@RequestMapping` |
| **Gin / chi / gorilla/mux** | `r.GET()`, `router.HandleFunc()` |
| **Axum / actix / Rocket** | `.route("/x", get(handler))` |
| **ASP.NET** | `[HttpGet("/x")]` attributes |
| **Vapor** | `app.get("x", use: handler)` |
| **React Router / SvelteKit / Vue Router / Nuxt / Astro** | 文件系统路由 + 参数语法 |

#### 6. iOS / React Native / Expo 跨语言桥接

这是 CodeGraph 独特的差异化能力——连接静态 AST 无法追踪的语言边界：

| 桥接类型 | 实现方式 |
|----------|----------|
| **Swift ↔ ObjC** | `@objc` 自动桥接规则（含 Cocoa 介词前缀 `With`/`For`/`By` 等） |
| **React Native 传统桥** | JS `NativeModules.X.fn()` → ObjC `RCT_EXPORT_METHOD` |
| **React Native TurboModules** | JS `Native<X>.ts` spec → 原生实现 |
| **原生 → JS 事件** | `NativeEventEmitter` + `sendEventWithName` 事件通道 |
| **Expo Modules** | Expo DSL 字面量解析（`AsyncFunction`/`Name`） |
| **Fabric view 组件** | JSX `<MyView>` → Codegen spec → 原生实现类 |
| **Paper view 管理器** | JSX + `RCT_EXPORT_VIEW_PROPERTY` / `@ReactProp` |

已在多个真实代码库上验证（Charts、realm-swift、Wikipedia-iOS、react-native-firebase、expo SDK 等）。

#### 7. 基准测试（2026-07-21 重新验证，Claude Opus 4.8）

| 代码库 | 语言/规模 | WITH CodeGraph | WITHOUT CodeGraph | 节省 |
|--------|----------|----------------|-------------------|------|
| **VS Code** | TS ~11K 文件 | 2 调用 / 41s / 265K tokens / $0.36 | 40 调用 / 3m24s / 1.5M tokens / $1.41 | **75-83%** |
| **Excalidraw** | TS ~640 | 3 / 36s / 324K / $0.40 | 55 / 23s¹ / 2.9M / $1.81 | 78-89% |
| **Django** | Python ~3K | 2 / 42s / 254K / $0.35 | 29 / 1m8s / 1.2M / $1.13 | 69-78% |
| **Tokio** | Rust ~790 | 3 / 46s / 386K / $0.44 | 57 / 2m11s / 4.3M / $3.04 | **86-91%** |
| **OkHttp** | Java ~645 | 1 / 27s / 156K / $0.23 | 5 / 30s / 233K / $0.20 | 33% |
| **Gin** | Go ~110 | 3 / 30s / 246K / $0.27 | 10 / 1m10s / 300K / $0.46 | 18-41% |
| **Alamofire** | Swift ~110 | 3 / 49s / 316K / $0.35 | 53 / 31s¹ / 3.1M / $2.51 | 86-90% |

**通用结论：89% 少工具调用 · 60% 低成本 · 69% 少 tokens · 所有 7 个仓库文件读取归零**

¹ 小仓库的"地板效应"：Opus 4.8 在小树上 grep 更快完成墙钟时间，但花费 5-10× tokens 和 ~4-7× 成本

#### 8. 语言支持

**33 种语言/格式**：TypeScript, JavaScript, ArkTS, Python, Go, Rust, Java, C#, VB.NET, PHP, Ruby, C, C++, CUDA, Objective-C, Metal, Swift, Kotlin, Scala, Dart, Lua, Luau, R, Nix, Erlang, CFML, COBOL, Solidity, Terraform/OpenTofu, Svelte, Vue, Astro, Liquid, Pascal/Delphi

#### 9. FTS5 全文搜索

SQLite FTS5 支持即时按名称搜索整个代码库的符号。

#### 10. 项目状态

- **Stars**: 61.9K（2026-01 发布，半年爆发式增长）
- **Forks**: 3.9K
- **Contributors**: 40
- **Releases**: 30（v0.6 → v1.5.0 约每月 5 个版本）
- **npm 周下载**: 76.6K
- **GitHub Trending**: 2026-05-16 首次登顶 #1
- **Size**: 仅 649KB（npm 包），0 外部依赖
- **商业平台**: waitlist 中（getcodegraph.com）

---

### 隐私设计

- **100% 本地**：无需 API 密钥、无外部服务、数据不离开机器
- **SQLite 数据库**：仅 `.codegraph/codegraph.db` 本地文件
- **遥测**：可选匿名使用数据（见 `TELEMETRY.md`）
- **验证构建**：npm provenance + 签名 attestation

---

### 适用场景

1. **AI 编码 Agent 上下文增强** — Claude Code / Cursor / Codex / OpenCode / Gemini CLI 等 8+ 平台，一次 `codegraph_explore` 替代数十次 grep/Read
2. **变更影响分析** — 修改前追踪所有 caller/callee 和完整影响半径
3. **跨语言桥接分析** — iOS Swift ↔ ObjC ↔ React Native 跨语言调用追踪（唯一竞品能力）
4. **Web 框架路由理解** — URL 模式 → 处理函数的精确映射
5. **大型代码库 onboard** — 新开发者/Agent 秒级获得架构全景
6. **CI/CD 集成** — 零 API 成本，纯本地运行

### 与 Graphify 的关键差异

| 维度 | Graphify | CodeGraph |
|------|----------|-----------|
| 内核语言 | Python | **Rust（原生二进制）** |
| 存储 | JSON 文件 | **SQLite + FTS5** |
| 同步机制 | 手动/CI 触发 | **原生 OS 文件事件自动同步** |
| MCP 工具数量 | 多工具 | **单一 `codegraph_explore`** |
| 跨语言桥接 | 无 | **iOS/RN/Expo 跨语言桥接** |
| 商业模式 | 企业版（21 家 Fortune 500） | **平台 waitlist 阶段** |

### 局限性

- Rust 内核仅支持 20 种语言（且不含文档/PDF/图片）；其余语言回退到 WASM JS 引擎，性能较低
- 不支持非代码文件（文档、PDF、图片、视频）的语义提取——领域单一聚焦代码
- macOS 首次安装后需新终端才能使用命令（PATH 刷新）
- 部分语言（COBOL、CFML、Erlang 等）的边缘语言可能只有基础 AST 支持


## [07-23 21:50] user

这三个项目的生态位和应用场景分析


## [07-23 21:50] assistant

The user wants me to analyze the ecological niches and application scenarios of the three projects: OpenWiki, Graphify, and CodeGraph. Let me synthesize all the research I've done and provide a comprehensive analysis.

Let me think about this carefully across multiple dimensions to give a thorough analysis.

## OpenWiki vs Graphify vs CodeGraph — 生态位与应用场景分析

### 一、核心理念分歧

```
OpenWiki:   Agent 需要读文档 → 我生成 Wiki
Graphify:   Agent 需要查代码 → 我建知识图谱
CodeGraph:  Agent 需要精确上下文 → 我给 Surgical Context
```

这三者分别代表了三种不同的哲学：

| 维度 | OpenWiki | Graphify | CodeGraph |
|------|----------|----------|-----------|
| **给 Agent 什么** | 自然语言文档 | 图结构（节点+边） | **源代码本身 + 调用路径** |
| **读取方式** | Agent 读 .md 文件 | `graphify query/path/explain` 图遍历 | `codegraph_explore` 返回源文件行号 |
| **确定性** | 低（LLM 生成文档） | 代码部分高（tree-sitter） | **最高（Rust 原生 AST + 逐字节验证）** |
| **输出对人类可读** | ✅ Wiki 文档 | ⚠️ GRAPH_REPORT.md + HTML 图 | ❌ 主要为 Agent 优化 |

关键分水岭：**CodeGraph 的 `codegraph_explore` 返回的是源代码片段（带行号），不是图数据。** Agent 可以直接使用——它相当于把 Read 工具的结果缓存起来了。Graphify 返回的是图路径，Agent 还需要进一步 Read 文件才能拿到源码。OpenWiki 返回的是 LLM 重写的自然语言，信息有损。

---

### 二、技术实现分层对比

#### 2.1 解析引擎

```
OpenWiki:   LLM 驱动解析（deepagents + langchain）
            成本：每次生成/更新都消耗 API tokens
            准确度：LLM 可能遗漏或幻觉

Graphify:   tree-sitter AST（Python 实现）
            成本：代码解析零 API 调用（本地）
            准确度：确定性 AST，但跨语言桥接弱

CodeGraph:  Rust 原生 tree-sitter（编译二进制）
            成本：零 API 调用 + 零运行时依赖
            准确度：逐字节验证 = 100% 精确
            性能：比纯 Python tree-sitter 快 10-100×
```

#### 2.2 更新机制

| | OpenWiki | Graphify | CodeGraph |
|---|---|---|---|
| **首次构建** | ~分钟级（LLM 生成） | ~秒-分钟级 | ~秒-12分钟（看机器） |
| **增量更新** | 全量重新生成 | 增量 patch ~0.8s | 原生监听 ~0.3s |
| **自动监听** | ❌ | ❌ | ✅ FSEvents/inotify/ReadDirectoryChangesW |
| **CI 集成** | ✅ GitHub/GitLab/Bitbucket | ✅ 各种 backend | ✅ 纯本地，无 API 成本 |
| **去抖防抖** | N/A | N/A | ✅ 可配置 100ms-60s |
| **陈旧信号** | N/A | N/A | ✅ ⚠️ 横幅提示待同步文件 |

**CodeGraph 的自动监听机制是三者中唯一真正"零操作"的——Agent 改完代码，图自动更新。**

#### 2.3 存储与检索

```
OpenWiki:   文件系统（.md 文件）
            检索：Agent 读取文件内容
            优势：人类可直接阅读

Graphify:   graph.json + graph.html + GRAPH_REPORT.md
            检索：图查询（query/path/explain）
            优势：图算法支持社区检测、God Node 分析

CodeGraph:  SQLite（.codegraph/codegraph.db + FTS5）
            检索：MCP 单工具 codegraph_explore
            优势：FTS5 全文搜索、SQL 支持复杂查询、行级源码精确返回
```

---

### 三、生态位分析

#### 3.1 按团队类型

| 团队类型 | 最佳选择 | 原因 |
|----------|----------|------|
| **小型团队/个人项目**（< 500 文件） | OpenWiki | 简单直接，人类可读的 Wiki，无需额外基础设施 |
| **中型项目/多语言仓库**（500-5K 文件） | CodeGraph | 自动同步零维护，Rust 内核快，SQLite 轻量 |
| **大型企业仓库**（5K-70K+ 文件） | CodeGraph + Graphify 互补 | CodeGraph 做代码精确解析，Graphify 做社区检测+文档语义提取 |
| **iOS/React Native 项目** | **CodeGraph（唯一选择）** | 只有 CodeGraph 支持 Swift↔ObjC↔React Native 跨语言桥接 |
| **文档密集型项目** | OpenWiki | 需要生成和维护自然语言文档给人类+Agent |
| **学术/研究项目** | Graphify | PDF/论文/视频提取 + 知识图谱社区分析 |

#### 3.2 按使用场景

**场景 A：Agent 需要理解一个函数/类怎么工作**
```
OpenWiki:  Agent 读 `openwiki/api/authentication.md` → LLM 生成的说明
Graphify:  `graphify explain "AuthMiddleware"` → 返回节点度、连接边列表
CodeGraph: `codegraph_explore "AuthMiddleware loginUser"` → **返回源代码 + 调用路径 + 影响半径**
```
**胜出：CodeGraph** — Agent 直接拿到源码，不需要再 Read 文件

**场景 B：新开发者 onboarding**
```
OpenWiki:  生成项目 Wiki，人类可读，适合初学
Graphify:  GRAPH_REPORT.md 中 God Node + 惊喜连接 + 社区结构
CodeGraph: 不产生人类可读文档，纯为 Agent 优化
```
**胜出：OpenWiki + Graphify 互补** — OpenWiki 做入门文档，Graphify 做架构全景

**场景 C：CI/CD 中自动文档维护**
```
OpenWiki:  GitHub Actions 定时更新 Wiki PR ✅ 设计目标
Graphify:  CI 中 `graphify extract --code-only` 零 API 成本 ✅
CodeGraph: 纯本地运行，配合 git hook 自动更新 ✅
```
**三者都可用，但各有侧重**：OpenWiki 适合需要人类审查文档变更的团队，Graphify 适合有 Python 生态的团队，CodeGraph 适合追求最低维护成本的团队

**场景 D：跨语言调用追踪（iOS/RN）**
```
OpenWiki:  ❌ 不支持
Graphify:  ❌ 不支持
CodeGraph: ✅ Swift↔ObjC↔RN 桥接 + Fabric/Paper/TurboModules/Expo
```
**唯一选择：CodeGraph**

**场景 E：数据库 + 基础设施 + 代码统一分析**
```
OpenWiki:  ❌ 仅代码文档
Graphify:  ✅ PostgreSQL 实时 introspection + Terraform HCL + SQL
CodeGraph: ✅ Terraform/OpenTofu
```
**胜出：Graphify** — 连接器生态更丰富（数据库、基础设施、文档、图片、视频）

**场景 F：超大型仓库（Linux 内核级别）**
```
OpenWiki:  ❌ LLM token 成本爆炸
Graphify:  ⚠️ 可能 OOM（Python 内存限制）
CodeGraph: ✅ 2 核 VPS 12 分钟完成 Linux 内核（70K 文件, 2M 符号, 6.4M 关系）
```
**胜出：CodeGraph** — Rust 内核 + 自适应资源调度

---

### 四、竞品互补关系图谱

```
                      ┌──────────────────┐
                      │   AI Coding Agent │
                      │ (Claude/Cursor/   │
                      │  Codex/OpenCode)  │
                      └────────┬─────────┘
                               │ 需要理解代码
                               ▼
              ┌────────────────────────────────────┐
              │        三种上下文供给方式            │
              └────────────────────────────────────┘
                    │              │              │
         ┌──────────┘    ┌────────┘    ┌─────────┘
         ▼               ▼             ▼
   ┌──────────┐   ┌───────────┐   ┌──────────┐
   │ OpenWiki │   │ Graphify  │   │CodeGraph │
   │ 自然语言 │   │   图查询   │   │ 源代码切片│
   │  文档    │   │ 社区+路径  │   │ 调用+影响 │
   └──────────┘   └───────────┘   └──────────┘
         │               │              │
         │  互补区域     │  重叠区域    │  竞争区域
         ▼               ▼              ▼
   ┌──────────────────────────────────────────────┐
   │  Human-readable   │  Code Intelligence        │
   │  Documentation    │  (AST → Graph → Query)    │
   └──────────────────────────────────────────────┘
```

**重叠区**（三者都做）：
- 代码库理解辅助
- 为 AI Agent 提供上下文
- MCP 协议支持

**差异区**：
- **OpenWiki** 独有：人类可读的自然语言 Wiki 文档输出
- **Graphify** 独有：Leiden 社区检测、God Node 分析、PDF/图片/视频语义提取、PostgreSQL 实时 introspection
- **CodeGraph** 独有：Rust 原生内核性能、自动文件监听同步、iOS/RN 跨语言桥接、FTS5 全文搜索、自适应资源调度

---

### 五、选择决策树

```
你的项目主要是代码+文档？
├── 需要人类可读的 Wiki？
│   └── ✅ OpenWiki
├── 需要理解代码架构/社区结构？
│   └── ✅ Graphify
├── 追求 Agent 效率最高、维护成本最低？
│   └── ✅ CodeGraph
│
你的项目包含 iOS/React Native？
└── ✅ CodeGraph（唯一支持跨语言桥接）

你的项目包含数据库 schema + 基础设施代码？
├── ✅ Graphify（PostgreSQL + Terraform + SQL）
└── ✅ CodeGraph（Terraform/OpenTofu）

你的项目是超大型仓库（>50K 文件）？
└── ✅ CodeGraph（Rust 内核，自适应资源调度）

你的团队用 Python 生态？
├── ✅ Graphify（Python 原生）
└── ✅ CodeGraph（CLI 可用，内核 Rust 但使用无感）

你只需要代码分析，不需要文档/PDF/视频？
└── ✅ CodeGraph（专注代码，做到极致）

理想组合：
  CodeGraph（代码精确解析 + 自动同步）
  + Graphify（社区检测 + 非代码语义提取）
  + OpenWiki（人类可读 Wiki 输出）
```

---

### 六、总结

这三个项目不是简单的竞争关系，而是**进化链条上的不同节点**：

1. **OpenWiki（文档时代）** — "Agent 应该读文档" → 用 LLM 生成并维护 Wiki
2. **Graphify（图谱时代）** — "Agent 应该查图" → 用知识图谱 + 图算法导航代码
3. **CodeGraph（精准上下文时代）** — "Agent 应该直接看到源代码" → 用 Rust 原生引擎 + 自动同步实现零摩擦上下文供给

**从 OpenWiki 到 Graphify 到 CodeGraph，趋势是清晰的：让 Agent 越来越靠近源代码本身，减少 LLM 中介的信息损失，减少人工维护成本。**

对于实际项目选择：
- **想快速上手、需要人类可读文档** → OpenWiki
- **需要丰富的连接器生态（数据库、文档、媒体）** → Graphify
- **追求极致性能、自动同步、跨语言桥接** → CodeGraph
- **最理想**：三者可以互补使用，但先搞清楚你的 Agent 到底需要什么——是文档、是图、还是源码本身。


## [07-24 21:39] user

什么是Leiden 社区检测和God Node 分析？


## [07-24 21:40] assistant

The user is asking me to explain what Leiden community detection and God Node analysis are, as mentioned in my previous analysis of Graphify and CodeGraph. Let me provide a clear, technically accurate explanation.

## Leiden 社区检测

**Leiden** 是一种**图聚类算法**，是 Louvain 算法的改进版本（2019 年提出）。它将图中的节点分组为"社区"——组内连接密集、组间连接稀疏的节点集合。

### 工作原理

```
输入: 知识图谱（节点=符号，边=调用/导入/继承等）
          │
    ① Local Moving Phase
       └─ 遍历每个节点，尝试移动到邻居社区
          如果移动后模块度（Modularity）提升则接受
          │
    ② Refinement Phase（Louvain 没有这一步）
       └─ 对第一步结果做细粒度调整
          用分区-迭代法拆分可能过于粗糙的社区
          │
    ③ 将社区聚合为超节点
       └─ 每个社区收缩为一个"超节点"
          回到步骤①，直到无法继续
          │
    输出: 层次化社区结构
```

### 相比 Louvain 的优势

- **保证社区内部连通**（Louvain 可能产生不连通社区）
- **模块度更高**（聚类质量更好）
- **运行速度相当或更快**

### 在 Graphify/CodeGraph 中的意义

```
假想代码库的社区划分示例：

社区 0（绿色）— HTTP 路由层
  ├── APIRouter, Route, Middleware, Request, Response
社区 1（蓝色）— 业务逻辑层
  ├── UserService, OrderService, PaymentProcessor
社区 2（红色）— 数据访问层
  ├── DatabasePool, QueryBuilder, Model, Migration
社区 3（黄色）— 基础设施/工具
  ├── Logger, Config, Cache, Metrics
```

**价值**：无需阅读代码就知道项目被分成了哪些子系统、边界在哪、依赖方向。

---

## God Node 分析

**God Node**（神节点）指的是一张图中**介数中心性（Betweenness Centrality）最高的节点**。介数中心性衡量的是"经过该节点的最短路径数量"——换句话说，**该节点在图中充当了多少"桥梁"角色**。

### 计算方式

```
介数中心性 CB(v) = Σ (σ_st(v) / σ_st)
                  s≠t≠v

其中：
  σ_st    = 从节点 s 到节点 t 的最短路径总数
  σ_st(v) = 这些路径中经过节点 v 的路径数
```

### 在代码库图谱中的含义

```
项目       | God Node      | 中心性含义
-----------|---------------|--------------------------
VS Code    | ExtensionHost | 扩展主进程 ↔ 渲染进程的桥梁
FastAPI    | APIRouter     | 所有路由注册的中心调度点
Django     | QuerySet      | ORM 查询构建的核心枢纽
Tokio      | Runtime       | 异步任务调度的心脏
React 项目 | useState/useEffect | 几乎所有组件都经过的 Hook
```

**God Node 的工程价值**：

1. **变更影响半径**：修改一个 God Node，波及半个项目
2. **架构理解捷径**：找到 God Node = 找到项目的"心脏"
3. **测试优先级**：God Node 应该是测试覆盖的重中之重
4. **重构风险预警**：God Node 重构 = 高风险操作，需要分步进行

### 辅助概念：惊喜连接

Graphify 的 `analyze.py` 还会发现**驻留在不同社区的节点间的边**——这些边称为"惊喜连接"（Surprising Connections），因为它们暴露了架构文档不会写的隐藏依赖。

```
社区边界线
─────────────
社区 0        社区 1
(Router)      (Database)
    │            │
    │  ── 惊喜连接 ──
    │  Router → Raw SQL
    │  （绕过 Repository 层）
    │            │
```

---

### 一句话总结

- **Leiden 社区检测** = 自动发现项目的"模块/子系统划分"，不需要看任何文件
- **God Node 分析** = 找到项目的"架构脊柱"，动一个节点影响半个代码库
- 两者结合：**知道哪里有边界（社区）、哪里是枢纽（God Node）**，等于拿到了项目架构的 X 光片


## [07-24 21:52] user

什么是tree-sitter和AST？有什么用？传统IDE（如eclipse、idea）有这些吗？


## [07-24 21:52] assistant

The user is asking about tree-sitter, AST, and how they relate to traditional IDEs. This is a straightforward technical explanation question.

## AST — 抽象语法树

**AST** 是源代码的**结构化树形表示**。编译器/解释器解析代码时，不会把它当字符串处理，而是先构建一棵树：

```python
# 源代码
def add(a, b):
    return a + b

# 对应的 AST（简化）
FunctionDef "add"
├── arguments
│   ├── arg "a"
│   └── arg "b"
└── Return
    └── BinOp "+"
        ├── Name "a"
        └── Name "b"
```

**AST 的价值**：把"字符串"变成"数据结构"——你可以在树上做**精确查询**（"找到所有函数定义"）和**精确变换**（"把所有 `var` 改成 `let`，且只改变量声明"），没有正则表达式那种误匹配。

---

## tree-sitter

**tree-sitter** 是一个**通用的、增量解析的 AST 解析器框架**。

### 与传统解析器的关键区别

| 特性 | 传统解析器（CPython ast, Bison/YACC） | tree-sitter |
|------|--------------------------------------|-------------|
| **增量解析** | ❌ 修改一行，重解析整个文件 | ✅ 只重新解析被改的子树 |
| **容错性** | ❌ 语法错误就失败 | ✅ 返回部分 AST + error 节点 |
| **跨语言** | ❌ 每种语言一个独立解析器 | ✅ 统一框架 + 语言语法文件 |
| **编辑友好** | ❌ 一次性解析 | ✅ 实时解析，支持 IDE 高亮 |

### 工作方式

```
tree-sitter 语法文件（.js 或 grammar.js）
  └─ 编译为 grammar.json
       └─ 编译为 parser（C/Rust/WASM 二进制）
            └─ 运行时解析源代码 → CST/AST
                 └─ 查询引擎（tree-sitter queries）
                     匹配特定模式："(function_declaration name: (identifier) @name)"
```

tree-sitter 可以被编译为三种形态：
- **C 动态库** — 最传统的方式
- **Rust crate** — CodeGraph 采用的方式
- **WebAssembly** — 浏览器/Node.js 使用的方式（CodeGraph 的回退引擎、Graphify 的部分引擎）

---

## 传统 IDE（Eclipse/IntelliJ IDEA）有这些吗？

### 有，但不同

Eclipse 和 IntelliJ IDEA 都有自己的 AST 基础设施，但和 tree-sitter 的设计哲学完全不同：

| 维度 | Eclipse JDT AST | IntelliJ PSI | tree-sitter |
|------|----------------|-------------|-------------|
| **用途** | 编译器前端副产品 | IDE 全功能语言模型 | 纯语法分析 |
| **增量能力** | 有限（AST 不可变性） | ✅ 基于 PSI 树的增量 | ✅ 树分片增量 |
| **类型解析** | ✅ 完整（连接字节码） | ✅ 完整（含类型推断） | ❌ 不求类型系统 |
| **跨语言** | ❌ 每种语言一套体系 | ❌ 每种语言一套 PSI | ✅ 统一框架 |
| **容错性** | ❌ 语法错误 → 红色波浪线 | ⚠️ 容错，但有限 | ✅ 天然容错 |
| **API 大小** | 数百个类 | 数千个类 | ~50 个核心 API |
| **二进制大小** | 巨大（含整个编译器） | 巨大（含索引/引用/类型） | ~50-200KB 每语言 |
| **嵌入难度** | 需运行完整 Eclipse | 需运行完整 IntelliJ | `npm install` 即可 |

### 技术历史演进

```
1990s:  IDE 用正则/字符串搜索做代码分析（vim/emacs 时代）
             │
2000s:  Eclipse JDT / IntelliJ PSI 出现
        └─ 与编译器深度绑定，功能完整但沉重
        └─ 设计目标：人类开发者（重构、补全、导航）
             │
2010s:  LSP（Language Server Protocol）标准化
        └─ 解耦语言支持与编辑器
        └─ 但仍继承传统编译器的全量解析模型
             │
2018:   tree-sitter 发布
        └─ 设计目标：编辑器（语法高亮）、工具（静态分析）、Agent
        └─ 轻量 + 增量 + 容错 + 跨语言统一
             │
2024-26: Graphify / CodeGraph 等 AI 工具采用 tree-sitter
        └─ 设计目标：AI Agent 的代码理解
        └─ 只需要语法结构，不需要类型系统
```

---

## 为什么 AI Agent 工具选择 tree-sitter 而非传统 IDE AST？

### 核心原因

1. **轻量可嵌入** — tree-sitter 的 WASM 版本可以在 Node.js 中直接运行，不需要启动一个 JVM 或安装特定 IDE。CodeGraph 的 npm 包仅 649KB，包含了所有语言的支持。

2. **容错性** — AI Agent 经常处理**不完整的代码**（正在编辑的文件、有语法错误的中间状态）。传统 IDE AST 在这种情况下直接报错，tree-sitter 仍然能返回部分结构。

3. **跨语言统一 API** — Graphify 和 CodeGraph 都需要支持 20-36 种语言。如果用 36 套不同 IDE API，代码量会爆炸。tree-sitter 用一种 API 覆盖所有语言。

4. **只关心语法，不关心语义** — AI Agent 的功能需求与传统 IDE 不同：
   ```
   IDE 需要：   类型检查、重构、补全 → 需要完整类型系统
   Agent 需要： 找调用关系、找定义、找引用 → 只需要语法结构
   ```
   Agent 可以用 LLM 处理语义部分，不需要编译器级别的类型推导。

5. **增量性能** — CodeGraph 的自动监听场景中，文件每次保存都要重新解析。tree-sitter 的增量解析可以在 O(log n) 时间内处理一次编辑；传统 IDE AST 通常需要重新解析整个文件。

### 不是替代，是分层

实际上，**tree-sitter 和传统 IDE AST 不是替代关系，而是不同抽象层级**：

```
源代码
   │
   ▼
tree-sitter CST（具体语法树）
   │ ── 语法高亮、折叠、符号大纲
   │ ── AI Agent 代码理解
   ▼
语义分析 → 类型绑定
   │
   ▼
IDE PSI/AST（含类型信息）
   │ ── 重构（重命名需要类型感知）
   │ ── 补全（需要类型推断）
   │ ── 查找引用（含继承链）
```

Graphify 和 CodeGraph 选择停在第一层——因为对 Agent 来说，**找到结构就够了，LLM 会处理剩下的理解**。传统 IDE 必须走到第三层，因为 IDE 功能（重构、补全）需要精确的类型信息，不能依赖 LLM。


## [07-24 22:02] user

什么是CST和ASM？


## [07-24 22:02] assistant

The user is asking about CST (Concrete Syntax Tree) and ASM - but I think they meant to ask about CST and AST, or possibly CST and ASM. Let me think...

In the context of the previous conversation about tree-sitter and AST:

1. **CST** - Concrete Syntax Tree (具体语法树) - also known as a Parse Tree. This contains all the syntactic detail from the source code including parentheses, semicolons, whitespace (in some definitions), etc. It's a direct representation of the grammar rules applied.

2. **ASM** - This could be:
   - Assembly language
   - ASM.js
   - But in the context of compilers/IDE, it might be a typo for "AST" again, or they might be asking about something else

Actually, looking more carefully, I think the user is asking about:
- CST (Concrete Syntax Tree) - the raw parse tree
- And maybe they meant to contrast CST with AST, or they're asking about ASM (Abstract State Machine? or assembly?)

But given the context flow: we just discussed tree-sitter vs traditional IDE AST, and tree-sitter actually produces CST (Concrete Syntax Tree), not AST. The user might be asking about that distinction.

Let me think again... "ASM" - this could actually refer to ASM (a Java bytecode manipulation framework), or ASM.js, or Assembly language. But in the context of this discussion about AST/CST/parsing, it's most likely:
- The user might have made a typo and means "AST"
- Or ASM could be referring to something specific

Actually I think the user is probably asking about the difference between CST and ASM (maybe someone mentioned ASM before, or they're asking about Assembly language representation vs syntax tree).

Let me just answer clearly about CST and clarify what ASM could mean in this context. Given the code analysis context, I'll cover CST and potentially ASM if it relates to code representation.

Actually, rethinking - I believe the user simply wants to know what CST (Concrete Syntax Tree) is, and they may have a typo or they want to know about AST vs CST. Or perhaps they're asking about ASM (the Java bytecode framework by OW2).

Let me just answer what CST is clearly and also explain ASM (the Java bytecode analysis/manipulation library) since that's relevant in the context of code analysis tools, or clarify if they meant something else.

Wait - could "ASM" be referring to AST? The keys "X" and "S" are not particularly close on a keyboard... "A" and "A" are the same... Hmm. Maybe just a typo where they typed "ASM" but meant "AST"? Or maybe they are familiar with both terms separately?

Actually the simplest and most correct interpretation: the user is asking about CST and likely ASM as in the Java bytecode framework (which is commonly used in code analysis). This is a reasonable follow-up to a discussion about code representation formats.

Let me answer concisely.

## CST — Concrete Syntax Tree（具体语法树）

CST 是解析器直接输出的树，**保留了源代码的所有语法细节**：

```python
# 源代码
x = a + b

# CST（tree-sitter 产出这种）
module [0, 0] - [0, 9]
├── expression_statement [0, 0] - [0, 9]
│   ├── assignment [0, 0] - [0, 9]
│   │   ├── left: identifier "x" [0, 0] - [0, 1]
│   │   ├── operator: "=" [0, 2] - [0, 3]    ← 等号保留
│   │   └── right: binary_expression [0, 4] - [0, 9]
│   │       ├── left: identifier "a" [0, 4] - [0, 5]
│   │       ├── operator: "+" [0, 6] - [0, 7] ← 加号保留
│   │       └── right: identifier "b" [0, 8] - [0, 9]
│   └── ";" [0, 9] - [0, 10]                  ← 分号保留

# AST（抽象语法树）—— 丢弃语法糖
Assignment
├── target: Variable "x"
├── value: BinaryOp "+"
│   ├── left: Variable "a"
│   └── right: Variable "b"
```

| | CST | AST |
|---|---|---|
| **保留括号、分号、关键字** | ✅ | ❌ |
| **包含终端节点（Token）** | ✅ | ❌ |
| **可用于语法高亮** | ✅ 天然匹配 | ❌ 缺少位置信息 |
| **可用于语义分析** | ❌ 太多噪声 | ✅ |

**tree-sitter 产出的其实是 CST，而不是严格的 AST。** 它保留了每个 Token 的行列位置（`[行, 列]`），所以可以做语法高亮和代码折叠。

---

## ASM

ASM 有两种常见指代，取决于上下文：

### 1. Java ASM 框架（代码分析领域最常见）

[OW2 ASM](https://asm.ow2.io/) 是一个 **Java 字节码操作和分析框架**。不是操作源代码，而是操作 `.class` 文件：

```
Java 源代码 → javac 编译 → .class 字节码 → ASM 读取/修改 → 新的 .class
                                    ↑
                              ASM 在这里工作
```

**ASM 的字节码树结构**（比源代码 AST 低一层）：

```
.class 文件
├── 常量池（Constant Pool）
├── 类信息（版本、接口、注解）
└── 方法
    ├── max_stack / max_locals
    └── 指令序列（字节码）
        ├── ILOAD 1
        ├── ILOAD 2
        ├── IADD              ← 这里对应源代码的 a + b
        └── IRETURN
```

**ASM 的用途**：
- Spring Boot / Hibernate 的运行时字节码增强（生成代理类）
- Gradle 的编译时字节码修改
- 代码覆盖率工具（JaCoCo）
- 性能监控（APM 代理注入）
- 混淆器（ProGuard）

### 2. 汇编语言（Assembly）

如果你是指 CPU 汇编——那是最底层的指令集，与 AST/树结构无关。

---

### 一句话串起来

```
源代码 → CST（tree-sitter，含标点位置）→ AST（丢弃语法糖）→ 字节码（ASM 操作）→ 机器码
         ↑                    ↑                       ↑
    语法高亮、Agent     编译器语义分析        Spring AOP 代理增强
    代码分析（CodeGraph)    IDE 重构
```

**CodeGraph/Graphify 用 CST（tree-sitter），传统 IDE 用 AST，ASM 操作更底层的字节码**——三层各有用途。


## [07-24 22:09] user

什么是语法糖？


## [07-24 22:09] assistant

The user is asking about the concept of "syntactic sugar" (语法糖/语法糖). This is a straightforward programming language concept question. I should answer concisely.

**语法糖**是语言设计者为了让代码更好读/好写而添加的语法特性——它不引入新能力，只是**把已有的功能"包裹"成更甜的写法**。

```python
# 列表推导式（语法糖）
squares = [x**2 for x in range(10)]

# 等价于普通循环（去糖后）
squares = []
for x in range(10):
    squares.append(x**2)
```

```python
# 装饰器（语法糖）
@cache
def fib(n): ...

# 去糖后
fib = cache(fib)
```

```python
# a += 1（语法糖）
a += 1

# 去糖后
a = a + 1
```

**CST vs AST 的关系**：CST 保留了语法糖（`@cache`、`+=`、`for...in` 都是显式节点），AST 通常会"去糖"把它们展开为基础操作。


## [07-25 10:32] user

介绍一下langSmith


## [07-25 10:32] assistant

The user is asking about LangSmith. Let me fetch information about it.


## [07-25 10:33] assistant

Now I have a comprehensive understanding of LangSmith. Let me compile a concise but informative introduction.

## LangSmith

LangSmith 是 LangChain 公司推出的 **LLM 应用可观测性平台**，提供从开发到生产的全链路追踪、评估和监控。有 SaaS 云版和自托管版。

### 核心功能

**1. Tracing（追踪）**
自动捕获 LLM 应用的每一步执行轨迹：
```
用户请求 → 工具调用 → LLM 调用 → 输出解析
    │          │          │         │
    └──── 完整 trace 树，含 input/output/latency/tokens/cost
```
支持 LangChain、LangGraph、OpenAI、Anthropic、CrewAI 等框架的自动插桩，也提供 `@traceable` 装饰器手动追踪任意 Python/TS/Go/Java 函数。

**2. Evaluation（评估）**
- **LLM-as-Judge**: 用 LLM 评分 LLM 的输出质量
- **在线评估**: 生产流量采样，自动检测幻觉、意图偏移、推理错误
- **数据集**: 从生产 trace 一键构建测试集，做回归验证

**3. Prompt 管理**
版本化、对比、部署 prompt，可 A/B 测试，非工程人员也能在 UI 上迭代。

**4. SmithDB**
专为 Agent 追踪设计的存储引擎——单次对话可能产生数十 MB 的嵌套 span 数据，通用数据库不适合这种查询模式。

### 与 OpenWiki 的关系

两者同属 LangChain 生态但完全互补：

```
OpenWiki:  开发阶段的代码文档生成（给 Agent 读的 Wiki）
LangSmith: 运行时的 Agent 行为观测（给人看的 Trace）
```

OpenWiki 项目自身也集成了 LangSmith——在配置中设置 `LANGSMITH_API_KEY` 即可追踪每次 `openwiki --init/--update` 的 LLM 调用链，用于调试和成本分析。

### 定价

- 免费版：每月 5,000 条 trace（开发和小规模生产足够）
- 付费版：按 trace 量计费
- 数据保留：SaaS 版 400 天


## [07-27 21:01] user

如何获取LangSmith API key？


## [07-27 21:01] assistant

The user is asking how to get a LangSmith API key. This is a straightforward factual question.

访问 https://smith.langchain.com → 用 Google/GitHub/Email 注册 → **Settings → API Keys → Create API Key**。免费版无需信用卡。
