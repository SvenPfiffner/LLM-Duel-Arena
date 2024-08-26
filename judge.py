# The judge class implements a judge that controls the 
# discussion between the two LLM instances. It keeps track of the
# conversation history and orchestrates the flow of the conversation.

from character import Character

class Judge:
    def __init__(self):
        self.conversation_history = []
        self.topic = None

        self.models = self.create_models()
        
        self.counter = 0

    def create_models(self):
        models = {0: Character("Alice", ""),
                  1: Character("Bob", "")}
        
        return models

    def reset_conversation(self):
        self.conversation_history = []
        self.counter = 0

    def progress_conversation(self):
        speaker = self.models[self.counter % 2]

        speech = speaker.speak()
        self.conversation_history.append(speech)
        self.counter += 1

    def conversation_history_to_json(self):
        return self.conversation_history
