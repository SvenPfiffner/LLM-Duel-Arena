import gradio as gr
from gradio import ChatMessage
import random
import time

from judge import Judge

# Define the Judge instance
judge = Judge()

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages", elem_id="chatbot")
    progress_btn = gr.Button("Progress Conversation")
    audio = gr.Audio(type="numpy", autoplay=True)
    clear = gr.ClearButton([chatbot])
    download_history = gr.Button("Download Conversation History")

    def progress(chat_history):
        response, audio = judge.progress_conversation()
        print(audio)
        chat_history.append(response)

        return chat_history, audio

    def download():
        print(judge.conversation_history_to_json())

    progress_btn.click(progress, [chatbot], [chatbot, audio])
    download_history.click(download)

    def character_settings(id):
        return gr.Textbox(label=f"Name", placeholder="Name of character is displayed in chat and known to model"), \
               gr.TextArea(label=f"Personality", placeholder="Enter a system prompt that describes the character's personality.")

    with gr.Accordion("Define LLM Personas", open=True):
        with gr.Tab("Persona 1"):
            character_settings(0)
        with gr.Tab("Persona 2"):
            character_settings(1)

if __name__ == "__main__":
    demo.launch()