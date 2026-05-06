#!/usr/bin/env python3
"""Capture screenshots of posters.science for documentation."""

from playwright.sync_api import sync_playwright
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "public")

PAGES = [
    ("https://posters.science", "landing-page.png"),
    ("https://posters.science/discover", "discover-page.png"),
    ("https://posters.science/overview", "overview-page.png"),
    ("https://posters.science/share", "share-page.png"),
]

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})

        for url, filename in PAGES:
            page = context.new_page()
            page.goto(url, wait_until="networkidle", timeout=30000)
            page.wait_for_timeout(2000)
            filepath = os.path.join(OUTPUT_DIR, filename)
            page.screenshot(path=filepath, full_page=False)
            print(f"Captured: {filename}")
            page.close()

        context.close()
        browser.close()

    print(f"\nScreenshots saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
