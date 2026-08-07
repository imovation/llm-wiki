---
source_url: opencode://session-history/2026-07-20-cosmic-harbor
title: Session: AI编程工具Comet、OpenWiki、Graphify研究与应用
ingested: 2026-08-07
sha256: 03a414ab98c74a135cc5fb0c350b45d63ff284880e9da0d00021a5432ace3538
---

# Session: AI编程工具Comet、OpenWiki、Graphify研究与应用

- slug: `cosmic-harbor`  session-id: `ses_080346ebbffe7d2bnhs0z8lOut`  created: 2026-07-20 21:51
- 源目录：/home/imovation/projects/llm-wiki


## [07-20 21:51] user

comet:https://github.com/rpamis/comet
openwiki:https://github.com/langchain-ai/openwiki
graphify:https://github.com/Graphify-Labs/graphify
研究并介绍上面三个工具，然后分析如何在AI编程中综合应用？


## [07-20 21:51] assistant

The user wants me to research and introduce three tools from their GitHub repositories, then analyze how they can be comprehensively applied in AI programming. Let me fetch information about all three repositories in parallel.


## [07-20 21:51] assistant

Now let me fetch the README for each repo to get more detailed information.


## [07-20 21:52] assistant

I now have comprehensive information about all three tools. Let me synthesize this into a clear, structured response.

**Comet** (rpamis/comet): A resumable long-running task workflow and Skill platform for AI coding. It combines OpenSpec artifacts and Superpowers execution methodology into a 5-phase workflow (Open → Design → Build → Verify → Archive). Key features:
- State machine with phase guards ensuring reliable execution
- Resumable workflows that survive context loss and device switching
- Skill platform: compose any skills into distributable bundles with `/comet-any`
- Eval platform: scientific evaluation of skills with Rubric, Pass@k, Pass^k scoring
- Supports 33+ AI coding platforms
- Dashboard for visual tracking
- Integration with LangSmith/LangFuse for enterprise evaluation

**OpenWiki** (langchain-ai/openwiki): A CLI that writes and maintains agent documentation for codebases. Key features:
- Two modes: Code mode (repository documentation) and Personal mode (personal brain wiki)
- Connects to local knowledge sources: Git repositories, Gmail, Notion, Web Search, Hacker News, X/Twitter
- Emits Google Open Knowledge Format (OKF) bundles
- Multi-provider support: OpenAI, Anthropic, Gemini, Bedrock, Ollama, etc.
- CI/CD integration for automated documentation updates
- Maintains AGENTS.md/CLAUDE.md for AI coding assistants

**Graphify** (Graphify-Labs/graphify): An AI coding assistant skill that turns any folder of code/docs/media into a queryable knowledge graph. Key features:
- Local code parsing via tree-sitter (deterministic, no LLM)
- Graph-based traversal: query, path, explain commands
- Community detection via Leiden algorithm
- Cross-file links (calls/imports/inherits) across ~40 languages
- Supports code, docs, PDFs, images, videos
- MCP server for team-wide graph access
- 92K+ stars, 20+ platform integrations

Now let me analyze how to comprehensively apply these in AI programming:

**Comprehensive Application in AI Programming:**

These three tools complement each other beautifully in the AI programming workflow:

1. **Understanding the codebase** (Graphify) → Before writing any code, understand the codebase's structure, dependencies, and architecture through a knowledge graph.

2. **Maintaining documentation** (OpenWiki) → Keep documentation current and accessible for both humans and AI agents.

3. **Executing structured workflows** (Comet) → Turn development tasks into reliable, resumable, phase-guarded workflows.

The integration pattern:

- Graphify maps the project → gives the AI agent semantic understanding
- OpenWiki documents the project → gives the AI agent persistent context
- Comet orchestrates the work → ensures reliable, traceable execution

A concrete pipeline:
1. Run Graphify on the codebase to build a knowledge graph
2. Use OpenWiki to generate/maintain project documentation (which can reference the Graphify graph)
3. Use Comet's `/comet` workflow, where each phase can leverage the graph for context and the wiki for documentation standards
4. Evaluate the quality of AI-generated code through Comet's eval platform
5. The documentation stays in sync through OpenWiki + Comet's archive phase

## 工具概览

### 1. Comet (rpamis/comet) — 2.4k Stars, MIT
**Agent Skill 平台 + 可恢复的长任务工作流引擎**

