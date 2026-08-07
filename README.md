# LLM Wiki — 元知识库

一个按 [Karpathy 的 LLM Wiki 模式](raw/articles/llm-wiki.md) 维护的**元知识库**：主题是「LLM Wiki 生态」本身——模式、工具、规范与应用。wiki 记录 LLM Wiki 的一切，且 wiki 自身就按其所记录的模式运转。

## 这是什么

不是 RAG。不是静态文档站。这是一个由 **LLM agent 增量编译并持续维护**的互链 Markdown 知识库：

- 每次摄入新来源，LLM 阅读 → 提取 → 更新实体页/概念页/交叉引用 → 记账
- 知识**一次性编译、持续保持最新**，而不是每次查询时重新推导
- 矛盾被显式标记，好答案归档回库，知识随时间复利增长

**分工**：人类负责找来源、提问题；LLM 负责摘要、交叉引用、归档与记账。

## 目录结构（三层）

```
llm-wiki/
├── AGENTS.md           # Agent 入口：每次会话先读 SCHEMA+index+log
├── SCHEMA.md           # Schema 层：领域、约定、标签分类法、Lint 清单
├── index.md            # 内容目录（先读找页）
├── log.md              # 仅追加操作台账
├── raw/                # 第一层：不可变原始来源（含 sha256）
│   ├── articles/       #   文章、规范、skill 手册
│   └── session-history/#   研究会话导出
├── entities/           # 第二层：工具/项目页（openwiki、codegraph…）
├── concepts/           #   概念页（LLM Wiki 模式、OKF、spec-vs-wiki…）
├── comparisons/        #   对比页
├── queries/            #   归档的好答案
└── scripts/lint.py     # 可执行健康检查
```

## 快速开始

**维护**（摄入新来源 / 查询 / 健康检查）：

```bash
# 打开项目即被 AGENTS.md 引导（任何支持 agent 指令的编辑器/CLI 均可）
# 三大操作：
#   Ingest  — 把新来源丢给 agent："摄入 https://..."
#   Query   — 问问题："spec 和 wiki 的分工？"
#   Lint    — 健康检查：
python3 scripts/lint.py .
```

**浏览**：本目录直接作为 Obsidian vault 打开，用图谱视图看知识连接；也可纯文本/git 浏览。

## 内容全景

- 核心模式：[[llm-wiki-pattern]] · [[three-layer-architecture]] · [[spec-vs-wiki]]
- 规范：[[okf]]（Google Open Knowledge Format v0.1）
- 工具：[[openwiki]] · [[codegraph]] · [[graphify]] · [[qmd]] · [[llm-wiki-compiler]] · [[nashsu-llm-wiki]] · [[openspec]] · [[comet]] · [[langsmith]]
- 全景：[[llm-wiki-ecosystem]]

完整索引见 [index.md](index.md)。

## 为什么这样维护

维护知识库的瓶颈是记账——更新交叉引用、保持摘要最新、记录矛盾。人类因维护成本增长而放弃 wiki；LLM 不会厌倦、一次可触及 15 个文件，**维护成本趋近于零**。人类做的只是策划来源、指导分析、提出好问题。

## 许可与说明

- 源材料版权归各自作者（Karpathy gist、Hermes Agent、Google Cloud、各开源项目）
- 本仓库为个人知识整理用途，遵循 Karpathy 原文的"copy-paste 给 agent 使用"意图