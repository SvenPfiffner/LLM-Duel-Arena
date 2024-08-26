# The character class implements a LLM instance modeling a character.
# It is a wrapper around the Ollama API that ensures that the character
# remains in character and adheres to the specified discussion topic.

class Character:
    
    def __init__(self, name, character_description, character_id):
        self.name = name
        self.character_description = character_description
        character_id = character_id

    def sytem_prompt(self):
        return f"Your name is {self.name}. {self.character_description}."
    
    def speak(self):
        pass