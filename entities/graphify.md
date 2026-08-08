---
title: Graphify
created: 2026-08-07
updated: 2026-08-08
type: entity
tags: [graphify, knowledge-base, cli]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-20-cosmic-harbor.md, raw/session-history/2026-07-23-mighty-star.md, raw/releases/tool-updates-2026-08.md]
confidence: high
---

# Graphify

[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)（作者 Safi Shamsi，YC S26）的**开源代码知识图谱工具**（Python，Apache-2.0 + MIT）。约 104k star（2026-08）、1.2M+ PyPI 下载，最新 v0.9.35（2026-08-06，迭代高频）。将整个代码库（代码/文档/PDF/图片/视频/SQL/Terraform）转化为可查询的**知识图谱**，让 agent 以图查询替代 grep。^[raw/session-history/2026-07-23-mighty-star.md] ^[raw/releases/tool-updates-2026-08.md]

## 是什么

**多模态知识图谱 builder。** tree-sitter AST 本地解析代码（零 LLM 成本）+ 语义提取文档/媒体，构建 NetworkX 图，配 HTML 可视化与报告。

## 关键特性

- **多模态**：代码(40+ 语言) + 文档/PDF/图片/视频/论文 URL 入同一图谱
- **Leiden 社区检测**：[[leiden-community-detection]] 自动识别子系统，零向量聚类，无需向量库
- **God Node 分析**：[[god-node-analysis]] 找桥梁节点、惊喜连接
- **边置信度**：每条边标记 `EXTRACTED` / `INFERRED` / `AMBIGUOUS`，"诚实置信度"
- **Token 压缩**：实测 71.5×（Karpathy 混合语料）
- **`--watch` / git hook**：文件保存自动增量重建；post-commit/post-checkout 钩子
- **`--wiki`**：每个社区生成 Wikipedia 风格 Markdown 页 + `index.md`，任何 agent 可浏览
- **`graphify export obsidian`**：导出 Obsidian vault
- **MCP server**：`python -m graphify.serve`

## 便携之处

```bash
uv tool install graphifyy    # PyPI 包名双 y
graphify install
/graphify .                  # 在 chat 中构建
graphify query "谁负责支付模块？"
graphify path "UserService" "DatabasePool"
```

## 架构（8 阶段管道）

```
detect() → extract() → build_graph() → cluster() → analyze() → report() → export()
```
独立模块、无共享状态，Python dict + NetworkX 图通信。

## 相关

- 概念：[[leiden-community-detection]]、[[god-node-analysis]]
- 工具：[[codegraph]]（最接近的竞品）、[[openwiki]]、[[qmd]]
- 对比：[[openwiki-vs-graphify-vs-codegraph]]