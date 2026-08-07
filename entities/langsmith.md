---
title: LangSmith
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [langsmith, evaluation, observability]
sources: [raw/session-history/2026-07-23-mighty-star.md]
confidence: medium
---

# LangSmith

LangChain 公司的 **LLM 应用可观测性平台**，从开发到生产的全链路追踪、评估、监控。SaaS + 自托管。@^[raw/session-history/2026-07-23-mighty-star.md]

## 核心功能

- **Tracing**：自动捕获每一步执行轨迹（工具调用/LLM 调用/输出解析），含 input/output/latency/tokens/cost；`@traceable` 装饰器手动追踪任意函数
- **Evaluation**：LLM-as-Judge 评分、在线评估（生产流量采样检测幻觉/意图偏移）、数据集回归验证
- **Prompt 管理**：版本化、对比、A/B 测试
- **SmithDB**：为 agent 追踪设计的高吞吐存储（单对话可达数十 MB 嵌套 span）

## 与 OpenWiki 的关系

同属 LangChain 生态但互补：OpenWiki 是开发阶段的代码文档生成（给 agent 读的 Wiki），LangSmith 是运行时 agent 行为观测（给人看的 Trace）。OpenWiki 集成 LangSmith 追踪每次 `openwiki --init/--update` 的 LLM 调用链。

## 获取 API key

访问 https://smith.langchain.com → 注册（Google/GitHub/Email）→ Settings → API Keys → Create API Key。免费版每月 5,000 条 trace，无需信用卡。

## 相关

- 工具：[[openwiki]]（集成）、[[comet]]（`comet eval` 对接 LangSmith/LangFuse）