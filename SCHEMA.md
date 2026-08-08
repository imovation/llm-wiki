---
title: Wiki Schema
created: 2026-08-07
updated: 2026-08-07
type: schema
tags: [wiki, schema]
---

# Wiki Schema — LLM Wiki 生态

## Domain

本 wiki 研究并记录 **LLM Wiki 生态**：一切关于"LLM 增量构建与维护持久知识库"的模式、工具、规范与应用。包括 Karpathy 原始模式、各实现（Hermes SKILL / OpenWiki / llm-wiki-compiler / nashsu llm_wiki / qmd）、规范（OKF）、配套的代码知识图谱工具（CodeGraph / Graphify）与 Spec 驱动开发体系（OpenSpec / Comet），以及它们在 AI 原生软件工程与离职交接等场景中的应用。

本 wiki 自身即按其所记录的模式运转——**元应用**（meta-application）。

## Convention

- 文件命名：小写、连字符、无空格（如 `openwiki.md`）
- 每个 wiki 页面以 YAML frontmatter 开头
- 使用 `[[wikilinks]]` 互链，每页至少 2 个出链
- 更新页面时更新 `updated` 日期
- 每个新页面必须加入 `index.md` 对应章节
- 每次操作追加到 `log.md`
- **溯源**：综合 3+ 来源的页面加 `^[raw/...]` 标记；`sources:` frontmatter 不可省

## Frontmatter

```yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | schema
tags: [from taxonomy]
sources: [raw/...]
confidence: high | medium | low
---
```

## raw/ Frontmatter

```yaml
---
source_url:
ingested: YYYY-MM-DD
sha256:
---
```

## Tag Taxonomy（领域：LLM Wiki 生态）

消费前先注册。此列表由 lint 审计（2026-08-07 全面检查时补齐，覆盖全部在用标签 43 个）。

- **模式**: `llm-wiki`, `wiki`, `rag-alternative`, `knowledge-base`, `three-layer`
- **工具/项目**: `openwiki`, `graphify`, `codegraph`, `qmd`, `llmwiki-compiler`, `hermes-skill`, `comet`, `openspec`, `langsmith`, `nashsu-app`
- **工具形态**: `cli`, `desktop`, `skill`, `search`
- **规范/流程**: `okf`, `spec-driven`, `spec-vs-wiki`, `index-log`
- **场景**: `handover`, `ai-native-engineering`, `workflow`
- **技术**: `tree-sitter`, `ast`, `cst`, `parser`, `syntax`, `lsp`, `ide`, `compiler`
- **图谱**: `knowledge-graph`, `algorithm`, `leiden`, `god-node`, `ecosystem`
- **开发**: `ai-coding`
- **元**: `schema`, `evaluation`, `observability`

## Page Thresholds

- **创建页面**：实体/概念出现在 2+ 来源，或对单一来源至关重要
- **添加到已有页**：来源提及已涵盖内容
- **不要**给附带提及创建页面
- 超过约 200 行则拆分
- 完全被取代则归档到 `_archive/`

## Lint 清单（触发：用户要求 lint / 维护时定期 / 关键动作后）

1. **断链**：`[[wikilink]]` 目标页不存在
2. **孤页**：无入向 `[[wikilink]]` 的页面
3. **index 完整性**：每个 wiki 页都在 index.md；index 头部「总页面数」必须与实际条目数一致（由 index 条目自动计数，禁止手工数字）
4. **frontmatter**：必填字段齐全；标签在分类法内；`type` 取值合法（entity/concept/comparison/query/schema/summary）；`updated ≥ created`；`contested`/`contradictions` 页面列出供审查
5. **sources 路径**：每页 `sources:` 中每条 raw 路径必须在 `raw/` 下真实存在（`raw/` vs `raw/articles/` 的错位是已知腐化点）
6. **过期内容**：`updated` 早于 90 天且被新来源提及
7. **矛盾**：`contested: true` / `contradictions:` 页面列出
8. **来源漂移**：raw/ 的 sha256 与 frontmatter 不符
9. **页面大小**：>200 行
10. **单一来源偏薄**：重要结论只有 1 个 `sources:` 且未设 confidence——提示补证或降级 confidence

## 实体页面（entities/）
每个项目/工具：概述、关键事实、唯一能力、与其他工具的关系、来源

## 概念页面（concepts/）
模式、规范、关键概念：定义、当前认知、开放问题、相关概念

## 对比页面（comparisons/）
并排分析：对比动机、维度（表格）、结论、来源

## 自动更新机制（2026-08-08 起）

- **检测**：`scripts/check_updates.py` 每日 09:00（cron）查询 `scripts/tracked-projects.json` 中所有项目的 GitHub releases / npm dist-tags
- **基线**：`scripts/.state.json` 记录各项目上次已知版本，**入库**（作为 GHA 云端基线）；新增/改名项目需在 `tracked-projects.json` 登记并重跑 `--seed`；无更新时不写盘（避免 git 噪音）
- **落盘**：检测到新版本 → 生成 `raw/releases/updates-YYYY-MM-DD.md`（含 sha256，作为不可变来源）
- **自动摄取**：`scripts/auto_ingest.sh` 检测到更新后调 `opencode run`，agent 按 Ingest 流程处理 updates-*.md
- **自动提交**：摄取完成后 `auto_ingest.sh` 自动 `git add -A && git commit`（message：`ingest: YYYY-MM-DD auto updates`）；无变更则跳过
- **仓库**：本 wiki 是 git 仓库（main 分支）。`.gitignore` 忽略 `.state.json` 与运行时日志；raw/ 与页面均入库（raw 不可变，提交即快照）
- **手工触发**：`python3 scripts/check_updates.py --dry-run`（只报告）；`--seed`（重设基线）
- **日志**：raw/releases/.auto-ingest.log、.cron.log（raw 下非 .md 文件，lint 豁免）
- **维护注意**：`updates-*.md` 是 agent 待处理队列，摄取完成后不可删除（raw/ 不可变），处理时以最新日期文件为准

## 更新策略

新信息与旧内容冲突时：
1. 比较日期——较新来源通常取代较旧
2. 真矛盾则两种立场都记录，标注日期与来源
3. frontmatter 标记 `contradictions:`
4. lint 报告中列出供用户审查