- **核心能力**：将 OpenSpec（规格）和 Superpowers（执行方法）组合成五阶段工作流：`Open → Design → Build → Verify → Archive`
- **关键特性**：
  - 状态机 + 阶段守卫（phase guards），确保 Agent 只在当前阶段做允许的事
  - 可中断恢复：`.comet.yaml` 记录进度，跨设备零上下文恢复
  - `/comet-any`：将任意 Skill 组合为可分发的 Bundle
  - `comet eval`：基于 Rubric / Pass@k / Pass^k 的科学化评估，对接 LangSmith
  - 支持 33+ AI 编码平台，纯 Node.js 运行时
  - Dashboard 可视化每一步进展

### 2. OpenWiki (langchain-ai/openwiki) — 12.6k Stars, MIT
**Agent 文档 CLI — 为代码库自动生成并维护文档**

- **核心能力**：两种模式 — Code 模式（仓库文档）和 Personal 模式（个人知识脑）
- **关键特性**：
  - 多源连接器：Git 仓库、Gmail、Notion、Web Search、Hacker News、X/Twitter
  - 输出 Google Open Knowledge Format (OKF) 标准
  - 自动维护 `AGENTS.md` / `CLAUDE.md`，让 AI 编码助手自动参考 Wiki
  - CI/CD 集成（GitHub Actions / GitLab CI / Bitbucket Pipelines），文档随代码自动更新
  - 多模型供应商：OpenAI、Anthropic、Gemini、Bedrock、Ollama 等

### 3. Graphify (Graphify-Labs/graphify) — 92k Stars, MIT
**知识图谱 Skill — 将代码/文档/图片/视频变成可查询的图**

- **核心能力**：用 tree-sitter AST 本地解析代码（零 LLM 成本），构建跨文件的知识图谱
- **关键特性**：
  - `graphify query "问题"` / `graphify path A B` / `graphify explain X` 图查询替代 grep
  - Leiden 社区检测，自动分模块
  - 每条边标记 `EXTRACTED`（显式）或 `INFERRED`（推断），置信度透明
  - 40+ 语言 AST 解析 + 文档/PDF/图片/视频语义抽取
  - MCP Server 支持团队共享
  - git hook 在每次 commit 时自动重建

---

## 在 AI 编程中的综合应用分析

这三个工具形成了一条完整的 **理解 → 记录 → 执行 → 评估** 流水线：

```
Graphify（理解）  →  OpenWiki（记录）  →  Comet（执行 + 评估）
   知识图谱           项目文档             工作流编排 & 科学评测
```

### 组合工作流

| 阶段 | 工具 | 作用 |
|------|------|------|
| **1. 项目理解** | Graphify | 构建知识图谱，AI Agent 通过图查询理解代码架构、依赖关系、关键路径，替代逐文件 grep |
| **2. 文档同步** | OpenWiki | 生成并维护项目 Wiki，注入 `AGENTS.md` 让后续 AI 会话自动获取上下文 |
| **3. 任务执行** | Comet | 用 `/comet` 驱动五阶段 Spec 工作流，每次编码都有规格、设计、实现、验证、归档 |
| **4. 质量评估** | Comet Eval | 对生成的 Skill 做科学评估（Rubric/Pass@k），接入 LangSmith 做生产级追踪 |
| **5. 持续更新** | Graphify Hook + OpenWiki CI | git commit 触发图重建；CI 自动更新文档 PR，保持知识资产始终最新 |

### 关键协同点

1. **Graphify → Comet 的 Design 阶段**：AI Agent 在 Comet 的设计阶段可以 `graphify query "认证模块如何连接数据库"` 获取准确的架构上下文，产出更精准的设计文档

2. **Graphify → OpenWiki**：OpenWiki 生成的文档可以引用知识图谱中的概念节点，形成「文档 ↔ 代码」双向链接

3. **OpenWiki → Comet 的 Build 阶段**：Comet 的 Build 阶段读取 OpenWiki 维护的 `AGENTS.md`，让 Agent 自动遵循项目文档规范编码

4. **Comet → OpenWiki 的 Archive 阶段**：Comet 归档时触发 OpenWiki 更新文档，确保 Spec 变更反映到 Wiki

