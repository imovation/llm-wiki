---
title: Spec 与 Wiki 的分工
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [spec-vs-wiki, spec-driven, knowledge-base]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-20-cosmic-harbor.md]
confidence: high
---

# Spec 与 Wiki 的分工

AI 原生软件工程中最重要的概念区分：**Spec 是指令，Wiki 是知识。**

## 核心对照

| | **Spec** | **Wiki** |
|---|---|---|
| 回答 | "我们要建什么？" | "已经建了什么？它怎么工作？" |
| 时间方向 | 向前看（将要发生） | 向后看（已经是） |
| 状态 | 描述**意图**——应在但可能未实现 | 描述**事实**——当前状态 |
| 读者 | 实现者（后继 Agent） | 理解者（问"认证怎么走"的 Agent/人） |
| 示例 | "用户 SHALL 能切换暗色主题" | "认证流程：JWT → AuthMiddleware → verify()" |
| 生命周期 | 实现 → 归档（历史记录） | 持续更新（每次新知识都刷新） |

## 在项目中的位置

```
Spec     = 意图层 → 驱动实现，实现后归档为决策记录
原始文档  = 事实层 → 驱动理解，LLM 编译为 wiki 页面
代码     = 实现层 → 唯一真实状态
Wiki     = 理解层 → 从代码 + raw + spec 归档提取/综合
```

## 关键洞察：Spec 是不是 Wiki 的原始文档？

**不完全是，但"Spec 归档后的产物"应该被摄入。**
- Spec 的源是需求意图，目标输出是**代码**；Wiki 从**已实现的事实**提取
- Spec 语气是祈使句（"SHALL 做"），Wiki 编译后变陈述句（"系统用两阶段确认是因为…"）
- 归档后的 spec（openspec/changes/archive/）可作为 raw 源喂给 wiki ingesting

## 传统文档的分类（AI 原生体系）

| 传统文档 | 归入 |
|---|---|
| 需求文档（PRD、用户故事） | **Spec**（proposal + specs） |
| 概要设计（架构决策） | **Spec**（design.md） |
| 详细设计 | **不写** — 自动生成（CodeGraph AST / OpenAPI 等） |
| API 文档 | **不写** — 自动生成（OpenAPI / gRPC proto） |
| 测试计划 | **Spec**（验收标准在 specs/ 内） |
| 测试用例 | **不写** — 测试代码即规格 |
| 测试报告 | **Wiki**（定期摄入历史质量数据） |
| 部署/运维文档 | **Wiki** |
| 用户手册 | **Wiki** |
| 事故报告 | **Wiki**（最有价值：出过什么问题、怎么修的） |

## 管理方式

- Spec 用 [[openspec]] 驱动（`/opsx:propose → apply → archive`），写入 `openspec/`
- Wiki 用 [[llm-wiki-模式]] 维护（ingest/query/lint），写入 `wiki/`
- 二者都服务于同一个目标：**知识不随人走**（离职交接场景见 [[离职交接方案]]）

## 相关

- [[llm-wiki-模式]]、[[openspec]]、[[llm-wiki-生态]]
- 查询页：[[离职交接方案]]