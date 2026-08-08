---
title: qmd
created: 2026-08-07
updated: 2026-08-08
type: entity
tags: [qmd, knowledge-base, cli, search]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/articles/llm-wiki.md, raw/articles/llm-wiki.zh.md, raw/releases/tool-updates-2026-08.md]
confidence: high
---

# qmd

[tobi/qmd](https://github.com/tobi/qmd)（Query Markup Documents），作者 tobi。**全本地 Markdown 混合搜索引擎**。TypeScript（Bun/Node.js），MIT，约 28k star，当前 v2.6.3（2026-06-24）。^[raw/session-history/2026-07-18-misty-river.md] ^[raw/releases/tool-updates-2026-08.md]

这是 [Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 中提到的 "wiki 规模扩大后的可选搜索方案"。

## 是什么

给你的笔记/文档/知识库装上一套混合搜索引擎：**BM25 关键词 + 向量语义 + LLM 重排序**，全设备端运行，CLI/MCP/SDK 三种方式给 AI agent 用。

## 安装与基本流程

```bash
npm install -g @tobilu/qmd
qmd collection add ~/notes --name notes
qmd context add qmd://notes "个人笔记和想法"   # 添加上下文（关键特性）
qmd embed
qmd query "部署流程"
```

## 搜索管线

```
用户查询 → 查询扩展(微调 LLM ×2权重) + 原查询
        → 原查询 FTS5+向量 / 扩展1 / 扩展2
        → RRF 融合 + Top-Rank Bonus + Top30
        → LLM 重排(qwen3-reranker, 本地 GGUF)
        → 位置感知混合
```

三个本地 GGUF 模型（首次使用自动下载到 `~/.cache/qmd/models/`）：embeddinggemma-300M（嵌入）、qwen3-reranker-0.6b（重排）、qmd-query-expansion-1.7B（查询扩展）。支持 `QMD_EMBED_MODEL` 环境变量切换（如 Qwen3-Embedding 提升中日韩）。

## Score 融合

- **RRF**：`Σ(1/(k+rank+1))`, k=60
- Top-Rank Bonus：#1 +0.05，#2-3 +0.02
- 位置感知混合：顶部重排权重低，防止淹没精确匹配

## 相关

- 概念：[[llm-wiki-ecosystem]]（搜索层可选工具）
- 工具：[[openwiki]]、[[llm-wiki-compiler]]