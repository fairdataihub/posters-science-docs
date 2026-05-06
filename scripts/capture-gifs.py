#!/usr/bin/env python3
"""
Capture GIF recordings of the poster sharing workflow.

Requires: playwright, Pillow
Install: pip install playwright Pillow && playwright install chromium

This script captures individual frames of the sharing flow
and assembles them into an animated GIF.
"""

from playwright.sync_api import sync_playwright
from PIL import Image
import os
import glob

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "public")
FRAMES_DIR = os.path.join(OUTPUT_DIR, "_frames")

def capture_sharing_flow():
    os.makedirs(FRAMES_DIR, exist_ok=True)
    frame_num = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        # Frame 1: Landing page
        page.goto("https://posters.science", wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(1500)
        page.screenshot(path=os.path.join(FRAMES_DIR, f"frame_{frame_num:04d}.png"))
        print(f"Frame {frame_num}: Landing page")
        frame_num += 1

        # Frame 2: Click Share
        page.click("text=Share")
        page.wait_for_timeout(2000)
        page.screenshot(path=os.path.join(FRAMES_DIR, f"frame_{frame_num:04d}.png"))
        print(f"Frame {frame_num}: Share page")
        frame_num += 1

        # Add more frames here for the full flow:
        # - File upload interaction
        # - Metadata review
        # - Publishing step

        context.close()
        browser.close()

    return frame_num

def assemble_gif(frame_count, output_name="sharing-flow.gif", duration=2000):
    frames = []
    for i in range(frame_count):
        path = os.path.join(FRAMES_DIR, f"frame_{i:04d}.png")
        if os.path.exists(path):
            img = Image.open(path)
            # Scale down for reasonable GIF size
            img = img.resize((960, 600), Image.Resampling.LANCZOS)
            frames.append(img)

    if frames:
        output_path = os.path.join(OUTPUT_DIR, output_name)
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0,
        )
        print(f"\nGIF saved to {output_path}")
    else:
        print("No frames captured")

def main():
    print("Capturing sharing workflow frames...")
    frame_count = capture_sharing_flow()

    print(f"\nAssembling {frame_count} frames into GIF...")
    assemble_gif(frame_count)

    # Clean up frames
    for f in glob.glob(os.path.join(FRAMES_DIR, "*.png")):
        os.remove(f)
    os.rmdir(FRAMES_DIR)

if __name__ == "__main__":
    main()