5. **Comet Eval + Graphify**：评估 Skill 质量时，Graphify 提供代码变更影响范围分析，辅助判断 Spec 覆盖是否完整

### 一键初始化脚本思路

```bash
# 1. 构建项目知识图谱
graphify install && /graphify .

# 2. 初始化项目文档
openwiki --init

# 3. 初始化工作流平台
cd your-project && comet init

# 4. 安装自动更新钩子
graphify hook install          # git commit 时自动重建图
cp openwiki-update.yml .github/workflows/  # CI 自动文档 PR
```

这一组合的本质是：**Graphify 让 AI 真正理解代码，OpenWiki 让知识持久化，Comet 让编码过程可靠、可评估、可进化**。三者从「静态理解」到「动态执行」覆盖了 AI 编程的完整生命周期。


## [07-20 22:06] user

三者生态位有重叠部分吗？


## [07-20 22:06] assistant

The user is asking whether the three tools have overlapping niches/ecosystem positions. Let me analyze this carefully based on what I've learned about each tool.

Let me think about the overlaps:

1. **Comet vs OpenWiki** - Both interact with AGENTS.md/CLAUDE.md files. Comet injects phase-guard rules and ambient resume blocks; OpenWiki injects wiki-reference blocks. Both are effectively "agent context management" tools in that sense. But their purpose is different: Comet manages workflow state, OpenWiki manages knowledge/documentation.

2. **Comet vs Graphify** - Both want to help the AI agent understand the codebase. Comet does this through OpenSpec specs + Superpowers design docs; Graphify does this through knowledge graphs. Both are installed as "skills" for AI coding assistants. Both support many platforms. Both have some notion of "phase" or "context" awareness. But Comet is workflow-oriented while Graphify is knowledge-graph-oriented.

3. **OpenWiki vs Graphify** - Both are about understanding/documenting the codebase. OpenWiki generates markdown wiki documentation; Graphify generates a knowledge graph with query capabilities. Both can be committed to git. Both output structured knowledge about the project. This is the most overlapping pair.

Let me think deeper about the specific overlaps:

**Comet ↔ Graphify overlap:**
- Both install as skills into AI coding platforms (Claude Code, Codex, Cursor, OpenCode, etc.)
- Both modify AGENTS.md/CLAUDE.md to inject rules
- Both have hooks mechanism on Claude Code (Comet: PreToolUse phase guard; Graphify: PreToolUse nudge to use graph)
- Both care about "context" - Comet compresses context between phases, Graphify provides context through graph queries
- However their philosophies differ: Comet is about workflow discipline; Graphify is about knowledge retrieval

**Comet ↔ OpenWiki overlap:**
- Both manage AGENTS.md/CLAUDE.md blocks
- Comet writes `<comet-ambient-resume>` block; OpenWiki writes `<!-- OPENWIKI:START -->…<!-- OPENWIKI:END -->` block
- Both are designed to coexist (they use different delimiters)
- Both are CLI tools (npm install -g)
- OpenWiki does documentation; Comet's archive phase also touches documentation

**OpenWiki ↔ Graphify overlap:**
- This is the most significant overlap
- Both are about "understanding the codebase"
- OpenWiki generates a wiki (markdown documents); Graphify generates a knowledge graph (JSON + HTML + report)
- OpenWiki uses LLM to read code and write docs; Graphify uses tree-sitter AST (deterministic) for code
- OpenWiki can cross-reference between docs (wikilinks); Graphify can traverse graph edges
- Both can be used to answer "how does X work?" questions
- Both are meant to be consumed by AI agents
- OpenWiki is more narrative/documentation-oriented; Graphify is more structural/query-oriented
- KEY DIFFERENCE: Graphify provides real-time graph traversal (query, path, explain); OpenWiki provides prose documentation
- Graphify has graph.html for visual exploration; OpenWiki has none
- OpenWiki connects to personal data sources (Gmail, Notion, X); Graphify connects to code/docs/media

So in summary, the overlaps are partial:
- OpenWiki ↔ Graphify: moderate overlap in "understand and document codebase"
- Comet ↔ Graphify: light overlap in "skill platform + AGENTS.md injection"
- Comet ↔ OpenWiki: light overlap in "AGENTS.md management"

None of the three is fully redundant with another. Each has a distinct primary purpose.

是的，三者有部分生态位重叠，但核心定位各不相同：

