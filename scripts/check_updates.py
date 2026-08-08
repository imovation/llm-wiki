#!/usr/bin/env python3
"""check_updates.py — 检测 tracked-projects.json 中所有工具/项目的最新版本。

流程:
1. 读取 scripts/tracked-projects.json（追踪清单）
2. 读取 scripts/.state.json（上次记录的版本）
3. 查询各项目最新版本（GitHub releases / npm dist-tags）
4. 有更新 → 生成 raw/releases/updates-YYYY-MM-DD.md（sha256 = 正文哈希，与 lint 口径一致）
5. 退出码: 0 = 无更新, 1 = 有更新（供 cron 判断是否触发摄取）

用法:
  python3 scripts/check_updates.py            # 检测并落盘
  python3 scripts/check_updates.py --dry-run  # 只报告不落盘
  python3 scripts/check_updates.py --seed     # 只记录当前版本为基线，不落盘
"""
import argparse
import datetime
import hashlib
import json
import os
import sys
import urllib.request

WIKI = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SCRIPTS = os.path.join(WIKI, "scripts")
TRACKED = os.path.join(SCRIPTS, "tracked-projects.json")
STATE = os.path.join(SCRIPTS, ".state.json")
RELEASES_DIR = os.path.join(WIKI, "raw", "releases")
UA = {"User-Agent": "llm-wiki-update-checker/1.0"}


def fetch_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def latest_github(repo):
    d = fetch_json(f"https://api.github.com/repos/{repo}/releases/latest")
    return d.get("tag_name") or d.get("name"), d.get("published_at", ""), d.get("html_url", "")


def latest_npm(pkg):
    d = fetch_json(f"https://registry.npmjs.org/{pkg}/latest")
    return d.get("version", ""), "", f"https://www.npmjs.com/package/{pkg}"


def query(project):
    t = project["type"]
    if t == "github":
        return latest_github(project["repo"])
    if t == "npm":
        return latest_npm(project["pkg"])
    raise ValueError(f"unknown type {t}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--seed", action="store_true",
                    help="只记录当前版本为基线（初始化/手动同步后使用）")
    args = ap.parse_args()

    with open(TRACKED, encoding="utf-8") as f:
        projects = json.load(f)

    state = {}
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as f:
            state = json.load(f)

    found = []
    for name, project in sorted(projects.items()):
        try:
            version, when, url = query(project)
        except Exception as e:
            print(f"[check] {name}: ERROR {e}", file=sys.stderr)
            continue
        prev = state.get(name, {}).get("version")
        if version != prev:
            found.append({"name": name, "page": project["page"], "version": version,
                          "published": when, "url": url, "previous": prev})
            print(f"[check] {name}: {prev or '(none)'} -> {version}")
        state[name] = {"version": version,
                       "checked": datetime.date.today().isoformat()}

    if not found:
        print("[check] no updates")
        if not args.dry_run:
            with open(STATE, "w", encoding="utf-8") as f:
                json.dump(state, f, ensure_ascii=False, indent=2)
        return 0

    if args.seed:
        print(f"[check] seed: {len(state)} projects baselined")
        with open(STATE, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        return 0

    date = datetime.date.today().isoformat()
    lines = ["| 项目 | 页面 | 新版本 | 上次记录 | 发布时间 |", "|---|---|---|---|---|"]
    for u in found:
        lines.append(
            f"| {u['name']} | `{u['page']}` | {u['version']} | {u['previous'] or '—'} | "
            f"{u['published'][:10] if u['published'] else '—'} |")
    body = "检测到以下工具/项目有新版本（由 `scripts/check_updates.py` 自动生成）：\n\n" + "\n".join(lines) + "\n"
    for u in found:
        body += (f"\n## {u['name']}（{u['version']}）\n"
                 f"- 页面：`{u['page']}`；上次记录版本：{u['previous'] or '无'}\n"
                 f"- 来源：{u['url'] or '—'}\n"
                 f"- 请按 SCHEMA.md 的 Ingest 流程：更新实体页 frontmatter/正文 → 登记 log.md → 跑 lint.py\n")

    if args.dry_run:
        print(body)
        return 1

    sha256 = hashlib.sha256(body.encode()).hexdigest()
    content = (f"---\n"
               f"source_url: {TRACKED} (automatic check)\n"
               f"ingested: {date}\n"
               f"sha256: {sha256}\n"
               f"---\n\n{body}")
    os.makedirs(RELEASES_DIR, exist_ok=True)
    path = os.path.join(RELEASES_DIR, f"updates-{date}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(f"[check] wrote {os.path.relpath(path, WIKI)}")
    return 1


if __name__ == "__main__":
    sys.exit(main())