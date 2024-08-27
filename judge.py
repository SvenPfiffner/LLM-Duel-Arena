from typing import List, Dict, Optional
from character import Character

from tts import TTS

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
        self.tts_engine = TTS()
        self.counter: int = 0

    def create_models(self) -> Dict[int, Character]:
        """
        Creates and returns the default models if none are provided during initialization.

        Returns:
            Dict[int, Character]: A dictionary of models with unique integer keys.
        """
        models = [
            Character(name="Alice", description="You are a math expert that colaborates with your chat partner to find the most efficient solution to solve a polynomial equation", id=0),
            Character(name="Bob", description="You are a math expert that colaborates with your chat partner to find the most efficient solution to solve a polynomial equation", id=1)
        ]
        return models

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

            # Speak the response
            audio = self.tts_engine.generate_audio(speech["content"])
            return speech, audio
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
