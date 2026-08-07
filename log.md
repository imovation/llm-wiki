# Wiki 日志

> 所有 wiki 操作的按时间顺序记录。仅追加。
> 格式：`## [YYYY-MM-DD] action | subject`
> 动作：ingest, update, query, lint, create, archive, delete
> 当此文件超过 500 条记录时，轮换：重命名为 log-YYYY.md，重新开始。

## [2026-08-07] create | Wiki 已初始化
- 领域：LLM Wiki 生态（模式、工具、规范、应用）
- 依据 Hermes [[llm-wiki-skill]] 方法论，在 /home/imovation/projects/llm-wiki 就地搭建
- 创建 SCHEMA.md、index.md、log.md，及 entities/ concepts/ comparisons/ queries/ 目录

## [2026-08-07] move | 源文件归档到 raw/
- llm-wiki.{md,zh.md}、SKILL.{md,zh.md}、okf-spec.{md,zh.md} 移入 raw/articles/，添加 source_url/ingested/sha256 frontmatter

## [2026-08-07] ingest | 历史会话导出
- 从 opencode.db 导出 6 个会话到 raw/session-history/（2026-07-18 至 2026-08-07）

## [2026-08-07] create | 实体页（10）
- codegraph、comet、graphify、langsmith、llm-wiki-compiler、llm-wiki-skill、nashsu-llm-wiki、openwiki、openspec、qmd

## [2026-08-07] create | 概念页（12）
- ast、cst-vs-ast、god-node-analysis、leiden-community-detection、llm-wiki-ecosystem、llm-wiki-pattern、lsp、okf、spec-vs-wiki、syntactic-sugar、three-layer-architecture、tree-sitter

## [2026-08-07] create | 对比页（2）
- graphify-vs-codegraph、openwiki-vs-graphify-vs-codegraph

## [2026-08-07] create | 查询页（1）
- handover-plan

## [2026-08-07] lint | 0 个问题
- 全量 wikilink 校验通过；修复若干候选链接与大小写（LSP→lsp）
