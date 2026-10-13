#!/usr/bin/env python3
"""YouTube Music Downloader.

A beginner-friendly script that downloads audio from YouTube videos and playlists,
converts them to MP3, and saves them locally.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

import yt_dlp


DEFAULT_OUTPUT_DIR = Path("downloads")


def ensure_ffmpeg() -> None:
    """Check that FFmpeg is installed and available on PATH."""
    if shutil.which("ffmpeg") is None:
        raise RuntimeError(
            "FFmpeg was not found on your system.\n"
            "Please install FFmpeg and make sure 'ffmpeg' is available in PATH.\n"
            "- macOS: brew install ffmpeg\n"
            "- Ubuntu/Debian: sudo apt install ffmpeg\n"
            "- Windows: install FFmpeg and add it to PATH"
        )


def build_ydl_options(output_dir: Path) -> dict:
    """Return yt-dlp options for audio extraction and MP3 conversion."""
    return {
        "format": "bestaudio/best",
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",
            }
        ],
        "noplaylist": False,
        "quiet": False,
        "no_warnings": False,
        "geo_bypass": True,
        "extract_flat": False,
        "nocheckcertificate": True,
    }


def download_audio(url: str, output_dir: Path) -> None:
    """Download a single YouTube video or a full playlist."""
    output_dir.mkdir(parents=True, exist_ok=True)
    ensure_ffmpeg()

    ydl_opts = build_ydl_options(output_dir)

    print(f"\nDownloading from: {url}")
    print(f"Saving to: {output_dir.resolve()}\n")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        if not info:
            raise RuntimeError("No information was returned for the URL.")

        if "entries" in info:
            entries = [entry for entry in info.get("entries", []) if entry is not None]
            print(f"\n✓ Playlist download complete.")
            print(f"✓ Downloaded {len(entries)} items.")
        else:
            title = info.get("title", "Unknown title")
            print(f"\n✓ Download complete.")
            print(f"✓ Title: {title}")

        print(f"\nYour MP3 files are in: {output_dir.resolve()}\n")

    except Exception as exc:
        print(f"\n✗ Download failed: {exc}")
        sys.exit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download the best available audio from a YouTube video or playlist and save it as MP3."
    )
    parser.add_argument(
        "url",
        nargs="?",
        help="YouTube video or playlist URL",
    )
    parser.add_argument(
        "--url",
        dest="url_flag",
        help="YouTube video or playlist URL",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Directory where downloaded files will be saved (default: downloads)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    url = args.url or args.url_flag
    if not url:
        print("Usage: python main.py --url 'https://www.youtube.com/watch?v=VIDEO_ID'")
        print("Or: python main.py 'https://www.youtube.com/watch?v=VIDEO_ID'")
        sys.exit(1)

    if "youtube.com" not in url and "youtu.be" not in url:
        print("Invalid URL. Please provide a valid YouTube video or playlist URL.")
        sys.exit(1)

    output_dir = Path(args.output_dir)
    download_audio(url, output_dir)


if __name__ == "__main__":
    main()
