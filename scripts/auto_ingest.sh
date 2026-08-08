#!/usr/bin/env bash
# auto_ingest.sh — 检测工具更新并自动触发 wiki 摄取。
# cron 入口。流程：
#   1. check_updates.py 检测最新版本
#   2. 有更新（exit 1）→ 调 opencode run 让 agent 按 SCHEMA Ingest 流程处理
#   3. 摄取完成 → git 自动提交
#   4. 无更新 → 静默退出
set -u
WIKI="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$WIKI" || exit 2

LOGFILE="$WIKI/raw/releases/.auto-ingest.log"
stamp() { date '+%Y-%m-%d %H:%M:%S'; }

# 1) 检测
OUT="$(python3 "$WIKI/scripts/check_updates.py")"
rc=$?

if [ "$rc" -eq 0 ]; then
  exit 0
fi

echo "$(stamp) updates detected (rc=$rc)" >> "$LOGFILE"
echo "$OUT"

# 2) 找出今天生成的 updates-*.md
UPDATES="$(ls -t "$WIKI"/raw/releases/updates-*.md 2>/dev/null | head -1)"
if [ -z "$UPDATES" ]; then
  echo "$(stamp) no updates file found" >> "$LOGFILE"
  exit 1
fi

echo "$(stamp) ingesting: $(basename "$UPDATES")" >> "$LOGFILE"

# 3) 调用 opencode headless，让它执行 SCHEMA Ingest 流程
if command -v opencode >/dev/null 2>&1; then
  MSG="自动摄取任务：检测到工具更新，见 raw/releases/updates-*.md（最新一份为准）。
请按 SCHEMA.md 的 Ingest 流程处理：
1. 读取所有 raw/releases/updates-*.md（取最新）
2. 逐个工具更新对应 entities/*.md 页面（frontmatter 的 updated/sources + 正文版本信息）
3. 更新 index.md 对应摘要（如需）
4. 追加 log.md 记账（action: ingest）
5. 运行 python3 scripts/lint.py，确保 0 问题
6. 完成后运行 git add -A 与 git commit，message 格式：'ingest: <日期> 监控工具更新'（详情供仓库记录）
只做上述摄取，不要做其他修改。"
  opencode run "$MSG"
  echo "$(stamp) opencode ingest done (rc=$?)" >> "$LOGFILE"
else
  echo "$(stamp) opencode not found — manual ingest required" >> "$LOGFILE"
  echo "WARN: opencode 不在 PATH，无法自动摄取。请手动执行 Ingest 或安装 opencode。"
fi

# 4) git 自动提交（若摄取产生变更；scm 不可用时跳过）
commit_auto() {
  if ! command -v git >/dev/null 2>&1; then
    echo "$(stamp) git not found — skip commit" >> "$LOGFILE"
    return 0
  fi
  cd "$WIKI" || return 1
  if git diff --quiet && git diff --cached --quiet; then
    echo "$(stamp) no changes to commit" >> "$LOGFILE"
    return 0
  fi
  DAY="$(date '+%Y-%m-%d')"
  if git add -A && git commit -m "ingest: $DAY auto updates" >/dev/null 2>&1; then
    echo "$(stamp) committed" >> "$LOGFILE"
  else
    echo "$(stamp) commit failed" >> "$LOGFILE"
  fi
  if git remote -v | grep -q origin; then
    if git push origin main >/dev/null 2>&1; then
      echo "$(stamp) pushed to origin" >> "$LOGFILE"
    else
      echo "$(stamp) push failed (remote may be unavailable)" >> "$LOGFILE"
    fi
  fi
}
commit_auto