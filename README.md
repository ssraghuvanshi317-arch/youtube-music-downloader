# YouTube Music Downloader

A simple Python project that downloads audio from YouTube videos and playlists, converts it to MP3, and saves the files locally.

## Features
- Downloads audio from a single YouTube video
- Downloads every track in a YouTube playlist
- Saves the highest-quality audio available
- Converts audio to MP3 automatically
- Stores files on your local machine in a `downloads` folder

## Requirements
Before running this script, install:
- Python 3.9+
- FFmpeg

### Install FFmpeg
- macOS: `brew install ffmpeg`
- Ubuntu/Debian: `sudo apt install ffmpeg`
- Windows: install FFmpeg and add it to your PATH

## Installation
1. Open a terminal in the project folder.
2. Install the Python dependency:

```bash
pip install -r requirements.txt
```

## Run the script
Single video:

```bash
python main.py --url "https://www.youtube.com/watch?v=MdmRadVnVlw"
```

Playlist:

```bash
python main.py --url "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

You can also use the positional argument style:

```bash
python main.py "https://youtu.be/MdmRadVnVlw"
```

## Output
The script saves the resulting MP3 files in a folder named `downloads/` inside the project directory.

## Troubleshooting
- If you see `FFmpeg was not found`, install FFmpeg and ensure it is on your PATH.
- If `yt_dlp` is missing, run:

```bash
pip install -r requirements.txt
```

- If a video is unavailable or blocked, the download may fail for that item.

## Legal note
Only download content that you own or are allowed to download. Respect copyright law and YouTube's terms of service.
