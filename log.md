# Wiki 日志

> 所有 wiki 操作的按时间顺序记录。仅追加。
> 格式：`## [YYYY-MM-DD] action | subject`
> 动作：ingest, update, query, lint, create, archive, delete
> 当此文件超过 500 条记录时，轮换：重命名为 log-YYYY.md，重新开始。

## [2026-08-08] ingest | OpenWiki 仓库 README 摄入
- 新增 raw/articles/openwiki-readme.md（github README 快照，body sha256 落盘，3-mode/12-provider 等新事实）
- entities/openwiki.md：特性 16 条重写（visualize 命令/`.openwikiignore` 读边界/no-op 快照/OKF detail/telemetry 精确边界/LangSmith connector code 模式细节/12 provider/OpenAI-ChatGPT Codex 后端/OpenRouter pinning/Windows bun 提示），新增「命令快览」表（openwiki/`-p`/ingest/auth/ngrok/visualize）
- queries/openwiki-usage.md 同步新命令集与配置细节
- index.md 摘要不动；log 追加；lint 待跑

## [2026-08-08] create | OpenWiki 使用说明归档
- 新增 queries/openwiki-usage.md（安装/命令/两模式工作流/CI/模型调试/局限，引用 07-18、07-23 两会话 + changelog）
- index.md 查询章节登记，页数 26→27（lint 校验通过）
- lint：32 页 0 问题

## [2026-08-08] update | openwiki 实体页架构细化
- 架构小节扩充：写保护设计（write guard/`..` 穿越拒绝、markers 保留 agent 指令、并发保存序列化）、输出卫生（内容块不泄漏、connector 超时/重试退避、telemetry 如实上报）、扩展性（agent graph factory、OPENAI_BASE_URL/gateway 路由）
- 版本表补全 0.2.1–0.2.3 行（向导重构、Gemini 新 provider、Mermaid 生成）
- 连接器条目补注：可配多实例，原始数据落 `~/.openwiki/connectors/<name>/raw/`
- 来源不变（changelog 已在 sources）

## [2026-08-08] ingest | OpenWiki v0.2.0 → v0.3.1 更新
- 用户提示 openwiki 有更新；本地已装 openwiki@0.3.1（2026-08-05 发布）
- 新增 raw/releases/openwiki-changelog-2026-08.md（sha256 记录，release 摘录）
- 关键新特性：原生 wiki 可视化器（v0.2.5）、.openwikiignore 排除（v0.2.5）、生成后内部链接验证（v0.3.0）、OKF 化+telemetry（v0.2.0）、LangSmith connector / GitHub Copilot provider / 多语言（0.2.4）

## [2026-08-08] update | openwiki 实体页 + 对比页
- entities/openwiki.md：star 数 12-13k→14.6k，新增版本表、8 条新特性（含架构 checkpoint 修剪）、sources 追加 changelog
- comparisons/openwiki-vs-graphify-vs-codegraph.md：视觉化 ❌→✅（原生 wiki visualizer）、stars 更新、sources 追加
- index.md 日期与摘要同步

## [2026-08-08] ingest | 生态工具版本盘点（openwiki 之外 7 项）
- 新增 raw/releases/tool-updates-2026-08.md（sha256），覆盖 nashsu/openspec/graphify/codegraph/compiler/qmd/comet
- 有版本更新：nashsu v0.6.7（08-02）、openspec 1.8.0（08-05）、graphify v0.9.35 + star 94k→104k、codegraph v1.5.0 Rust 引擎、compiler v1.1.0、qmd v2.6.3、comet 0.4.0-beta.14（Native 工作流/dashboard/eval）
- 无更新：hermes llm-wiki skill（v2.1.0）、langsmith（SaaS）

