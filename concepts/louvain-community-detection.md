---
title: Louvain 社区检测
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [algorithm, knowledge-graph, leiden]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-23-mighty-star.md]
confidence: high
---

# Louvain 社区检测

**Louvain** 是一种**图聚类算法**（2008，Blondel 等），通过模块度（Modularity）优化把图的节点分组为"社区"——组内连接密集、组间稀疏。它是社区发现领域最经典的算法之一，也是 [[leiden-community-detection]] 的前身。

## 工作原理

```
输入: 图（节点+边）
 ① 遍历每个节点，尝试移动到邻居社区
    若模块度提升则接受（Local Moving）
 ② 将社区聚合为"超节点"（Aggregation）
 ③ 重复 ①②，直到模块度不再提升
输出: 层次化社区结构
```

## 在 LLM Wiki 生态中的出现

- [[nashsu-llm-wiki]] 的**知识图谱**用 Louvain 做知识社区发现：自动把知识点聚成主题簇，配合凝聚度评分与"意外关联/知识缺口"洞察^[raw/session-history/2026-07-18-misty-river.md]
- 与 [[graphify]] 使用的 [[leiden-community-detection]] 同族同目标——都是"自动把图分成有意义的组"

## vs Leiden（核心对比）

| 维度 | Louvain | Leiden（2019 改进） |
|---|---|---|
| 社区连通性 | **可能产生不连通社区** | 保证内部连通 |
| 模块度质量 | 基准 | 通常更高 |
| 运行速度 | 快 | 相当或更快 |
| 额外阶段 | 无 | Refinement 阶段（细粒度拆分） |

Leiden 论文明确指出 Louvain 的缺陷：局部移动阶段后随机聚合可能产生**不连通社区**，Leiden 通过 Refinement Phase 修复。^[raw/session-history/2026-07-23-mighty-star.md]

## 相关

- [[leiden-community-detection]]（改进版）、[[god-node-analysis]]（同属图分析）
- [[nashsu-llm-wiki]]、[[graphify]]