import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

REPO_ROOT = Path.cwd()
PAGES_DIR = REPO_ROOT / "v3-src" / "pages"
ASSETS_DIR = REPO_ROOT / "v3-src" / "assets"
TEMPLATES_DIR = REPO_ROOT / "v3-src" / "templates"
LAYOUT_NAME = "layout.html"
OUT_DIR = REPO_ROOT / "build"

env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), autoescape=False)
layout_template = env.get_template(LAYOUT_NAME)


def ensure_parent(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)


def build_pages():
    for html_file in PAGES_DIR.glob("*.html"):
        page_html = html_file.read_text(encoding="utf-8")
        rendered = layout_template.render(content=page_html)
        dest = OUT_DIR / html_file.name
        ensure_parent(dest)
        dest.write_text(rendered, encoding="utf-8")
        print(f"Rendered: {html_file} -> {dest}")


def copy_assets():
    if ASSETS_DIR.exists():
        for asset in ASSETS_DIR.rglob("*"):
            if asset.is_file():
                dest = OUT_DIR / asset.relative_to(ASSETS_DIR)
                ensure_parent(dest)
                shutil.copy2(asset, dest)
                print(f"Copied: {asset} -> {dest}")


def main():
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_pages()
    copy_assets()


if __name__ == "__main__":
    main()
