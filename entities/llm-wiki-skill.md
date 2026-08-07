---
title: Hermes llm-wiki skill
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [hermes-skill, knowledge-base, skill]
sources: [raw/articles/SKILL.md, raw/articles/SKILL.zh.md]
confidence: high
---

# Hermes llm-wiki skill

Nous Research [hermes-agent](https://github.com/NousResearch/hermes-agent) 内置的 **llm-wiki skill**（v2.1.0，作者 Hermes Agent，MIT），位于 `skills/research/llm-wiki/SKILL.md`。基于 Karpathy 的 LLM Wiki 模式实现的操作指导。本 wiki 的施工即遵循此 skill 的方法论。^[raw/SKILL.md]

## 三层架构

```
wiki/
├── SCHEMA.md           # 约定、结构规则、领域配置
├── index.md            # 分节内容目录，一行摘要
├── log.md              # 时间顺序操作日志（仅追加）
├── raw/                # 第一层：不可变原始材料
├── entities/ concepts/ comparisons/ queries/   # 第二层 wiki
```

## 核心操作

- **Ingest（摄入）**：捕获 raw → 讨论要点 → 检查已有 → 写/更新页面（≥2 出链）→ 更新 index/log
- **Query（查询）**：先读 index → 读相关页 → 综合答案带引用 → 好答案归档
- **Lint（检查）**：孤立页、断链、index 完整性、frontmatter 验证、过期内容、矛盾、来源漂移（sha256）、页面大小、标签审计

## 关键约定

- **raw/ 不可变**——纠正写在 wiki 页而非 raw
- 每页 ≥2 出链；frontmatter 必填（title/created/updated/type/tags/sources）
- 标签必须来自 SCHEMA 分类法
- 溯源标记 `^[raw/...]`（3+ 来源页面）
- 矛盾显式处理：两种立场+日期+frontmatter 标记
- log.md 超过 500 条轮换
- 初始化新 wiki 时先问领域、写 SCHEMA → index → log

## 相关

- 概念：[[llm-wiki-ecosystem]]
- 工具：[[llm-wiki-compiler]]（批量编译的替代路线）、[[nashsu-llm-wiki]]、[[openwiki]]