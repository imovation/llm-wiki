---
title: Tree-sitter
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [tree-sitter, ast, parser]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-23-mighty-star.md, raw/session-history/2026-07-24-playful-cactus.md]
confidence: high
---

# Tree-sitter

**通用的、增量解析的 AST 解析器框架**——代码知识图谱工具（[[graphify]]/[[codegraph]]）的共同底层技术。^[raw/session-history/2026-07-23-mighty-star.md]

## 与传统解析器的区别

| 特性 | 传统解析器（CPython ast, Bison/YACC） | tree-sitter |
|---|---|---|
| 增量解析 | ❌ 改一行重解析整个文件 | ✅ 只重解析被改子树 |
| 容错性 | ❌ 语法错误即失败 | ✅ 返回部分 AST + error 节点 |
| 跨语言 | ❌ 每语言独立解析器 | ✅ 统一框架 + 语言语法文件 |
| 编辑友好 | ❌ 一次性解析 | ✅ 实时解析，IDE 高亮 |

## 工作方式

```
语法文件（grammar.js）→ grammar.json → parser（C/Rust/WASM 二进制）
  → 解析源码 → CST/AST → 查询引擎（如 (function_declaration name: (identifier) @name)）
```

三种编译形态：**C 动态库**（最传统）、**Rust crate**（CodeGraph 采用）、**WebAssembly**（浏览器/Node.js，CodeGraph 回退引擎、Graphify 部分引擎）。

## 重要细节

**tree-sitter 产出的其实是 [[cst-vs-ast|CST]]，而不是严格 AST。** 保留每个 token 的行列位置，所以可做语法高亮与代码折叠。

## 为什么代码图谱工具选它

- **确定性**：AST 解析不调 LLM，纯算法，无歧义
- **全本地**：零隐私风险、零 API 成本
- 与语义向量检索互补：结构精确 vs 语义模糊

## 相关

- [[cst-vs-ast]]、[[graphify]]、[[codegraph]]
- 其他问答：LSP 见 [[lsp]]