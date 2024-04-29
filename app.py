import whisper
from IPython.display import Audio
from moviepy.editor import AudioFileClip
from openai import OpenAI
import sys
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
transcription = speech_to_text(audio_file_path)
if transcription is None:
    print("Transcription was not successful. Exiting program.")
    sys.exit(1)
print("Transcription:")
print(transcription)

OPENAI_API_KEY = "YOUR API KEY"
client = OpenAI(api_key=OPENAI_API_KEY)
prompt = f"""Give me an english movie script in atleast 5000-8000 words depicting the following instructions and scene discription:

[Additional Instructions]:
- Ensure the script captures the essence of the scene in a conversational Tamil-English (Thanglish) style.
- Include descriptive dialogue and actions that reflect the mood and atmosphere of the scene.
- Also give the discription of the SCENE HEADING,ACTION,CHARACTER,DIALOGUE,INTERCUT,SUBHEADER,FADE IN,Cut to in thanglish.

[Notes for the AI]:
- Consider the emotions and motivations of the characters involved in the scene.
- Incorporate elements of the setting, such as location, time of day, and any relevant background details.
- Feel free to add creative elements or embellishments to enhance the narrative.


[Output format]:

SCENE HEADING

One line description of the
location and time of day

ACTION

The description of the
actions in a scene

CHARACTER

Identifies the character who
Is speaking

DIALOGUE

The lines of speech your
character says

INTERCUT

Instructions when eutting to
muttiple locations

SUBHEADER

Used when there are minor
changes in a location

FADE IN

Marks the start of the
screenplay.

SCENE NUMBER

Generally numbered only
in the shooting script,

TRANSITION

EXTENSION

Clarifies where a character
Is when they can't be seen

PARENTHETICAL

Provides info on how the
actor should say the line

SHOT

Indicates the camera angle
or movement in a scene


[Reminder]:
Please remember this is an tamil script, to ensure accessibility and cultural relevance.

[scene discription]:"""

if transcription:
    prompt += "\n\n[Scene Discription]:\n" + transcription

completion = client.chat.completions.create(
  model = 'gpt-3.5-turbo',
  messages=[ {"role":"system", "content":"You are a tamil movie script co-writer who writes scenes based on the discriptions given by the main writer"}, {"role": "user", "content":prompt }],
  temperature = 0  
)

script_text = completion.choices[0].message.content

file_path = "translated_text.txt"

# Write the translated text to the file
with open(file_path, "w") as file:
    file.write(script_text)
