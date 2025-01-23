# Video-Transcript

Easily transcribe any video from anywhere! This tool allows you to extract transcripts from **YouTube videos**, **Canvas videos**, **McGraw Hill**, and any **streaming links or local files**. Powered by advanced speech-to-text technology, it works with MP4, MP3, and streaming links, organizing the transcripts neatly with timestamps.

---

## How It Works
1. **For YouTube Videos**:
   - Paste the YouTube video link into the program.
   - The tool will automatically download the audio and generate the transcript.

2. **For Canvas Videos**:
   - Open the video in your browser.
   - **Right-click** on the video and select **Inspect** or press `Ctrl + Shift + I` (Windows) or `Cmd + Option + I` (Mac).
   - Find the video source (`src`) link in the **HTML code** under the `<video>` tag or **Network** tab.
   - Copy the source link and paste it into the program.

3. **For McGraw Hill Videos**:
   - Follow the same steps as for Canvas videos. Inspect the video source, find the `src` link, and paste it into the program.

4. **For Other Websites or Local Files**:
   - Paste the streaming link or load a local video/audio file to generate transcripts.

---

## Features
- Works with platforms like YouTube, Canvas, McGraw Hill, and more.
- Supports MP4, MP3, and direct streaming links.
- Organizes transcripts in a `transcripted` folder with filenames based on timestamps (e.g., `transcript_2025-01-23_12-30-45.txt`).
- Use the transcript as input to ChatGPT to **summarize the video content**, so you no longer have to watch it!

---

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dannyphantom55/Video-Transcript.git
   cd Video-Transcript

2. pip install -r requirements.txt

3. Windows:
Download FFmpeg from FFmpeg.org.
Add the ffmpeg/bin directory to your system's PATH.


4. Run the program:
python video2script.py
Paste the video link or local file path as prompted:

YouTube: Paste the YouTube link.
Canvas/McGraw Hill: Use the Inspect Element tool to get the video src link and paste it.
Other Files: Provide the file path to a local MP4 or MP3 file.
The transcript will be saved in the transcripted folder with a unique filename based on the current date and time.
