# Wiki 日志

> 所有 wiki 操作的按时间顺序记录。仅追加。
> 格式：`## [YYYY-MM-DD] action | subject`
> 动作：ingest, update, query, lint, create, archive, delete
> 当此文件超过 500 条记录时，轮换：重命名为 log-YYYY.md，重新开始。

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