## 重叠分析

### 最大重叠：OpenWiki ↔ Graphify（"理解代码库"层）

| 维度 | OpenWiki | Graphify |
|------|----------|----------|
| 目标 | 生成可读的 Markdown Wiki 文档 | 构建可查询的知识图谱 |
| 方式 | LLM 阅读代码 → 写叙事性文档 | tree-sitter AST 解析（确定性）+ LLM 处理文档/媒体 |
| 输出 | `openwiki/` 下多个 .md 文件 | `graph.json` + `graph.html` + `GRAPH_REPORT.md` |
| 交互 | 阅读文档 | `query` / `path` / `explain` 图遍历 |
| 视觉化 | 无 | 力导向图 HTML，社区着色，可交互 |
| 外部数据源 | Gmail、Notion、X、Hacker News | PDF、图片、视频、论文 URL |

两者都解决"AI Agent 怎么理解项目"的问题，但路径不同：OpenWiki 是**叙事型**（像技术文档），Graphify 是**结构型**（像代码地图）。GR/APH_REPORT.md 和 Wiki 在某些场景下提供相似的信息（模块介绍、关键概念）。

### 轻度重叠：Comet ↔ Graphify（"Agent Skill 平台"层）

- **共用 AGENTS.md / CLAUDE.md**：Comet 注入 `<comet-ambient-resume>` 规则块，Graphify 注入 `graphify query` 优先指令，两者都通过 `<!-- ... -->` 标记实现共存
- **共用 Hook 机制**：在 Claude Code 上，Comet 用 PreToolUse 阻止非当前阶段文件写入，Graphify 用 PreToolUse 在 Read/Glob 前推图查询——同机制，不同目的
- **都支持 20+ AI 编码平台**，都能 `install --project` 或 `install --platform xxx`

### 轻度重叠：Comet ↔ OpenWiki（"AGENTS.md 管理"层）

- 两者都写入 `AGENTS.md` / `CLAUDE.md`，但用不同分隔符，设计上兼容
- OpenWiki 负责**知识内容**（项目怎么工作），Comet 负责**流程规则**（当前处于哪个阶段、什么时候该做什么）
- Comet 的 Archive 阶段也涉及文档同步，但范围限定在 Spec 与 Design Doc 的对齐，不涉及全项目 Wiki

## 不重叠的核心差异

| 独有能力 | Comet | OpenWiki | Graphify |
|----------|-------|----------|----------|
| 五阶段状态机工作流 | **独占** | — | — |
| Skill 创建/分发/评估平台 | **独占** | — | — |
| 科学化评估（Rubric/Pass@k） | **独占** | — | — |
| LangSmith 集成 | **独占** | — | — |
| Personal 知识脑（Gmail/Notion/X） | — | **独占** | — |
| CI 自动文档 PR | — | **独占** | — |
| 无 LLM 本地代码 AST 解析 | — | — | **独占** |
| 图查询（path/explain/query） | — | — | **独占** |
| 社区检测（Leiden） | — | — | **独占** |
| git hook 自动重建图 | — | — | **独占** |

## 结论

三者重叠面积小——**OpenWiki 和 Graphify 的"项目理解"职能有替代关系**，根据需求二选一或互补（Graphify 做结构分析 + OpenWiki 做叙事文档）。Comet 与其他两者几乎没有职能重叠，是纯粹的流程编排层。三者更多是**上下游关系**而不是竞品关系。


## [07-23 20:31] user

介绍一下codegraph：https://github.com/colbymchenry/codegraph


## [07-23 20:31] assistant

The user wants me to fetch and introduce the CodeGraph tool from the given GitHub URL.


## [07-23 20:32] assistant

Now I have comprehensive information about CodeGraph (colbymchenry/codegraph). Let me synthesize this into a clear introduction. This is a different tool from the codegraph MCP tool already in the session - it's a separate project by Colby McHenry.

Key points:
- 61.9k Stars, MIT license
- Language: C (but has a Rust kernel for parsing)
- Description: Pre-indexed code knowledge graph, auto syncs on code changes
- Supports Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, Hermes Agent
- Key features: Rust kernel, auto-sync via file watcher, 20+ languages, framework-aware routes, RN/iOS bridging, MCP server, 100% local

Now let me also compare it with Graphify (Graphify-Labs/graphify) since they occupy the same niche - both are code knowledge graphs for AI coding assistants. This is the key comparison the user will likely want.

