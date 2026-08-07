---
title: CST 与 AST 的区别
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [cst, ast, parser]
sources: [raw/session-history/2026-07-23-mighty-star.md, raw/session-history/2026-07-24-playful-cactus.md]
confidence: high
---

# CST 与 AST 的区别

**CST**（Concrete Syntax Tree，具体语法树）= Parse Tree，解析器直接输出，**保留源码全部语法细节**（括号、分号、关键字、Token 位置）。**AST**（Abstract Syntax Tree，抽象语法树）**丢弃语法糖**，只留结构。^[raw/session-history/2026-07-24-playful-cactus.md]

## 示例对比

```python
# 源码
x = a + b

# CST（tree-sitter 产出这种）— 保留 "="、"+"、";" 及行列位置
module [0,0] - [0,9]
└── assignment
    ├── left:  identifier x
    ├── operator: "="        ← 保留
    └── right: binary_expression
        ├── "+"              ← 保留
        └── b

# AST — 去掉语法细节
Assignment
├── target: Variable "x"
└── value:  BinaryOp "+"
```

## 对照表

| | CST | AST |
|---|---|---|
| 保留括号、分号、关键字 | ✅ | ❌ |
| 包含终端节点（Token） | ✅ | ❌ |
| 语法高亮 | ✅ 天然匹配 | ❌ 缺位置信息 |
| 语义分析 | ❌ 太多噪声 | ✅ |

## 与语法糖（[[syntactic-sugar]]）的关系

CST 保留语法糖（`@cache`、`+=`、`for...in` 是显式节点）；AST 去糖把它们展开为基础操作。

## 相关

- [[tree-sitter]]、[[ast]]、[[syntactic-sugar]]
- 问答：[[lsp]] 悬而未决（候选页）