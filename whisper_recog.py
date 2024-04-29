import whisper
from IPython.display import Audio
from moviepy.editor import AudioFileClip
import os

# Load the Whisper base model
model = whisper.load_model("base")

def mp3_to_wav(mp3_file_path):
    try:
        # Convert MP3 to WAV using moviepy
        clip = AudioFileClip(mp3_file_path)
        wav_file_path = mp3_file_path.replace(".mp3", ".wav")
        clip.write_audiofile(wav_file_path)
        return wav_file_path
        print(wav_file_path)
    except Exception as e:
        print(f"An error occurred during MP3 to WAV conversion: {e}")
        return None
    
def speech_to_text(audio_file_path):
    try:
        if not os.path.exists(audio_file_path):
            print("Error: The specified audio file does not exist.")
            return None
        # Convert MP3 to WAV
        wav_file_path = mp3_to_wav(audio_file_path)
        if not wav_file_path:
            return None
        print(f"Attempting to load audio from: {wav_file_path}")
        
        # Load audio from the converted WAV file
        audio = whisper.load_audio(wav_file_path)
        # Pad or trim the audio to fit 30 seconds
        audio = whisper.pad_or_trim(audio, duration=90)
        # Generate log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        # Detect the spoken language
        _, probs = model.detect_language(mel)
        print(f"Detected language: {max(probs, key=probs.get)}")
        # Decode the audio
        options = whisper.DecodingOptions()
        result = whisper.decode(model, mel, options)
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Specify the path to the audio file
audio_file_path = "D:\embrok\SPEECH_Script\LAst_Comit\scriptaudio.mp3"
# Call the speech_to_text function with the audio file path
transcription = speech_to_text(audio_file_path)
if transcription:
    print("Transcription:")
    print(transcription)