## [2026-08-08] query | Wiki 自动更新机制建设
- 会话归档：从 openwiki 更新摄取起步，建成并验证「检测→落盘→自动摄取→lint 门禁→git 提交推送」自动维护体系
- 交付：check_updates.py / auto_ingest.sh / tracked-projects.json（9 项目）/ cron / GHA 双保险 / README / 内容体检
- 修复：cron 环境（PATH/代理/超时）、GHA 误报（state 基线、grep 判定、YAML）、lint 硬门禁
- 状态：机制闭环，远程已同步，待明日 cron 与 GHA 首轮真机观察

## [2026-08-08] update | auto_ingest 加 lint 硬门禁
- commit 前强制跑 lint：摄取失败/不完整时绝不提交，lint 失败详情写入 .auto-ingest.log 留待人工
- 失败路径已测（注入断链 → lint 拦截 ✓）；当前 31 页 0 问题，仓库干净

## [2026-08-08] fix | GHA 重新验证通过（run 31237710818）
- 上一版修复中内联 python 多行字符串破坏 YAML → push 触发 run 直接失败、dispatch 422
- 改用 `grep -qE '\[check\].*->'` 修复判定（避免 grep 选项歧义 + YAML 嵌套引号）
- 云端复验：有基线后 `[check] no updates`，无 issue 误报；check-updates ✓ 9s、lint ✓ 10s 全绿
- 备注：PyYAML 1.1 把 `on:` 解析为 True 是检查陷阱，GitHub 解析器无碍（验证以 jobs 键为准）

## [2026-08-08] fix | GHA 误报修复（state 基线入库 + 判定修复）
- 排查发现 GHA 云端 check 有 2 个 bug：① .state.json 被 gitignore → 云端无基线 → 9 项目全部显示 (none)→误报；② grep -q "->" 把模式当选项报错 → has_updates 恒 no → issue step 永远 skipped
- 修复：.state.json 移出 gitignore 并入库（云端基线）；check 判定改用 python 正则；check_updates.py 无更新时不写盘（防 git 噪音）
- 本地模拟验证：基线场景 yes / 无更新 no；lint 31 页 0 问题

## [2026-08-08] update | GHA 云端验证 + README 维护机制 + cron 就绪
- 手动触发 auto-update-check workflow（run 31237444602）：lint ✓ 6s、check-updates ✓ 5s，全绿；仅 Node 20 弃用警告（非错误，不阻塞）
- README.md 新增「自动维护机制」章节（四环节表 + 触发方式）
- cron 确认激活：每日 09:00；下次 2026-08-09 09:00
- 观察点：明日首次真机运行后看 raw/releases/.cron.log 是否记录「no updates」静默退出

## [2026-08-08] update | 自动 lint 机制（GHA 每日巡检）
- 用户问询后确认补：SCHEMA.md lint 触发场景本含「维护时定期」，此前只实现了「关键动作后」
- auto-update-check.yml 新增 lint job：每日跑 scripts/lint.py，非零退出时开 issue（'lint: knowledge base issues'，去重）；不占本地资源
- 本地 cron 不重复加（避免双跑）；修复 github-script 变量笔误
- 至此三通道齐备：本地摄取门禁（已有）、GHA 版本检测（已有）、GHA 每日 lint 巡检（新增）

## [2026-08-08] update | 内容质量体检
- 孤儿源清零：2026-07-23-playful-planet（文档体系问答）→ spec-vs-wiki 传统文档分类表补充溯源；2026-08-07-proud-forest（本 wiki 搭建决策）→ llm-wiki-pattern 新增「元应用」小节 + llm-wiki-ecosystem 新增「选型经验」小节
- 单源页面审查：6 页均已有 confidence（SCHEMA #10 合规，不需降级）
- 无矛盾/contested 标记；lint：31 页 0 问题

## [2026-08-08] create | 远程仓库 + CI 兜底
- 关联现有公开仓库 imovation/llm-wiki 为 origin，main 已推送
- auto_ingest.sh 摄取提交后自动 push origin
- 新增 .github/workflows/auto-update-check.yml：GitHub Actions 每日检测上游版本，若本地 cron 未同步则开 issue 提醒（双保险）

