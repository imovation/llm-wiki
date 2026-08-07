---
title: God Node 分析
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [god-node, knowledge-graph, algorithm]
sources: [raw/session-history/2026-07-23-mighty-star.md]
confidence: medium
---

# God Node 分析

**God Node（神节点）**：图中**介数中心性（Betweenness Centrality）最高**的节点——充当最多"桥梁"的节点。

## 定义

```
介数中心性 CB(v) = Σ (σ_st(v) / σ_st)
                   s≠t≠v
  σ_st     = 从 s 到 t 的最短路径总数
  σ_st(v)  = 经过 v 的路径数
```

## 在代码库图谱中的含义

| 项目 | God Node | 中心性含义 |
|---|---|---|
| VS Code | ExtensionHost | 扩展主进程 ↔ 渲染进程的桥梁 |
| FastAPI | APIRouter | 所有路由注册的中心调度点 |
| Django | QuerySet | ORM 查询构建核心枢纽 |
| Tokio | Runtime | 异步任务调度的心脏 |
| React | useState/useEffect | 几乎所有组件经过 |

## 用途

- 识别**核心模块**（连接最多，改动影响最大）
- [[graphify]] 的 `analyze()` 阶段计算它并生成建议问题，配合 [[leiden-community-detection]] 输出 `GRAPH_REPORT.md`
- 交接场景：先看 God Node = 先锁定"最重要最该先理解"的代码

## 相关

- [[leiden-community-detection]]、[[graphify]]、[[codegraph]]（影响分析类似能力）