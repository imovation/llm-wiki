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

消费前先注册新标签。

- **模式**: llm-wiki, rag-alternative, knowledge-base, three-layer, meta
- **工具/项目**: openwiki, codegraph, graphify, qmd, llmwiki-compiler, hermes-skill, comet, openspec, nashsu-app
- **规范**: okf, spec-driven, citation, index-log
- **概念**: spec-vs-wiki, acl-matching, ingest, lint, query, graph-nothing
- **场景**: handover, ai-native-engineering
- **技术**: tree-sitter, ast, cst, leiden, god-node, mcp, cli

## Page Thresholds

- **创建页面**：实体/概念出现在 2+ 来源，或对单一来源至关重要
- **添加到已有页**：来源提及已涵盖内容
- **不要**给附带提及创建页面
- 超过约 200 行则拆分
- 完全被取代则归档到 `_archive/`

## 实体页面（entities/）
每个项目/工具：概述、关键事实、唯一能力、与其他工具的关系、来源

## 概念页面（concepts/）
模式、规范、关键概念：定义、当前认知、开放问题、相关概念

## 对比页面（comparisons/）
并排分析：对比动机、维度（表格）、结论、来源

## 更新策略

新信息与旧内容冲突时：
1. 比较日期——较新来源通常取代较旧
2. 真矛盾则两种立场都记录，标注日期与来源
3. frontmatter 标记 `contradictions:`
4. lint 报告中列出供用户审查