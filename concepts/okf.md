---
title: OKF (Open Knowledge Format)
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [okf, spec-driven, index-log]
sources: [raw/articles/okf-spec.md, raw/session-history/2026-07-18-misty-river.md]
confidence: high
---

# OKF (Open Knowledge Format)

**Open Knowledge Format v0.1（草案）**——Google Cloud Knowledge Catalog（原 Dataplex）发布的**开放知识表示规范**。原文在 `GoogleCloudPlatform/knowledge-catalog` 仓库 `okf/SPEC.md`（约 450 行，Apache 2.0）。本仓库 `raw/articles/okf-spec.md` + zh 译文。

## 一句话

> 用一个 **Markdown 文件目录 + YAML frontmatter** 表示"知识"（围绕数据和系统的元数据/上下文/整理洞见）。无 schema 注册中心、无中央权威、无必需工具链。**能 `cat` 就能读，能 `git clone` 就能分发。**

## 四个核心属性

**人类可读**（无需工具）· **agent 可解析**（无需专 SDK）· **可 diff**（版本控制友好）· **可移植**（跨工具/组织/时间）。

## 术语

- **Knowledge Bundle（知识包）**：自包含层级化知识文档集合，分发单元
- **Concept（概念）**：知识最小单元 = 一个 Markdown 文档（表、API、指标、流程等）
- **Concept ID**：文件在包里相对路径去 `.md`（`tables/users.md` → `tables/users`）
- Frontmatter / Body / Link / Citation

## 规范要点

1. **保留文件名只有两个**：`index.md`（目录清单）、`log.md`（更新历史）——**Karpathy llm-wiki 的 index/log 约定在此被正式规范化了**
2. **Concept = frontmatter + body**：frontmatter 唯一必填字段 `type`（无中央注册表，消费者必须容忍未知类型）；推荐 title/description/resource/tags/timestamp
3. **交叉链接**：建议**包相对绝对路径** `/tables/customers.md`（移动子目录内稳定）；容忍断链（可能是未写出的知识）
4. **index.md**：无 frontmatter（除根 `okf_version`），按章节分组
5. **log.md**：日期分组 `## YYYY-MM-DD`，最新在前
6. **Citations**：`# Citations` 编号列表
7. **合规性**：宽松消费模型——缺可选字段、未知 type/键、断链、缺 index 都不得拒绝

## 与 LLM Wiki 的关系

OKF 标准不进 Karpathy llm-wiki 的自然演进：把"约定"变"规范"。既可用于 llm-wiki 也用于 OpenWiki 输出。它**不规定工具**，只固定互操作性所需的最小规则集。

## 相关

- 概念：[[llm-wiki-模式]]、[[llm-wiki-生态]]、[[spec-vs-wiki]]
- 输出方：[[openwiki]]
- 附录：`raw/articles/okf-spec.md` 尾部有最小示例包