---
source_url: https://github.com/langchain-ai/openwiki/releases
ingested: 2026-08-08
sha256: a0bcadea304ef5671bd5a1e361b782cba25a0518119f006920a32e214368f939
---

# OpenWiki Releases Changelog (v0.2.0 → v0.3.1)

> 来源：https://github.com/langchain-ai/openwiki/releases 摘录（2026-08-08 检索）
> 版本号：v0.3.1 为 latest（2026-08-05 发布）

## v0.3.1 (2026-08-05)

- fix: stop the internal link validator from falsely flagging valid links (#585)
- fix: fingerprint innermost cause and chain-walk origin tag (#589)

## v0.3.0 (2026-08-04)

- feat(#579): Improve coding-agent wiki prompts and make OpenWiki guidance optional and just-in-time
- feat(#371): validate wiki internal links after generation
- refactor(#560): expose openwiki agent graph factory
- fix(#555): report rejected and timed-out telemetry sends accurately
- fix(#547): preserve agent instructions when managed markers are malformed
- fix(#549): serialize concurrent environment saves and isolate temporary files
- fix(#577): fetch full git history in scheduled update workflows

## v0.2.5 (2026-07-31)

- feat(#455): implement native wiki visualizer for openwiki
- feat(#165): exclude paths from doc runs via `.openwikiignore`
- fix(#481): ignore stray oauth callback requests
- fix(#530): allow comma in model id for gateway/proxy routing identifiers
- fix(#504): route summarization history offload outside the documented repo
- chore(#500): improve health telemetry

## 0.2.4 (2026-07-29)

- feat(#436): implement langsmith connector for code brains
- feat(#192): add github copilot as a model provider for inference
- feat(#477): add support for multilingual output in openwiki agent
- feat(#418): support AWS SDK credential chain for Bedrock
- feat(#417): resilient HTTP for connectors (timeout + retry/backoff on 429/5xx)
- fix(#453): preserve contested local-wiki claims
- fix(#476): prune old checkpoints so sqlite storage doesn't grow unbounded
- fix(#215): prevent file/image content blocks from leaking into CLI output
- docs(#511): document requesty via the openai-compatible provider

## 0.2.3 (2026-07-23)

- feat(#199): generate mermaid diagrams in the generated wiki
- fix(#435): keep personal from following repository agent files
- fix(#285): preserve customized code workflows
- fix(#406): reject ".." traversal in docs-only write guard
- fix(#430): honor provider base url env overrides

## 0.2.2 (2026-07-21)

- feat(#428): add gemini 3.6 flash and 3.5 flash lite providers

## 0.2.1 (2026-07-20)

- feat(#374): overhaul the `openwiki --init` setup wizard
- feat(#332): support openrouter provider nesting
- feat(#328): support `OPENAI_BASE_URL` for the openai provider
- fix(#383): stop code-mode runs from targeting ~/.openwiki/wiki
- fix(#376): tolerate optional OKF index metadata
- fix(#373): align okf output with google v0.1

## 0.2.0 (2026-07-16)

- feat(#345): OKF + telemetry（OKF frontmatter validator、index.md 中间件、migrate-wiki-to-okf skill、匿名 CLI telemetry）
- feat(#154): gemini (ai studio) + gemini enterprise (vertex ai) providers，vertex model-family routing
- feat(#327): aws bedrock provider
- feat(#147): nebius token factory provider
- feat(#179): google vertex ai (claude) provider

## 背景：既有页面已覆盖的早期版本（0.1.x）

- 0.1.2 (2026-07-13)：nvidia nim provider、bitbucket pipelines example、deepagents 1.10.8
- "Make OpenWiki general purpose"（0.1.0 →）：Personal 模式、connectors（git-repo/gmail/notion/x/web-search/slack/mcp/hackernews）、OAuth、schedules、multi-provider