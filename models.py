import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class LiteraryCharacter:
    def __init__(self, name, age, character):
        self.name = name
        self.age = age
        self.character = character
        self.summary = f"Имя персонажа: {self.name}, возраст: {self.age}, характер: {self.character}"

    def introduce(self):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{self.summary}. Представься от лица {self.name}"}
            ]
        )

        print(completion.choices[0].message.content)
