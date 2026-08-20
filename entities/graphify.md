---
title: Graphify
created: 2026-08-07
updated: 2026-08-20
type: entity
tags: [graphify, knowledge-base, cli]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/session-history/2026-07-20-cosmic-harbor.md, raw/session-history/2026-07-23-mighty-star.md, raw/releases/tool-updates-2026-08.md, raw/releases/updates-2026-08-08.md, raw/releases/updates-2026-08-09.md, raw/releases/updates-2026-08-10.md, raw/releases/updates-2026-08-11.md, raw/releases/updates-2026-08-13.md, raw/releases/updates-2026-08-14.md, raw/releases/updates-2026-08-18.md, raw/releases/updates-2026-08-20.md]
confidence: high
---

# Graphify

[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)（作者 Safi Shamsi，YC S26）的**开源代码知识图谱工具**（Python，Apache-2.0 + MIT）。约 108k star（2026-08）、1.2M+ PyPI 下载，最新 v0.9.47（2026-08-19，迭代高频）。将整个代码库（代码/文档/PDF/图片/视频/SQL/Terraform）转化为可查询的**知识图谱**，让 agent 以图查询替代 grep。^[raw/session-history/2026-07-23-mighty-star.md] ^[raw/releases/tool-updates-2026-08.md]

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

- **v0.9.42（2026-08-13，correctness/determinism/portability 版）**：JS/TS `for...of`/`for...in` 循环绑定遮蔽——不再伪造 `indirect_call` 边（#2685，完成 loop/closure/catch 遮蔽家族 #2568/#2569/#2517）；Python 相对子包 import（`from ..pkg.sub import x`）解析到包 `__init__`（#2688）；树中 FIFO/设备等非普通文件不再挂起提取、直接跳过（#2463）；装了但坏的 tree-sitter-sql 下 `.sql` 文件解析失败报真实错误而非"未安装"（#2602）；`graphify update` 在同一 mtime tick 内重写到等长文件会重新入队（#2466，补 0.9.40 文件哈希守卫）；`built_at_commit` 溯源从被分析仓库而非 shell cwd 盖章（#2699）；损坏语义缓存条目浮出并重新提取而非静默错过（#2683）；`graph_has_legacy_ids` 不再对全局 MCP 节点 id 误报（#2408）；`source_file`/模型可见路径 POSIX 规范化、Windows 原子写入与安装加固（含只读打包 bundle，#2620/#2622/#2453）；`GRAPH_REPORT.md` 用可移植 basename 而非绝对主机路径（#2682）；`apm.yml` fallback 解析器捕获包版本（#2465）；`affected` 解析 `./` 相对 seed 而非静默空结果（#2707）；`graph.html` hyperedge 区域按凸包序描边、着色多边形不再自交（#2449）；Windows 可移植性测试修复、`ARCHITECTURE.md` 模块表刷新（doc 一致性测试）+ README CI/Windows 前提说明。^[raw/releases/updates-2026-08-14.md]

- **v0.9.46（2026-08-17，correctness/feature 版，自 v0.9.42 跳跃）**：node-id 规范化对组合字符序列 caseless 稳定——`casefold` 与 NFKC 不交换，单遍处理会留 `normalize_id(s) != normalize_id(s.casefold())`（如希腊语 ypogegrammeni 后接组合重音），现迭代 casefold+NFKC 至不动点；字母/数字 id 不变，既有图不重键。Java 注解现产出指向其类型的 `references` 边——含类字面量实参（`@Repeatable(Foo.class)`、`@Uses({A.class, B.class})`）与注解成员返回类型，容器注解不再成孤立岛；字符串/枚举实参不被误当类型引用（#2426）。`graphify query` 将 `_` 视为分词符（同 `-`），`user_service` 可匹配 `user-service` 标签，coverage-scaling 防无关单 token 噪声（#2473）。`post-checkout` 钩子在 HEAD 未变时跳过重建（如 `git checkout -b` 无起点），建分支不再触发全量图重建（#2421）。Markdown 节点携带 `node_kind`（`page`/`heading`），前导 YAML frontmatter 解析为受限净化属性挂到页节点；frontmatter 内 `#` 注释不再被误提取为标题（id 不变，既有 markdown 图不重键）。新增 Common Lisp `.lisp`/`.cl`/`.lsp`/`.asd` 提取（tree-sitter-commonlisp，可选 `[commonlisp]` extra）——包/类/函数/方法/generic/宏/变量定义器与同文件调用，`open`/`:use` 的包跨文件解析。`query` 节点集适配预算但边超预算时打印诚实的 "complete answer over budget" 及真实大小，不再静默返回数倍预算负载（#2784）。非 UTF-8 编码的 `.gitignore`/`.graphifyignore` 不再静默丢规则——按 UTF-8→UTF-16 BOM→宿主 codepage/latin-1 解码并告警（#2798）。节点 dedup 合并时超边成员重连至幸存节点而非静默丢弃（#2805）；剪枝源文件时清扫被遗留的度 0 外部 import 占位节点（真孤立节点带 `source_file` 不受影响，#2807）；同一节点对多关系边保留更具体关系（`calls`/`imports`/`inherits`…）而非被通用 `references`/`uses`/`mentions` 覆盖——此前真 `calls` 可被降级为 `references` 后从调用图掉落（#2803）。^[raw/releases/updates-2026-08-18.md]

