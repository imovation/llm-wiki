---
source_url: https://github.com/GoogleCloudPlatform/knowledge-catalog (zh translation)
ingested: 2026-08-07
sha256: ce4900a9ea4b420397375ebf8f8de0a11d5adcf3cc3d201572db7e147af579e2
---

# 开放知识格式（Open Knowledge Format, OKF）

**版本 0.1 — 草案**

OKF 是一种开放的、对人类和 agent 都友好的格式，用于表示*知识*——即围绕
数据和系统的元数据、上下文和经过整理的洞察。它被设计为：由人类撰写、
由 agent 生成、跨组织交换、并被双方共同消费。

本格式有意保持极简：一个带有 YAML frontmatter 的 Markdown 文件目录。
没有 schema 注册中心，没有中央权威机构，没有必需的工具链。
能 `cat` 一个文件，你就能阅读 OKF；能 `git clone` 一个仓库，你就能分发它。

---

## 1. 动机

面向 AI agent 的知识表示领域正在快速演进，许多互不兼容的约定正在涌现。
OKF 的立场是：知识最好用普遍可及的、成熟的格式来表示，这些格式应当是：

- **可读的（Readable）**——人类无需工具即可阅读。
- **可解析的（Parseable）**——agent 无需专用 SDK 即可解析。
- **可 diff 的（Diffable）**——可在版本控制中进行差异比较。
- **可移植的（Portable）**——可跨工具、跨组织、跨时间迁移。

本格式的立场是最小化干预。它只标准化使知识库*自描述*所需的那一小套
结构性约定——除此之外的一切都留给生产者决定。

### 目标

1. 定义一个**富化 agent（enrichment agents）**可以写入的通用格式。
2. 指导**消费 agent（consumption agents）**应当如何读取和遍历它。
3. 促进知识跨系统、跨组织的**交换**。
4. 标准化使内容能够被有意义地消费所必须存在的少量**必需**字段。

### 非目标

- 定义一套固定的概念类型分类法。
- 规定存储、服务或查询基础设施。
- 取代领域特定的 schema（Avro、Protobuf、OpenAPI 等）——
  OKF *引用*它们；它不吞并它们。

---

## 2. 术语

- **知识包（Knowledge Bundle）**——一个自包含的、层级化的知识文档集合。
  是分发单位。
- **概念（Concept）**——包内知识的最小单元。表示为一个 Markdown 文档。
  可以描述实体资产（一张表、一个 API）、抽象概念（一个指标、
  一个业务流程），或介于两者之间的任何事物。
- **概念 ID（Concept ID）**——概念文件在包内的路径，去掉 `.md` 后缀。
  例如 `tables/users.md` 的概念 ID 是 `tables/users`。
- **Frontmatter**——由 Markdown 文件顶部的 `---` 分隔的 YAML 元数据块。
- **正文（Body）**——文件中 frontmatter 之后的所有内容。
- **链接（Link）**——从一个概念指向另一个概念的标准 Markdown 链接，
  用于表达超出隐式父子层级之外的关系。
- **引用（Citation）**——从概念指向外部来源的链接，用于支撑正文中的主张。

---

## 3. 知识包结构

一个知识包就是一棵 Markdown 文件的目录树。目录结构与领域无关——
生产者以最适合所捕获知识的方式组织概念。

```
path/to/bundle/
├── index.md                      # 可选。用于渐进式披露的目录清单。
├── log.md                        # 可选。按时间顺序的更新历史。
├── <concept>.md                  # 包根级的一个概念。
└── <subdirectory>/               # 子目录将概念组织成组。
    ├── index.md
    ├── <concept>.md
    └── <subdirectory>/
        └── …
```

知识包可以以以下形式分发：

- 一个 git 仓库（推荐——提供历史、归因和 diff）。
- 目录的 tar 包或 zip 压缩包。
- 一个更大仓库中的子目录。

### 3.1 保留文件名

以下文件名在层级的任何级别都有已定义的含义，且不得用作概念文档：

| 文件名       | 用途                                                     |
|--------------|----------------------------------------------------------|
| `index.md`   | 目录清单。见 §6。                                        |
| `log.md`     | 更新历史。见 §7。                                        |

所有其他 `.md` 文件都是概念文档。

标签（tags）本身仍然是一等概念——见 §4.1 中的 `tags` frontmatter 字段。
OKF 不规定按标签聚合文档的单独文件格式；想要标签浏览视图的生产者可以
在消费时通过扫描 frontmatter 现场合成一个。

---

## 4. 概念文档

每个概念都是一个 UTF-8 Markdown 文件。它由两部分组成：

1. 一个 **YAML frontmatter 块**，由文件开头单独一行上的 `---` 和
   单独一行上的闭合 `---` 分隔。
