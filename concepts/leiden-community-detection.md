---
title: Leiden 社区检测
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [leiden, knowledge-graph, algorithm]
sources: [raw/session-history/2026-07-23-mighty-star.md, raw/session-history/2026-07-18-misty-river.md]
confidence: high
---

# Leiden 社区检测

**Leiden** 是一种**图聚类算法**，是 Louvain 算法的改进版（2019）。把图中的节点分组为"社区"——组内连接紧密、组间连接稀疏。

## 工作原理

```
输入: 知识图谱（节点=符号，边=调用/导入/继承）
 ① Local Moving Phase    遍历节点，移动若提升模块度则接受
 ② Refinement Phase      （Louvain 没有）细粒度调整，分区-迭代拆分
 ③ 聚合为超节点           每个社区收缩，回到①直到收敛
输出: 层次化社区结构
```

## 相比 Louvain 的优势

- 保证社区内部连通（Louvain 可能产生不连通社区）
- 模块度更高、运行速度相当或更快

## 在知识图谱工具中的意义

- [[graphify]] 用它自动把代码库分成子系统（路由层/业务层/数据层...），**无需读代码就能了解边界与依赖方向**，且是零向量聚类（无 embedding 库）
- [[nashsu-llm-wiki]] 用 Louvain（同族算法）做知识社区发现

## 相关

- [[god-node-analysis]]（同属图分析）、[[graphify]]、[[nashsu-llm-wiki]]、[[tree-sitter]]