## [2026-08-08] update | 追踪清单修复 + 端到端演练
- check_updates.py 新增 github-tags / raw（远端文件抓 frontmatter version）两种类型
- tracked-projects.json：qmd 由 npm 改 github-tags（npm 与 tags 均停在 v2.5.3，CHANGELOG 2.6.3 未发 tag）；新增 llm-wiki-skill 追踪（抓 hermes-agent SKILL.md 的 version 字段，2.1.0）；基线 9 项目
- entities/qmd.md 校准：以发布 tag v2.5.3 为准，加版本口径说明块
- **端到端演练成功**：模拟 graphify v0.9.35→v0.9.36 → auto_ingest.sh 全链路自动执行（检测→updates-2026-08-08.md→opencode 真实摄取→页面+index+log→lint→git commit 384aa71）
- lint：31 页 0 问题

## [2026-08-08] create | git 自动提交机制
- auto_ingest.sh 摄取完成后自动 git commit（`ingest: YYYY-MM-DD auto updates`），无变更则跳过
- .gitignore 补：scripts/.state.json、raw/releases/.auto-ingest.log、.cron.log
- 提交基线 commit aefc07b：自动机制全套 + 8 工具版本/star 同步 + 2 份 raw changelog
- SCHEMA.md 机制说明补「自动提交」与「仓库」条目；AGENTS.md 提示手动摄取也提交 git

## [2026-08-08] update | 自动更新机制对照补全
- 用户问询 openwiki 是否也有类似机制 → 补 entities/openwiki.md「自动更新机制」小节（定时重跑+PR vs 感知触发+agent）
- concepts/llm-wiki-ecosystem.md 新增「自动更新机制（生态内）」对照表
- 观点：盲跑适合守护性文档，感知触发适合追踪型知识

## [2026-08-08] create | 自动更新机制（检测→落盘→自动摄取）
- scripts/tracked-projects.json：8 个工具追踪清单（6 GitHub + 2 npm）
- scripts/check_updates.py：GitHub releases / npm dist-tags 检测，生成 raw/releases/updates-*.md（sha256 与 lint 口径一致），支持 --dry-run/--seed
- scripts/auto_ingest.sh：检测到更新 → opencode run 自动执行 SCHEMA Ingest 流程
- cron 已装：每日 09:00 运行 auto_ingest.sh；基线已 seed（8 项目）
- SCHEMA.md 登记「自动更新机制」；AGENTS.md 增加会话开始检查 updates-*.md 的规约

## [2026-08-08] update | 6 实体页版本/star 同步
- nashsu-llm-wiki（v0.6.7）、comet（0.4.0-beta 要点）、graphify（v0.9.35+104k）、codegraph（v1.5.0）、openspec（v1.8.0）、qmd（v2.6.3）、llm-wiki-compiler（v1.1.0）
- 对比页 stars 列同步（graphify 104k）；index 摘要同步

## [2026-08-07] create | Wiki 已初始化
- 领域：LLM Wiki 生态（模式、工具、规范、应用）
- 依据 Hermes [[llm-wiki-skill]] 方法论，在 /home/imovation/projects/llm-wiki 就地搭建
- 创建 SCHEMA.md、index.md、log.md，及 entities/ concepts/ comparisons/ queries/ 目录

## [2026-08-07] move | 源文件归档到 raw/
- llm-wiki.{md,zh.md}、SKILL.{md,zh.md}、okf-spec.{md,zh.md} 移入 raw/articles/，添加 source_url/ingested/sha256 frontmatter

## [2026-08-07] ingest | 历史会话导出
- 从 opencode.db 导出 6 个会话到 raw/session-history/（2026-07-18 至 2026-08-07）

## [2026-08-07] create | 实体页（10）
- codegraph、comet、graphify、langsmith、llm-wiki-compiler、llm-wiki-skill、nashsu-llm-wiki、openwiki、openspec、qmd