- **v0.9.47（2026-08-19，correctness/portability 版）**：超时提取按文件块二分降级而非整块失败——单个慢文件不再拖掉同块其余文件，子进程/SDK/botocore 超时与超 context 走同一有界 split-and-merge 路径，无法拆分的单文件超时留未盖章、下次重试（#2866）；缓存按文件键控不再折叠符号链接——symlink 别名与目标各自独立身份，warm cache 下一个不再顶掉另一个，detect 层越界防护不变（#2832）；`graphify extract --out <dir>` 转换的 Office/Google-Workspace sidecar 不再写回被扫描源码树——sidecar 走 cache root、内容哈希仍锚定扫描根，只读/固定 checkout 保持干净（#2787）；git-hook 项目外读防护在 Windows 不再把有根无盘符路径（`\foo\bar`）误判为 cwd 相对（#2795）；partial-parse 告警不再硬编码指向已关闭的 Kotlin #2551 引用，改报幸存符号数（#2788）；Obsidian 导出社区标签保留非 ASCII 字母（Hangul/CJK/西里尔/带重音拉丁）不再塌缩成同一个下划线标签，graph-view 配色组查同名标签、颜色重新对齐（#2862）；JS/TS 工厂函数把可调用成员赋给本地对象字面量（`const api = {}; api.foo = fn`）现保留这些成员——API 对象建模在工厂下、被赋函数挂为方法（含箭头赋值与工厂内调用边），仅对证明为对象字面量绑定的标识符铸造 owner，不重燃 phantom-owner 泛滥，`contains` 边只发一次（#2745）；`graph.json` 字段序跨 read-rebuild 稳定——未变图上重跑 `graphify update` 产出字节级相同文件（#2582）；`graphify query` 答案开头声明打开的是哪个图及其节点数（CWD 下为相对、否则绝对）——父项目内查询不再静默用错语料而毫无提示（#2789）；`claude` 后端 extended-thinking 以 thinking 块开头的响应不再 `AttributeError: 'ThinkingBlock'`，改读首个文本块（#2697）；`graphify update`/`save_manifest` no-op 不再改写 `manifest.json` 时间戳——无变更时 `graphify-out/` 不再变脏、不再产生尾部 graph 提交，真实变更仍持久化（#2838）；C# 12 主构造器参数现在被遍历——`class Svc(IRepo repo)` 产出指向 `IRepo` 的 `references` 边、经 `repo` 的调用可解析，内置/类型参数类型不伪造（#2829）；AST 推导的 INFERRED 边带按关系键控的 rubric `confidence_score`（`uses` 0.95、`indirect_call`/未解析跨文件 `calls` 0.85）而非落在 rubric 禁止的 0.5 或扁平 0.8，INFERRED 默认 0.5→0.55 使每条无分数 INFERRED 边落在离散 rubric 集上（#2813）；存数值 `confidence` 的旧版 `graph.json`（pre-enum）增量重载不再每条边告警一次——数值归一为 INFERRED 标签、原浮点存进 `confidence_score`。^[raw/releases/updates-2026-08-20.md]

## 相关

- 概念：[[leiden-community-detection]]、[[god-node-analysis]]
- 工具：[[codegraph]]（最接近的竞品）、[[openwiki]]、[[qmd]]
- 对比：[[openwiki-vs-graphify-vs-codegraph]]