---
title: Graphify
created: 2026-08-07
updated: 2026-08-13
type: entity
tags: [graphify, knowledge-base, cli]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-20-cosmic-harbor.md, raw/session-history/2026-07-23-mighty-star.md, raw/releases/tool-updates-2026-08.md, raw/releases/updates-2026-08-08.md, raw/releases/updates-2026-08-09.md, raw/releases/updates-2026-08-10.md, raw/releases/updates-2026-08-11.md, raw/releases/updates-2026-08-13.md]
confidence: high
---

# Graphify

[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)（作者 Safi Shamsi，YC S26）的**开源代码知识图谱工具**（Python，Apache-2.0 + MIT）。约 106k star（2026-08）、1.2M+ PyPI 下载，最新 v0.9.41（2026-08-12，迭代高频）。将整个代码库（代码/文档/PDF/图片/视频/SQL/Terraform）转化为可查询的**知识图谱**，让 agent 以图查询替代 grep。^[raw/session-history/2026-07-23-mighty-star.md] ^[raw/releases/tool-updates-2026-08.md]

## 是什么

**多模态知识图谱 builder。** tree-sitter AST 本地解析代码（零 LLM 成本）+ 语义提取文档/媒体，构建 NetworkX 图，配 HTML 可视化与报告。

## 关键特性

- **多模态**：代码(40+ 语言) + 文档/PDF/图片/视频/论文 URL 入同一图谱
- **Leiden 社区检测**：[[leiden-community-detection]] 自动识别子系统，零向量聚类，无需向量库
- **God Node 分析**：[[god-node-analysis]] 找桥梁节点、惊喜连接
- **边置信度**：每条边标记 `EXTRACTED` / `INFERRED` / `AMBIGUOUS`，"诚实置信度"
- **Token 压缩**：实测 71.5×（Karpathy 混合语料）
- **`--watch` / git hook**：文件保存自动增量重建；post-commit/post-checkout 钩子
- **`--wiki`**：每个社区生成 Wikipedia 风格 Markdown 页 + `index.md`，任何 agent 可浏览
- **`graphify export obsidian`**：导出 Obsidian vault
- **MCP server**：`python -m graphify.serve`

## 便携之处

```bash
uv tool install graphifyy    # PyPI 包名双 y
graphify install
/graphify .                  # 在 chat 中构建
graphify query "谁负责支付模块？"
graphify path "UserService" "DatabasePool"
```

## 架构（8 阶段管道）

```
detect() → extract() → build_graph() → cluster() → analyze() → report() → export()
```
独立模块、无共享状态，Python dict + NetworkX 图通信。

## 版本动态

- **v0.9.36（2026-08-07，correctness 版）**：修复 4 处静默失败（`cluster-only` 忽略 `--backend`/`--model`/`--batch-size` 时告警、community-label 提示词与丢弃哨兵不再冲突、`tree --root` 根无匹配时非零退出、`cluster-only` 从分析图中盖 `built_at_commit`）；Swift 跨文件 `extension` 不再丢调用边；node-id 冲突消解改为确定性（生命周期罚分 + 路径段逆序平局）；Windows skill 改用 PowerShell 可运行。^[raw/releases/updates-2026-08-08.md]
- **v0.9.37（2026-08-08，correctness 版）**：TypeScript 成员调用不再仅凭接收者类型同名伪造高置信 `calls` 边——接收者类型须定义于同文件或被调用方实际导入，第三方 `import type { Repo }` 不再误绑本地同名 `class Repo`，表推断接收者降级为 INFERRED（#2553）；回调体内调用不再丢失（`wrapper(async (req) => { helper() })`，#2552）；Kotlin 补齐——`import` 节点此前静默丢弃现能解析、全限定调用 `com.example.Foo.bar()` 产出 `calls` 边、语法不可解析文件（如单行 `class C { val x }`）告警而非静默（#2526/#2550/#2551）；`graphify update` 重试上次提取失败的文件而非永久标记 up-to-date，毒化 manifest 下次运行自愈（#2543）；claude-cli 后端透出 stdout 信封内的 API 错误（如零退出码限流）而非当作空成功，零/非零退出两条路径均上报（#2554）。^[raw/releases/updates-2026-08-09.md]
- **v0.9.38（2026-08-09，correctness 版）**：修复 v0.9.37 回调作用域回归（#2568）——回调局部名改为仅作用域于自身 body，兄弟回调中同名局部不再抑制真实 `indirect_call`（只恢复丢失边、绝不伪造）；Kotlin 属性初始化器调用纳入——类属性 `val repo = createRepo()`、`by lazy { }` 委托、伴生对象属性、顶层属性初始化器均产出 `calls` 边（含全限定调用），纯字面量初始化器不产边（#2565）；Swift 接收者类型推断补 `@Environment(Store.self)` 属性与工厂初始化绑定（`let x = ServiceFactory.make()`），opaque `some P`/数组/语料外返回类型仍保持未解析而不猜测（#2561）；SQL 提取器不再对 `WITH cte AS (...)` 名称产出 `reads_from` 边——CTE 名限定于自身查询，不再生成可能绑定到无关同名符号的裸 stub（#2577）；嵌套函数/模块作用域内的动态 `await import('…')` 现在产出边，`dynamic_import` 边纳入 `affected`，已被捕获的 deferred `imports_from` 不重复计数（#2575）。^[raw/releases/updates-2026-08-10.md]

