import whisper
from IPython.display import Audio
from moviepy.editor import AudioFileClip
import os
import math
import sys

# Load the Whisper base model
model = whisper.load_model("base")

def mp3_to_wav(mp3_file_path):
    try:
        # Convert MP3 to WAV using moviepy
        clip = AudioFileClip(mp3_file_path)
        wav_file_path = mp3_file_path.replace(".mp3", ".wav")
        clip.write_audiofile(wav_file_path)
        return wav_file_path
    except Exception as e:
        print(f"An error occurred during MP3 to WAV conversion: {e}")
        return None

def transcribe_long_audio(audio_file_path):
    try:
        if not os.path.exists(audio_file_path):
            print("Error: The specified audio file does not exist.")
            return None

        # Convert MP3 to WAV
        wav_file_path = mp3_to_wav(audio_file_path)
        if not wav_file_path:
            return None

        # Load audio 
        audio = whisper.load_audio(wav_file_path)
        options = {"fp16": False, "language": "ta", "task": "translate"}
        result = model.transcribe(audio, **options)
        translation=result['text']
        return translation
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
# Specify the path to the audio file
audio_file_path = "D:\embrok\SPEECH_Script\LAst_Comit\scriptaudio.mp3"
# Call the speech_to_text function with the audio file path
transcription = transcribe_long_audio(audio_file_path)
if transcription is None:
    print("Transcription was not successful. Exiting program.")
    sys.exit(1)
print("Transcription:")
print(transcription)
