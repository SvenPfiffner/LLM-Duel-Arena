<div align="center">

<img src="https://github.com/SvenPfiffner/LLM-Duel-Arena/blob/main/llmarena/media/robot_pfp02.png" width="300">

</div>

# LLM Conversational UI

This project provides a user interface that allows users to observe a conversation between two Large Language Models (LLMs). The UI enables the creation of unique character personas for each model, and the models converse with each other based on the predefined personas. The conversation can be progressed manually (step-by-step) or be fully automated for a predefined number of interactions. Further, the conversation history is logged via a JSON and can be saved for further analysis or synthetic dataset generation.

## Features

- **Define Character Personas:** Customize the personality and role of each LLM character.
- **Watch LLMs Converse:** Observe how two LLMs interact with each other based on the defined personas.
- **Download Conversation History:** Save the conversation history in JSON format for analysis.
- **Ollama & API Integration:** Interfaces directly with the chat endpoint of Ollama and can use it to perform on-device inference with all [supported models](https://ollama.com/library).

## Installation

### Prerequisites

- **Python** must be installed on your system. The current version is developed and tested under **Python 3.11** and may or may not work with other versions. Integration tests with other versions is *TODO*
- **Ollama server** (if using Ollama for LLM management). Ensure [it is installed](https://ollama.com/) and available in your system's PATH.

### Steps

**Clone the Repository:**

```bash
git clone https://github.com/SvenPfiffner/LLM-Duel-Arena.git
cd LLM-Duel-Arena
```

**Automatic Launch:**

The main entry point for the application is `start.py`. You can start the UI by running:

```bash
python start.py
```

This script will:
- Create a virtual environment with the required dependencies (if it does not exist).
- Start the Ollama server.
- Launch the UI.

**Manual Launch:**
If you prefer to set up and launch manually, you can install the requirements from `requirements.txt` and directly run the UI

```bash
pip install -r requirements.txt
python llmarena/ui.py
```

*Note: Manual launch skips the ollama management. So you must ensure that ollama is serving in the background*

## Contributing
Contribution is more than welcome. Feel free to fork the project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
