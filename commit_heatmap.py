#!/usr/bin/env python3
"""
สแกน git repo ทั้งหมดใน ~/Desktop/Rudy
นับจำนวน commit ต่อวันของ author email ที่กำหนด
แล้ว export เป็น JSON สำหรับทำ heatmap (รูปแบบเดียวกับ GitHub contribution graph)

วิธีใช้:
    python3 commit_heatmap.py

Output:
    commit_heatmap.json  -> { "YYYY-MM-DD": จำนวน commit, ... }
"""

import os
import json
import subprocess
from collections import defaultdict

# ---------- ตั้งค่า ----------
BASE_DIR = os.path.expanduser("~/Desktop/Rudy")
AUTHOR_EMAIL = "chaiwat.s@merudy.com"
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "commit_heatmap.json")
# ------------------------------


def find_git_repos(base_dir):
    """หาโฟลเดอร์ที่เป็น git repo (มี .git อยู่ข้างใน) ทั้งหมดใต้ base_dir"""
    repos = []
    for root, dirs, _files in os.walk(base_dir):
        if ".git" in dirs:
            repos.append(root)
            dirs.remove(".git")  # ไม่ต้องเดินเข้าไปใน .git เอง
    return repos


def count_commits(repo_path, author_email):
    """คืนค่า list ของวันที่ (YYYY-MM-DD) ของ commit ที่ author ตรงกับ email ที่กำหนด"""
    try:
        result = subprocess.run(
            [
                "git", "-C", repo_path, "log",
                f"--author={author_email}",
                "--date=short",
                "--pretty=format:%ad",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"  [ข้าม] {repo_path}: {e}")
        return []

    return [line for line in result.stdout.strip().split("\n") if line]


def main():
    if not os.path.isdir(BASE_DIR):
        print(f"ไม่พบโฟลเดอร์: {BASE_DIR}")
        return

    print(f"กำลังสแกน git repo ใน: {BASE_DIR}")
    repos = find_git_repos(BASE_DIR)
    print(f"พบ {len(repos)} repo(s)\n")

    counts = defaultdict(int)
    total = 0

    for repo in repos:
        dates = count_commits(repo, AUTHOR_EMAIL)
        if dates:
            print(f"- {os.path.relpath(repo, BASE_DIR)}: {len(dates)} commit(s)")
        for d in dates:
            counts[d] += 1
            total += 1

    sorted_counts = dict(sorted(counts.items()))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted_counts, f, ensure_ascii=False, indent=2)

    print(f"\nรวมทั้งหมด: {total} commit(s) โดย {AUTHOR_EMAIL}")
    print(f"เขียนผลลัพธ์ไปที่: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
