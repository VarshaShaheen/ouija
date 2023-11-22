import os

from litellm import completion

from constants import BASE_PROMPT

os.environ["OPENAI_API_KEY"] = "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"


class Mistral:
    def __init__(self, ghost, model="gpt-3.5-turbo"):
        with open(ghost) as f:
            self.system_prompt = f.read()
            self.system_prompt += BASE_PROMPT

        self.model = model
        self.messages = [
            {"content": self.system_prompt, "role": "system"}
        ]

    def __call__(self, question, **kwargs):
        self.messages.append({"content": question, "role": "user"})
        answer = completion(
            model=self.model,
            messages=self.messages
        )

        text = answer["choices"][0].message.content
        agent = answer["choices"][0].message.role

        self.messages.append({"content": text, "role": agent})

        return text


if __name__ == '__main__':
    mistral = Mistral("ghosts/Caligula.txt")

    while True:
        q = input("Question: ")
        a = mistral(q)
        print("Answer:", a)
