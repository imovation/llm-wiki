---
title: AST (抽象语法树)
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [ast, parser, compiler]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-24-playful-cactus.md]
confidence: high
---

# AST (Abstract Syntax Tree)

源代码的**结构化树状表示**——编译器/解析器读取源码时解析成 AST，每个节点是一个语法元素。^[raw/session-history/2026-07-18-misty-river.md]

```python
result = a + b * 2
```
的 AST：
```
        =
      /   \
result     +
          / \
         a   *
             / \
            b   2
```

## 核心价值

把"字符串"变成"数据结构"→ 可在树上做**精确查询**（"找到所有函数定义"）和**精确变换**（"把所有 `var` 改 `let`，且只改变量声明"），没有正则的误匹配。

## 在本 wiki 语境中的用处

所有代码知识图谱工具（[[graphify]]、[[codegraph]]）都用 [[tree-sitter]] 解析代码 → 生成 AST/CST → 提取符号、调用关系、继承链 → 构建知识图谱：
1. **确定性**（无 LLM 调用）
2. **无歧义**（不像向量嵌入有语义模糊）
3. **全本地**（privacy/成本为零）

**注意**：tree-sitter 的产出严格说是 [[cst-vs-ast|CST]] 而非 AST（保留了语法细节）。

## 相关

- [[tree-sitter]]、[[cst-vs-ast]]、[[syntactic-sugar]]
- Java ASM 见 [[cst-vs-ast]] 的补充说明（bytecode 层操作，比 AST 低一层）
- LSP 桥接概念（候选页）