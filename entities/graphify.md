---
title: Graphify
created: 2026-08-07
updated: 2026-08-09
type: entity
tags: [graphify, knowledge-base, cli]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-20-cosmic-harbor.md, raw/session-history/2026-07-23-mighty-star.md, raw/releases/tool-updates-2026-08.md, raw/releases/updates-2026-08-08.md, raw/releases/updates-2026-08-09.md]
confidence: high
---

# Graphify

[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)（作者 Safi Shamsi，YC S26）的**开源代码知识图谱工具**（Python，Apache-2.0 + MIT）。约 104k star（2026-08）、1.2M+ PyPI 下载，最新 v0.9.37（2026-08-08，迭代高频）。将整个代码库（代码/文档/PDF/图片/视频/SQL/Terraform）转化为可查询的**知识图谱**，让 agent 以图查询替代 grep。^[raw/session-history/2026-07-23-mighty-star.md] ^[raw/releases/tool-updates-2026-08.md]

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

## 版本动态

- **v0.9.36（2026-08-07，correctness 版）**：修复 4 处静默失败（`cluster-only` 忽略 `--backend`/`--model`/`--batch-size` 时告警、community-label 提示词与丢弃哨兵不再冲突、`tree --root` 根无匹配时非零退出、`cluster-only` 从分析图中盖 `built_at_commit`）；Swift 跨文件 `extension` 不再丢调用边；node-id 冲突消解改为确定性（生命周期罚分 + 路径段逆序平局）；Windows skill 改用 PowerShell 可运行。^[raw/releases/updates-2026-08-08.md]
- **v0.9.37（2026-08-08，correctness 版）**：TypeScript 成员调用不再仅凭接收者类型同名伪造高置信 `calls` 边——接收者类型须定义于同文件或被调用方实际导入，第三方 `import type { Repo }` 不再误绑本地同名 `class Repo`，表推断接收者降级为 INFERRED（#2553）；回调体内调用不再丢失（`wrapper(async (req) => { helper() })`，#2552）；Kotlin 补齐——`import` 节点此前静默丢弃现能解析、全限定调用 `com.example.Foo.bar()` 产出 `calls` 边、语法不可解析文件（如单行 `class C { val x }`）告警而非静默（#2526/#2550/#2551）；`graphify update` 重试上次提取失败的文件而非永久标记 up-to-date，毒化 manifest 下次运行自愈（#2543）；claude-cli 后端透出 stdout 信封内的 API 错误（如零退出码限流）而非当作空成功，零/非零退出两条路径均上报（#2554）。^[raw/releases/updates-2026-08-09.md]

## 相关

- 概念：[[leiden-community-detection]]、[[god-node-analysis]]
- 工具：[[codegraph]]（最接近的竞品）、[[openwiki]]、[[qmd]]
- 对比：[[openwiki-vs-graphify-vs-codegraph]]