---
title: LSP (Language Server Protocol)
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [lsp, ide]
sources: [raw/session-history/2026-07-24-playful-cactus.md]
confidence: medium
---

# LSP (Language Server Protocol)

**编辑器与语言服务器之间的标准化协议**——让编辑器获得语言功能而不必理解每种语言。

## 是什么

- 编辑器/IDE 通过 LSP 与语言服务器通信，获得：自动补全、跳转定义、悬停提示、诊断等
- 语言服务器负责解析代码（通常用 [[ast]]），编辑器只做展示
- 一份语言服务器实现，所有支持 LSP 的编辑器（VS Code、Neovim、JetBrains 等）通用

## 在 [[tree-sitter]] 语境中的位置

```
源代码
  ├── 编辑器用 tree-sitter 解析 → CST（高亮、折叠）
  └── 语言服务器解析 → AST（补全、跳转、诊断）
          ↑
     LSP 在此桥接编辑器与语言服务器
```

- Tree-sitter 是**语法分析层**（快、容错、增量）
- LSP 是**协议层**（编辑器 ↔ 语言智能服务）
- 二者互补：tree-sitter 管显示，LSP 管功能

## 相关

- [[tree-sitter]]、[[ast]]、[[cst-vs-ast]]