2. 一个 **Markdown 正文**，包含自由形式的内容。

### 4.1 Frontmatter

```yaml
---
type: <Type name>                  # 必需
title: <可选的显示名称>
description: <可选的一句话摘要>
resource: <可选的底层资产规范 URI>
tags: [<tag>, <tag>, …]            # 可选
timestamp: <ISO 8601 datetime>     # 可选的最后修改时间
# …其他生产者定义的键/值对
---
```

**必需：**

- `type`——标识概念种类的短字符串。消费者用它进行路由、过滤和展示。
  示例值：`BigQuery Table`、`BigQuery Dataset`、`API Endpoint`、`Metric`、
  `Playbook`、`Reference`。

  类型值**不**进行中央注册。生产者应当选择描述性、不言自明的值；
  消费者必须优雅地容忍未知类型（通常将其视为通用概念）。

**推荐（按优先级排序）：**

- `title`——人类可读的显示名称。如果省略，消费者可以从文件名推导标题。
- `description`——概括概念的一句话。被 `index.md` 生成器、搜索摘要
  和预览使用。
- `resource`——唯一标识概念所描述的底层资产的 URI。对于描述抽象概念
  而非物理资源的概念，此字段缺省。
- `tags`——用于横向分类的短字符串 YAML 列表。
- `timestamp`——最后一次有意义变更的 ISO 8601 日期时间。

**扩展：** 生产者可以包含任何额外的键。消费者在往返处理时应当保留
未知键，且不应当拒绝带有未识别字段的文档。

### 4.2 正文

正文是标准 Markdown。生产者应当优先使用结构化 Markdown——
标题、列表、表格、围栏代码块——而非自由散文，因为结构同时有助于
人类阅读和 agent 检索。

没有必需的正文章节。以下章节标题具有**约定**含义，适用时应当使用：

| 标题           | 用途                                                     |
|----------------|----------------------------------------------------------|
| `# Schema`     | 资产列/字段的结构化描述。                                |
| `# Examples`   | 具体使用示例，常为围栏代码块。                           |
| `# Citations`  | 支撑正文主张的外部来源。见 §8。                          |

### 4.3 示例：绑定到资源的概念

```markdown
---
type: BigQuery Table
title: Customer Orders
description: One row per completed customer order across all channels.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, orders, revenue]
timestamp: 2026-05-28T14:30:00Z
---

# Schema

| Column        | Type      | Description                              |
|---------------|-----------|------------------------------------------|
| `order_id`    | STRING    | Globally unique order identifier.        |
| `customer_id` | STRING    | Foreign key into [customers](/tables/customers.md). |
| `total_usd`   | NUMERIC   | Order total in US dollars.               |
| `placed_at`   | TIMESTAMP | When the customer submitted the order.   |

# Joins

Joined with [customers](/tables/customers.md) on `customer_id`.

# Citations

[1] [BigQuery table schema](https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders)
```

### 4.4 示例：不绑定到资源的概念

```markdown
---
type: Playbook
title: Incident response — data freshness alert
description: Steps to triage a freshness alert on the orders pipeline.
tags: [oncall, incident]
timestamp: 2026-04-12T09:00:00Z
---

# Trigger

A freshness alert fires when `orders` lags more than 30 minutes behind
its expected SLA. See the [orders table](/tables/orders.md).

# Steps

1. Check the [ingestion job dashboard](https://example.com/dash).
2. …
```

---

## 5. 交叉链接

概念可以使用标准 Markdown 链接链接到其他概念。支持两种形式：

### 5.1 绝对（包相对）链接

以 `/` 开头，相对于包根目录解析。

```markdown
See the [customers table](/tables/customers.md) for the join key.
```

这是**推荐**的形式，因为当文档在其子目录内移动时它是稳定的。

### 5.2 相对链接

标准 Markdown 相对路径。

```markdown
See the [neighboring concept](./other.md).
```

### 5.3 链接语义

从概念 A 到概念 B 的链接断言了一种*关系*。关系的具体种类
（父子、引用、joins-with、depends-on 等）由周围的散文传达，
而不是由链接本身传达。构建图谱视图的消费方通常将所有链接视为
无类型关系的有向边。

消费者必须容忍断链——目标在包中不存在的链接不是格式错误；
它可能只是代表尚未写出的知识。

---

## 6. 索引文件

`index.md` 文件可以出现在任何目录中，包括包根目录。它枚举该目录的
内容，以支持**渐进式披露**——让人类或 agent 在打开单个文档之前
先看看有什么可用。

索引文件不含 frontmatter。正文使用一个或多个章节，
每个章节将概念分组在一个标题下：

```markdown
# Section / Group Heading

* [Title 1](relative-url-1) - short description of item 1
* [Title 2](relative-url-2) - short description of item 2

# Another Section

* [Subdirectory](subdir/) - short description of the subdirectory
```

