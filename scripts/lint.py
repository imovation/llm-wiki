#!/usr/bin/env python3
"""llm-wiki lint 脚本 — 实现 SCHEMA.md 的 Lint 清单。

用法: python3 scripts/lint.py  [要检查的 wiki 根路径，默认 ../]
退出码: 0 = 干净, 1 = 发现问题
"""
import os
import re
import sys
import hashlib

import yaml

WIKI = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(__file__)))
SKIP_DIRS = (".obsidian", "raw", ".git", "node_modules", "_archive")
CONFIG_SLUGS = ("index", "log", "schema", "agents")
FM_RE = re.compile(r"^---\n(.*?)\n---", re.S)
LINK_RE = re.compile(r"\[\[([^\]|#]*?)(?:\|[^\]]*)?\]\]")


def body_hash(path):
    """sha256 of the page body — everything after the frontmatter block,
    with the trailing blank-line separator (and any leading newlines) stripped."""
    txt = open(path, encoding="utf-8").read()
    m = FM_RE.search(txt)
    if not m:
        return None, txt
    return hashlib.sha256(txt[m.end() :].lstrip("\n").encode()).hexdigest(), txt


def walk_pages():
    pages = {}
    for root, dirs, files in os.walk(WIKI):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(".md"):
                path = os.path.join(root, f)
                pages[os.path.splitext(f)[0].lower()] = path
    return pages


def read_fm(path):
    m = FM_RE.search(open(path, encoding="utf-8").read())
    return yaml.safe_load(m.group(1)) if m else None


def main():
    pages = walk_pages()
    issues = []

    # 1. broken wikilinks
    for slug, path in pages.items():
        if slug in CONFIG_SLUGS:
            continue
        txt = re.sub(r"```.*?```", "", open(path, encoding="utf-8").read(), flags=re.S)
        for m in LINK_RE.finditer(txt):
            t = m.group(1).strip().lower()
            if t not in pages:
                issues.append(f"BROKEN  {path}: [[{m.group(1)}]]")

    # 2. orphan pages (no inbound link)
    inbound = set()
    for slug, path in pages.items():
        txt = open(path, encoding="utf-8").read()
        for m in LINK_RE.finditer(txt):
            inbound.add(m.group(1).strip().lower())
    for slug, path in sorted(pages.items()):
        if slug in CONFIG_SLUGS:
            continue
        if slug not in inbound:
            issues.append(f"ORPHAN  {path}")

    # 3. index completeness + page-count drift
    idx_path = os.path.join(WIKI, "index.md")
    idx = open(idx_path, encoding="utf-8").read()
    idx_links = {t.strip().lower() for t in LINK_RE.findall(idx)}
    for slug in pages:
        if slug not in CONFIG_SLUGS and slug not in idx_links:
            issues.append(f"NOT-IN-INDEX {slug}")
    for t in idx_links:
        if t not in pages:
            issues.append(f"INDEX-GHOST {t}")
    declared = re.search(r"总页面数[:：]?\s*(\d+)", idx)
    n_entries = len(idx_links)
    if declared and int(declared.group(1)) != n_entries:
        issues.append(f"INDEX-DRIFT declared={declared.group(1)} actual={n_entries}")

    # 4. frontmatter validation
    VALID_TYPES = {"entity", "concept", "comparison", "query", "schema", "summary"}
    for slug, path in sorted(pages.items()):
        if slug in CONFIG_SLUGS:
            continue
        data = read_fm(path)
        if data is None:
            issues.append(f"NO-FRONTMATTER {path}")
            continue
        miss = [k for k in ("title", "created", "updated", "type", "tags", "sources") if k not in data]
        if miss:
            issues.append(f"FM-MISS {path}: {miss}")
        t = data.get("type")
        if t and t not in VALID_TYPES:
            issues.append(f"BAD-TYPE {path}: {t}")
        c, u = data.get("created"), data.get("updated")
        if c and u and u < c:
            issues.append(f"DATE-INVERSION {path}: {c} -> {u}")
        if data.get("contested") is True or data.get("contradictions"):
            issues.append(f"CONTESTED {path}: review needed")

    # 5. sources path existence
    for slug, path in sorted(pages.items()):
        if slug in CONFIG_SLUGS:
            continue
        data = read_fm(path)
        if not data:
            continue
        for s in data.get("sources", []):
            if not os.path.exists(os.path.join(WIKI, s)):
                issues.append(f"BAD-SOURCE {path}: {s}")

    # 6. tag audit
    schema_txt = open(os.path.join(WIKI, "SCHEMA.md"), encoding="utf-8").read()
    known = set(re.findall(r"`([a-z-]+)`", schema_txt))
    used = set()
    for slug, path in pages.items():
        data = read_fm(path)
        if data:
            used.update(data.get("tags", []))
    for u in sorted(used - known):
        issues.append(f"UNKNOWN-TAG {u}")

    # 7. page size > 200
    for slug, path in sorted(pages.items()):
        if slug in CONFIG_SLUGS:
            continue
        n = sum(1 for _ in open(path, encoding="utf-8"))
        if n > 200:
            issues.append(f"PAGE>200 {path} ({n})")

    # 8. source drift (raw sha256)
    for root, _, files in os.walk(os.path.join(WIKI, "raw")):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            cur, _ = body_hash(path)
            m = FM_RE.search(open(path, encoding="utf-8").read())
            if not m:
                continue
            data = yaml.safe_load(m.group(1))
            stored = data.get("sha256")
            if not stored:
                continue
            if cur != stored:
                issues.append(f"RAW-DRIFT {os.path.relpath(path, WIKI)}")

    if issues:
        print(f"LINT: {len(issues)} issue(s) in {os.path.relpath(WIKI)}")
        for i in issues:
            print("  -", i)
        return 1
    print(f"LINT: clean — {len(pages)} pages, no issues.")
    return 0


if __name__ == "__main__":
    sys.exit(main())