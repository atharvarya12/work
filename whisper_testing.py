import whisper
from IPython.display import Audio
from pydub import AudioSegment

# Load the Whisper base model
model = whisper.load_model("base")

def speech_to_text(audio_file_path):
    try:
        # Convert MP3 to WAV
        audio = AudioSegment.from_mp3(audio_file_path)
        wav_file_path = audio_file_path.replace(".mp3", ".wav")
        audio.export(wav_file_path, format="wav")
        
        # Load audio from the converted WAV file
        audio = whisper.load_audio(wav_file_path)
        # Pad or trim the audio to fit 30 seconds
        audio = whisper.pad_or_trim(audio, duration=30)
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
audio_file_path = "D:\embrok\SPEECH_Script\final_Comit\scriptaudio.mp3"
# Call the speech_to_text function with the audio file path
transcription = speech_to_text(audio_file_path)
if transcription:
    print("Transcription:")
    print(transcription)
