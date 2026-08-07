---
source_url: opencode://session-history/2026-07-18-misty-river
title: "Session: Spec是指令，Wiki是知识。"
ingested: 2026-08-07
sha256: 657f596b6961d9e7f70cb12a02e9334b61c78b1b335bf6993372071b6b549e6c
---

# Session: Spec是指令，Wiki是知识。

- slug: `misty-river`  session-id: `ses_08cc61cd4ffeRdNnoeHQn8lAE6`  created: 2026-07-18 11:16
- 源目录：/home/imovation/projects/llm-wiki


## [07-18 11:16] user

请将 LLM Wiki 这篇文章保存在本地，并翻译成中文版。


## [07-18 11:16] assistant

The user wants me to:
1. Save the LLM Wiki article locally
2. Translate it to Chinese

Let me first understand what "LLM Wiki" refers to. Let me check the current directory to understand the project structure first.


## [07-18 11:16] assistant

The directory is empty. The user wants me to save the "LLM Wiki" article. I think "LLM Wiki" might refer to a specific article or online resource. Let me search the web to find what "LLM Wiki" refers to - it could be a Wikipedia article or some other resource about Large Language Models.

Let me search for it.


## [07-18 11:16] assistant

The user mentioned "LLM Wiki 这篇文章" (this article). Let me look at the search results. There are a few possibilities:

1. The Wikipedia article "Large language model" - https://en.wikipedia.org/wiki/Large_language_model
2. The GitHub project "llm_wiki" by nashsu - based on Karpathy's LLM Wiki pattern
3. Karpathy's original gist about LLM Wiki pattern

The project name is "llm-wiki" and the directory is also called `llm-wiki`. Let me check what "LLM Wiki" specifically refers to. The GitHub project seems to be the most relevant "LLM Wiki" application. But the user said "这篇文章" (this article), so they're referring to an article about LLM Wiki.

Let me look at Karpathy's original gist which seems to be the source of the "LLM Wiki" concept. Let me fetch that.

Actually, let me re-read: the project is called "llm-wiki" and the directory is empty. The user wants to save "LLM Wiki 这篇文章" which could be:

1. Karpathy's original `llm-wiki.md` gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
2. The Wikipedia article on "Large language model"

Given the directory name "llm-wiki", I think Karpathy's gist is most likely what they're referring to. Let me fetch it.

Actually, looking at the search results more carefully, the search result about the GitHub project says:
- "This project is based on Karpathy's LLM Wiki pattern"
- The foundational methodology comes from Andrej Karpathy's llm-wiki.md

So "LLM Wiki" is Karpathy's concept/pattern. Let me fetch the original gist.


## [07-18 11:17] assistant

I got the full content of Karpathy's LLM Wiki gist. Now I need to:

1. Save the English original locally
2. Create a Chinese translation

The user mentioned "LLM Wiki 这篇文章", and the project directory is `llm-wiki`, which matches Karpathy's `llm-wiki.md` gist. Let me now create both files:
- `llm-wiki.md` - the original English version
- `llm-wiki.zh.md` - the Chinese translation

Let me carefully extract the article content from the fetched page. I need to separate the actual article content from the comments/reactions at the bottom.

Let me read the saved output file to get the exact content.


## [07-18 11:17] assistant

The directory is empty. Let me read the tool output file to get the exact content of the gist.


## [07-18 11:17] assistant

Good. Now I have the full content of the article (lines 76-167 are the actual article content). Let me extract just the article content (excluding the GitHub UI and comments) and write both files:

1. Original English version: `llm-wiki.md`
2. Chinese translation: `llm-wiki.zh.md`

Let me first write the original English version by extracting just the article content from the fetched page.

The article starts at line 76 (`# LLM Wiki`) and ends at line 167 (before "Load earlier comments...").

Let me also try to get the raw markdown version from GitHub for cleaner content.


## [07-18 11:17] assistant

Now I have the clean article content. I need to:
1. Write the original English as `llm-wiki.md`
2. Write the Chinese translation as `llm-wiki.zh.md`

Let me create both files now.


## [07-18 11:17] assistant

Both files have been written. Let me verify them.


## [07-18 11:18] assistant

Both files are there. Let me confirm with the user.

已保存到 `llm-wiki/` 目录下：

- **`llm-wiki.md`** — Andrej Karpathy 的 LLM Wiki 原文（英文）
- **`llm-wiki.zh.md`** — 中文翻译版


## [07-18 12:51] user

hermes-agent（https://github.com/NousResearch/hermes-agent）是否有内置的 llm-wiki skill ？如有请帮我下载到本地。


## [07-18 12:51] assistant