- **v0.9.39（2026-08-10，correctness 版）**：修复函数内/模块作用域动态 `import('…')` 的 `affected` 缺口（#2584）——0.9.38 的 dedupe 只按目标键控，函数内动态 import（其符号级边锚定在外层函数）抑制了 `affected` 追踪的文件级边，现改为按导入文件键控，每文件/目标产出一条文件级 `dynamic_import` 边并保留调用点边；Python 无类型接收者的成员调用（`x.get(...)`）不再仅凭同名模块级函数绑定，伪造高置信 `calls` 边与 god node（#2417/#2586）——现仅凭接收者类型/import/`self`/`cls`/`super` 证据解析（与 0.9.37 TypeScript 修复一致），`super().method()` 仍解析；fuzzy dedup 不再过度合并同文件内长标签仅差一个内容词的两个实体（#2576）——一词差异按差异 token 判断而非前缀加权整体相似度，`asset contribution flow` 与 `asset consumption flow` 保持分离，真 typo 与空白/大小写变体仍折叠；`graphify watch` 对纯文档删除批次立即重建而非只标记（#2580），被删文档节点即时驱逐（大规模删文件泄漏已在 0.9.10 修复，此关闭 live-watcher 残留）；Objective-C 成员调用解析三连（#2589/#2590/#2591）——`@protocol` 声明不再被当作接收者类型（与同名 class 冲突）、category/类扩展 `@interface Foo (Bar)` 折叠进基类而非制造重复节点、发给 `@property`/ivar 接收者的消息（`[self.svc run]`/`[_svc run]`）现经属性/ivar 声明类型解析。^[raw/releases/updates-2026-08-11.md]

- **v0.9.41（2026-08-12，correctness/determinism/data-integrity 版）**：`graphify update` 拒绝用因本次提取器失败而缩小的图覆盖好数据（#2663），真删除仍允许缩小；JS/TS `catch` 绑定作调用实参不再对无关同名可调用对象伪造 `indirect_call` 边（#2568，完成 0.9.38/0.9.40 的箭头参数修复链）；`Cargo.toml` 识别为包清单（#2434），铸造规范包节点 + `depends_on` 边；显式传入的扫描根不再被父目录 `.gitignore` 中未锚定模式排除（#2468）；API 提取提示词指示后端捕获每节点 `rationale` 属性（#2482，与 skill 路径一致），使语义缓存块失效并在下次重提取；`source_file` 规范化到 POSIX 分隔符（#2627）——Windows 相对输入不再产生不可移植节点 id；warm cache 命中不再把 CWD 相对 `source_file` 重新锚定到与图根不同的幽灵路径（#2632）；wiki/obsidian audit trail 每条 incident 边只计一次，不再重复计社区内边（#2635）；C# 预处理器 `#if … #endif` 块内成员现被提取并挂到所属类（#2634）；`query` 在未裁节点时不再打印截断横幅（#2601），真截断仍告警；PHP 带前导反斜杠/全限定前缀的 `use` import 解析到目标定义（#2661）；未解析的本地 JS/TS import（目标不在扫描内）发出稳定可移植的 `ref` 目标 id，而非按 checkout 的绝对路径 slug（#2457）；`graphify benchmark` 不再因标签为 `None` 的节点崩溃（#2674）。^[raw/releases/updates-2026-08-13.md]

## 相关

- 概念：[[leiden-community-detection]]、[[god-node-analysis]]
- 工具：[[codegraph]]（最接近的竞品）、[[openwiki]]、[[qmd]]
- 对比：[[openwiki-vs-graphify-vs-codegraph]]