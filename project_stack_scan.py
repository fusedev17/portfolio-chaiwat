#!/usr/bin/env python3
"""
สแกน git repo ทั้งหมดใน ~/Desktop/Rudy
หาว่าแต่ละโปรเจกต์คืออะไร ทำปีไหน และใช้ tech stack อะไรบ้าง
(ตรวจจาก dependency file เช่น package.json, requirements.txt, composer.json ฯลฯ
 และ config file เช่น nuxt.config, next.config, tailwind.config เป็นต้น)

วิธีใช้:
    python3 project_stack_scan.py

Output:
    projects_stack.json -> list ของโปรเจกต์ พร้อมปีที่ทำ และ tech stack
"""

import os
import json
import subprocess

# ---------- ตั้งค่า ----------
BASE_DIR = os.path.expanduser("~/Desktop/Rudy")
AUTHOR_EMAIL = "chaiwat.s@merudy.com"  # ใช้กรองว่าปีไหนที่ "เรา" commit จริง (ถ้าอยากรวมทุกคนตั้งเป็น None)
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "projects_stack.json")
# ------------------------------

# key = ชื่อ dependency ที่ต้องเจอใน package.json, value = ชื่อที่จะแสดงผล
NPM_STACK_MAP = {
    "vue": "Vue.js",
    "nuxt": "Nuxt.js",
    "react": "React",
    "next": "Next.js",
    "typescript": "TypeScript",
    "tailwindcss": "Tailwind CSS",
    "@nestjs/core": "NestJS",
    "express": "Express",
    "vite": "Vite",
    "vuex": "Vuex",
    "pinia": "Pinia",
    "redux": "Redux",
    "axios": "Axios",
    "prisma": "Prisma",
    "mongoose": "MongoDB (Mongoose)",
    "sequelize": "Sequelize",
}

# key = ไฟล์/โฟลเดอร์ที่เจอในโปรเจกต์, value = tech ที่จะแสดงผล
FILE_STACK_MAP = {
    "requirements.txt": "Python",
    "Pipfile": "Python",
    "go.mod": "Go",
    "Gemfile": "Ruby",
    "pom.xml": "Java",
    "build.gradle": "Java/Kotlin",
    "composer.json": "PHP",
    "Dockerfile": "Docker",
    "docker-compose.yml": "Docker Compose",
}


def find_git_repos(base_dir):
    repos = []
    for root, dirs, _files in os.walk(base_dir):
        if ".git" in dirs:
            repos.append(root)
            dirs.remove(".git")
    return repos


def get_commit_years(repo_path, author_email=None):
    """คืน (ปีแรก, ปีล่าสุด) ของ commit ในโปรเจกต์นี้ (ค.ศ.)"""
    cmd = ["git", "-C", repo_path, "log", "--date=format:%Y", "--pretty=format:%ad"]
    if author_email:
        cmd.insert(4, f"--author={author_email}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError:
        return None, None

    years = sorted(set(y for y in result.stdout.strip().split("\n") if y))
    if not years:
        return None, None
    return years[0], years[-1]


def detect_stack_from_package_json(repo_path):
    stack = set()
    pkg_path = os.path.join(repo_path, "package.json")
    if not os.path.isfile(pkg_path):
        return stack
    try:
        with open(pkg_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return stack

    deps = {}
    deps.update(data.get("dependencies", {}))
    deps.update(data.get("devDependencies", {}))

    for dep_name, label in NPM_STACK_MAP.items():
        if dep_name in deps:
            stack.add(label)
    return stack


def detect_stack_from_files(repo_path):
    stack = set()
    try:
        entries = os.listdir(repo_path)
    except OSError:
        return stack
    for filename, label in FILE_STACK_MAP.items():
        if filename in entries:
            stack.add(label)
    return stack


def main():
    if not os.path.isdir(BASE_DIR):
        print(f"ไม่พบโฟลเดอร์: {BASE_DIR}")
        return

    print(f"กำลังสแกนโปรเจกต์ใน: {BASE_DIR}")
    repos = find_git_repos(BASE_DIR)
    print(f"พบ {len(repos)} repo(s)\n")

    projects = []

    for repo in repos:
        name = os.path.relpath(repo, BASE_DIR)
        start_year, end_year = get_commit_years(repo, AUTHOR_EMAIL)

        stack = set()
        stack |= detect_stack_from_package_json(repo)
        stack |= detect_stack_from_files(repo)

        year_label = ""
        if start_year and end_year:
            year_label = start_year if start_year == end_year else f"{start_year}-{end_year}"

        project_info = {
            "name": name,
            "year": year_label,
            "techStack": sorted(stack),
        }
        projects.append(project_info)

        print(f"- {name} | ปี: {year_label or 'ไม่พบ commit'} | stack: {', '.join(sorted(stack)) or '-'}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(projects, f, ensure_ascii=False, indent=2)

    print(f"\nเขียนผลลัพธ์ไปที่: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
