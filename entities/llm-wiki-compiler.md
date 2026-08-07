---
title: llm-wiki-compiler
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [llmwiki-compiler, knowledge-base, cli]
sources: [raw/session-history/2026-07-18-misty-river.md]
confidence: medium
---

# llm-wiki-compiler

[atomicstrata/llm-wiki-compiler](https://github.com/atomicstrata/llm-wiki-compiler)（别名 `llmwiki`）。Karpathy LLM Wiki 模式的 **CLI/SDK 编译器实现**。TypeScript 98.5%，MIT，约 1.8k star。@^[raw/session-history/2026-07-18-misty-river.md]

## 一句话

**源码进，wiki 出。** 两阶段 LLM 管线：先提取概念，再生成类型化页面。

## 核心能力

1. **两阶段编译器**
   - raw（Markdown/PDF/图片/网页/会话）→ 类型化、交叉引用、可追溯引用的 wiki 页面
   - 增量编译：未变更源不走 LLM；并行编译概念提取和页面生成
2. **可配置生命周期模板（CLP, v1.0）**
   - 内置 `autosci`（学术研究）、`newsroom`（编辑）模板
   - 类型化实体（Paper/Idea/Experiment...）、定向关系、生命周期状态机
   - 运行时门控：关系门、证据门、审批门由写入路径强制，不依赖 prompt 约定
   - 哈希锚定内容寻址证据文件；内置 Crossref 学术引用导入
3. **质量模型**
   - 审核门：低置信/矛盾/不合 schema 页面自动挂起待审
   - 新鲜度：fresh/stale/orphaned/unverified 状态，`refresh --stale` 修复
   - `lint` / `eval`：损坏链接、孤儿页、引用覆盖率、置信度分布
   - CI 门：质量阈值，失败阻断

## 权衡（来自 SKILL.md）

它与 Hermes [[llm-wiki-skill]] 的取舍：`llmwiki` **拥有页面生成权**（取代 agent 在页面创建上的判断力），适合**批量编译**来源目录 + 定时/CI pipeline；而 skill 方法适合"agent 在环策划"（agent-in-the-loop curation）。

## 相关

- 概念：[[llm-wiki-ecosystem]]、[[llm-wiki-pattern]]（模式）
- 工具：[[openwiki]]，[[nashsu-llm-wiki]]，[[llm-wiki-skill]]，[[okf]]
- 对比：见 [[llm-wiki-ecosystem]] 的"五项目定位对比"表