The user wants to know if the hermes-agent project (https://github.com/NousResearch/hermes-agent) has a built-in llm-wiki skill, and if so, download it locally. Let me explore the repository.


## [07-18 12:51] assistant

I can see that the hermes-agent has a `skills/` directory, but I don't see a specific "llm-wiki" skill listed. The skill directories visible are:
- apple
- autonomous-ai-agents
- computer-use
- creative
- data-science
- dogfood
- email
- github
- hermes-desktop-plugins
- index-cache
- media
- mlops
- note-taking
- productivity
- research
- smart-home
- social-media
- software-development
- yuanbao

No "llm-wiki" skill. Let me also check the `optional-skills/` directory and search more broadly.


## [07-18 12:51] assistant

Yes! Hermes-agent has a built-in llm-wiki skill at `skills/research/llm-wiki/`. It includes a `SKILL.md` file. Let me fetch the SKILL.md file content.


## [07-18 12:51] assistant

I have the full SKILL.md content. Now let me save it to the local directory.

最棒了！Hermes Agent **确实内置了 llm-wiki skill**，位于 `skills/research/llm-wiki/SKILL.md`（v2.1.0）。正在下载到本地：


## [07-18 12:52] assistant

Done. Let me verify the final state of the directory and summarize.


## [07-18 12:52] assistant

Yes, Hermes-agent does have a built-in llm-wiki skill. It's located at `skills/research/llm-wiki/SKILL.md`. I've downloaded it. Let me verify there's an `.obsidian` directory too.

已完成。Hermes Agent **确实内置了 llm-wiki skill**（位于 `skills/research/llm-wiki/`，v2.1.0），已下载到本地：

```
llm-wiki/
├── llm-wiki.md        # Karpathy 原文（英文）
├── llm-wiki.zh.md     # Karpathy 原文（中文翻译）
├── SKILL.md           # Hermes Agent 内置的 llm-wiki skill（v2.1.0）
└── .obsidian/         # Obsidian vault 配置
```

`SKILL.md`（507 行）是 Hermes Agent 团队基于 Karpathy 模式实现的完整技能定义，包含三层架构、三阶段操作（Ingest/Query/Lint）、SCHEMA 模板、Obsidian 集成、lint 检查清单、批量摄取、归档流程等。


## [07-18 12:56] user

请将SKILL.md翻译成中文版


## [07-18 12:56] assistant

The user wants me to translate SKILL.md into Chinese. I'll create a `SKILL.zh.md` file.


## [07-18 12:56] assistant

Done. Let me confirm the directory listing.


## [07-18 12:56] assistant

Done. All files are in place.

已完成。`SKILL.zh.md` 已保存到 `llm-wiki/` 目录下。

当前目录文件：
```
llm-wiki/
├── llm-wiki.md        # Karpathy 原文（英文）
├── llm-wiki.zh.md     # Karpathy 原文（中文翻译）
├── SKILL.md           # Hermes Agent llm-wiki skill（英文原版）
└── SKILL.zh.md        # Hermes Agent llm-wiki skill（中文翻译）
```


## [07-18 18:08] user

给我介绍一下openwiki：https://github.com/langchain-ai/openwiki


## [07-18 18:08] assistant

The user is asking about openwiki at https://github.com/langchain-ai/openwiki. Let me fetch this repository to learn about it.


## [07-18 18:08] assistant

I have a good overview of OpenWiki. Let me also check the skills directory briefly to see if there's anything relevant, and maybe get a bit more detail on the architecture. Actually, I have enough information to give the user a good introduction. Let me summarize it in Chinese.

Key facts about OpenWiki:
1. It's a CLI tool by LangChain (langchain-ai org)
2. Writes and maintains "agent wikis" for codebases or personal memory
3. Two modes:
   - **Code mode**: builds repository documentation in `openwiki/` for the current codebase
   - **Personal mode**: builds a local personal brain wiki in `~/.openwiki/wiki` from configured sources (local repos, Gmail, Notion, Web Search, Hacker News, X/Twitter)
4. Installation: `npm install -g openwiki`
5. Commands: `openwiki --init`, `openwiki --update`, `openwiki personal --init`, `openwiki personal --update`, `openwiki auth <provider>`
6. Emits Google Open Knowledge Format (OKF) v0.1 bundles
7. Local connectors: git-repo, x, notion, google (Gmail), web-search (Tavily), hackernews
8. Multiple inference providers: OpenAI, OpenRouter, Gemini, Gemini Enterprise, Nebius, Fireworks, Baseten, NVIDIA NIM, OpenAI-compatible, AWS Bedrock, Anthropic, ChatGPT login
9. CI integration: GitHub Actions, GitLab CI, Bitbucket Pipelines — auto PR with docs updates
10. Maintains AGENTS.md and CLAUDE.md at repo root with pointers to the wiki
11. Telemetry: anonymous, opt-out via OPENWIKI_TELEMETRY_DISABLED
12. 12.2k stars, 840 forks, TypeScript 87%
13. Latest release 0.2.0 (Jul 16, 2026)

Comparison to llm-wiki (Karpathy pattern):
- Both are about persistent markdown wikis maintained by agents
- OpenWiki is a concrete product/CLI by LangChain; Karpathy's llm-wiki is an abstract pattern
- OpenWiki code mode = codebase documentation; personal mode = personal knowledge base from connectors
- OpenWiki has built-in connectors (Gmail, Notion, X, etc.) — data ingestion is automated
- OpenWiki emits OKF format with index.md + log.md reserved documents (interestingly, the same index.md/log.md convention as Karpathy's pattern!)

That's a nice observation: OKF also uses index.md and log.md as reserved documents — same convention.

The user is Chinese-speaking, so respond in Chinese. Should be a concise but informative introduction. I don't need to fetch more pages — I have plenty. Let me structure:

1. 是什么 (what it is)
2. 两种模式
3. 核心用法/命令
4. 连接器
5. 模型提供商
6. OKF 格式 (and its relation to Karpathy's index.md/log.md convention)
7. CI 集成
8. 与 Karpathy llm-wiki 的关系/对比

Keep it reasonably concise.

## OpenWiki 简介

**OpenWiki** 是 LangChain 官方（`langchain-ai` 组织）开源的一个 CLI 工具，用 TypeScript 编写（12.2k star，MIT 协议，最新版 v0.2.0，2026-07-16 发布）。一句话概括：**它为你的代码库或个人知识源自动编写并持续维护一个 agent 可读的 Markdown wiki**。

### 两种模式

| 模式 | 命令 | 输出位置 | 用途 |
|---|---|---|---|
| **Code 模式**（默认） | `openwiki --init` / `--update` | 仓库根目录 `openwiki/` | 为当前代码库生成架构/模块文档 |
| **Personal 模式** | `openwiki personal --init` / `--update` | `~/.openwiki/wiki/` | 构建个人"第二大脑"，聚合多来源知识 |

### 工作方式

1. **安装**：`npm install -g openwiki`
2. **初始化**：`openwiki --init` 会引导你配置推理提供商、API key 和模型（默认 OpenAI `gpt-5.6-terra`）
3. **自动维护 AGENTS.md / CLAUDE.md**：每次 code 模式运行都会在仓库根部注入 `<!-- OPENWIKI:START -->` 块，引导你的编程 agent 先查 wiki 再找上下文——不会覆盖你自己的内容
4. **CI 集成**：提供 GitHub Actions / GitLab CI / Bitbucket Pipelines 模板，定时跑 `--update` 并自动提 PR 更新文档

### 内置连接器（Personal 模式的数据源）

- `git-repo`（本地仓库 manifest）
- `notion`（走官方托管 MCP，OAuth 授权）
- `google`（Gmail API，OAuth）
- `x`（X/Twitter API）
- `web-search`（Tavily，需 `TAVILY_API_KEY`）
- `hackernews`（免凭证）

同一连接器可配置多个实例（如两个不同主题的 web-search），原始数据落在 `~/.openwiki/connectors/<name>/raw/`，再由 agent 综合成 wiki。

### 模型支持

OpenAI（API key 或 **ChatGPT 账号 OAuth 登录**）、Anthropic、Gemini、Gemini Enterprise（Vertex AI）、AWS Bedrock、OpenRouter、Nebius、Fireworks、Baseten、NVIDIA NIM，以及任意 OpenAI 兼容端点（如 LiteLLM 网关）。

### 一个有趣的细节：OKF 格式

OpenWiki 输出的 wiki 遵循 **Google Open Knowledge Format (OKF) v0.1** 规范——其中 `index.md` 和 `log.md` 是保留文档，概念页带 YAML frontmatter（`type` 必填），页面间用标准 Markdown 链接表达关系。**这正是 Karpathy llm-wiki 模式里 index.md / log.md 的同一套约定**，可以看出该模式已被多家产品采纳。

### 与 Karpathy llm-wiki 的关系

| | Karpathy llm-wiki | OpenWiki |
|---|---|---|
| 性质 | 抽象设计模式（idea 文档） | 具体产品（npm CLI） |
| 维护者 | 你 + 你的任意 agent | OpenWiki 自己的 agent 循环 |
| 数据来源 | 手动喂给 agent | 内置连接器自动摄取 + 定时任务 |
| 适用面 | 任意领域（读书、研究、团队知识） | 主打代码库文档 + 个人信息聚合 |

如果你之前关注的 llm-wiki 是"方法论"，OpenWiki 可以看作 LangChain 把这套方法论产品化后的实现，尤其在**代码库文档自动化**这个场景做得更开箱即用。

需要我把它下载到本地，或者深入看它的某部分源码（比如 agent 循环、OKF 生成逻辑）吗？


## [07-18 18:44] user

介绍一下Google Open Knowledge Format (OKF) v0.1 规范


## [07-18 18:44] assistant

The user wants an introduction to Google Open Knowledge Format (OKF) v0.1 specification. Let me fetch the spec from the URL mentioned earlier: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md


## [07-18 18:44] assistant

I now have the full OKF v0.1 spec. Let me write a comprehensive introduction in Chinese. The spec is 451 lines, and I have all the key content. Let me structure the answer:

1. 是什么/背景
2. 设计原则（goals/non-goals）
3. 核心术语
4. Bundle 结构
5. Concept 文档（frontmatter + body）
6. 交叉链接
7. index.md / log.md
8. Citations
9. 合规性（conformance）
10. 版本控制
11. 与 Karpathy llm-wiki 的关系（呼应上下文）

I could also save the spec locally since the user seems to be collecting these documents. But the user only asked for an introduction. I'll offer to save it at the end. Actually, given the pattern of this conversation (saving things locally), I could proactively save the SPEC. But the instruction says "Never give the user more than what they want." The user asked for an introduction, so I'll introduce it and offer to save. Hmm, but the previous pattern suggests they like having things saved. Let me just introduce and ask if they want it saved/translated. Actually let me just present the introduction well.

## Google Open Knowledge Format (OKF) v0.1 规范介绍

OKF（Open Knowledge Format）是 Google Cloud 在其 **Knowledge Catalog**（原 Dataplex，AI 驱动的数据目录/元数据管理平台）项目下发布的一份开放规范草案，位于 `GoogleCloudPlatform/knowledge-catalog` 仓库的 `okf/SPEC.md`（约 450 行，Apache 2.0）。当前版本 **v0.1（Draft 草案状态）**。

### 一句话概括

> 用一个 **Markdown 文件目录 + YAML frontmatter** 来表示"知识"——即围绕数据和系统的元数据、上下文和经过整理的洞察。没有 schema 注册中心、没有中央权威机构、没有必需的工具链：**能 `cat` 就能读，能 `git clone` 就能分发**。

### 设计目标与非目标

| 目标 | 非目标 |
|---|---|
| 定义让"富化 agent"写入的统一格式 | 不定义固定的概念类型分类法 |
| 指导"消费 agent"如何读取和遍历 | 不规定存储/服务/查询基础设施 |
| 促进知识跨系统、跨组织交换 | 不取代 Avro/Protobuf/OpenAPI 等领域 schema（OKF 引用它们，不吞并它们） |
| 只标准化少量**必需**字段 | — |

四个核心属性：**人可读**（无需工具）、**agent 可解析**（无需专用 SDK）、**可 diff**（版本控制友好）、**可移植**（跨工具、跨组织、跨时间）。

### 核心术语

- **Knowledge Bundle（知识包）**：自包含的、层级化的知识文档集合，是分发单位
- **Concept（概念）**：知识的最小单元 = 一个 Markdown 文档，可描述实体资产（表、API）或抽象概念（指标、业务流程）
- **Concept ID**：文件在包内的相对路径去掉 `.md`，如 `tables/users.md` → `tables/users`
- **Frontmatter / Body / Link / Citation**：YAML 元数据块 / 正文 / 概念间的 Markdown 链接 / 指向外部来源的引用

### Bundle 结构

```
path/to/bundle/
├── index.md          # 可选。目录清单，用于渐进式披露
├── log.md            # 可选。变更历史
├── <concept>.md      # 根级概念
└── <子目录>/
    ├── index.md
    └── <concept>.md
```

分发形式：git 仓库（推荐，自带历史/归因/diff）、tar/zip 压缩包、或大仓库的子目录。

**保留文件名**只有两个：`index.md` 和 `log.md`（任何层级都有特殊含义，不得用作概念文档）——**这正是 Karpathy llm-wiki 里那套约定被正式规范化了**。

### Concept 文档 = Frontmatter + Body

**Frontmatter**（唯一必填字段是 `type`）：

```yaml
---
type: BigQuery Table              # 必填：概念类型，无中央注册表，消费者须容忍未知类型
title: Customer Orders            # 推荐：显示名（缺省可从文件名推导）
description: 每行一个已完成订单    # 推荐：一句话摘要，供索引/搜索摘要使用
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders  # 可选：底层资产的规范 URI
tags: [sales, orders, revenue]    # 可选：横向分类
timestamp: 2026-05-28T14:30:00Z   # 可选：最后有意义变更时间（ISO 8601）
# …允许任意生产者自定义扩展键
---
```

- 消费者**不得**因未知 type、未知字段、缺失可选字段而拒绝文档
- 消费者**应该**在往返处理时保留未知键

**Body**：标准 Markdown，推荐结构化（标题、列表、表格、代码块）优于纯散文。三个有约定含义的标题：

| 标题 | 用途 |
|---|---|
| `# Schema` | 资产的列/字段结构化描述 |
| `# Examples` | 具体使用示例（常为代码块） |
| `# Citations` | 支撑正文主张的外部来源（编号列表，置于文末） |

### 交叉链接

- **绝对链接（推荐）**：`/tables/customers.md`，相对 bundle 根解析——移动文件时稳定
- **相对链接**：`./other.md`
- 链接断言一种"关系"，关系类型由上下文散文表达（joins-with、depends-on 等），链接本身无类型
- **消费者必须容忍断链**——断链不算格式错误，可能只是"尚未写出的知识"

### index.md（索引文件）

- 可出现在任何目录，支持**渐进式披露**（先看有什么，再打开具体文档）
- 无 frontmatter（唯一例外：根 index.md 可声明 `okf_version: "0.1"`）
- 格式：分节标题 + `* [标题](相对路径) - 一句话描述` 列表
- 可由生产者自动生成，也可由消费者现场合成

### log.md（日志文件，可选）

- 按日期分组的扁平列表，**最新的在前**，日期必须是 `YYYY-MM-DD`
- 条目为散文，开头加粗词（`**Update**`、`**Creation**`、`**Deprecation**`）是惯例而非强制

### 合规性（Conformance）

一个 bundle 符合 OKF v0.1 只需满足 3 条：

1. 每个非保留 `.md` 文件含可解析的 YAML frontmatter
2. 每个 frontmatter 含非空 `type` 字段
3. 出现的 `index.md` / `log.md` 遵循 §6/§7 结构

其余全部是软指导。这种**宽容消费模型**是有意为之：让 bundle 在增长、重构、被 agent 部分生成的过程中始终保持可用。

### 版本规则

`<major>.<minor>`：minor = 向后兼容的新增（新可选字段、新约定标题）；major = 可能破坏性变更。

### 与 Karpathy llm-wiki / Hermes SKILL 的对照

规范自己也承认（§10），OKF 有意贴近三类既有实践：**LLM wiki 仓库**、**Obsidian/Notion 类个人知识工具**、**"metadata as code"**。OKF 的独特之处仅在于它被**正式规范化**了——固定了互操作所需的最小规则集。

对照你本地的几份文档：

| 概念 | Karpathy llm-wiki | Hermes SKILL.md | OKF v0.1 |
|---|---|---|---|
| 索引 | `index.md` | `index.md` | `index.md`（保留文件名） |
| 日志 | `log.md`，`## [日期] action \| 主题` | `log.md`，同格式 | `log.md`，`## 日期` + 加粗动作词 |
| 页面元数据 | 未规定 | 丰富 frontmatter（title/created/updated/type/tags/sources/confidence…） | 最小 frontmatter（仅 `type` 必填） |
| 交叉引用 | `[[wikilinks]]` | `[[wikilinks]]` | 标准 Markdown 链接（绝对 `/` 开头推荐） |
| 层级组织 | entities/concepts/… | entities/concepts/… | 任意目录，生产者优先 |

可以说：**OKF 是这套社区实践的最小公分母规范**——它不做 Obsidian wikilink、不做置信度标记，只保证"任何工具都能读、任何 agent 都能写"的底线互操作性。OpenWiki 选择输出 OKF，就是看中了这一点。

---

需要我把 `SPEC.md` 原文下载到本地（并出一份中文翻译）吗？


## [07-18 18:59] user

需要


## [07-18 19:00] assistant

The user wants me to download the SPEC.md and create a Chinese translation. I already fetched the spec content in the previous turn. Let me fetch the raw version to get clean markdown, then save both files.


## [07-18 19:00] assistant

Got the clean raw spec. Now saving the English original and the Chinese translation.


## [07-18 19:03] assistant

Both files saved successfully. Let me summarize for the user.

已完成。OKF 规范原文和中文翻译已保存到本地：

```
llm-wiki/
├── llm-wiki.md        # Karpathy LLM Wiki 原文（英文）
├── llm-wiki.zh.md     # Karpathy LLM Wiki（中文翻译）
├── SKILL.md           # Hermes Agent llm-wiki skill（英文原版）
├── SKILL.zh.md        # Hermes Agent llm-wiki skill（中文翻译）
├── okf-spec.md        # Google OKF v0.1 规范（英文原文）
└── okf-spec.zh.md     # Google OKF v0.1 规范（中文翻译）
```

翻译说明：
- **代码块内容保持英文原样**——规范中的示例 frontmatter、Markdown 示例、目录树等代码内容未翻译（它们是格式定义，翻译反而会失真），仅翻译了散文正文、表格和注释性说明
- 术语首次出现时中英对照，如"知识包（Knowledge Bundle）"、"概念（Concept）"、"渐进式披露（progressive disclosure）"
- RFC 2119 风格的关键字（MUST/SHOULD/MAY）按中文惯例译为"必须/应当/可以"


## [07-20 16:42] user

介绍一下llm-wiki-compiler：https://github.com/atomicstrata/llm-wiki-compiler


## [07-20 16:43] assistant

The user wants me to introduce llm-wiki-compiler from https://github.com/atomicstrata/llm-wiki-compiler. Let me fetch the repo page.


## [07-20 16:43] assistant

Let me now provide a summary of llm-wiki-compiler.

## llm-wiki-compiler 简介

**llm-wiki-compiler**（别名 `llmwiki`）是 [atomicstrata](https://github.com/atomicstrata)（即 [atomicmemory](https://github.com/atomicstrata/atomicmemory) 团队）开发的 [Karpathy LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)的一个**具体编译器实现**。当前 `v1.1.0`（TypeScript，98.5%，MIT，1.8k star）。

一句话：**源码进，wiki 出。** 两阶段 LLM 管线：先提取概念，再生成类型化页面。

### 五个项目的定位对比

| | Karpathy 原文 | Hermes Agent Skill | OpenWiki | llm-wiki-compiler | OKF v0.1 |
|---|---|---|---|---|---|
| **性质** | 抽象模式 | 内置技能（Agent 指导） | CLI（知识源→wiki） | **CLI/SDK 编译器**（raw→Page） | 数据交换规范 |
| **语言** | Markdown | Markdown | TypeScript (CLI) | **TypeScript (CLI+SDK+MCP)** | — |
| **输出** | 概念.md | 概念/实体/对比.md | OKF 格式 bundle | **类型化页面 + OKF** | 无实现 |
| **模式** | 手动喂给 agent | agent 自己执行 | 代码/个人两种 | **领域模板**（autosci/newsroom） | 仅格式定义 |
| **核心差异** | 一个主意 | 告诉 agent 怎么干 | 自动摄取多源 | **两阶段编译 + 生命周期 + 质量门** | 互操作标准 |

### llmwiki 的核心能力

**1. 两阶段编译器**
- 将原始来源（Markdown、PDF、图片、网页）编译为类型化、交叉引用、可追溯引用的 wiki 页面
- 增量编译：未变更的源不走 LLM
- 并行编译：概念提取和页面生成并发进行

**2. 可配置生命周期模板（CLP, v1.0 新特性）**
- 内置 `autosci`（学术研究）和 `newsroom`（编辑工作）两种领域模板
- 类型化实体（Paper/Idea/Experiment...）、定向关系、生命周期状态机
- 运行时门控：关系门、证据门、审批门由写入路径强制，不依赖 prompt 约定
- 工件：哈希锚定的内容寻址证据文件
- 连接器：内置 Crossref（学术引用自动导入）

**3. 质量模型**
- **审核门**：`compile --review` 将低置信度/矛盾/不合 schema 的页面自动挂起为候审候选人
- **新鲜度**：页面分 fresh/stale/orphaned/unverified，`llmwiki refresh --stale` 修复
- **Lint + Eval**：校验损坏链接、孤页、引用覆盖率、置信度分布
- **CI 门**：`llmwiki lint` 和 `llmwiki eval` 可设质量阈值，失败则阻断

**4. Agent 集成**
- **MCP 服务器**：`llmwiki serve --root <project>` 暴露 ingest/compile/query/lint/eval 等工具
- **TypeScript SDK**：`createWiki({ root })` 一行驱动整个管线
- **Context Pack**：`llmwiki context "task" --json` 构建混合检索（语义+BM25+图谱扩展）证据包

**5. OKF 输入输出**

本身就是 OKF 的生产者和消费者：
```
llmwiki export --target okf --out ./dist/okf   # 导出
llmwiki import --okf ./dist/okf --dry-run       # 导入（默认走审核队列）
```

### 安装与使用

```bash
npm install -g llm-wiki-compiler
export ANTHROPIC_API_KEY=sk-...

llmwiki quickstart ./notes.md   # 一步：摄入+编译+打开浏览器
llmwiki query "key ideas?"      # 问答
llmwiki view --open             # 本地只读浏览器
llmwiki serve --root .          # 启动 MCP 服务器
```

### 项目结构

```
sources/         原始材料
wiki/
  concepts/      编译页面
  queries/       保存的问答
  graph/         类型化关系和审计事件
  index.md       目录
.llmwiki/
  profile.json   领域合同
  config.json    审核策略
  state.json     源哈希与所有权
  candidates/    审核候审
  workflows/     工作流运行状态
  eval/          质量历史
artifacts/       哈希锚定工件
log.md           活动日志
```

> llmwiki 最与众不同的是它的**运行时门控体系**。Hermes SKILL 和 Karpathy 原文告诉你"应该做审核"，llmwiki 在代码层面强制了：不符合证据要求、不在生命周期状态机中的写入操作会直接失败。这是一个从"告诉 agent 怎么做"到"编译器替你保证这么做"的跃迁。


## [07-20 17:27] user

介绍一下https://github.com/nashsu/llm_wiki


## [07-20 17:27] assistant

The user wants me to introduce the GitHub project https://github.com/nashsu/llm_wiki. Let me fetch the repository page.


## [07-20 17:27] assistant

I now have a very detailed look at nashsu/llm_wiki. Let me write a concise but comprehensive introduction in Chinese. I'll highlight the key differentiators and then show the mapping against the other projects in this category.

## nashsu/llm_wiki 简介

**nashsu/llm_wiki**（作者 [nash_su](https://x.com/nash_su)）是 Karpathy LLM Wiki 模式**最完整的桌面端产品化实现**。14.9k star，GPL v3，752 commits，当前 v0.6.5（2026-07-20），TypeScript 71% + Rust 25%（Tauri v2 桌面壳）。

核心定位：**一个构建自身知识库的跨平台桌面应用。** 把文档丢进去，LLM 自动增量构建并维护一个结构化的互链 wiki。

### 一句话与同类项目的区别

| | nashsu/llm_wiki | Hermes Agent Skill | llm-wiki-compiler | OpenWiki |
|---|---|---|---|---|
| **形态** | **桌面 GUI 应用**（Tauri） | Agent 内置 skill | CLI + SDK + MCP | CLI |
| **交互** | 三栏 UI：文件树 + 聊天 + 预览 | 聊天对话 | 命令行 / 浏览器 viewer | 命令行 / 聊天 |
| **核心技术** | 两阶段 CoT 摄入 + **知识图谱** + **社区发现** | Agent 驱动的 ingest/query/lint | 两阶段 LLM 编译 + 生命周期门控 | 连接器自动摄取+OKF 输出 |
| **文档格式** | PDF/DOCX/PPTX/XLSX/EPUB/图片/音视频/网页 | 纯文本/Markdown | Markdown/PDF/图片/网页/会话 | 网页/邮件/Notion/代码仓库 |
| **安装方式** | 下载 dmg/msi/deb/AppImage | hermes 内置 | npm install -g | npm install -g |
| **图谱** | **有**：sigma.js 4 信号 + **Louvain** 聚类 + 洞察 | 无（靠 wikilink） | 依赖 graph 目录 + OKF | 无 |
| **审核** | 异步 Review 队列 | 在 schema 中描述 | 运行时门控强制 | 无 |

### 核心亮点

**1. 两阶段 CoT 摄入**（区别于单步）
- Step 1：LLM 读取源 → 结构化分析（提取实体/概念/矛盾）
- Step 2：LLM 基于分析 → 生成 wiki 页面
- SHA256 增量缓存 + 持久化摄入队列 + 崩溃恢复

**2. 知识图谱（这是它最独特的地方）**
- **4 信号相关模型**：直接链接(×3) + 来源重叠(×4) + Adamic-Adar(×1.5) + 类型亲和(×1.0)
- **Louvain 社区发现**：自动发现知识聚类，凝聚度评分
- **图谱洞察**：自动检测"意外关联"和"知识缺口"，点击可触发 Deep Research
- sigma.js + ForceAtlas2 力导向布局渲染，交互式探索

**3. 多格式文档解析**
PDF（内置 pdf-extract + 可选 MinerU Cloud/Local）、DOCX、PPTX、XLSX、EPUB/MOBI、图片、音视频、网页剪藏

**4. 向量搜索（可选）**
LanceDB 嵌入式向量数据库，任意 OpenAI 兼容端点，召回率 58.2% → 71.4%

**5. Deep Research**
图谱洞察中发现缺口 → LLM 生成多组搜索查询 → Tavily/SerpApi/SearXNG 搜索 → 结果合成 wiki 页面

**6. Chrome Web Clipper 扩展**
Manifest V3，Readability.js + Turndown.js，一键剪藏到指定项目，自动触发摄入

**7. Rust 后端聊天 Agent**
工具调用（wiki/图谱/网页/文件搜索/Shell），技能管理（SKILL.md），Mermaid 渲染，异步审核

**8. Purpose.md**
Karpathy 原文有 schema（怎么组织），nashsu 加了 purpose.md（**为什么存在**）——定义目标、关键问题、研究范围，LLM 每次摄入和查询时都读

### 技术栈

| 层 | 技术 |
|---|---|
| 桌面壳 | Tauri v2（Rust） |
| 前端 | React 19 + TypeScript + Vite |
| UI | shadcn/ui + Tailwind CSS v4 |
| 编辑器 | Milkdown（ProseMirror WYSIWYG） |
| 图谱 | sigma.js + graphology + ForceAtlas2 |
| 向量 | LanceDB（Rust，可选） |
| 搜索 | 分词搜索 + 图谱相关 + 可选向量 |
| i18n | 中/英双语 |
| LLM | OpenAI / Anthropic / Google / Ollama / 自定义 |

### 项目结构

```
my-wiki/
├── purpose.md        # 目标、关键问题、研究范围
├── schema.md         # 结构规则、页面类型
├── raw/sources/      # 上传文档（不可变）
├── wiki/
│   ├── index.md / log.md / overview.md
│   ├── entities/ concepts/ sources/
│   ├── queries/ synthesis/ comparisons/
├── .obsidian/        # Obsidian vault 配置
└── .llm-wiki/        # 应用配置、聊天历史、审核项
```

### 安装

- **预编译**：Releases 页面下载 `.dmg`（macOS） / `.msi`（Windows） / `.deb` / `.AppImage`（Linux）
- **源码**：`git clone` → `npm install` → `npm run tauri dev`
- **Chrome 扩展**：`extension/` 目录加载为未打包扩展

**总结：** 如果说 Karpathy 原文是模式文档，Hermes Skill 是告诉 agent 怎么做，llm-wiki-compiler 是 CLI/编译器，OpenWiki 是代码库文档工具——那么 **nashsu/llm_wiki 是面向普通用户（非开发者）的最完整的桌面端产品**，尤其在知识图谱可视化和多格式文档摄入上无人能及。


## [07-20 17:28] assistant

All the tasks the user asked for have been completed. Let me summarize what's been done in this session.

本次会话已完成所有任务，`llm-wiki/` 目录内容：

```
llm-wiki/
├── llm-wiki.md          # Karpathy LLM Wiki 原文
├── llm-wiki.zh.md       # --- 中文翻译
├── SKILL.md             # Hermes Agent llm-wiki skill（内置）
├── SKILL.zh.md          # --- 中文翻译
├── okf-spec.md          # Google OKF v0.1 规范
├── okf-spec.zh.md       # --- 中文翻译
└── .obsidian/           # Obsidian vault 配置
```

涉及 5 个项目/规范的介绍和关系梳理：
- **Karpathy llm-wiki.md**（抽象模式，Gist）
- **Hermes Agent SKILL.md**（Agent 内置技能，Nous Research）
- **OpenWiki**（LangChain CLI，代码库文档）
- **OKF v0.1**（Google 开放知识格式标准）
- **llm-wiki-compiler**（atomicstrata CLI/SDK 编译器）
- **nashsu/llm_wiki**（14.9k star 桌面应用，最完善的产品化实现）


## [07-20 17:35] user

介绍一下https://github.com/tobi/qmd


## [07-20 17:35] assistant

The user wants me to introduce qmd from https://github.com/tobi/qmd.


## [07-20 17:35] assistant

I got a very detailed view of qmd. Let me now provide a concise but comprehensive introduction in Chinese. I have all the info I need - the architecture, features, usage patterns, and how it fits into the LLM wiki ecosystem.

## qmd 简介

**qmd**（Query Markup Documents）是作者 [tobi](https://github.com/tobi) 开发的一款**全本地 Markdown 搜索引擎**，28.1k star，TypeScript 实现（Bun/Node.js），MIT 协议。

Karpathy 在 llm-wiki.md 里提到它作为"wiki 规模扩大后的可选搜索方案"——它就是那个方案。

### 一句话

> 给你的笔记、文档、知识库上一套**混合搜索引擎**，BM25 关键词 + 向量语义 + LLM 重排序，全设备端运行，还能以 CLI/MCP/SDK 三种方式给你的 AI Agent 用。

### 安装

```bash
npm install -g @tobilu/qmd
```

### 核心流程

```bash
qmd collection add ~/notes --name notes      # 1. 添加集合
qmd context add qmd://notes "个人笔记和想法"    # 2. 添加上下文（关键特性）
qmd embed                                      # 3. 生成向量嵌入
qmd query "部署流程"                            # 4. 混合搜索（最佳质量）
```

### 搜索管线架构

```
用户查询 → 查询扩展(fine-tuned LLM) + 原查询(×2权重)
         ↓
   原查询 FTS5 + 向量  │  扩展1 FTS5 + 向量  │  扩展2 FTS5 + 向量
         ↓
         RRF 融合 + Top-Rank Bonus + Top 30 候选
         ↓
         LLM 重排序 (qwen3-reranker, 本地 GGUF)
         ↓
         位置感知混合 (前3名 75%检索+25%重排, 后续递增重排比重)
```

**三个本地 GGUF 模型（首用自动下载到 `~/.cache/qmd/models/`）：**

| 模型 | 用途 | 大小 |
|---|---|---|
| `embeddinggemma-300M-Q8_0` | 向量嵌入 | ~300MB |
| `qwen3-reranker-0.6b-q8_0` | 重排序 | ~640MB |
| `qmd-query-expansion-1.7B-q4_k_m` | 查询扩展（微调） | ~1.1GB |

支持 `QMD_EMBED_MODEL` 环境变量切换嵌入模型（如 Qwen3-Embedding 提升中日韩多语言效果）。

### Score 融合策略

- **RRF**（Reciprocal Rank Fusion）：`score = Σ(1/(k+rank+1))`，k=60
- **Top-Rank Bonus**：#1 +0.05，#2-3 +0.02
- **位置感知混合**：RRF 前 3 名给重排序 25% 权重，11+ 名给 60% 权重，防止重排序淹没精确匹配

### 三种搜索模式

| 命令 | 模式 | 精度 | 速度 |
|---|---|---|---|
| `qmd search` | BM25 全文检索（FTS5） | ★★☆ | 最快 |
| `qmd vsearch` | 向量语义搜索 | ★★★ | 中等 |
| `qmd query` | 混合：查询扩展 + FTS + 向量 + RRF + 重排序 | ★★★★★ | 最慢但最佳 |

### Agent 集成

**CLI 方式**（最简单）：告诉 Agent 直接 shell 调用 `qmd search --json` / `qmd query --json`

**MCP 服务器**（推荐）：`qmd mcp` 启动，暴露 `query`、`get`、`multi_get`、`status` 四个工具，还支持 HTTP 传输（localhost:8181）

```json
{
  "mcpServers": { "qmd": { "command": "qmd", "args": ["mcp"] } }
}
```

Claude Code 还有专用插件：`claude plugin marketplace add tobi/qmd`

**SDK 库方式**：

```ts
import { createStore } from '@tobilu/qmd'
const store = await createStore({ dbPath: './index.sqlite', config: { ... } })
const results = await store.search({ query: "认证流程", explain: true })
```

### 关键特性

- **Context 系统**——给集合/路径加描述性元数据（`qmd context add qmd://notes "想法和笔记"`），搜索时作为上下文返回，帮助 LLM 判断文档相关性。这是 qmd 区别于普通搜索引擎的核心差异
- **AST 感知分块**（`--chunk-strategy auto`）——用 tree-sitter 以函数/类/导入边界分块代码文件，非简单按文本位置截断
- **编辑器超链接**——TTY 下结果路径为可点击的超链接（支持 VS Code、Cursor、Zed、Sublime 等）
- **`--explain`** 逐条打分分解：显示 FTS 原始分、向量原始分、每个子查询的 RRF 贡献、重排序得分
- **`qmd bench`** 基准测试：用查询-期望文档的 fixture 对比四种后端（bm25 / vector / hybrid / full）的 precision@k / recall / MRR / F1
- **项目本地索引**：`qmd init` 在 `.qmd/index.yml` 创建项目级配置，索引和配置都在项目内

### 在 LLM Wiki 生态中的位置

Karpathy 原文中推荐 qmd 作为 wiki 规模扩大后的搜索方案。回顾整体生态：

| | qmd | nashsu/llm_wiki | llm-wiki-compiler |
|---|---|---|---|
| **角色** | **搜索引擎** | 完整桌面 wiki 应用 | CLI/SDK 编译器 |
| **搜索能力** | 混合 BM25+向量+重排序，顶级 | 内置分词+向量+图谱 | 语义+BM25+图谱扩展 |
| **用途** | 任何 Markdown 目录的即插即用搜索 | 全生命周期知识管理 | 原始来源→wiki 页面编译 |
| **定位** | 通用搜索基础设施 | 端到端桌面产品 | 编译器管线 |

qmd 可以被 `llm-wiki-compiler` 用作其混合检索后端，也可以被 `nashsu/llm_wiki` 替代其内置搜索——但在仅需要**给已有 Markdown 文件夹加搜索能力**的场景下，qmd 是最轻量的选择。


## [07-20 17:38] user

介绍一下graphify和codegraph


## [07-20 17:38] assistant

The user wants me to introduce "graphify" and "codegraph". Let me search for both to understand what they are.

graphify - probably a tool related to knowledge graphs
codegraph - this might be the CodeGraph MCP tool that was mentioned in the AGENTS.md at the start of our conversation

Let me search for both.


## [07-20 17:38] assistant

Now I have both. Let me organize the information:

**Graphify** (Graphify-Labs/graphify):
- By Safi Shamsi, YC S26, MIT license
- Multi-modal knowledge graph builder for AI coding assistants
- Parses code (36 languages via tree-sitter) + docs + PDFs + images + videos
- Outputs: graph.html (interactive), GRAPH_REPORT.md, graph.json
- Every edge tagged EXTRACTED/INFERRED/AMBIGUOUS
- Zero embedding clustering (Leiden algorithm on graph topology)
- CLI: `uv tool install graphifyy` → `graphify install` → `/graphify .`
- Token compression: 71.5x on mixed Karpathy corpus
- MCP server, wiki export, auto-sync, git hooks
- ~90k+ GitHub stars, 3.2M+ PyPI downloads
- Supports 17+ AI coding assistants

**CodeGraph** (colbymchenry/codegraph):
- By Colby McHenry, ~60k stars, MIT, 742 commits
- Pre-indexed code knowledge graph for AI coding agents
- Local-first, auto-syncs on file changes (native OS events)
- Used in the AGENTS.md at the start of this session as well (referred to as MCP tool)
- CLI: `npx @colbymchenry/codegraph` or install script
- MCP server for Claude Code, Codex, Cursor, OpenCode, Hermes, Gemini, etc.
- Features: surgical context, impact analysis, full-text search (FTS5), framework-aware routes
- Results: ~58% fewer tool calls, ~16% cheaper
- 20+ languages via tree-sitter
- Can also be used via npm: `npx @colbymchenry/codegraph`

Let me present this clearly side by side and also relate it to the ecosystem we've been discussing.

## Graphify vs CodeGraph

当前 AI 编码辅助领域最火的两个代码知识图谱工具，定位相似但实现思路不同。

---

### Graphify（`graphifyy`）

| 项目 |  |
|---|---|
| 作者 | Graphify Labs / Safi Shamsi（YC S26） |
| 仓库 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) |
| 语言 | Python |
| 安装 | `uv tool install graphifyy` |
| 数据 | 代码(36语言) + 文档/PDF/图片/音视频 → **多模态图谱** |
| 图谱引擎 | NetworkX + Leiden 社区发现（**零嵌入聚类**，无向量库） |
| 边置信度 | 每条关系标记 `EXTRACTED` / `INFERRED` / `AMBIGUOUS` |
| 输出 | `graph.html` + `GRAPH_REPORT.md` + `graph.json` |
| Token 压缩 | 实测 71.5×（Karpathy 仓库+论文+图片混合语料） |
| 集成 | 17+ AI 编码助手（优先 hook 方式） |
| 核心差异 | **多模态**（代码+论文+图片+视频入同一图谱）、**诚实置信度**、**Leiden 零向量聚类** |

核心工作流：

```bash
uv tool install graphifyy    # 安装（PyPI 包名用双 y）
graphify install             # 注册到你的 AI coding assistant
# 然后在聊天中：
/graphify .                  # 构建当前项目知识图谱
graphify query "谁负责支付模块？"  # 查询
graphify path "UserService" "DatabasePool"  # 路径分析
```

特色功能：
- **`--wiki`**：每个社区/神节点生成 Wikipedia 风格 Markdown 文章 + `index.md`，任何 agent 可直接浏览
- **`--watch`**：文件保存自动增量重建（代码改动用纯 AST，文档变更通知你跑 `--update`）
- **`graphify hook install`**：post-commit / post-checkout git hook，每次提交/切换分支自动重建图谱
- **`graphify export obsidian`**：导出为 Obsidian vault
- **MCP server**：`python -m graphify.serve`，10 个 MCP 工具

---

### CodeGraph（`@colbymchenry/codegraph`）

| 项目 |  |
|---|---|
| 作者 | Colby McHenry |
| 仓库 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) |
| 语言 | TypeScript（自打包运行时，无需 Node） |
| 安装 | `npx @colbymchenry/codegraph` 或一键安装脚本 |
| 数据 | **纯代码**（20+ 语言，tree-sitter AST） |
| 图谱引擎 | SQLite FTS5 + 自定义符号解析 + MCP |
| 索引方式 | 文件监听自动同步（FSEvents/inotify/ReadDirectoryChangesW） |
| 输出 | `.codegraph/` 目录（二进制索引 + SQLite 图） |
| Token 压缩 | ~58% 工具调用减少，~16% 成本降低（实测报告） |
| 集成 | Claude Code / Cursor / Codex / OpenCode / Hermes / Gemini / Antigravity / Kiro |
| 核心差异 | **专精代码**、**文件监听自动同步**、**框架路由感知**（14 主流框架） |

核心工作流：

```bash
# 安装（免 Node）
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh

codegraph install        # 自动配置 agent
codegraph init .         # 构建当前项目索引
# Agent 后续会自动调用 MCP 工具来查询图谱
```

特色功能：
- **Auto-sync**（默认开启）：原生 OS 文件事件监听 + debounce，代码修改后图谱自动更新，**永远不 stale**
- **Impact Analysis**：`codegraph explore "<symbol>"`，任何符号的调用链、影响半径一次查出
- **Framework-aware Routes**：识别 Express、Next.js、Django 等 14 个框架的路由模式，URL 模式直接关联到处理器代码
- **Surgical Context**：一次 MCP 调用返回入口点 + 相关符号 + 代码片段，无需逐文件探索
- **`codegraph uninstall`**：一键清除所有 agent 配置 + CLI 自身

---

### 对比总览

| 维度 | Graphify | CodeGraph |
|---|---|---|
| **核心能力** | 多模态 → 统一图谱 | 纯代码 → 精确符号图 |
| **聚类** | Leiden 零向量聚类 | 无聚类（专注符号定位） |
| **边置信度** | ✅ EXTRACTED/INFERRED/AMBIGUOUS | ❌ 无（AST 确定性的） |
| **多模态** | ✅ 代码+文档+PDF+图片+视频 | ❌ 仅代码 |
| **文件监听** | `--watch` 或 git hook | 内置自动监听（默认） |
| **框架路由** | ❌ | ✅ 14 框架原生识别 |
| **Token 压缩** | 71.5× | ~58% 工具调用减少 |
| **安装方式** | Python（uv/pipx） | 自包含二进制 / npx |
| **Wiki 导出** | ✅ `--wiki` / `export obsidian` | ❌ |
| **MCP** | ✅ | ✅ |
| **Star** | ~90k+ | ~60k |

### 在本会话生态中的位置

```
知识管理/搜索层：  qmd（通用搜索引擎）
知识编译层：       llm-wiki-compiler → nashsu/llm_wiki（桌面产品）
代码知识图谱层：   Graphify（多模态） ↔ CodeGraph（纯代码）
格式标准：         OKF v0.1（交换规范）
技能指导：         Hermes Agent SKILL.md → Karpathy 原文
```

如果你关注**代码之外的知识**（论文、图片、视频），Graphify 是唯一支持多模态的。如果你专注**纯代码场景**且希望**零维护自动同步**，CodeGraph 更合适。


## [07-20 17:49] user

AST 是什么？


## [07-20 17:49] assistant

The user is asking a simple definition question about AST (Abstract Syntax Tree) - what is it. This is a basic computer science concept. I should give a concise, clear explanation.

**AST**（Abstract Syntax Tree，抽象语法树）是源代码的**结构化树状表示**。

编译器/解析器读取源码时，不会把它当字符串处理，而是解析为 AST——每个节点是一个语法元素。比如：

```python
result = a + b * 2
```

的 AST 大概是：

```
        =
      /   \
result     +
          / \
         a   *
            / \
           b   2
```

**为什么这里相关？** 本会话中提到的所有代码知识图谱工具（Graphify、CodeGraph）都用 **tree-sitter** 解析你的代码→生成 AST→从中提取符号、调用关系、继承链等，然后构建知识图谱。这个过程：

1. **确定性的**：AST 解析不调用 LLM，纯算法
2. **无歧义的**：不像向量嵌入那样有语义模糊
3. **全本地的**：tree-sitter 是一个 C 库，纯设备端运行

这就是 Graphify 和 CodeGraph 能声称"代码分析完全在本地、无需 LLM、零隐私风险"的原因——它们分析的原材料是 AST，不是源码文本。


## [07-20 19:17] user

总结本会话的研究成果，回答这些工具到底在解决什么问题？为什么需要它？


## [07-20 19:18] assistant

The user wants me to summarize the entire conversation's research findings, answering what problems these tools solve and why they're needed. Let me synthesize everything we've discussed.

Let me trace back through the conversation:

1. Karpathy's LLM Wiki - the original pattern
2. Hermes Agent llm-wiki SKILL.md
3. OpenWiki (langchain-ai)
4. Google OKF v0.1 spec
5. llm-wiki-compiler (atomicstrata)
6. nashsu/llm_wiki (desktop app)
7. qmd (search engine)
8. Graphify and CodeGraph (code knowledge graphs)

The core problem they all address: how to make knowledge (both code and general knowledge) persistent, queryable, and structured for both humans and AI agents, rather than having agents rediscover it every time.

Let me write a clear, structured summary.


## [07-20 19:19] assistant

Now let me write the summary.

## 总结：这些工具到底在解决什么问题？

本会话研究的所有工具，都在回答同一个核心问题：

> **当 AI Agent 每次会话都从零开始"发现"知识时，如何让它像人类一样拥有持久、结构化、可积累的记忆？**

### 一、根本矛盾：RAG 的缺陷

传统 RAG 的工作方式是——你有一堆文档，每次提问时 LLM 检索相关片段、现场拼凑答案。表面上它能回答问题，但存在三个致命问题：

1. **没有积累**：同一个知识，问 100 次就推导 100 次，token 浪费、答案不一致
2. **没有结构**：拿到的是碎片片段，不是经过整理的实体、概念和关系
3. **没有持续**：知识在会话结束后消失，下次来又是陌生人

Karpathy 在 2026 年 4 月写下 `llm-wiki.md`，就是抓住了这个矛盾：**"NotebookLM、ChatGPT file uploads 和大多数 RAG 系统都是这样工作的——每次从头重新发现知识，没有积累。"**

### 二、解决方案：三层知识编译模式

所有工具的共同架构——Karpathy 称之为 **"三层架构"**：

```
原始来源（Raw Sources）    ← 不可变的原材料
     ↓
Wiki（编译知识）           ← LLM 生成的结构化、互链页面
     ↓
Schema（模式）             ← 规则、约定、领域定义
```

以及三个核心操作：

- **Ingest**（摄取）：新知识进入 → 更新相关页面
- **Query**（查询）：在编译后的知识上问答
- **Lint**（检查）：健康检查、矛盾检测、过期清理

### 三、解决了什么价值？为什么需要它？

| 问题 | 传统做法 | LLM Wiki 方案 |
|---|---|---|
| 知识不积累 | 每次重复检索 | 编译一次，持续更新 |
| 知识无结构 | 碎片片段 | 实体页、概念页、对比页，相互链接 |
| 会话遗忘 | 关掉聊天窗口就丢失 | 存储在 Markdown 文件中，跨会话持久 |
| Agent 上下文爆炸 | 为找到答案需要读大量文件 | 精确命中相关页面，节省 50-70%+ token |
| 人类维护负担重 | 手工更新 Wiki/文档，没人愿意做 | LLM 自动维护，人类只管来源和提问 |

**核心洞察**：维护知识库最累的不是阅读或思考，而是**记账（bookkeeping）**——更新交叉引用、保持摘要最新、记录矛盾、保持一致性。人类放弃 wiki 是因为维护负担增长快于价值。**LLM 不会厌倦、不会忘记更新交叉引用、一次能操作 15 个文件。维护成本趋近于零。**

### 四、本会话涉及的所有工具概览

```
┌─────────────────────────────────────────────────────────────────────┐
│                      知识管理与代码智能生态                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  格式标准层                                                         │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  OKF v0.1 (Google)      ← 互操作的最小公分母格式             │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                         ↑ 所有工具实现/兼容                         │
│                                                                     │
│  知识编译层 —— 将原始材料编译为结构化知识                           │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐               │
│  │  Karpathy    │ │ nashsu/      │ │ llm-wiki-    │               │
│  │  llm-wiki.md │ │ llm_wiki     │ │ compiler     │               │
│  │  (抽象模式)   │ │ (桌面应用)    │ │ (CLI/SDK)    │               │
│  └──────────────┘ └──────────────┘ └──────────────┘               │
│                                         ↑                          │
│  技能/自动化层                              ↑  OpenWiki             │
│  ┌──────────────┐                          (LangChain, 代码库文档)  │
│  │ Hermes Agent │                                                 │
│  │ SKILL.md     │                                                 │
│  └──────────────┘                                                 │
│                                                                     │
│  搜索/检索层 —— 在编译后的知识上高效查询                           │
│  ┌──────────────────────────────────────────────┐                  │
│  │  qmd (tobi)                                 │                  │
│  │  混合 BM25 + 向量 + LLM 重排序，全本地       │                  │
│  └──────────────────────────────────────────────┘                  │
│                                                                     │
│  代码知识图谱层 —— 对源代码的"编译"                               │
│  ┌──────────────────────┐ ┌──────────────────────┐                │
│  │  Graphify            │ │  CodeGraph           │                │
│  │  多模态(代码+文档+图)  │ │  纯代码 (tree-sitter) │                │
│  │  71.5x token 压缩    │ │  58% 工具调用减少     │                │
│  └──────────────────────┘ └──────────────────────┘                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 五、一句话总结每个工具的角色

- **Karpathy llm-wiki.md**：提出"让 LLM 帮你维护持久 wiki"这个模式本身
- **Hermes Agent SKILL.md**：把这个模式编码为 Agent 可执行的技能指令
- **nashsu/llm_wiki**：给普通用户一个桌面 GUI 应用，拖入文档就自动建 wiki
- **llm-wiki-compiler**：CLI/SDK 编译器，带生命周期门控和质量引擎，适合工程化集成
- **OpenWiki**：LangChain 出品，专注代码库文档自动化 + 个人信息聚合
- **OKF v0.1**：Google 规范的开放格式，让这些工具产出的知识可以互操作
- **qmd**：给你的 Markdown wiki 加混合搜索，CLI/MCP/SDK 三形态
- **Graphify**：代码+文档+图片+视频 → 多模态知识图谱，给 agent 省 71.5x token
- **CodeGraph**：纯代码 AST → 精确符号图，自动文件监听，给 agent 省 58% 工具调用

所有这些工具的逻辑终点是一样的：**把"每次从头发现"变成"一次编译，持续复用"**——无论编译的是自然语言文档（LLM Wiki 家族）还是源代码（Graphify/CodeGraph），思路完全一致。


## [07-20 19:20] assistant

All tasks completed.

全部会话任务已完成。`llm-wiki/` 目录最终包含 6 个文件：

```
llm-wiki/
├── llm-wiki.md          # Karpathy 原文
├── llm-wiki.zh.md       # 中文翻译
├── SKILL.md             # Hermes Agent llm-wiki skill（英文）
├── SKILL.zh.md          # 中文翻译
├── okf-spec.md          # Google OKF v0.1 规范（英文）
├── okf-spec.zh.md       # 中文翻译
└── .obsidian/           # Obsidian vault 配置
```


## [07-20 20:40] user

如何接手同事离职后的遗留项目？需要用到这些工具吗？


## [07-20 20:41] assistant

The user is asking a practical question: how to take over a legacy project left by a departing colleague, and specifically whether these tools we've been studying would be useful for that scenario.

This is actually the perfect use case for several of the tools we studied. Let me think about this:

1. **CodeGraph / Graphify** - These are the most directly relevant. They build a code knowledge graph from the existing codebase, allowing you to understand the code structure, call graphs, dependency relationships without having to read every file manually.

2. **nashsu/llm_wiki** - If the departing colleague left behind any documentation, notes, or you can gather related materials, the desktop app can ingest them into a structured wiki for ongoing reference.

3. **qmd** - If there are existing markdown notes or documentation, qmd can provide fast hybrid search across them.

4. **Karpathy's LLM Wiki pattern / Hermes SKILL** - You can use this methodology to incrementally build understanding of the project as you explore it, filing what you learn into a persistent wiki.

The key insight is: when taking over a legacy project, the main bottleneck is **understanding the codebase** - what connects to what, what are the key modules, what's the architecture. Traditional approach is grep + read files one by one, burning days or weeks. These tools shift the cost by pre-indexing the code into a queryable graph.

Let me structure this as a practical guide covering:
- The standard problems when inheriting a legacy project
- Which tools help with which problem
- A concrete workflow using the tools

Let me write this in Chinese as the user has been using Chinese throughout.

接手离职同事的遗留项目，本质上是两个问题：**理解代码**（这是什么？谁调谁？哪里是关键？）和**持久化理解**（今天搞懂的东西，下周不能忘）。

这正是本会话研究的工具最擅长的场景。逐个看：

---

### 第一步：快速建立代码全局认知

**用 CodeGraph 或 Graphify 先跑一遍。**

这是接手项目最高回报的第一步。不要逐个文件读，直接构建知识图谱：

```bash
# CodeGraph（纯代码，推荐先用这个）
npx @colbymchenry/codegraph
codegraph init .
codegraph explore "认证模块是怎么工作的？"

# 或者 Graphify（如果还有遗留文档/架构图）
uv tool install graphifyy
graphify install
/graphify .
```

你会立刻得到：
- **神节点（god nodes）**：代码库里连接最多的核心模块在哪
- **调用关系**：谁调谁，数据怎么流
- **意外关联**：跨文件/跨模块但逻辑相关的代码
- **影响面分析**：改某个函数会波及哪些地方

传统做法是 grep + 逐个文件读，CodeGraph 实测减少 58% 的工具调用。这不是省 token，是省你的时间。

---

### 第二步：消化遗留文档

离职同事通常会留下一些文档——交接文档、设计文档、会议记录、README。

**用 nashsu/llm_wiki 摄入这些材料**，让它自动构建 wiki：

```
raw/sources/
├── handover-notes.md      # 交接文档
├── architecture.md         # 架构设计
├── meeting-notes/          # 会议记录
├── api-specs/              # API 文档
```

LLM 自动提取实体（模块、服务、数据库表）、概念（认证流程、计费逻辑）、交叉引用，生成一个你不必手动维护的知识库。每当你搞懂一个新模块，跟 Agent 聊一聊，它帮你更新 wiki——你今天理解的，明天不会忘。

---

### 第三步：建你自己的理解日志

**用 Karpathy 的 LLM Wiki 模式（或用 Hermes SKILL 驱动你的 Agent）**，把探索过程变成持久化的知识：

每当你研究一个模块：
1. **丢给 Agent**：读取相关源码文件
2. **讨论**：Agent 总结关键点，你纠正、补充
3. **归档**：Agent 写 wiki 页面 + 更新交叉引用 + 记日志

一个月后，当你已经搞懂了 50 个模块——每个模块的知识不是散落在你的聊天历史里，而是结构化的、互链的 wiki。

---

### 第四步：搜索复用

**qmd** 给整个 wiki 目录加混合搜索：

```bash
qmd collection add ~/wiki --name project-wiki
qmd embed
qmd query "支付超时的重试机制"
```

---

### 工具选型建议

| 你的情况 | 推荐工具 | 理由 |
|---|---|---|
| 纯代码，无人接手文档 | **CodeGraph** | 最快建立代码结构认知，自动同步 |
| 有遗留文档+设计图 | **Graphify** | 支持多模态，文档和代码入同一图谱 |
| 需要长期积累理解 | **nashsu/llm_wiki** 或 **LLM Wiki 模式 + Agent** | 每次搞懂的东西持久化，越积累越省力 |
| 已有 Markdown 笔记 | **qmd** | 纯搜索，最轻量 |
| 团队接手（多人协作） | **llm-wiki-compiler** | 有运行时门控，防止知识腐败 |

---

### 一句话

接手遗留项目的痛苦在于**重复理解**——同一段代码今天读了明天忘，别人搞懂的东西无法复用。这些工具的核心价值是把"每个接手者独自重新发现"变成"**一次编译，持续复用**"。代码图谱工具替你理解结构，LLM Wiki 替你记住理解。


## [07-20 20:49] user

介绍一下https://github.com/Fission-AI/OpenSpec


## [07-20 20:50] assistant

The user wants me to introduce a GitHub repository: https://github.com/Fission-AI/OpenSpec. Let me fetch it.


## [07-20 20:51] assistant

The user wants me to introduce OpenSpec from Fission-AI. I have a good amount of information from the README. Let me structure a concise introduction in Chinese, and relate it to the "接手离职同事项目" scenario since this is the context of our previous discussion.

Key facts:
- Fission-AI/OpenSpec, 61.7k stars, MIT, TypeScript
- "Spec-driven development (SDD) for AI coding assistants"
- Philosophy: fluid not rigid, iterative not waterfall, easy not complex, built for brownfield not just greenfield
- CLI: `npm install -g @fission-ai/openspec@latest` → `openspec init`
- Key workflow: `/opsx:explore` → `/opsx:propose` → `/opsx:apply` → `/opsx:archive`
- Changes get their own folder with proposal.md, specs/, design.md, tasks.md
- Specs are plain Markdown with requirements + scenarios
- Stores (beta): planning in a separate repo, cross-repo features
- 30+ AI assistants support
- vs GitHub Spec Kit (heavier), vs Kiro (locked in), vs nothing (vague prompts)
- The user is in the context of "接手离职同事项目", so I should relate it to that

## OpenSpec 简介

**OpenSpec**（Fission-AI，61.7k star，MIT，TypeScript CLI）是一个为 AI 编码助手设计的**规范驱动开发（SDD）框架**。核心理念：在写代码之前，人类和 AI 先在规范上达成一致。

### 一句话

> 用 `/opsx:propose "想法"` 让 AI 把你的需求变成结构化规范（提案→需求→设计→任务清单），你审核通过后 `/opsx:apply` 让 AI 按清单实现，`/opsx:archive` 归档。所有决策以 Markdown 文件形式留在仓库里，不散落在聊天历史中。

### 工作流四步

```
/opsx:explore                 → 不确定怎么做？AI 先读代码，跟你讨论方案
/opsx:propose "功能描述"        → 生成 openspec/changes/<name>/
                                   ├── proposal.md   为什么做
                                   ├── specs/        需求和场景（WHEN/THEN 格式）
                                   ├── design.md     技术方案
                                   └── tasks.md       实现清单
          ↓ 人类审核，对齐需求
/opsx:apply                   → AI 按 tasks.md 逐项实现
/opsx:archive                 → 归档到 archive/，规范更新，准备下一个功能
```

### 需求规范长什么样？

纯 Markdown，无特殊语法：

```markdown
## ADDED Requirements

### Requirement: Theme selection
The app SHALL let users switch between light and dark themes,
defaulting to the system preference.

#### Scenario: User toggles dark mode
- **WHEN** the user clicks the theme toggle
- **THEN** the app switches to dark mode and persists the choice
```

### 设计哲学

`fluid not rigid` · `iterative not waterfall` · `easy not complex` · **`built for brownfield not just greenfield`**（为既有项目而设计，不只是新项目）· `scalable from personal to enterprise`

### 与同类工具的对比

| | OpenSpec | GitHub Spec Kit | Kiro (AWS) |
|---|---|---|---|
| 重量 | 轻量，Markdown 驱动 | 重量级，Python 依赖，严格阶段门 | 中等 |
| 灵活性 | 随时改任何产物 | 刚性阶段门 | 锁定 Kiro IDE |
| 模型 | 任何 AI 编码助手 | — | 仅限 Claude |
| 适配 | 30+ 工具 | — | Kiro IDE 独占 |

### 对"接手离职项目"场景的意义

与本会话之前的结论完全一致——OpenSpec 解决的是**决策持久化**问题：

> 正常情况下，需求只存在于聊天历史中，关掉窗口就丢了。等下一个人（或明天的你）接手，不知道"为什么这么设计"、"尝试过哪些方案被否决了"。

OpenSpec 把**每个变更的决策链留在仓库里**：
- `proposal.md`：为什么做（动机、上下文）
- `design.md`：怎么做（技术选型、权衡）
- `specs/`：验收标准（什么才算做完）
- `tasks.md`：实现路径

这与 LLM Wiki 模式在底层逻辑上完全一致——**从"散落在聊天中的记忆"变成"持久化的知识"**。区别在于，LLM Wiki 编译的是**已有知识**（文档、论文、笔记），OpenSpec 记录的是**将要发生的决策**（需求、设计、任务）。

### 与本会话生态的关系

```
决策层（向前看）：
  OpenSpec  ←  在写代码之前，人类+AI 对齐规范

知识层（向后看）：
  LLM Wiki / OpenWiki / nashsu  ←  编译已有知识为持久 wiki

代码理解层（向内看）：
  CodeGraph / Graphify  ←  把代码变成可查询的知识图谱
```

三者互补：接手项目时，CodeGraph 帮你理解代码结构，LLM Wiki 帮你沉淀理解，OpenSpec 帮你留下未来每一次变更的完整决策链。


## [07-20 21:11] user

什么是spec？什么是wiki？在AI编程项目中，spec和wiki都需要吗？如果都需要，分别用来干什么？如何管理项目中的spec和wiki？


## [07-20 21:12] assistant

The user is asking a fundamental conceptual question about the difference between spec and wiki in the context of AI coding projects. This is a natural progression from our research - we've covered LLM Wiki (knowledge) and OpenSpec (specs), and now they want to understand the relationship between the two.

Let me give a clear, practical answer that ties everything together.

## Spec 与 Wiki 的区别

| | **Spec** | **Wiki** |
|---|---|---|
| **回答什么问题** | "我们要建什么？" | "已经建了什么？它怎么工作的？" |
| **时间方向** | 向前看（将要发生） | 向后看（已经存在） |
| **状态** | 描述**意图**——应该在但可能还没实现 | 描述**事实**——知识的当前状态 |
| **阅读者** | 实现者（接下来的开发者/Agent） | 理解者（问你"认证怎么走"的人/Agent） |
| **示例** | "用户 SHALL 能切换暗色主题" | "认证流程：JWT token 经过 AuthMiddleware → UserService.verify()" |
| **生命周期** | 实现→归档（写完代码后 spec 成为历史记录） | 持续更新（每次新知识进入都刷新） |

---

### 都需要吗？

**对个人项目**：Spec 可选的，Wiki 看规模。小项目你脑子里装着就够。

**对团队/长期项目/遗留项目**：两者都需要，因为解决的是不同的问题：

```
Spec 解决：  "三个人用三个 Agent 写同一个功能，每个人理解的需求为什么不一样？"
Wiki 解决：  "离职同事写的支付模块，为什么没人敢动？"
```

---

### 分别用来干什么

**Spec（规范）** 

你准备做一个变更时——先对着 Spec 聊，AI 帮你把模糊的想法变成结构化规格：

```
/opsx:propose add-refund-flow

openspec/changes/add-refund-flow/
├── proposal.md    → 为什么加退款流程（动机）
├── specs/         → 退款流程的需求和验收场景
├── design.md      → 技术方案：退款状态机、与支付模块的交互
└── tasks.md       → 实现清单
```

Spec 归档后，它就是一份**带动机、带方案、带验收标准的变更记录**。三年后有人问"退款为什么用了两阶段确认"，答案在 `design.md` 里。

**Wiki（知识库）** 

你把文档、论文、架构图、会议记录摄入 Wiki，LLM 帮你维持实体页、概念页、交叉引用。Wiki 回答的是：系统里有什么、它们怎么关联、当前状态是什么。

```
wiki/
├── entities/
│   ├── payment-service.md       → 支付服务：端口、依赖、负责人
│   └── order-state-machine.md   → 订单状态机
├── concepts/
│   └── refund-flow.md           → 退款流程：两阶段确认的原因
├── comparisons/
│   └── payment-providers.md     → 支付宝 vs 微信 vs Stripe
└── index.md                     → 所有页面的目录
```

---

### 如何管理项目中的 Spec 和 Wiki

一张图：

```
项目根目录/
├── openspec/           ← Spec 层（OpenSpec 管理）
│   ├── specs/          ← 当前有效的系统规范（"应该是什么"）
│   ├── changes/        ← 进行中的变更提案
│   └── changes/archive/← 已完成变更的历史记录
│
├── wiki/               ← Wiki 层（LLM Wiki 模式管理）
│   ├── entities/       ← 系统中有哪些实体
│   ├── concepts/       ← 核心概念怎么运作
│   ├── raw/sources/    ← 原始文档（不可变的输入材料）
│   ├── index.md        ← 目录
│   └── log.md          ← 操作日志
│
├── .codegraph/         ← 代码图谱层（CodeGraph 管理）
│                       ← AST 提取的符号关系图
│
└── src/                ← 源代码（唯一的真实实现）
```

---

### 三层的协作关系

```
你要改一个旧模块 ──→ CodeGraph 告诉你：
                      "这个模块被 12 个地方调用，改了会影响 A/B/C"
                   ↓
你要理解这个模块 ──→ Wiki 告诉你：
                      "支付模块用了两阶段确认，因为 2025 年 3 月出了一次重复扣款事故"
                   ↓
你要加新功能   ──→ Spec 帮你：
                      "/opsx:propose —— 先对齐需求，再生成设计文档和任务清单"
                   ↓
你改完了       ──→ 留下什么：
                      Spec (archive) —— 这个变更为什么做、怎么做、验收标准
                      Wiki (更新)   —— 支付模块现在支持退款了
                      CodeGraph    —— 文件监听自动更新，图谱永远是最新的
```

---

### 一句话总结

- **Spec** 是"我们要建什么"——在代码之前对齐意图，实现后成为可审计的变更记录
- **Wiki** 是"已建了什么、怎么运作"——把散落的理解编译成持久、可查询的知识
- **CodeGraph** 是"代码之间怎么关联"——让 Agent 不读文件就能定位符号和影响面

三者不互斥，解决的是同一件事的不同面：**让知识——无论是"意图"、"理解"还是"结构"——不随聊天窗口关闭而消失。**


## [07-20 21:20] user

在你的这个设计里面，我是不是可以这样理解：spec是wiki的原始文档？


## [07-20 21:20] assistant

The user is asking whether spec can be understood as the "raw source" (原始文档) for the wiki, similar to how in the LLM Wiki pattern, raw source documents are fed into the wiki and the LLM compiles them into structured knowledge pages.

This is a sharp question. Let me think about it carefully.

In the LLM Wiki pattern:
- Raw sources (immutable) → LLM reads them → generates wiki pages
- The spec (proposal.md, design.md, specs/) are akin to raw source material

So the user's intuition is: spec documents are a kind of raw source that can be fed into the wiki, and the wiki can extract entities, concepts, and relationships from them.

But there's a subtle difference:
1. Raw sources in LLM Wiki are "documents that already exist" - they describe what IS
2. Specs describe what SHOULD BE - they're prescriptive, not descriptive
3. Specs have a different lifecycle - once implemented, they become historical records

So the user is partially right - specs CAN be used as wiki raw sources, but they're a special kind of raw source with their own purpose.

The relationship is actually:
- Spec = raw source material that feeds into wiki ingestion (the "input")
- But spec also has independent value as a decision record / intent document

Let me answer this concisely.

不完全是。你的直觉很敏锐，但有一个关键区分：

### 类比是对的，但不全对

```
LLM Wiki 模式：  原始文档 → LLM 编译 → Wiki 页面
OpenSpec 模式：  Spec    → AI 实现  → 代码
```

Spec 的"源"是**需求意图**，它的"目标输出"是**代码**，不是 Wiki。Spec 描述的是"应该怎么样"，Wiki 描述的是"实际怎么样"。

### 更准确的模型

```
Spec        = 意图层  → 驱动实现，实现后归档为决策记录
原始文档    = 事实层  → 驱动理解，LLM 编译为 Wiki 页面
代码        = 实现层  → 唯一真实状态
Wiki        = 理解层  → 从代码+原始文档+Spec 存档中提取、综合的知识
```

### 但你的理解对一个场景完全成立

当 Spec 归档后成为 `archive/` 中的历史变更记录，**它确实可以作为 Wiki 的原始文档被摄入**：

```
openspec/changes/archive/
├── add-refund-flow/
│   ├── proposal.md    ← 喂给 LLM Wiki
│   ├── design.md      ← 提取"两阶段确认"概念、与支付模块的关系
│   └── specs/         ← 提取关键需求作为实体属性

                    ↓ Ingest

wiki/
├── concepts/refund-two-phase.md    ← 为什么用两阶段确认
├── entities/payment-service.md     ← 更新：现在支持退款
└── comparisons/refund-vs-void.md   ← 退款 vs 撤销的对比
```

区别在于：原始的 Spec 是**指令**（"SHALL 做到"），经过 Wiki 编译后变成**事实陈述**（"系统使用两阶段确认是因为…"）。语气从祈使句变成了陈述句。

### 一句话

Spec 不是 Wiki 的原始文档——但 **Spec 归档后的产物**可以也应该被 Wiki 摄入。Spec 是写给实现者的，Wiki 是写给后继者的。


## [07-20 22:34] user

开发同事准备离职，遗留项目后续还需维护和扩展。为了能无缝接手遗留项目，应如何交接？


## [07-20 22:35] assistant

The user is asking about how to handle a handover when a developer is leaving and their project needs to be maintained and extended. This is a practical application of all the tools we've been discussing. Let me synthesize everything we've covered into a concrete handover plan.

The key insight is: the entire ecosystem we've studied (Spec, Wiki, CodeGraph, etc.) naturally maps onto what a good handover should produce. Let me structure this as a practical action plan.

在你过去三个小时研究的所有工具，恰好构成一套完整的离职交接方案。不是巧合——这些工具就是在解决"知识怎么不随人走"这个问题。

## 离职交接方案（四步走）

### 第一步：代码结构快照（CodeGraph）

人走之前，先把代码结构冻结为可查询的知识图谱。

```bash
# 离职同事执行
npx @colbymchenry/codegraph
codegraph init .        # 构建整个代码库的符号关系图
codegraph explore .     # 验证：关键模块能查到
```

**产出**：`.codegraph/` 目录（二进制索引，git add 即可），后来者打开项目就能查——"支付回调入口在哪？""这个函数被谁调？"

### 第二步：Spec 补齐（OpenSpec）

这是最关键也最容易被忽略的一步。交接通常只交接代码，不交接**意图**。

让离职同事在最后一周，把记忆里的关键决策倒出来——格式不重要，重要的是**倒出来**：

```bash
# 不要写长篇文档，太慢。用 Agent 做速记
/opsx:propose "补充支付模块的状态机文档"
/opsx:propose "记录订单去重的竞态条件解决方案"
/opsx:propose "说明为什么退款没用异步而是同步"
```

**产出**：`openspec/` 下每个关键模块都有 `proposal.md`（为什么这么做）+ `design.md`（怎么做的），而不是一句"看代码"。

### 第三步：理解固化（LLM Wiki）

把已有的文档、Spec 归档、交接笔记统一喂给 LLM Wiki。

```
raw/sources/
├── handover-notes.md         # 离职同事写的随便什么格式的问题记录
├── project-requirements.md   # PRD
├── architecture-*.md         # 架构文档
├── incident-reports/         # 历史事故报告（最有价值）
├── meeting-notes/            # 关键决策会议记录
```

```bash
# 一次性批量摄入
# LLM 自动：提取实体页、概念页、交叉引用、矛盾标记
```

**产出**：`wiki/` 目录——模块文档、实体关系、核心流程图。跨模块的交叉引用已经建好了，不用后来者自己去 grep。

### 第四步：搜索就绪（qmd）

给 Wiki 加搜索，后来者不用在文件树里迷路。

```bash
qmd collection add wiki --name project-wiki
qmd embed
```

### 全部提交为 git

```
git add .
git commit -m "handover: codegraph + openspec + wiki + qmd index"

# 后来者 clone 完直接可用
```

---

## 一张图总结

```
离职前一周，离职同事做的事情：

第一天    CodeGraph init     → 代码图谱冻结
第二天    OpenSpec           → 把"为什么这么做"写成 Spec
第三天    Wiki 批量摄入      → 所有文档喂给 LLM Wiki
第四天    git commit         → 提交，交接完成
```

## 后来者的第一天

```
git clone 项目                   ← 包含所有交接产物
codegraph explore "支付模块"      ← 结构秒懂
qmd query "支付重复扣款怎么处理的"  ← 知识秒查
cat openspec/.../design.md       ← 设计决策秒读
cat wiki/concepts/payment-flow.md ← 完整理解秒获
```

之后你在 Wiki 中的每一次理解、修正、发现，都会被 LLM 维护——**你的理解不会随你走，也不会随前同事走。**

## 关键原则

> **代码是结果，决策是历史。只交接代码等于只交卷子不交草稿。**  
> **Spec 留下草稿（为什么这么答），Wiki 留下知识点（这道题考什么），CodeGraph 留下索引（知识点在哪页）。**


## [07-24 00:00] user

传统软件工程的文档包括：需求文档、设计文档（概要/详细设计）、测试文档（测试计划/用例/报告）、部署/运维文档、用户手册/帮助文档、API文档等。
搭建AI原生软件工程，传统软件工程的这些文档哪些应作为spec？哪些应作为wiki？


## [07-24 00:01] assistant

The user is asking a very insightful question: in an AI-native software engineering workflow (using the tools we've discussed - OpenSpec, LLM Wiki, CodeGraph), how should traditional software engineering documents be categorized between Spec and Wiki?

Let me think about this carefully:

Traditional docs:
1. 需求文档 (Requirements docs)
2. 设计文档 - 概要/详细设计 (Design docs - high-level/detailed)
3. 测试文档 - 计划/用例/报告 (Test docs - plan/cases/reports)
4. 部署/运维文档 (Deployment/ops docs)
5. 用户手册/帮助文档 (User manual/help docs)
6. API文档 (API docs)

The key distinction we established:
- **Spec** = forward-looking, describes intent ("what we SHOULD build"), drives implementation
- **Wiki** = backward-looking, describes fact ("what IS built and how it works"), drives understanding

Let me map each:

1. **需求文档** → **Spec** (mostly)
   - PRD, user stories, acceptance criteria → Spec (they describe intent before code exists)
   - But once implemented, the requirements become part of the system's "why" knowledge → can be ingested into Wiki as reference context

2. **设计文档** → **Both, split by nature**
   - Architecture decisions (why microservices? why PostgreSQL?) → Spec (decision records)
   - Technical approach for a specific feature → Spec (part of `/opsx:propose` → `design.md`)
   - Current system architecture diagram → Wiki (describes what IS)
   - Module interaction flows → Wiki

3. **测试文档** → **Neither exactly, but:**
   - Test plans → Spec? Actually... no. Test plans describe what WILL be tested, which is intent. But in AI-native dev, tests are generated alongside code. The test plan is more of a quality gate spec.
   - Test cases → Generated by agent as part of implementation
   - Test reports → Wiki (historical record of test results, bugs found)

Hmm, this is getting complex. Let me think more carefully about the fundamental split.

Actually, the core insight is simpler than I'm making it:

**Spec = anything that describes what SHOULD be (prescriptive, before code)**
**Wiki = anything that describes what IS (descriptive, after code)**

But there's a third category - things that are best **generated by tools, not manually documented**:
- API docs → generated from code (OpenAPI/Swagger)
- Code structure → CodeGraph (auto-indexed from AST)

Let me restructure:

**→ Spec (prescriptive, drives implementation):**
- 需求文档 (Requirements) - what to build
- 架构决策 (Architecture decisions) - why this approach
- 设计文档中"方案选型"的部分 (design tradeoffs)

**→ Wiki (descriptive, documents existing system):**
- 部署/运维文档 (Deployment/ops) - how it's deployed
- 用户手册 (User manual) - how to use it
- 历史事故报告 (Incident reports) - what happened
- 模块间的实际交互流程

**→ 代码即文档 (generated from code, doesn't need manual maintenance):**
- API文档 → OpenAPI/Swagger 自动生成
- 代码结构/调用关系 → CodeGraph 自动索引
- 详细设计中的类图/时序图 → 从代码反向生成

**→ Spec归档后成为Wiki素材:**
- 需求文档在实现后归档→Wiki可引用作为"为什么这么设计"的溯源
- 测试报告→Wiki中作为质量历史

Let me organize this into a clear answer.

好问题。传统文档的"去留"取决于一个根本区分：**这份文档是驱动实现的指令，还是描述已有系统的知识。**

---

## 按"Spec / Wiki / 自动生成 / 不需要"四类重新归类

| 传统文档 | 归入 | 理由 |
|---|---|---|
| **需求文档**（PRD、用户故事） | **Spec** | "要建什么"——这是 OpenSpec `proposal.md` + `specs/` 的原材料 |
| **概要设计**（架构决策、技术选型） | **Spec** | "为什么选这个方案"——OpenSpec `design.md` |
| **详细设计**（类图、时序图、接口定义） | **不写（自动生成）** | CodeGraph 从 AST 提取调用关系；API 用 OpenAPI/Swagger 从代码生成。AI 项目里详细设计文档是**人肉维护的低价值产物**——维护成本远超使用价值 |
| **API 文档** | **不写（自动生成）** | OpenAPI / gRPC proto 注解 → 生成文档站。手写 API 文档 = 注定过时的负债 |
| **测试计划** | **Spec** | 验收标准是需求的一部分，随 `specs/` 走 |
| **测试用例** | **不写（自动生成）** | Agent 实现功能时同时生成测试代码，测试即规格 |
| **测试报告** | **Wiki（定期摄入）** | 历史质量数据，供后来者了解"什么地方容易出问题" |
| **部署/运维文档** | **Wiki** | "怎么部署、怎么排查"是事实知识，LLM Wiki 维护 |
| **用户手册** | **Wiki** | 同上，使用者需要查的知识 |
| **事故报告** | **Wiki** | 最有价值的那类文档——"出现过什么问题、怎么修的" |

---

## 简化结论

```
Spec 中保留的（传统文档的子集）：
  ├── 需求文档（PRD、用户故事）          → proposal.md + specs/
  ├── 架构决策（为什么选这个方案）       → design.md
  └── 验收标准（怎么算做完）             → specs/ 中的 Scenario

Wiki 中保留的（传统文档的子集）：
  ├── 部署/运维文档                     → 跑在哪个集群、怎么扩缩容
  ├── 用户手册                          → 怎么用
  ├── 事故报告                          → 出过什么问题
  └── 所有 Spec 归档后的决策记录          → 作为"为什么这么设计"的溯源

自动生成（从代码中来，不需要人写）：
  ├── 详细设计（调用链、类关系）          → CodeGraph
  └── API 文档                          → OpenAPI / Swagger

不再需要（AI 原生工程中成为负债）：
  ├── 手写详细设计文档                   → 维护成本 > 使用价值
  └── 手写测试用例文档                   → 测试代码即文档
```

---

## 核心洞察

传统文档的最大问题是**维护成本**——写完就过时，越久越没人敢信。AI 原生工程的解决思路不是"用 AI 写更好的文档"，而是：

1. **Spec 成为约束而非文档**：需求不是"写到文档里就完了"，而是作为 Agent 实现的驱动力。Spec 错了 → 代码错了 → Agent 自己检测出不一致
2. **Wiki 让 LLM 维护**：部署文档、事故记录这种"会随时间变化的事实"，人类只负责提供新信息，LLM 负责更新交叉引用和保持一致性
3. **能自动生成的绝不手写**：API 文档、调用关系、类层次——代码本身就是权威来源，工具读取代码而非文档

**一句话：Spec 留下的是"未发生的事"，Wiki 留下的是"已发生的事"，代码留下的是"正在发生的事"。三者不重叠，各司其职。**


## [07-24 00:59] user

为了能无缝接手开发同事离职后的遗留项目，且后继者接手的是AI原生软件工程。应如何制定离职交接方案？


## [07-24 00:59] assistant

The user is asking me to synthesize everything we've discussed into a concrete, actionable handover plan for an AI-native software engineering project when a developer is leaving. 

Let me think about this carefully. We've covered:
1. LLM Wiki pattern (Karpathy) - knowledge compilation
2. Hermes Agent SKILL.md - skill instructions for agents
3. OpenWiki - codebase documentation
4. OKF v0.1 - knowledge exchange format
5. llm-wiki-compiler - knowledge compiler with lifecycle gates
6. nashsu/llm_wiki - desktop wiki application
7. qmd - search engine
8. Graphify / CodeGraph - code knowledge graphs
9. OpenSpec - spec-driven development
10. AST (Abstract Syntax Tree) basics

The user's scenario: A developer is leaving, and the successor should receive an AI-native software engineering project. The question is how to structure the handover.

The key insight is: in an AI-native project, the handover artifacts are designed for AGENTS to consume and maintain, not just humans. The successor + their AI agent should be able to start working immediately.

Let me think about what assets should be in place:

1. **Code Graph** (CodeGraph) - pre-built index so the successor's agent can understand the codebase structure immediately without reading files
2. **Spec Archive** (OpenSpec) - all historical decisions captured as archived specs
3. **Wiki** - compiled knowledge about the system (what exists, how it works, known issues)
4. **Search** (qmd) - hybrid search over the wiki
5. **AGENTS.md / CLAUDE.md** - entry point that tells the successor's agent how to use all of the above
6. **Skills** (Hermes-style SKILL.md) - domain-specific workflows

The plan should be:
- Phase 1 (before last day): Freeze and verify all artifacts
- Phase 2 (last 2-3 days): Knowledge transfer - spec completion + wiki compilation
- Phase 3 (last day): Verification - successor's agent can answer questions

Let me also think about what makes this "AI-native" vs traditional handover:
- Traditional: Word docs, emails, verbal walkthroughs, wiki that no one updates
- AI-native: CodeGraph index, Spec archive, Wiki compiled by LLM, search index, AGENTS.md entry point

The successor doesn't need to "learn" the codebase - their agent queries CodeGraph. They don't need to maintain wiki - LLM does it. They don't need to reverse-engineer decisions - they're in the spec archive.

## AI 原生工程的离职交接方案

传统交接的痛点："这是需求文档在那个文件夹，设计文档部分在这里部分在 Confluence，部署文档小王写了一半就走了…"——然后后来者面对一堆**过时的、零散的、互相矛盾的文档碎片**。

AI 原生交接的核心不同：**交接产物是给 Agent 读的，Agent 维护它。**

---

### 交接清单（按优先级排列）

离离职还有一周，按这个顺序做：

```
第 1-2 天：代码图谱冻结 + 质量门
第 3-4 天：决策补齐（Spec 归档）
第 5 天：  知识编译（Wiki 构建）
第 6 天：  搜索就绪 + 入口文件
第 7 天：  验证交接
```

---

### 第 1-2 天：代码图谱冻结

```bash
# 离职同事执行
npx @colbymchenry/codegraph
codegraph init .              # 构建全量索引
codegraph explore "核心流程"    # 验证：神节点、调用链、影响面能不能查到

# CI 门：确保图谱不 stale
# .github/workflows/codegraph-check.yml
# 如果图谱与最新代码不一致，PR 合并前告警
```

**产物**：`.codegraph/` 目录（git 追踪）。后来者的 Agent 第一次打开项目就能精确查询，不需要逐文件探索。

---

### 第 3-4 天：决策补齐

离职同事脑子里有、代码里没有的东西——**"为什么这么做"**。不要让他写长篇文档，用 Agent 速记：

```bash
# 离职同事口述，Agent 整理为 Spec
/opsx:propose "记录支付模块两阶段确认的设计决策"
/opsx:propose "记录订单去重的竞态条件及其解决方案"
/opsx:propose "记录为什么退款用同步而非异步"
/opsx:propose "记录计费精度用 decimal 而非 float 的原因"
```

**不是要求写完整的需求 Spec，而是用 Spec 的格式倒灌已有的决策**。

可以开一个 Batch Spec：

```
openspec/changes/handover-legacy/
├── proposal.md    → 本次交接覆盖了哪些模块、哪些已知风险
├── specs/
│   ├── payment-knowledge.md    → 支付模块的已知坑与设计约束
│   ├── order-knowledge.md      → 订单模块的边界条件
│   └── deployment-knowledge.md → 部署环境、配置项、监控指标
├── design.md      → 遗留架构的整体视图（哪部分是稳定的，哪部分需要重构）
└── tasks.md       → 后继者应该处理的技术债务清单（优先级排序）
```

然后**归档**：

```bash
/opsx:archive   # 进入 openspec/changes/archive/，成为永久决策记录
```

---

### 第 5-6 天：知识编译

把项目所有现存文档 + Step 4 的 Spec 归档 → 喂给 LLM Wiki 编译。

```bash
# 收集原始材料
raw/sources/
├── handover-notes.md          # 离职同事口述的任何问题
├── 2025Q2-architecture.md     # 架构文档
├── incident-reports/          # 历史事故复盘（最有价值的一类）
│   ├── 2025-03-payment-dedup.md
│   └── 2025-07-db-migration-failure.md
├── meeting-notes/             # 关键技术决策会议记录
├── deployment-playbook.md     # 部署手册
└── known-issues.md            # 已知问题清单

# 批量摄入
# LLM 自动提取：实体页 / 概念页 / 交叉引用 / 矛盾标记

wiki/
├── index.md                   # 全量目录
├── log.md                     # 操作日志
├── entities/
│   ├── payment-service.md
│   ├── order-state-machine.md
│   └── deployment-topology.md
├── concepts/
│   ├── payment-refund-flow.md
│   ├── order-dedup-race-condition.md
│   └── db-migration-strategy.md
├── comparisons/
│   └── sync-vs-async-refund.md
└── queries/
    └── common-troubleshooting.md
```

---

### 第 6 天：搜索 + 入口文件

```bash
# 搜索就绪
qmd collection add wiki --name project-wiki
qmd embed
```

**最关键的一步**——写 `AGENTS.md`，这是后来者的 Agent 的入口文件：

```markdown
# AGENTS.md — 项目 Wiki 使用指南

## 上手路径
本项目包含预编译的知识产物。在你开始工作之前，务必先读取：

1. 代码图谱：`.codegraph/`（调用 codegraph explore 获取代码结构）
2. 规范归档：`openspec/changes/archive/`（历史决策，每个模块为什么这么做）
3. 知识 Wiki：`wiki/index.md`（系统有什么，怎么关联）
4. 搜索工具：`qmd query "你的问题"`（在 Wiki 中查具体知识点）

## 核心工作流
- 理解代码：先查 CodeGraph，不要逐文件读
- 查询知识：先搜 qmd，不要从聊天历史猜
- 修改代码：先读对应模块的 Spec 归档（了解为什么这么设计）
- 新增功能：先 `/opsx:propose` 写 Spec，不要直接改代码
- 更新知识：任何新的理解、修复的事故、部署变更 → 告诉 LLM 更新 Wiki

## 已知风险区域
- 支付模块：两阶段确认，不要改状态机
- 数据库迁移：不要直接改 Migration 文件，用迁移工具
- 计费：精度问题，永远用 decimal

## 技术债务
- 订单去重逻辑需要异步化（见 openspec/changes/archive/ 中 order-* 相关 Spec）
- 用户服务缺少熔断
```

---

### 第 7 天：验证交接

**让后继者的 Agent 回答以下问题，验证交接完整性：**

```
1. "这个系统的支付模块是怎么工作的？"       → Wiki 能回答
2. "payment-service.js 被哪些模块调用？"     → CodeGraph 能回答  
3. "为什么退款用了同步而非异步？"            → Spec Archive 能回答
4. "历史上有过什么重大事故？"                → Wiki 能回答（事故报告已摄入）
5. "如果要加一个退款重试功能，从哪里开始？"    → AGENTS.md 指导的工作流能引导
```

如果 Agent 能回答前 4 个问题 — 交接成功。第 5 个问题验证了"后继者可以继续工作"而不仅仅是"后继者可以观看"。

---

### 交付物清单

| 产物 | 工具 | 形式 | 位置 |
|---|---|---|---|
| 代码符号图谱 | CodeGraph | 二进制索引 | `.codegraph/`（git 追踪） |
| 历史决策记录 | OpenSpec | Markdown | `openspec/changes/archive/` |
| 系统知识 Wiki | LLM Wiki | Markdown | `wiki/` |
| 搜索索引 | qmd | SQLite | `.qmd/`（git 追踪或本地重建） |
| Agent 入口 | 手写 | Markdown | `AGENTS.md`（项目根目录） |
| 原始文档 | 收集 | 原始格式 | `raw/sources/` |

**全部一起 git commit：**

```bash
git add .
git commit -m "handover: codegraph + openspec archive + wiki + qmd index + AGENTS.md"
```

---

### 后来者第一天

```bash
git clone <project>
# .codegraph/, openspec/, wiki/ 全部在仓库里

codegraph explore "支付模块核心流程"     # Agent 直接查图谱
qmd query "订单去重是怎么处理的"           # Agent 搜 Wiki
cat openspec/changes/archive/*/design.md  # 读历史决策
cat AGENTS.md                             # Agent 入口指南
```

不需要问离职同事任何问题。不是因为同事不愿意回答，而是因为**离职同事能留下的全部知识，已经以 Agent 可以查询、理解和维护的形式，冻结在了仓库里。**
