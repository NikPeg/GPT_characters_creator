import os
import openai
import config
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Say 'Hello world!'"}
  ]
)

print(completion.choices[0].message.content)