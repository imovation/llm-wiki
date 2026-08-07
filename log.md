# Wiki 日志

> 所有 wiki 操作的按时间顺序记录。仅追加。
> 格式：`## [YYYY-MM-DD] action | subject`
> 动作：ingest, update, query, lint, create, archive, delete
> 当此文件超过 500 条记录时，轮换：重命名为 log-YYYY.md，重新开始。

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
