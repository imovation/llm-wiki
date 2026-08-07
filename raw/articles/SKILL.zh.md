---
source_url: https://github.com/NousResearch/hermes-agent (zh translation)
ingested: 2026-08-07
sha256: 3078c7426ae10cbb445e72b325c46e0893198fb6ff1754fbdd93bd45a2b39586
---

---
name: llm-wiki
description: "Karpathy 的 LLM Wiki：构建/查询相互链接的 Markdown 知识库。"
version: 2.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wiki, knowledge-base, research, notes, markdown, rag-alternative]
    category: research
    related_skills: [obsidian, arxiv]
---

# Karpathy 的 LLM Wiki

构建并维护一个持久的、不断积累的、以相互链接的 Markdown 文件形式存在的知识库。
基于 [Andrej Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。

与传统 RAG（每次查询都从头重新发现知识）不同，该 wiki 一次性编译知识并保持其最新。
交叉引用已经存在。矛盾已经被标记。综合结论反映了所有已摄入的内容。

**分工：** 人类负责策划来源和指导分析。Agent 负责摘要、交叉引用、归档和维护一致性。

## 何时激活本技能

在用户出现以下情况时使用本技能：
- 要求创建、构建或启动 wiki 或知识库
- 要求将来源摄入、添加或处理到他们的 wiki 中
- 提问时，在配置的路径下存在现有 wiki
- 要求对 wiki 进行 lint、审计或健康检查
- 在研究语境中引用他们的 wiki、知识库或"笔记"

## Wiki 位置

**位置：** 通过 `WIKI_PATH` 环境变量设置（例如在 `${HERMES_HOME:-~/.hermes}/.env` 中）。

如果未设置，默认为 `~/wiki`。

```bash
WIKI="${WIKI_PATH:-$HOME/wiki}"
```

wiki 仅仅是一个 Markdown 文件的目录——可以在 Obsidian、VS Code 或任何编辑器中打开。
无需数据库，无需特殊工具。

## 架构：三个层次

```
wiki/
├── SCHEMA.md           # 约定、结构规则、领域配置
├── index.md            # 分节的内容目录，含一行摘要
├── log.md              # 按时间顺序的操作日志（仅追加，每年轮换）
├── raw/                # 第一层：不可变的原始材料
│   ├── articles/       # 网页文章、剪藏
│   ├── papers/         # PDF、arxiv 论文
│   ├── transcripts/    # 会议记录、访谈
│   └── assets/         # 来源引用的图片、图表
├── entities/           # 第二层：实体页面（人物、组织、产品、模型）
├── concepts/           # 第二层：概念/主题页面
├── comparisons/        # 第二层：对比分析
└── queries/            # 第二层：值得保留的归档查询结果
```

**第一层——原始来源：** 不可变。Agent 从中读取但从不修改。
**第二层——Wiki：** Agent 拥有的 Markdown 文件。由 Agent 创建、更新和交叉引用。
**第三层——模式（Schema）：** `SCHEMA.md` 定义了结构、约定和标签分类法。

## 恢复现有 Wiki（关键——每次会话都必须执行）

当用户已有 wiki 时，**在做任何事之前务必先定位**：

① **读取 `SCHEMA.md`**——了解领域、约定和标签分类法。
② **读取 `index.md`**——了解存在哪些页面及其摘要。
③ **扫描最近的 `log.md`**——阅读最后 20-30 条记录以了解近期活动。

```bash
WIKI="${WIKI_PATH:-$HOME/wiki}"
# 会话开始时的定位读取
read_file "$WIKI/SCHEMA.md"
read_file "$WIKI/index.md"
read_file "$WIKI/log.md" offset=<最后30行>
```

只有在定位之后才能进行摄入、查询或 lint。这可以防止：
- 为已存在的实体创建重复页面
- 遗漏对现有内容的交叉引用
- 与模式中的约定相矛盾
- 重复已完成的工作

对于大型 wiki（100 页以上），在创建新内容之前，还要对当前主题快速执行一次 `search_files`。

## 初始化新 Wiki

当用户要求创建或启动 wiki 时：

1. 确定 wiki 路径（来自 `$WIKI_PATH` 环境变量，或询问用户；默认为 `~/wiki`）
2. 创建上述目录结构
3. 询问用户 wiki 涵盖的领域——要具体
4. 根据领域定制写入 `SCHEMA.md`（参见下面的模板）
5. 写入初始 `index.md`，包含分节标题
6. 写入初始 `log.md`，包含创建条目
7. 确认 wiki 已就绪，并建议首批要摄入的来源

### SCHEMA.md 模板

根据用户的领域进行调整。模式约束了 Agent 的行为并确保一致性：

```markdown
# Wiki 模式

## 领域
[此 wiki 涵盖的内容——例如"AI/ML 研究"、"个人健康"、"创业情报"]

## 约定
- 文件名：小写、连字符、无空格（例如 `transformer-architecture.md`）
- 每个 wiki 页面以 YAML frontmatter 开头（见下文）
- 使用 `[[wikilinks]]` 在页面之间建立链接（每页至少 2 个出链）
- 更新页面时，始终更新 `updated` 日期
- 每个新页面必须添加到 `index.md` 中正确的章节下
- 每个操作必须追加到 `log.md` 中
- **溯源标记：** 在综合了 3 个以上来源的页面上，在段落末尾追加 `^[raw/articles/source-file.md]`
  以标识特定来源的主张。这让读者无需重新阅读整个原始文件即可追溯每条主张。
  在单来源页面上为可选项，因为 `sources:` frontmatter 已足够。

## Frontmatter
  ```yaml
  ---
  title: 页面标题
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  type: entity | concept | comparison | query | summary
  tags: [来自下方分类法的标签]
  sources: [raw/articles/source-name.md]
  # 可选的质量信号：
  confidence: high | medium | low        # 主张的受支持程度
  contested: true                        # 当页面存在未解决的矛盾时设置
  contradictions: [other-page-slug]      # 与此页面冲突的页面
  ---
  ```

`confidence` 和 `contested` 是可选的，但建议用于意见性较强或快速变化的话题。
Lint 会找出 `contested: true` 和 `confidence: low` 的页面以供审查，这样薄弱的主张
不会悄无声息地固化为被接受的 wiki 事实。

### raw/ 的 Frontmatter

原始来源也有一个小的 frontmatter 块，以便重新摄入时检测漂移：

```yaml
---
source_url: https://example.com/article   # 原始 URL（如适用）
ingested: YYYY-MM-DD
sha256: <frontmatter 下方原始内容的十六进制摘要>
---
```

`sha256:` 允许将来对同一 URL 的重新摄入在内容未变化时跳过处理，
并在内容变化时标记漂移。仅对正文（结束 `---` 之后的所有内容）计算，
不包括 frontmatter 本身。

## 标签分类法
[为领域定义 10-20 个顶级标签。在使用之前先将新标签添加到此文件中。]

AI/ML 示例：
- 模型：model, architecture, benchmark, training
- 人物/组织：person, company, lab, open-source
- 技术：optimization, fine-tuning, inference, alignment, data
- 元类：comparison, timeline, controversy, prediction

规则：页面上的每个标签都必须出现在此分类法中。如果需要新标签，
请先在此处添加，然后再使用。这可以防止标签泛滥。

## 页面阈值
- **创建页面**：当实体/概念出现在 2 个以上来源中或对单个来源至关重要时
- **添加到现有页面**：当来源提及已涵盖的内容时
- **不要创建页面**：对于附带提及、次要细节或领域之外的内容
- **拆分页面**：当页面超过约 200 行时——拆分为子主题并建立交叉链接
- **归档页面**：当页面内容被完全取代时——移至 `_archive/`，从索引中移除

## 实体页面
每个值得注意的实体一个页面。包括：
- 概述/是什么
- 关键事实和日期
- 与其他实体的关系（[[wikilinks]]）
- 来源引用

## 概念页面
每个概念或主题一个页面。包括：
- 定义/解释
- 当前知识状态
- 未解决问题或争议
- 相关概念（[[wikilinks]]）

## 对比页面
并排分析。包括：
- 对比的内容和原因
- 对比维度（首选表格格式）
- 结论或综合
- 来源

## 更新策略
当新信息与现有内容冲突时：
1. 检查日期——较新的来源通常取代较旧的来源
2. 如果确实存在矛盾，记录两种观点及其日期和来源
3. 在 frontmatter 中标记矛盾：`contradictions: [page-name]`
4. 在 lint 报告中标记供用户审查
```

### index.md 模板

索引按类型分节。每条记录一行：wikilink + 摘要。

```markdown
# Wiki 索引

> 内容目录。每个 wiki 页面在其类型下列出，附一行摘要。
> 首先阅读此文件以找到与任何查询相关的页面。
> 最后更新：YYYY-MM-DD | 总页面数：N

## 实体
<!-- 在章节内按字母顺序排列 -->

## 概念

## 对比

## 查询
```

**扩展规则：** 当任何章节超过 50 条记录时，按首字母或子领域拆分为子章节。
当索引总计超过 200 条记录时，创建一个 `_meta/topic-map.md`，按主题对页面分组以加快导航。

### log.md 模板

```markdown
# Wiki 日志

> 所有 wiki 操作的按时间顺序记录。仅追加。
> 格式：`## [YYYY-MM-DD] action | subject`
> 操作：ingest, update, query, lint, create, archive, delete
> 当此文件超过 500 条记录时，轮换：重命名为 log-YYYY.md，重新开始。

## [YYYY-MM-DD] create | Wiki 已初始化
- 领域：[领域]
- 使用 SCHEMA.md、index.md、log.md 创建了结构
```

## 核心操作

### 1. 摄入（Ingest）

当用户提供来源（URL、文件、粘贴内容）时，将其集成到 wiki 中：

① **捕获原始来源：**
   - URL → 使用 `web_extract` 获取 Markdown，保存到 `raw/articles/`
   - PDF → 使用 `web_extract`（可处理 PDF），保存到 `raw/papers/`
   - 粘贴的文本 → 保存到相应的 `raw/` 子目录
   - 文件命名要具有描述性：`raw/articles/karpathy-llm-wiki-2026.md`
   - **添加 raw frontmatter**（`source_url`、`ingested`、正文的 `sha256`）。
     对于同一 URL 的重新摄入：重新计算 sha256，与存储的值进行比较——
     如果相同则跳过，如果不同则标记漂移并更新。这样做成本足够低，
     可以在每次重新摄入时执行，并能捕获悄悄的源更改。

② **与用户讨论要点**——哪些内容有趣、哪些对领域重要。
   （在自动化/cron 上下文中跳过此步骤——直接继续。）

③ **检查已有内容**——搜索 index.md 并使用 `search_files` 查找
   提到的实体/概念的现有页面。这是不断增长的 wiki 与重复堆砌之间的区别。

④ **写入或更新 wiki 页面：**
   - **新实体/概念：** 仅当符合 SCHEMA.md 中的页面阈值时才创建页面
     （2 个以上来源提及，或对单个来源至关重要）
   - **已有页面：** 添加新信息、更新事实、更新 `updated` 日期。
     当新信息与现有内容矛盾时，遵循更新策略。
   - **交叉引用：** 每个新的或更新的页面必须通过 `[[wikilinks]]` 链接到至少 2 个
     其他页面。检查现有页面是否链接回来。
   - **标签：** 仅使用 SCHEMA.md 分类法中的标签
   - **溯源：** 在综合 3 个以上来源的页面上，将 `^[raw/articles/source.md]`
     标记追加到主张可追溯到特定来源的段落末尾。
   - **置信度：** 对于意见性较强、快速变化或单来源的主张，设置
     `confidence: medium` 或 `low`。除非主张在多个来源中都有充分支持，
     否则不要标记为 `high`。

⑤ **更新导航：**
   - 将新页面添加到 `index.md` 的正确章节下，按字母顺序排列
   - 更新索引标头中的"总页面数"计数和"最后更新"日期
   - 追加到 `log.md`：`## [YYYY-MM-DD] ingest | Source Title`
   - 在日志条目中列出每个创建或更新的文件

⑥ **报告更改内容**——向用户列出每个创建或更新的文件。

单个来源可以触发 5-15 个 wiki 页面的更新。这是正常的且符合预期——
这就是积累效应。

### 2. 查询（Query）

当用户询问有关 wiki 领域的问题时：

① **读取 `index.md`** 以识别相关页面。
② **对于 100 页以上的 wiki**，还要在所有 `.md` 文件中 `search_files`
   查找关键术语——仅靠索引可能遗漏相关内容。
③ **使用 `read_file` 读取相关页面**。
④ **从编译的知识中综合出答案**。引用你使用的 wiki 页面：
   "基于 [[page-a]] 和 [[page-b]]..."
⑤ **将有价值的答案归档回来**——如果答案是实质性的对比、
   深入分析或新颖的综合，在 `queries/` 或 `comparisons/` 中创建页面。
   不要归档琐碎的查找——仅归档那些重新推导会很痛苦的答案。
⑥ **更新 log.md**，记录查询及其是否已归档。

### 3. 检查（Lint）

当用户要求对 wiki 进行 lint、健康检查或审计时：

① **孤立页面：** 查找没有来自其他页面的入向 `[[wikilinks]]` 的页面。
```python
# 使用 execute_code 进行此操作——跨所有 wiki 页面的编程扫描
import os, re
from collections import defaultdict
wiki = "<WIKI_PATH>"
# 扫描 entities/、concepts/、comparisons/、queries/ 中的所有 .md 文件
# 提取所有 [[wikilinks]]——构建入链映射
# 入链为零的页面即为孤立页面
```

② **损坏的 wikilinks：** 查找指向不存在页面的 `[[links]]`。

③ **索引完整性：** 每个 wiki 页面都应出现在 `index.md` 中。对比
   文件系统中的页面和索引条目。

④ **Frontmatter 验证：** 每个 wiki 页面必须包含所有必填字段
   （title、created、updated、type、tags、sources）。标签必须在分类法中。

⑤ **过期内容：** `updated` 日期早于提及相同实体的最近来源超过 90 天的页面。

⑥ **矛盾：** 同一主题下存在冲突主张的页面。查找共享标签/实体
   但陈述不同事实的页面。将所有包含 `contested: true` 或 `contradictions:` frontmatter
   的页面提交给用户审查。

⑦ **质量信号：** 列出 `confidence: low` 的页面以及仅引用单个来源但未设置
   confidence 字段的页面——这些页面要么需要寻找佐证，要么降级为 `confidence: medium`。

⑧ **来源漂移：** 对于 `raw/` 中带有 `sha256:` frontmatter 的每个文件，重新计算
   哈希值并标记不匹配。不匹配表明原始文件被编辑过
   （不应发生——raw/ 是不可变的）或者是从后来发生变化的 URL 摄入的。
   不是硬性错误，但值得报告。

⑨ **页面大小：** 标记超过 200 行的页面——适合拆分的候选。

⑩ **标签审计：** 列出所有正在使用的标签，标记不在 SCHEMA.md 分类法中的标签。

⑪ **日志轮换：** 如果 log.md 超过 500 条记录，轮换它。

⑫ **报告发现**，包含具体的文件路径和建议操作，按严重性分组
   （损坏的链接 > 孤立页面 > 来源漂移 > 有争议的页面 > 过期内容 > 风格问题）。

⑬ **追加到 log.md：** `## [YYYY-MM-DD] lint | 发现 N 个问题`

## 使用 Wiki

### 搜索

```bash
# 按内容查找页面
search_files "transformer" path="$WIKI" file_glob="*.md"

# 按文件名查找页面
search_files "*.md" target="files" path="$WIKI"

# 按标签查找页面
search_files "tags:.*alignment" path="$WIKI" file_glob="*.md"

# 近期活动
read_file "$WIKI/log.md" offset=<最后20行>
```

### 批量摄入

当一次摄入多个来源时，批量处理更新：
1. 先读取所有来源
2. 识别所有来源中的实体和概念
3. 一次性检查所有现有页面（一次搜索，不是 N 次）
4. 一次过创建/更新页面（避免冗余更新）
5. 最后一次性更新 index.md
6. 编写一个涵盖整个批次的日志条目

### 归档

当内容被完全取代或领域范围发生变化时：
1. 如果不存在则创建 `_archive/` 目录
2. 将页面移动到 `_archive/` 下保持原始路径（例如 `_archive/entities/old-page.md`）
3. 从 `index.md` 中移除
4. 更新所有链接到它的页面——将 wikilink 替换为纯文本 + "（已归档）"
5. 记录归档操作

### Obsidian 集成

wiki 目录开箱即用作为 Obsidian 仓库：
- `[[wikilinks]]` 呈现为可点击的链接
- 图谱视图可视化知识网络
- YAML frontmatter 为 Dataview 查询提供支持
- `raw/assets/` 文件夹存放通过 `![[image.png]]` 引用的图片

为获得最佳效果：
- 将 Obsidian 的附件文件夹设置为 `raw/assets/`
- 在 Obsidian 设置中启用"Wikilinks"（通常默认开启）
- 安装 Dataview 插件以执行诸如 `TABLE tags FROM "entities" WHERE contains(tags, "company")` 之类的查询

如果同时使用 Obsidian 技能，请将 `OBSIDIAN_VAULT_PATH` 设置为与
wiki 路径相同的目录。

### Obsidian Headless（服务器和无头机器）

在没有显示器的机器上，使用 `obsidian-headless` 替代桌面应用。
它通过 Obsidian Sync 在无 GUI 的情况下同步仓库——非常适合在服务器上运行、
写入 wiki 而 Obsidian 桌面版在另一台设备上读取的 Agent。

**设置：**
```bash
# 需要 Node.js 22+
npm install -g obsidian-headless

# 登录（需要具有 Sync 订阅的 Obsidian 账户）
ob login --email <email> --password '<password>'

# 为 wiki 创建远程仓库
ob sync-create-remote --name "LLM Wiki"

# 将 wiki 目录连接到仓库
cd ~/wiki
ob sync-setup --vault "<vault-id>"

# 初始同步
ob sync

# 持续同步（前台——使用 systemd 实现后台运行）
ob sync --continuous
```

**通过 systemd 实现持续后台同步：**
```ini
# ~/.config/systemd/user/obsidian-wiki-sync.service
[Unit]
Description=Obsidian LLM Wiki 同步
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/path/to/ob sync --continuous
WorkingDirectory=/home/user/wiki
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
```

```bash
systemctl --user daemon-reload
systemctl --user enable --now obsidian-wiki-sync
# 启用 linger 以便在注销后同步继续运行：
sudo loginctl enable-linger $USER
```

这样 Agent 可以往服务器上的 `~/wiki` 写入内容，而你可以在笔记本电脑/手机上
使用 Obsidian 浏览同一个仓库——更改在数秒内出现。

## 注意事项

- **永远不要修改 `raw/` 中的文件**——来源是不可变的。更正应放在 wiki 页面中。
- **始终先定位**——在新会话中进行任何操作之前，先读取 SCHEMA + index + 最近的日志。
  跳过此步骤会导致重复和遗漏的交叉引用。
- **始终更新 index.md 和 log.md**——跳过此步骤会使 wiki 退化。这些是
  导航的骨干。
- **不要为附带提及创建页面**——遵循 SCHEMA.md 中的页面阈值。一个名字
  在脚注中出现一次并不值得创建一个实体页面。
- **不要创建没有交叉引用的页面**——孤立的页面是不可见的。每个页面必须
  链接到至少 2 个其他页面。
- **Frontmatter 是必需的**——它支持搜索、过滤和过期检测。
- **标签必须来自分类法**——自由格式的标签会退化为噪音。先将新标签添加到 SCHEMA.md，
  然后再使用它们。
- **保持页面可快速浏览**——一个 wiki 页面应在 30 秒内可读完。超过 200 行的
  页面请拆分。将详细分析移至专门的深度挖掘页面。
- **批量更新前先询问**——如果一次摄入会触及 10 个以上的现有页面，请先
  与用户确认范围。
- **轮换日志**——当 log.md 超过 500 条记录时，将其重命名为 `log-YYYY.md` 并重新开始。
  Agent 应在 lint 期间检查日志大小。
- **明确处理矛盾**——不要静默覆盖。同时记录两种主张及其日期，
  在 frontmatter 中标记，并提交用户审查。

## 相关工具

[llm-wiki-compiler](https://github.com/atomicmemory/llm-wiki-compiler) 是一个 Node.js CLI 工具，
可将来源编译成概念 wiki，灵感同样来自 Karpathy。它与 Obsidian 兼容，
因此想要定时/CLI 驱动编译管道的用户可以将它指向此技能维护的同一个仓库。
权衡：它拥有页面生成权（取代了 Agent 在页面创建上的判断力），并且针对小型语料库进行了优化。
当你需要 Agent 参与策划时使用此技能；当你想要批量编译来源目录时使用 llmwiki。
