import ollama


# The character class implements a LLM instance modeling a character.
# It is a wrapper around the Ollama API that ensures that the character
# remains in character and adheres to the specified discussion topic.

class Character:
    
    def __init__(self, name, description, pfp, id):
        self.name = name
        self.description = description
        self.pfp = pfp
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_pfp(self, pfp):
        self.pfp = pfp

    def system_prompt(self):
        return f"Your name is {self.name}. {self.description}."
    
    def prompt_from_history(self, chat_history):

        # The chat history recieved from the judge has the character id as the role.
        # We need to convert the id's to the user and assistant roles that the model expects.

        history = chat_history.copy()
        for i in range(len(history)):
            if history[i]['role'] == self.id:
                history[i]['role'] = 'assistant'
            else:
                history[i]['role'] = 'user'

        prompt = [
            {
                'role': 'system',
                'content': self.system_prompt(),
            }
        ] + history
        return prompt

    def speak(self, chat_history):
        message = ollama.chat(model='llama3', messages=self.prompt_from_history(chat_history))["message"]["content"]
        return {"role": self.id, "content": message}