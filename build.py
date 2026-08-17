#!/usr/bin/env python3
"""
Build script for the homepage. Converts markdown sections into a static HTML site.
Usage: python3 build.py
       python3 build.py --serve   (build and start local server on port 8000)
"""

import os
import re
import sys
import shutil
import yaml
from pathlib import Path
from markdown_it import MarkdownIt
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
BUILD_DIR = ROOT / "_site"
SECTIONS_DIR = ROOT / "_sections"
DATA_DIR = ROOT / "_data"
LAYOUTS_DIR = ROOT / "_layouts"
INCLUDES_DIR = ROOT / "_includes"
ASSETS_DIR = ROOT / "assets"

SECTION_ORDER = [
    "summary", "software", "projects", "skills", "publications",
    "awards", "interests", "editors", "committees", "reviewers",
    "activities", "students",
]

NAV_LABELS = {
    "summary": None,
    "software": "software",
    "projects": "projects",
    "skills": "skills",
    "publications": "papers",
    "awards": "awards",
    "interests": "interests",
    "editors": "editors",
    "committees": "committees",
    "reviewers": "reviewers",
    "activities": "activities",
    "students": "students/postdoc",
}


def load_sidebar_data():
    with open(DATA_DIR / "sidebar.yml") as f:
        return yaml.safe_load(f)


def auto_number_publications(html):
    """Add class="pub" to <p> tags inside <div class="pub-list"> that are not year headers."""
    YEAR_HEADER = re.compile(r'^<p><strong>-----\d{4}')
    parts = re.split(r'(<div class="pub-list">|</div>)', html)
    inside = False
    result = []
    for part in parts:
        if part == '<div class="pub-list">':
            inside = True
            result.append(part)
        elif part == '</div>' and inside:
            inside = False
            result.append(part)
        elif inside:
            part = re.sub(
                r'<p>(?!<strong>-----\d{4})',
                '<p class="pub">',
                part,
            )
            result.append(part)
        else:
            result.append(part)
    return ''.join(result)


def render_markdown(text):
    # Strip kramdown attribute syntax like {:target="_blank"} before rendering
    text = re.sub(r'\{:target="_blank"\}', '', text)
    md = MarkdownIt("commonmark", {"html": True})
    md.enable("table")
    html = md.render(text)
    # Make external links open in new tab
    html = html.replace('<a href="http', '<a target="_blank" href="http')
    html = auto_number_publications(html)
    return html


def render_sidebar(sidebar_data):
    html = '<div class="sidebar">\n'
    html += f'  <div class="photo"><img src="{sidebar_data["photo"]}" alt="{sidebar_data["name"]}"></div>\n'
    html += f'  <div class="info-block">{sidebar_data["title"]}</div>\n'
    html += f'  <div class="info-block">{sidebar_data["affiliation"]}</div>\n'
    html += '  <div class="info-block" style="font-weight: normal;">'
    for line in sidebar_data["address"]:
        html += f"{line}<br>"
    html += "</div>\n"
    html += f'  <div class="info-block">{sidebar_data["education"]}</div>\n'
    html += f'  <div class="membership">{sidebar_data["membership"]}</div>\n'
    html += '  <div class="email"><u>'
    html += " ".join(sidebar_data["emails"])
    html += "</u></div>\n"
    html += '  <div class="sidebar-links">\n'
    for link in sidebar_data["links"]:
        html += f'    <a href="{link["url"]}"><span class="arrow">&gt;&gt;</span> {link["text"]}</a>\n'
    html += "  </div>\n"
    html += "</div>\n"
    return html


def build_index(sidebar_data):
    nav_html = '<div class="section-nav">\n'
    for section_name in SECTION_ORDER:
        label = NAV_LABELS.get(section_name)
        if label:
            nav_html += f'  <a href="#{section_name}">{label}</a>\n'
    nav_html += "</div>\n\n"

    sections_html = ""
    for section_name in SECTION_ORDER:
        md_file = SECTIONS_DIR / f"{section_name}.md"
        if md_file.exists():
            md_text = md_file.read_text(encoding="utf-8")
            html_content = render_markdown(md_text)
            sections_html += f'<div id="{section_name}">\n{html_content}\n</div>\n\n'

    sidebar_html = render_sidebar(sidebar_data)

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dr. Sheng Di's Homepage</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

<div class="top-bar">
  <div class="name-cell">{sidebar_data['name']}</div>
  <div class="logos-cell">
    <img src="assets/images/argonne-logo-light.png" alt="Argonne">
    <img src="assets/images/glass.png" alt="" style="width:10px;">
    <img src="assets/images/uchicago-logo-light.png" alt="UChicago">
  </div>
</div>

<div class="page-wrapper">
{sidebar_html}
  <div class="content-area">
{nav_html}
<div class="content-body">
{sections_html}
</div>
  </div>
</div>

</body>
</html>
"""
    return page_html


def build_markdown_page(md_file, sidebar_data):
    md_text = md_file.read_text(encoding="utf-8")
    lines = md_text.split("\n")
    content_lines = []
    in_frontmatter = False
    frontmatter_count = 0
    for line in lines:
        if line.strip() == "---":
            frontmatter_count += 1
            if frontmatter_count <= 2:
                in_frontmatter = not in_frontmatter
                continue
        if not in_frontmatter or frontmatter_count > 2:
            content_lines.append(line)

    content_md = "\n".join(content_lines)
    content_html = render_markdown(content_md)

    sidebar_html = render_sidebar(sidebar_data)

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dr. Sheng Di's Homepage</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

<div class="top-bar">
  <div class="name-cell">{sidebar_data['name']}</div>
  <div class="logos-cell">
    <img src="assets/images/argonne-logo-light.png" alt="Argonne">
    <img src="assets/images/glass.png" alt="" style="width:10px;">
    <img src="assets/images/uchicago-logo-light.png" alt="UChicago">
  </div>
</div>

<div class="page-wrapper">
{sidebar_html}
  <div class="content-area">
{content_html}
  </div>
</div>

</body>
</html>
"""
    return page_html


def build():
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir()

    sidebar_data = load_sidebar_data()

    # Copy assets
    if ASSETS_DIR.exists():
        shutil.copytree(ASSETS_DIR, BUILD_DIR / "assets")

    # Copy download directory
    download_dir = ROOT / "download"
    if download_dir.exists():
        shutil.copytree(download_dir, BUILD_DIR / "download")

    # Copy photos_info.html if exists
    for extra_file in ["photos_info.html"]:
        src = ROOT / extra_file
        if src.exists():
            shutil.copy2(src, BUILD_DIR / extra_file)

    # Build index page
    index_html = build_index(sidebar_data)
    (BUILD_DIR / "index.html").write_text(index_html, encoding="utf-8")

    # Build other markdown pages (e.g., my-job-openings.md)
    for md_file in ROOT.glob("*.md"):
        if md_file.name in ("README.md",):
            continue
        page_html = build_markdown_page(md_file, sidebar_data)
        out_name = md_file.stem + ".html"
        (BUILD_DIR / out_name).write_text(page_html, encoding="utf-8")

    print(f"Site built successfully in {BUILD_DIR}/")
    print(f"  - index.html")
    for f in sorted(BUILD_DIR.glob("*.html")):
        if f.name != "index.html":
            print(f"  - {f.name}")


def serve():
    import http.server
    import functools

    os.chdir(BUILD_DIR)
    port = 8000
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(BUILD_DIR))
    with http.server.HTTPServer(("", port), handler) as httpd:
        print(f"Serving at http://localhost:{port}")
        print("Press Ctrl+C to stop.")
        httpd.serve_forever()


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        serve()
