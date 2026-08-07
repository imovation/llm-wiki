---
title: 语法糖
created: 2026-08-07
updated: 2026-08-07
type: concept
tags: [syntax, ast]
sources: [raw/session-history/2026-07-24-playful-cactus.md]
confidence: high
---

# 语法糖 (Syntactic Sugar)

**语法糖**是语言设计者为让代码好读/好写而添加的语法特性——不引入新能力，只是**把已有功能"包"成更甜的写法**。

## 例子

```python
# 列表推导式（语法糖）
squares = [x**2 for x in range(10)]
# = 普通循环（去糖后）
squares = []
for x in range(10):
    squares.append(x**2)

# 装饰器（语法糖）
@cache
def fib(n): ...
# = fib = cache(fib)

# +=（语法糖）
a += 1   # = a = a + 1
```

## CST 与 AST 的关系

- [[cst-vs-ast|CST]] 保存语法糖（`@cache`、`+=`、`for...in` 都是显式节点）
- [[cst-vs-ast|AST]] 会"去糖"把它们展开为基础操作

## 相关

- [[cst-vs-ast]]、[[tree-sitter]]、[[ast]]