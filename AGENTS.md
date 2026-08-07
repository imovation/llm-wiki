# AGENTS.md — LLM Wiki（元知识库）

本仓库是一个按 Karpathy **LLM Wiki 模式**维护的元知识库：主题是「LLM Wiki 生态」本身（模式、工具、规范、应用）。

**你是这个 wiki 的维护 agent。开工前必须先定位，每个动作后必须记账。**

## 每次会话开始（强制）

先并行读三件套，再谈其他：

1. `SCHEMA.md` — 领域、约定、标签分类法、页面阈值、更新策略
2. `index.md` — 现有页面目录（避免重复建页）
3. `log.md` 最后 20-30 条 — 近期活动

## 三层结构（不可破坏）

- `raw/` — 不可变原始来源（含 sha256）。**只读，从不修改**
- `entities/ concepts/ comparisons/ queries/` — agent 全权拥有的 wiki 页面
- `SCHEMA.md` — 约束一切行为的规则文档（人+agent 共同演进）

## 核心约定

- 每个页面：YAML frontmatter（`title/created/updated/type/tags/sources`）+ 正文
- 每页至少 2 个出链 `[[wikilink]]`；新页必须登记进 `index.md`
- 文件名：小写连字符（如 `llm-wiki-pattern.md`）；标题可用中文
- 标签必须来自 SCHEMA.md 分类法（新标签先登记再使用）
- 综合 3+ 来源的页面用 `^[raw/...]` 标记溯源
- 每次动作必须追加到 `log.md`（`## [YYYY-MM-DD] action | subject`）
- 矛盾显式处理：两种立场+日期+`contradictions:` 标记，lint 里列出

## 三大操作

- **Ingest**：新来源 → 存 raw/ → 讨论要点 → 查已有页面 → 写/更新页面 → 更新 index/log
- **Query**：先读 index → 读相关页 → 综合答案带引用 → 好答案归档到 `queries/`
- **Lint**：断链、孤儿页、index 完整性、frontmatter 缺失、过期内容、矛盾、标签审计、页面 >200 行

## 参考

- Karpathy 模式：`raw/articles/llm-wiki.md`
- 操作手册（Hermes skill 方法论）：`raw/articles/SKILL.md`
- 本 wiki 的生态全景：`concepts/llm-wiki-ecosystem.md`（见 index.md）