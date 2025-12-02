"""
Static Site Generator for SimpleHTML5 v3

This script builds a static website by:
1. Reading HTML page files from v3-src/pages/
2. Rendering each page through the layout.html template
3. Writing the final HTML to build/
4. Copying all assets from v3-src/assets/ to build/

Usage:
    python build-v3.py
"""

import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Define the project root directory (where this script is located)
REPO_ROOT = Path.cwd()

# Directory containing individual page HTML files to be built
PAGES_DIR = REPO_ROOT / "v3-src" / "pages"

# Directory containing static assets (CSS, JS, images, etc.) to copy to /build
ASSETS_DIR = REPO_ROOT / "v3-src" / "assets"

# Directory containing Jinja2 template files (layout.html)
TEMPLATE_DIR = REPO_ROOT / "v3-src" / "templates"

# Name of the master layout template that wraps all page content
LAYOUT_NAME = "layout.html"

# Output directory where the built static site will be generated
OUT_DIR = REPO_ROOT / "build"

# Initialize Jinja2 template environment
# FileSystemLoader tells Jinja2 where to find template files
# autoescape=False allows raw HTML in templates without escaping
env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)), autoescape=False)

# Load the master layout template that will wrap all page content
layout_template = env.get_template(LAYOUT_NAME)


def ensure_parent(path: Path):
    """
    Create parent directories for a given path if they don't exist.

    Args:
        path (Path): The file path whose parent directories should be created
    """
    # Create all parent directories; parents=True creates intermediate dirs,
    # exist_ok=True doesn't error if they exist
    path.parent.mkdir(parents=True, exist_ok=True)


def build_pages():
    """
    Build all HTML pages by rendering them through the layout template.

    Process:
    1. Find all .html files in v3-src/pages/
    2. Read each page file's HTML content
    3. Render the page through layout.html with content={{ content }}
    4. Write the final HTML to build/
    """
    # Glob finds all .html files in the pages directory (non-recursive)
    for html_file in PAGES_DIR.glob("*.html"):
        # Read the page file as a string
        page_html = html_file.read_text(encoding="utf-8")

        # Render the page through the layout template
        # The layout template receives the page content via the {{ content }}
        rendered = layout_template.render(content=page_html)

        # Determine output path: keep same filename in build/ directory
        dest = OUT_DIR / html_file.name

        # Create parent directories if needed
        ensure_parent(dest)

        # Write the final rendered HTML to the output file
        dest.write_text(rendered, encoding="utf-8")

        # Print status message showing source and destination
        print(f"Rendered: {html_file} -> {dest}")


def copy_assets():
    """
    Copy all static assets from v3-src/assets/ to build/.

    Preserves the directory structure of assets when copying.
    """
    # Only proceed if the assets directory exists
    if ASSETS_DIR.exists():
        # rglob("*") recursively finds all files in assets/ and subdirectories
        for asset in ASSETS_DIR.rglob("*"):
            # Only copy files, skip directories
            if asset.is_file():
                # Calculate relative path from assets dir to preserve structure
                # e.g., assets/css/style.css -> css/style.css
                relative_path = asset.relative_to(ASSETS_DIR)

                # Build destination path in build directory
                dest = OUT_DIR / relative_path

                # Create parent directories in build/ if needed
                ensure_parent(dest)

                # Copy the file, preserving metadata like modification time
                shutil.copy2(asset, dest)

                # Print status message showing source and destination
                print(f"Copied: {asset} -> {dest}")


def main():
    """
    Main build process:
    1. Clean the build directory (remove old build if it exists)
    2. Create a fresh build directory
    3. Build all pages through the layout template
    4. Copy all assets to the build directory
    """
    # Remove the existing build directory to start fresh
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)

    # Create a fresh, empty build directory
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Build all pages
    build_pages()

    # Copy all assets
    copy_assets()


# Entry point: only run main() if this script is run directly (not imported)
if __name__ == "__main__":
    main()