## [2026-08-07] create | 概念页（12）
- ast、cst-vs-ast、god-node-analysis、leiden-community-detection、llm-wiki-ecosystem、llm-wiki-pattern、lsp、okf、spec-vs-wiki、syntactic-sugar、three-layer-architecture、tree-sitter

## [2026-08-07] create | 对比页（2）
- graphify-vs-codegraph、openwiki-vs-graphify-vs-codegraph

## [2026-08-07] create | 查询页（1）
- handover-plan

## [2026-08-07] lint | 0 个问题
- 全量 wikilink 校验通过；修复若干候选链接与大小写（LSP→lsp）

## [2026-08-07] create | AGENTS.md 入口
- 项目根新增 AGENTS.md：指向 SCHEMA/index/log，规约每次会话先定位
- 使任何未来 agent 会话自动获得「纪律性维护员」身份

## [2026-08-07] query | 入职演练（新 agent 接管演练）
- 用全新 explore agent 模拟"只凭 wiki 接管"：零会话历史、唯一信息源是项目文件
- 结果成功：13 个文件内自足回答「spec-vs-wiki」与「离职交接产物」，逐句带 wikilink 溯源

## [2026-08-07] update | 演练发现的 3 处缺口修复
- index.md 页数漂移：24 → 25（与实际条目一致）
- sources 路径漂移：qmd.md、llm-wiki-skill.md 的 raw/ 路径改为 raw/articles/
- SCHEMA.md 新增「Lint 清单」：sources 路径存在性、index 自动计数、单一来源偏薄等规则（防止同类漂移再发生）

## [2026-08-07] create | 全局 skill + lint 脚本
- 创建全局 opencode skill `~/.config/opencode/skills/llm-wiki/`：任何目录/会话可触发，内置 WIKI_PATH 与 Ingest/Query/Lint 工作流
- 实现 `scripts/lint.py`：把 SCHEMA Lint 清单变成可执行工具（断链/孤页/index 完整性/sources 存在性/标签审计/raw sha256 漂移/页面大小）
- 修复 raw/session-history 6 个文件 frontmatter 的 YAML 引号问题（标题含冒号）
- lint 结果：29 页，0 问题

## [2026-08-07] delete | 全局 skill 移除
- 该 skill 定位反复后确认只需服务本项目 → 交付由 AGENTS.md（项目内）承担
- 删除 ~/.config/opencode/skills/llm-wiki/，从 ~/.profile 移除 WIKI_PATH 导出
- wiki/scripts/lint.py 保留（仓库自足），供任何接手 agent 使用

## [2026-08-07] create | 内容补齐（体检后优化）
- 新建 [[louvain-community-detection]]：nashsu 图谱的 Louvain vs Graphify 的 Leiden 对比；index 26 页
- llm-wiki-pattern 补「实操技巧」小节（Web Clipper/本地图片/Marp/Dataview/CLI/git），来源 raw/articles/llm-wiki.md
- openwiki-vs-graphify-vs-codegraph 追加指向 graphify-vs-codegraph 的专家链接
- Mermaid/FTS5 已在原页覆盖（无需新建）；lint.py 增强：type 枚举/created≤updated/contested 审查
- SCHEMA.md 同步 Lint 清单 #4
- lint：30 页 0 问题

## [2026-08-07] create | README 门面
- 新增 README.md：仓库门面（项目简介、三层结构、快速开始、内容全景、维护理念）
- lint.py 将 readme 纳入 CONFIG_SLUGS（豁免 frontmatter/index 要求）
- AGENTS.md 记录 README 的豁免地位
- lint：31 页 0 问题

