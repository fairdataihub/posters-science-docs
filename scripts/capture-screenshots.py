#!/usr/bin/env python3
"""Capture screenshots of posters.science for documentation.

Uses system Chrome in headless mode. Requires google-chrome or chromium
to be installed and accessible on PATH.
"""

import os
import subprocess

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "public")

PAGES = [
    ("https://posters.science", "landing-page.png"),
    ("https://posters.science/discover", "discover-page.png"),
    ("https://posters.science/share/new", "share-page.png"),
    ("https://posters.science/login", "login-page.png"),
    ("https://posters.science/signup", "signup-page.png"),
]

CHROME = "google-chrome"
VIEWPORT = "1440,900"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for url, filename in PAGES:
        filepath = os.path.join(OUTPUT_DIR, filename)
        result = subprocess.run(
            [
                CHROME,
                "--headless",
                "--disable-gpu",
                f"--screenshot={filepath}",
                f"--window-size={VIEWPORT}",
                url,
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"Captured: {filename} ({size:,} bytes)")
        else:
            print(f"Failed: {filename}")
            if result.stderr:
                print(f"  {result.stderr[:200]}")

    print(f"\nScreenshots saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
