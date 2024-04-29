import os
from openai import OpenAI

OPENAI_API_KEY = "YOUR OPRNAI API KEY HERE"
client = OpenAI(api_key=OPENAI_API_KEY)
scene_description=input("give the instruction:")
prompt=f"""Give me an english movie script in atleast 5000-8000 words depicting the following instructions and scene discription:

[Additional Instructions]:
- Ensure the script captures the essence of the scene in a conversational style.
- Include descriptive dialogue and actions that reflect the mood and atmosphere of the scene.

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

[scene discription]:
{scene_description}"""


completion = client.chat.completions.create(
  model = 'gpt-3.5-turbo',
  messages=[ {"role":"system", "content":"You are a tamil movie script writer who writes action scenes"}, {"role": "user", "content":prompt }],
  temperature = 0  
)

translated_text=completion.choices[0].message.content

file_path = "translated_text.txt"

# Write the translated text to the file
with open(file_path, "w") as file:
    file.write(translated_text)