## [2026-08-08] ingest | Graphify v0.9.35 → v0.9.36 更新
- cron 检测 raw/releases/updates-2026-08-08.md（sha256 已落盘）
- entities/graphify.md：正文版本更新为 v0.9.36（2026-08-07），新增「版本动态」小节（correctness 修复四点：静默失败告警、Swift 跨文件 extension 调用边、node-id 确定性冲突消解、Windows skill PowerShell），sources 追加 updates-2026-08-08.md
- index.md：graphify 摘要版本号同步 v0.9.36
- lint：通过
## [2026-08-08] query | opencode AI 原生开发环境搭建
- 用户问基于 opencode 的 AI 原生通用项目环境如何搭建
- 回答：五层框架（L0 安装连接 / L1 AGENTS.md 规则层 / L2 agent+permission / L3 skills 可复用能力 / L4 知识层 codegraph+openspec+wiki / L5 自动化）
- 引用 opencode 官方 docs（rules/agents/skills）+ 本 wiki 选型经验（proud-forest）
- 待定：是否归档为 queries/opencode-ai-env.md（需先摄入 opencode docs 到 raw/）
## [2026-08-09] ingest | Graphify v0.9.36 → v0.9.37、nashsu llm_wiki v0.6.7 → v0.6.8
- cron 检测 raw/releases/updates-2026-08-09.md（sha256 已落盘）
- entities/graphify.md：正文最新版本更新为 v0.9.37（2026-08-08），「版本动态」新增 correctness 修复五组：TS 成员调用伪边（import 门控 + 表推断降级 INFERRED）、回调体调用丢失、Kotlin import/全限定调用/不可解析告警、update 重试失败文件、claude-cli 信封错误透出；sources 追加 updates-2026-08-09.md
- entities/nashsu-llm-wiki.md：正文版本更新为 v0.6.8（2026-08-08），新增「版本动态」小节（GitHub Actions 自动发布、无发布说明）；sources 追加 updates-2026-08-09.md
- index.md：graphify 摘要同步 v0.9.37，头部日期更新 2026-08-09
- lint：通过

## [2026-08-10] ingest | Graphify v0.9.37 → v0.9.38
- cron 检测 raw/releases/updates-2026-08-10.md（sha256 已落盘）
- entities/graphify.md：正文最新版本更新为 v0.9.38（2026-08-09），「版本动态」新增 correctness 修复五组：回调作用域回归（兄弟回调同名局部不再抑制）、Kotlin 属性初始化器调用边（含 by lazy/伴生对象/顶层）、Swift @Environment/工厂绑定接收者推断、SQL CTE 名不再当表引用、嵌套/模块作用域动态 import 边纳入 affected；star 104k→105k；sources 追加 updates-2026-08-10.md
- index.md：graphify 摘要同步 v0.9.38，头部日期更新 2026-08-10
- lint：32 页 0 问题

## [2026-08-11] ingest | Comet 0.4.0-beta.16 → 0.4.0-beta.17、Graphify v0.9.38 → v0.9.39
- cron 检测 raw/releases/updates-2026-08-11.md（sha256 已落盘）
- entities/comet.md：正文最新版本更新为 0.4.0-beta.17（2026-08-10），新增「版本动态」小节（独立 Native 验证循环、Trae Hook 支持、Native 完成循环提速、便携式 `comet-state.yaml` 恢复、跨平台 Native 检查、doctor 识别 plugin-managed Superpowers、移除旧 Native 验证簿记）；star 2.4k→2.7k；sources 追加 updates-2026-08-11.md
- entities/graphify.md：正文最新版本更新为 v0.9.39（2026-08-10），「版本动态」新增 correctness 修复：函数内动态 import 的 affected 缺口（按文件键控 dedupe）、Python 无类型接收者成员调用不再伪造 calls 边/god node、fuzzy dedup 不再过度合并一词差异实体、watch 纯文档删除即时重建、Objective-C 成员调用解析三连；sources 追加 updates-2026-08-11.md
- index.md：graphify 摘要同步 v0.9.39，comet 摘要补充版本 0.4.0-beta.17，头部日期更新 2026-08-11
- lint：通过

