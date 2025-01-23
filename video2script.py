import os
from whisper import load_model
import yt_dlp
import warnings
from datetime import datetime

# Suppress PyTorch-specific warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="torch")
warnings.filterwarnings("ignore", category=UserWarning, module="whisper")

def download_audio(url, output_path="audio.mp3"):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.splitext(os.path.abspath(output_path))[0],  # Save without double extensions
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": False,  # Enable detailed output for debugging
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    corrected_path = os.path.abspath(output_path)
    print(f"Audio downloaded to: {corrected_path}")
    return corrected_path


def transcribe_audio(audio_path):
    if not os.path.exists(audio_path):
        print(f"DEBUG: File does not exist at: {audio_path}")
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    
    model = load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]


def clean_transcript(raw_text):
    sentences = raw_text.split("\n")
    cleaned_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            cleaned_sentences.append(sentence[0].upper() + sentence[1:])
    return "\n".join(cleaned_sentences)


def main():
    url = input("Enter the video/audio URL: ")
    try:
        # Create "transcripted" folder if it doesn't exist
        os.makedirs("transcripted", exist_ok=True)

        # Download audio from the URL
        audio_path = download_audio(url)

        # Verify if the file exists
        if not os.path.exists(audio_path):
            print(f"ERROR: Audio file not found: {audio_path}")
            return

        # Transcribe the downloaded audio
        print("Transcribing audio...")
        raw_transcript = transcribe_audio(audio_path)

        # Clean and organize the transcript
        print("Cleaning transcript...")
        cleaned_transcript = clean_transcript(raw_transcript)

        # Generate a unique filename with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        transcript_filename = os.path.join("transcripted", f"transcript_{timestamp}.txt")

        # Display and save the transcript
        print("Organized Transcript:")
        print(cleaned_transcript)
        with open(transcript_filename, "w", encoding="utf-8") as file:
            file.write(cleaned_transcript)
        print(f"Transcript saved to {transcript_filename}")

        # Delete the temporary audio file
        os.remove(audio_path)
        print("Temporary files cleaned up.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