## CodeGraph (colbymchenry/codegraph) — 61.9k Stars, MIT

**核心定位**：预索引的代码知识图谱，为 AI 编码助手提供"外科手术式"的符号查询能力，免去 Agent 逐文件 grep/Read 的 Token 浪费。

### 架构特色

- **Kernel 层用 Rust 实现**（20 种语言的 AST 解析），Node.js CLI 做胶水层
- **文件监听器**（FSEvents/inotify/ReadDirectoryChangesW）自动同步，每次保存文件 ~0.3s 完成增量更新
- **MCP Server** 输出给 AI Agent，一次 `codegraph_explore` 调用返回符号源码 + 调用路径 + 影响范围
- **SQLite 存储**，100% 本地，无 API Key，无需外网

### 关键能力

| 能力 | 说明 |
|------|------|
| 自动同步 | 原生文件监听器，debounce 后自动重建，永不 stale |
| 框架感知路由 | Django/Flask/FastAPI/Express/NestJS/Laravel/Rails/Spring/Gin/ASP.NET 等 17+ 框架的 URL → Handler |
| iOS/RN 跨语言桥接 | Swift↔ObjC、RN Legacy Bridge、TurboModules、Fabric View、Expo Modules |
| 影响分析 | 调用者/被调用者/完整影响半径 |
| 全文搜索 | FTS5 索引，全代码库即时符号搜索 |
| 多 Agent 平台 | Claude Code、Cursor、Codex、OpenCode、Gemini CLI、Antigravity、Kiro、Hermes Agent |

### 性能实测

7 个真实开源项目基准（Claude Opus 4.8，中位数 4 次）：

| 指标 | WITH CodeGraph | WITHOUT |
|------|---------------|---------|
| 工具调用 | **2-3 次** | 10-57 次 |
| Token 消耗 | 减少 **69%** | — |
| 成本 | 减少 **60%** | — |
| 文件读取 | **0**（所有 7 个仓库） | 1-24 次 |
| 加速比 | 最大 5×（VS Code: 41s vs 3m24s） |

---

## 与 Graphify-Labs/graphify 的对比

两者都在"将代码索引为 AI Agent 可查询的知识图"这一生态位，但技术路线和侧重点差异明显：

| 维度 | CodeGraph (colbymchenry) | Graphify (Graphify-Labs) |
|------|-------------------------|--------------------------|
| **解析引擎** | **Rust** 原生（20 语言，逐文件验证一致性） | **Python** + tree-sitter（40+ 语法） |
| **同步方式** | 原生文件监听器，自动增量同步（<1s） | git hook 触发，CI 重建 |
| **跨语言桥接** | iOS/RN/Expo 跨语言边界（Swift↔ObjC, JS↔Native） | 不支持 |
| **框架路由** | 17+ Web 框架的 URL→Handler 解析 | 不支持 |
| **部署方式** | MCP Server（stdio/HTTP），也可做 LLM Server | MCP Server + CLI 图查询 |
| **内容类型** | 仅代码 | 代码 + 文档 + PDF + 图片 + 视频 |
| **社区检测** | 无 | Leiden 算法，自动分模块着色 |
| **图可视化** | 无 | `graph.html` 力导向交互图 |
| **团队共享** | MCP HTTP Server + LLM Server | MCP HTTP Server |
| **Stars** | 61.9k | 92k |
| **关键差异** | **快**（Rust 内核+监听器）、**准**（影响分析、跨语言桥接）、**省**（60% 成本节省实测） | **广**（40+ 语言 + 文档/媒体）、**可视**（交互图 + 社区着色）、**查询**（query/path/explain） |

### 一句话总结

- **CodeGraph**：为"Agent 写代码时的即时理解"而生——Rust 内核足够快，文件监听器保证永远最新，影响分析让 Agent 知道改一处会炸哪里
- **Graphify**：为"人类/Agent 对代码库的整体认知"而生——图可视化+社区着色帮你鸟瞰架构，媒体/文档支持让知识图谱不限于代码

两者在 AI 编程中可互补：**Graphify 做项目初始化时的架构图谱构建和可视化**，**CodeGraph 在 Agent 日常编码中做实时上下文查询**，两者通过各自的 MCP Server 互不冲突。