## [2026-08-13] ingest | Graphify v0.9.39 → v0.9.41、OpenWiki v0.3.1 → v0.3.2
- cron 检测 raw/releases/updates-2026-08-13.md（sha256 已落盘）
- entities/graphify.md：正文最新版本更新为 v0.9.41（2026-08-12），「版本动态」新增 correctness/determinism/data-integrity 修复 13 项：update 拒绝用提取器失败缩小的图覆盖好数据、JS/TS catch 绑定伪造 indirect_call、Cargo.toml 包节点 + depends_on、扫描根不再被父目录 .gitignore 未锚定模式排除、API 提取 rationale 属性、source_file POSIX 规范化、warm cache 幽灵路径锚定、audit trail 单计数、C# 预处理块成员、query 截断横幅、PHP use 全限定解析、未解析 import 稳定 ref id、benchmark None 标签崩溃；star 105k→106k；sources 追加 updates-2026-08-13.md
- entities/openwiki.md：正文版本表新增 v0.3.2（2026-08-11）——pin js-yaml/undici、Windows stdio MCP 注入 APPDATA/LOCALAPPDATA、dist/cli.js exec bit、CLI/仓库领域模块重构 + 测试、错误分类与运行记账加固、credentials 拆分；star 14.6k→15k；sources 追加 updates-2026-08-13.md
- index.md：graphify 摘要同步 v0.9.41，openwiki 摘要同步 v0.3.2，头部日期更新 2026-08-13
- lint：通过

## [2026-08-14] ingest | Comet 0.4.0-beta.17 → 0.4.0-beta.18、Graphify v0.9.41 → v0.9.42、OpenSpec v1.8.0 → v1.9.0
- cron 检测 raw/releases/updates-2026-08-14.md（sha256 已落盘）
- entities/comet.md：正文最新版本更新为 0.4.0-beta.18（2026-08-13），「版本动态」新增：`comet eval` 独立 Skill 评估（去 comet-any 依赖、可选评估 agent Claude Code/Codex/Qoder/CodeBuddy、用户级 `~/.comet/eval/.env`、自动任务集、Langfuse 套件）、Native Supervisor Change 模式、worktree-aware Dashboard、WorkBuddy 平台支持、hook.allow_paths 白名单、Classic/OpenSpec 版本透传修复、依赖安全补丁（DOMPurify/Mermaid/Nanoid）；sources 追加 updates-2026-08-14.md
- entities/graphify.md：正文最新版本更新为 v0.9.42（2026-08-13），「版本动态」新增 correctness/determinism/portability 修复：for...of/in 循环绑定遮蔽不再伪造 indirect_call、Python 相对子包 import 解析到 __init__、FIFO/设备文件不再挂起提取、等长重写重入队、built_at_commit 从分析仓库盖章、损坏语义缓存重提取、source_file POSIX 规范化/Windows 安装加固、graph.html hyperedge 凸包描边等；sources 追加 updates-2026-08-14.md
- entities/openspec.md：正文最新版本更新为 v1.9.0（2026-08-13，Command Code & safer specs），新增「版本动态」小节（Command Code 工具支持、validate --archived、root 外诚实失败、场景计数、schema fork YAML 保真、.agents skills 所有权保护）；star 61.7k→64.8k；sources 追加 updates-2026-08-14.md
- index.md：graphify 摘要同步 v0.9.42，comet 摘要同步 0.4.0-beta.18，头部日期更新 2026-08-14
- lint：通过

