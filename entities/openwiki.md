---
title: OpenWiki
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [openwiki, knowledge-base, cli]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-20-cosmic-harbor.md, raw/session-history/2026-07-23-mighty-star.md]
confidence: high
---

# OpenWiki

LangChain（[langchain-ai](https://github.com/langchain-ai/openwiki)）开源的 **Agent 文档 CLI**，自动生成并持续维护代码库或个人知识源的 wiki。TypeScript，MIT，约 12-13k star。^[raw/session-history/2026-07-18-misty-river.md]

## 是什么

一句话：**为代码库或个人知识源自动编写并持续维护 agent 可读的 Markdown wiki。**

## 两种模式

| 模式 | 命令 | 输出位置 | 用途 |
|---|---|---|---|
| **Code 模式**（默认） | `openwiki --init/--update` | 仓库根 `openwiki/` | 当前代码库架构/模块文档 |
| **Personal 模式** | `openwiki personal --init/--update` | `~/.openwiki/wiki/` | 个人"第二大脑"，聚合多来源 |

## 关键特性

- **Agent-first**：生成 `AGENTS.md`/`CLAUDE.md` 中的 `# OPENWIKI:START` 块，引导 agent 先查 wiki
- **双向同步/CI**：GitHub Actions、GitLab CI、Bitbucket Pipeline 自动跑更新并提 PR
- **Mermaid 原生支持**：序列图、ER 图、状态图，带验证-降级-修复回路
- **输出兼容 [[okf]] v0.1 规范**：YAML frontmatter 标记文档类型
- **Built-in 连接器**（Personal 模式）：git-repo、Gmail、Notion、X、Web Search（Tavily）、Hackernews
- **多模型供应商**：OpenAI、Anthropic、Gemini、Bedrock、Ollama、OpenRouter 等

## 架构

- Agent 框架 `deepagents`；状态管理 LangGraph + SQLite checkpoint；终端渲染用 ink + React 18；遥测 posthog。

## 与同类的关系

见 [[openwiki-vs-graphify-vs-codegraph]]。核心：OpenWiki 是**叙事型文档**（LLM 写 .md），而 [[codegraph]]/[[graphify]] 是**结构化图谱**。

## 相关

- 概念：[[llm-wiki-生态]]、[[okf]]、[[spec-vs-wiki]]
- 工具：[[graphify]]、[[codegraph]]