条目应当包含所链接概念的 frontmatter 中的 description。
生产者可以自动生成 `index.md`；当不存在索引时，
消费者可以现场合成一个。

---

## 7. 日志文件（可选）

`log.md` 文件可以出现在层级的任何级别，用于记录该作用域的变更历史。
格式为按日期分组的扁平条目列表，最新的在前：

```markdown
# Directory Update Log

## 2026-05-22
* **Update**: Added new BigQuery table reference for [Customer Metrics](/tables/customer-metrics.md).
* **Creation**: Established the [Dataplex Playbook](/playbooks/dataplex.md).

## 2026-05-15
* **Initialization**: Created foundational directory structure.
* **Update**: Added progressive-disclosure guidelines to the root [index](/index.md).
```

日期标题必须使用 ISO 8601 `YYYY-MM-DD` 形式。日志条目是散文；
开头的加粗词（`**Update**`、`**Creation**`、`**Deprecation**` 等）
是惯例，而非强制要求。

---

## 8. 引用

当概念的正文提出了源自外部材料的主张时，这些来源应当以编号形式
列在文档底部的 `# Citations` 标题下：

```markdown
# Citations

[1] [BigQuery public dataset announcement](https://cloud.google.com/blog/products/data-analytics/...)
[2] [Internal data quality runbook](https://wiki.acme.internal/data/quality)
```

引用链接可以是绝对 URL、包相对路径，或指向 `references/` 子目录的
路径——该子目录将外部材料作为一等 OKF 概念进行镜像。

---

## 9. 合规性

一个知识包**符合** OKF v0.1 规范，需满足：

1. 目录树中的每个非保留 `.md` 文件都包含可解析的 YAML frontmatter 块。
2. 每个 frontmatter 块都包含非空的 `type` 字段。
3. 出现的每个保留文件名（`index.md`、`log.md`）都分别遵循 §6 和 §7
   中描述的结构。

消费者应当将其他所有约束视为软指导。特别是，消费者不得因以下原因
拒绝一个知识包：

- 缺少可选的 frontmatter 字段。
- 未知的 `type` 值。
- 未知的额外 frontmatter 键。
- 损坏的交叉链接。
- 缺少 `index.md` 文件。

这种宽容的消费模型是有意为之：OKF 旨在知识包增长、重构和被 agent
部分生成的过程中始终保持可用。

---

## 10. 与其他格式的关系

OKF 有意贴近几种既有实践：

- **LLM "wiki" 仓库**——使用 Markdown + frontmatter 作为
  agent 可读知识库的仓库。
- **个人知识工具**——如 Obsidian 和 Notion，使用带交叉链接的
  层级化 Markdown。
- **"元数据即代码"（Metadata as code）**——将目录元数据与源代码
  存储在一起，而不是放在单独的注册中心。

OKF 的主要区别在于它是**规范化了的**——固定了互操作性所需的
最小规则集，而不指定工具。

---

## 11. 版本控制

本文档规定 OKF 版本 **0.1**。未来修订将以 `<major>.<minor>` 形式
进行版本化：

- **minor** 版本升级引入向后兼容的新增（新的可选字段、
  新的约定章节标题）。
- **major** 版本升级可能引入破坏性变更（重命名必需字段、
  更改保留文件名）。

知识包可以通过在包根 `index.md` 的 frontmatter 块中包含
`okf_version: "0.1"` 来声明其目标 OKF 版本（这是 `index.md` 中
唯一允许 frontmatter 的地方）。不理解所声明版本的消费者应当尝试
尽力消费，而不是拒绝该知识包。

---

## 附录 A — 最小示例知识包

```
my_bundle/
├── index.md
├── datasets/
│   ├── index.md
│   └── sales.md
└── tables/
    ├── index.md
    ├── orders.md
    └── customers.md
```

`datasets/sales.md`：

```markdown
---
type: BigQuery Dataset
title: Sales
description: All sales-related tables for the retail business.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales
tags: [sales]
timestamp: 2026-05-28T00:00:00Z
---

The sales dataset contains transactional tables, including
[orders](/tables/orders.md) and [customers](/tables/customers.md).
```

`tables/orders.md`：

```markdown
---
type: BigQuery Table
title: Orders
description: One row per completed customer order.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, orders]
timestamp: 2026-05-28T00:00:00Z
---

# Schema

| Column        | Type      | Description                  |
|---------------|-----------|------------------------------|
| `order_id`    | STRING    | Unique order identifier.     |
| `customer_id` | STRING    | FK to [customers](/tables/customers.md). |
| `total_usd`   | NUMERIC   | Order total in USD.          |

Part of the [sales dataset](/datasets/sales.md).
```
