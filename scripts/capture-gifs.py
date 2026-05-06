#!/usr/bin/env python3
"""
Capture GIF recordings of the poster discovery workflow.

Requires: google-chrome, Pillow
Install: pip install Pillow

Uses system Chrome in headless mode to capture individual frames,
then assembles them into an animated GIF with Pillow.

The sharing flow GIF requires authentication, so it captures the
public discovery flow instead: landing -> discover -> search results.
"""

import os
import subprocess
import time
import glob
from PIL import Image

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "public")
FRAMES_DIR = os.path.join(OUTPUT_DIR, "_frames")

CHROME = "google-chrome"
VIEWPORT = "1280,800"


def capture_frame(url, frame_num, delay=0):
    """Capture a single frame using headless Chrome."""
    if delay:
        time.sleep(delay)

    filepath = os.path.join(FRAMES_DIR, f"frame_{frame_num:04d}.png")
    subprocess.run(
        [
            CHROME,
            "--headless",
            "--disable-gpu",
            f"--screenshot={filepath}",
            f"--window-size={VIEWPORT}",
            url,
        ],
        capture_output=True,
        timeout=30,
    )

    if os.path.exists(filepath):
        print(f"  Frame {frame_num}: {url}")
        return True
    return False


def capture_discovery_flow():
    """Capture the public discovery flow."""
    os.makedirs(FRAMES_DIR, exist_ok=True)
    frame_num = 0

    pages = [
        "https://posters.science",
        "https://posters.science/discover",
    ]

    for url in pages:
        if capture_frame(url, frame_num):
            frame_num += 1

    return frame_num


def assemble_gif(frame_count, output_name, duration=2500):
    """Assemble captured frames into an animated GIF."""
    frames = []
    for i in range(frame_count):
        path = os.path.join(FRAMES_DIR, f"frame_{i:04d}.png")
        if os.path.exists(path):
            img = Image.open(path)
            img = img.resize((960, 600), Image.Resampling.LANCZOS)
            frames.append(img.convert("P", palette=Image.ADAPTIVE, colors=256))

    if frames:
        output_path = os.path.join(OUTPUT_DIR, output_name)
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0,
            optimize=True,
        )
        size = os.path.getsize(output_path)
        print(f"GIF saved: {output_name} ({size:,} bytes, {len(frames)} frames)")
    else:
        print("No frames captured")


def cleanup_frames():
    """Remove temporary frame files."""
    for f in glob.glob(os.path.join(FRAMES_DIR, "*.png")):
        os.remove(f)
    if os.path.isdir(FRAMES_DIR):
        os.rmdir(FRAMES_DIR)


def main():
    print("Capturing discovery flow...")
    frame_count = capture_discovery_flow()

    print(f"\nAssembling {frame_count} frames...")
    assemble_gif(frame_count, "discovery-flow.gif")

    cleanup_frames()
    print("Done")


if __name__ == "__main__":
    main()
