from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# 📄 Reddit data file
filename = "kojied_raw.txt"

# 🔁 Read the combined Reddit user data
with open(filename, "r", encoding="utf-8") as file:
    user_data = file.read()

# 📌 Prompt to send to ChatGPT
prompt = f"""
You are an AI assistant. Based on the Reddit user's comments and posts below, create a detailed user persona. 

Include the following:
- Interests
- Personality traits
- Writing style
- Tone
- Possible occupation or life situation
- Any strong opinions or values
- Include 1–2 short quote citations from their posts or comments under each point.

Reddit Data:
{user_data}
"""

#  Send request to GPT model (gpt-3.5-turbo or gpt-4)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7
)

#  Extract the result
persona = response.choices[0].message.content

#  Save to output file
persona_file = filename.replace("_raw.txt", "_persona.txt")
with open(persona_file, "w", encoding="utf-8") as f:
    f.write(persona)

print(f"\n Persona saved to {persona_file}")
