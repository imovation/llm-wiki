---
source_url: opencode://session-history/2026-07-24-playful-cactus
title: Session: Tree-sitter, LSP, AST, CST, Java ASM 解释
ingested: 2026-08-07
sha256: 2a8f6c06eb15d5807e84205a4863fe984b2df1a7cf9a4b00e364cb72d1eb12d3
---

# Session: Tree-sitter, LSP, AST, CST, Java ASM 解释

- slug: `playful-cactus`  session-id: `ses_06b84f12effeJ4axUGToJAChfj`  created: 2026-07-24 22:15
- 源目录：/home/imovation/projects/llm-wiki


## [07-24 22:15] user

tree-sitter、LSP、AST、CST、java ASM 是什么？


## [07-24 22:15] assistant

The user is asking about several technical concepts in programming languages and tools. Let me provide concise explanations for each.

Let me think about what they're asking:

1. **Tree-sitter** - A parser generator tool and incremental parsing library. It builds concrete syntax trees (CSTs) from source code, is fast, error-tolerant, and used by editors like Neovim and GitHub for syntax highlighting, code folding, etc.

2. **LSP (Language Server Protocol)** - A protocol between an editor/IDE and a language server that provides language-specific features like autocomplete, go-to-definition, hover, diagnostics, etc. It standardizes how editors communicate with language tools.

3. **AST (Abstract Syntax Tree)** - A tree representation of source code that abstracts away syntactic details (like parentheses, semicolons). Each node represents a construct in the source code. Used by compilers, linters, formatters, etc.

4. **CST (Concrete Syntax Tree)** - Also called a parse tree, it preserves all syntactic details including whitespace, comments, parentheses, etc. It's a complete representation of the source text's syntax.

5. **Java ASM** - A Java bytecode manipulation and analysis framework. It reads, writes, transforms, and analyzes Java class files (bytecode) at the binary level. Used by frameworks like Spring, Hibernate, and tools like AspectJ for runtime bytecode manipulation.

These are all tools/representations for working with code at different levels of abstraction, from text (Tree-sitter/CST) to parsed structure (AST) to protocol (LSP) to binary bytecode (ASM).

- **Tree-sitter**: 增量解析库，生成 Concrete Syntax Tree (CST)，保留全部语法细节（含空格、注释），速度快、容错强，Neovim/GitHub 用于语法高亮、代码折叠等。
- **LSP (Language Server Protocol)**: 编辑器与语言服务器间的标准化协议，提供自动补全、跳转定义、悬停提示、诊断等功能。
- **AST (Abstract Syntax Tree)**: 抽象语法树，忽略标点/空格等细节，保留代码结构。编译器/分析工具使用。
- **CST (Concrete Syntax Tree)**: 具体语法树（又称 Parse Tree），保留源代码的所有语法细节（括号、分号、注释等），比 AST 信息更完整。
- **Java ASM**: Java 字节码操作框架，直接读写/转换/分析 `.class` 文件（bytecode 级别）。Spring、Hibernate 等用它做 AOP、动态代理。

关系：编辑器用 Tree-sitter 解析源码 → CST；编译器/工具解析源码 → AST；LSP 在两者之间搭桥提供 IDE 功能；ASM 则跳过源码，直接在字节码层操作 Java 类。
