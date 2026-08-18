---
title: qmd
created: 2026-08-07
updated: 2026-08-18
type: entity
tags: [qmd, knowledge-base, cli, search]
sources: [raw/session-history/2026-07-18-misty-river.md, raw/articles/llm-wiki.md, raw/articles/llm-wiki.zh.md, raw/releases/tool-updates-2026-08.md, raw/releases/updates-2026-08-18.md]
confidence: high
---

# qmd

[tobi/qmd](https://github.com/tobi/qmd)（Query Markup Documents），作者 tobi。**全本地 Markdown 混合搜索引擎**。TypeScript（Bun/Node.js），MIT，约 28.9k star，最新发布 tag v2.8.3（2026-08-16）。^[raw/session-history/2026-07-18-misty-river.md] ^[raw/releases/tool-updates-2026-08.md]

> **版本口径说明（2026-08-08 记，2026-08-18 更新）**：CHANGELOG 记录至 2.6.3（2026-06-24，含 `qmd embed --timeout` 等新能力），但 GitHub tags 与 npm 曾停留在 v2.5.3——2.6.x 未正式发 tag；**2026-08-16 上游发布 v2.8.3 tag**（2.7/2.8 未逐版发 tag），刷新为发布 tag 最新版。本页以发布 tag 为准，追踪口径为 `github-tags`。

这是 [Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 中提到的 "wiki 规模扩大后的可选搜索方案"。

## 是什么

给你的笔记/文档/知识库装上一套混合搜索引擎：**BM25 关键词 + 向量语义 + LLM 重排序**，全设备端运行，CLI/MCP/SDK 三种方式给 AI agent 用。

## 安装与基本流程

```bash
npm install -g @tobilu/qmd
qmd collection add ~/notes --name notes
qmd context add qmd://notes "个人笔记和想法"   # 添加上下文（关键特性）
qmd embed
qmd query "部署流程"
```

## 搜索管线

```
用户查询 → 查询扩展(微调 LLM ×2权重) + 原查询
        → 原查询 FTS5+向量 / 扩展1 / 扩展2
        → RRF 融合 + Top-Rank Bonus + Top30
        → LLM 重排(qwen3-reranker, 本地 GGUF)
        → 位置感知混合
```

三个本地 GGUF 模型（首次使用自动下载到 `~/.cache/qmd/models/`）：embeddinggemma-300M（嵌入）、qwen3-reranker-0.6b（重排）、qmd-query-expansion-1.7B（查询扩展）。支持 `QMD_EMBED_MODEL` 环境变量切换（如 Qwen3-Embedding 提升中日韩）。

## Score 融合

- **RRF**：`Σ(1/(k+rank+1))`, k=60
- Top-Rank Bonus：#1 +0.05，#2-3 +0.02
- 位置感知混合：顶部重排权重低，防止淹没精确匹配

## 版本动态

- **v2.8.3（2026-08-16，安全加固 + 大修版，自 v2.5.3 跳跃）**：
  - **安全加固（重点）**：项目本地 `.qmd/index.yml` 的 `update:` 命令不再未经审批执行——该文件随 `git clone` 带入并被自动采纳，克隆仓库后跑 `qmd update` 会执行别人写的 shell 命令；终端下逐条列出征询、无人在场则跳过并继续索引。审批记入 `<config dir>/trusted.json`（按配置文件与命令集），编辑命令或 `git pull` 改写后重新询问；新增 `qmd trust` / `qmd trust list` / `qmd trust revoke` 管理，`QMD_TRUST_UPDATE_HOOKS=1` 恢复无人值守（#886）。同一信任门覆盖越出项目范围的 collection `path` 与非默认 `models.embed`/`models.rerank`/`models.generate` URI——越界目录跳过直到 `qmd trust`，自定义模型 URI 不加载不下载（#889）。索引不再跟随文件符号链接或 `../`/绝对 glob 越出 collection 目录，`qmd://` 文件系统解析同样做包含性检查（`qmd://collection/../../../etc/passwd` 失效）。`qmd mcp --http` 校验每请求 `Origin`/`Host`，非 loopback 一律 403——绑 localhost 防不了用户浏览器 DNS rebinding 读走语料；`QMD_ALLOWED_ORIGINS`/`QMD_ALLOWED_HOSTS` 扩白名单，`--host 0.0.0.0` 通配绑定启动时告警（#881）。
  - **MCP 协议升级**：改用官方 TypeScript SDK 2.x，讲 2026-07-28 协议修订——HTTP 无会话（无 `Mcp-Session-Id`/initialize 握手/空闲 TTL）、实现 `server/discover`、Streamable HTTP POST 要求 `Mcp-Method`/`Mcp-Name`（不匹配 → `-32020`）、`tools/list` 确定性并带 `ttlMs`/`cacheScope`；2025-era stdio/HTTP 客户端仍兼容（#816）。现有工具（`query`/`get`/`multi_get`/`status`）不变。
  - **依赖与体验**：node-llama-cpp 3.18.1→3.20.0（llama.cpp b8390→b10361，2026-08-11）；`qmd pull`（及 embed/query 隐式下载）默认不再打印下载进度条——每几 KB 重绘曾以数千 token 淹没 agent 转录，`qmd pull --progress` 交互终端恢复（#776）；`--glob` 别名 `--mask`（OpenClaw 传 `--glob memory.md` 曾被静默忽略、落到默认 `**/*.md` 并撞重复 collection，#536）。
  - **修复要点**：`qmd cleanup` 补齐回收 content 与 FTS 空间（错误目录 update 只 tombstone 掉 `documents` 行，cleanup 现在删除未引用 content 哈希并跑 FTS5 `optimize`，`--dry-run` 报哈希，#550）；embedding 上下文池按权重文件尺寸而非默认 150MB/GGUF 计算（Qwen3-Embedding-0.6B 约 1190MB/2048-token，8 张卡上开 8 个曾耗竭 8GB VRAM，#799）；`qmd embed` 加独占锁（`.qmd-embed.lock`）防并发 `vectors_vec` 冲突（#825）；多 collection `-c A -c B` 改为逐库搜索后按分融合，不再全局 top-k 后过滤致假空（#775）；`store.searchVec`/SDK `searchVector` 用 store 自身 pinned embed 模型而非全局 `QMD_EMBED_MODEL`（#690）；`bin/qmd` trampoline 改 exec `process.execPath`，避开 nvm/fnm/mise 选错 Node major 的 `NODE_MODULE_VERSION`/`ERR_DLOPEN_FAILED`（#577/#319）；`--version` 改为构建期盖章 `dist/cli/build-info.json` 的 commit，不再 `git -C` 向上误报无关仓库 HEAD（#787）；`qmd doctor` 不再把 `.etag` sidecar 误报为坏 GGUF（#812）；`qmd mcp stop`/`--daemon` 校验 pidfile PID 仍属于 qmd 进程（回收 PID 视为 stale，#806）；Claude Code 插件 `source` 限定 `./skills`（安装 ~50KB 而非 ~230MB/9k+ 条目）并随发布 bump `marketplace.json` 版本（此前卡在 0.1.0，二月起的安装者从未收到技能更新，升级至 2.6.3 追赶，#790/#789）；UTF-16 代理对不再跨 chunk 边界切分（emoji 拆半被远程 API 拒收，#777）；CJK FTS 重建/带点 FTS 短语（`"1.0.21"`）匹配/`insertContext` `store_collections` 查找/legacy `fts5(name, body...)` schema 打开等多处修复。^[raw/releases/updates-2026-08-18.md]

## 相关

- 概念：[[llm-wiki-ecosystem]]（搜索层可选工具）
- 工具：[[openwiki]]、[[llm-wiki-compiler]]