## [2026-08-18] ingest | Graphify v0.9.42 → v0.9.46、nashsu llm_wiki v0.6.8 → v0.6.9、OpenWiki v0.3.2 → v0.3.3、qmd v2.5.3 → v2.8.3
- cron 检测 raw/releases/updates-2026-08-18.md（sha256 已落盘）
- entities/graphify.md：正文最新版本更新为 v0.9.46（2026-08-17），「版本动态」新增：node-id 规范化对组合字符 caseless 稳定（casefold+NFKC 迭代至不动点）、Java 注解产出指向类型的 references 边（类字面量/成员返回类型）、query 下划线分词、post-checkout HEAD 未变跳过重建、Markdown 节点 node_kind（page/heading）+ frontmatter 解析、Common Lisp 提取（可选 [commonlisp] extra）、query 超预算诚实告警、非 UTF-8 ignore 文件不静默丢规则、dedup 超边重连幸存节点、剪枝清扫孤立 import 占位节点、同对节点保更具体关系边；star 106k→108k；sources 追加 updates-2026-08-18.md
- entities/nashsu-llm-wiki.md：正文最新版本更新为 v0.6.9（2026-08-14），GitHub Actions 自动发布无说明（14 资产）；star 16.0k→16.5k；sources 追加 updates-2026-08-18.md
- entities/openwiki.md：版本表新增 v0.3.3（2026-08-14）——built-in custom-MCP 连接器、connector 工具仅 personal 运行门控、MCP 分页 nextCursor 跟随、openai-compatible 可选 responses API、CI workflow env 由 provider 生成、只读安装 bundled skills 同步、流式输出剥离终端控制序列、LangSmith APAC region、LEDGER 纵向基准、OpenAI 模型推理前校验 api-key、init 生成 CLAUDE.md 指向 AGENTS.md、OpenRouter MAX_TOKENS 上限；star 15k→15.2k；sources 追加 updates-2026-08-18.md
- entities/qmd.md：口径说明更新（v2.8.3 于 2026-08-16 发 tag，2.6.x 未发），新增「版本动态」小节——安全加固（项目本地 update hook 需 qmd trust 审批、路径/模型 URI 越界门控、符号链接与 ../ 索引越界封堵、mcp --http Origin/Host 校验防 DNS rebinding）、MCP 2026-07-28 协议（TS SDK 2.x）、node-llama-cpp 3.20.0、下载进度条默认关闭、--glob→--mask 别名、cleanup 回收 content/FTS 空间、embed 独占锁等；star 28k→28.9k；sources 追加 updates-2026-08-18.md
- index.md：graphify 摘要同步 v0.9.46，openwiki 摘要同步 v0.3.3，头部日期更新 2026-08-18
- lint：通过

## [2026-08-20] ingest | Graphify v0.9.46 → v0.9.47、OpenSpec v1.9.0 → v1.10.0
- cron 检测 raw/releases/updates-2026-08-20.md（sha256 已落盘）
- entities/graphify.md：正文最新版本更新为 v0.9.47（2026-08-19），「版本动态」新增 correctness/portability 修复 13 项：超时提取按文件块二分降级、缓存键控不再折叠 symlink、extract --out sidecar 不再写回源码树、Windows 无盘符路径读防护、partial-parse 告警去硬编码引用改报符号数、Obsidian 导出社区标签保留非 ASCII、JS/TS 工厂对象字面量成员建模（防 phantom-owner）、graph.json 字段序稳定、query 声明所用图与节点数、claude 后端 ThinkingBlock 崩溃修复、no-op 不再改写 manifest 时间戳、C# 12 主构造器 references 边、INFERRED 边 rubric confidence_score + 旧数值 confidence 归一；star 108k；sources 追加 updates-2026-08-20.md
- entities/openspec.md：正文最新版本更新为 v1.10.0（2026-08-19，Zed support & quieter installs），「版本动态」新增：Zed Agent 支持（.agents/skills、/openspec-propose）、init --language 非英语产物、零 install scripts 静默安装、任务计划须含验收判据、多选 picker 按键帮助、feedback 标题/正文修复、归档死路引导、stores specs 路径、profile 缺 sync、OpenCode 命令名丢失、telemetry 移 stderr、update 不再建议重启 IDE；star 64.8k→65.5k；sources 追加 updates-2026-08-20.md
- index.md：graphify 摘要同步 v0.9.47，openspec 摘要补充版本 v1.10.0，头部日期更新 2026-08-20
- lint：通过
