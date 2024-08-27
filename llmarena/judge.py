from typing import List, Dict, Optional
from character import Character

import json

class Judge:
    """
    The Judge class orchestrates the conversation between multiple LLM instances.
    It manages the conversation history, alternates between speakers, and handles the conversation flow.
    """

    def __init__(self, model_configs: Optional[Dict[int, Character]] = None):
        """
        Initializes the Judge with optional model configurations.

        Args:
            model_configs (Optional[Dict[int, Character]]): A dictionary of model instances or configurations.
        """
        self.conversation_history: List[Dict[str, str]] = []
        self.models: Dict[int, Character] = model_configs if model_configs else self.create_models()
        self.counter: int = 0

    def create_models(self) -> Dict[int, Character]:
        """
        Creates and returns the default models if none are provided during initialization.

        Returns:
            Dict[int, Character]: A dictionary of models with unique integer keys.
        """
        models = [
            Character(name="Alice", description="", pfp= "media/robot_pfp01.png", id=0),
            Character(name="Bob", description="", pfp="media/robot_pfp02.png", id=1)
        ]
        return models

    def adjust_models(self, config) -> None:
        """
        Adjusts the models with the provided configurations.

        Args:
            model_configs (Dict[int, Character]): A dictionary of model instances or configurations.
        """
        self.models[0].set_pfp(config["bot_one_pfp"])
        self.models[0].set_name(config["bot_one_name"])
        self.models[0].set_description(config["bot_one_description"])
        self.models[1].set_pfp(config["bot_one_pfp"])
        self.models[1].set_name(config["bot_two_name"])
        self.models[1].set_description(config["bot_two_description"])

    def get_pfps(self) -> List[str]:
        """
        Returns the profile picture URLs of the models.

        Returns:
            List[str]: A list of profile picture URLs.
        """
        return [model.pfp for model in self.models]

    def reset_conversation(self) -> None:
        """
        Resets the conversation history and speaker counter.
        """
        self.conversation_history.clear()
        self.counter = 0

    def progress_conversation(self) -> None:
        """
        Progresses the conversation by alternating between the models and recording their speech.
        """
        speaker_id = self.counter % len(self.models)
        speaker = self.models[speaker_id]
        try:
            speech = speaker.speak(self.conversation_history)
            self.conversation_history.append(speech)
            self.counter += 1
            # Set correct role for UI display
            if speaker_id == 0:
                speech["role"] = "user"
            else:
                speech["role"] = "assistant"

            return speech
        except Exception as e:
            print(f"Error during conversation: {e}")
            return None

    def conversation_history_to_json(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Returns the conversation history in a JSON-serializable format.

        Returns:
            Dict[str, List[Dict[str, str]]]: The conversation history as a list of dictionaries.
        """
        output = []
        sys_prompts = []
        messages = []
        for model in self.models:
            sys_prompts.append({"actor": model.id, "prompt": model.system_prompt()})
        output.append({"system_prompts": sys_prompts})
        for message in self.conversation_history:
            messages.append({"role": message["role"], "content": message["content"]})
        output[0]["messages"] = messages
        return json.dumps(output)
