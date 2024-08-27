import gradio as gr
from gradio import ChatMessage
import random
import time

from judge import Judge

# Define the Judge instance
judge = Judge()

theme = gr.themes.Monochrome()

with gr.Blocks(theme=theme, fill_height=True) as demo:
    gr.Markdown("# LLM Duel Arena", elem_id="title")
    
    chatbot = gr.Chatbot(label="Chat History",
                            type="messages",
                            avatar_images = judge.get_pfps(),
                            elem_id="chatbot",
                            scale=1)
    
    with gr.Tab("\U0001F4AC Chat"):
        

        with gr.Row():
            progress_btn = gr.Button("\U0001F4AC Advance Conversation")
            abort_btn = gr.Button("\U000023F9 Abort")
            nr_of_rounds = gr.Number(label="Number of Rounds", value=1)

        with gr.Row():
            download_history = gr.Button("\U0001F4E5 Export Conversation History")
            clear = gr.ClearButton([chatbot], value="\U0001F5D1 Clear Conversation")
        
        def progress(chat_history, nr_of_rounds):
            for i in range(nr_of_rounds):
                response = judge.progress_conversation()
                chat_history.append(response)
            return chat_history

        def download():
            print(judge.conversation_history_to_json())

        def set_bots(bot_one_pfp, bot_one_name, bot_one_description, bot_two_pfp, bot_two_name, bot_two_description):
            
            avatar_images = [bot_one_pfp, bot_two_pfp]
            
            judge.adjust_models({
                "bot_one_pfp": bot_one_pfp,
                "bot_one_name": bot_one_name,
                "bot_one_description": bot_one_description,
                "bot_two_pfp": bot_two_pfp,
                "bot_two_name": bot_two_name,
                "bot_two_description": bot_two_description
            })

    with gr.Tab("\U00002699 Settings"):

        with gr.Row():
            bot_one_pfp = gr.Image(label=f"Avatar",
                                   type="filepath",
                                   value="media/robot_pfp01.png",
                                   show_fullscreen_button=False,
                                   show_download_button=False,
                                   height=128,
                                   scale=1)
            bot_one_name = gr.Textbox(label=f"Character Name", placeholder="Enter character's display name", scale=3)
        bot_one_description = gr.TextArea(label=f"Character Personality", placeholder="Describe the character's personality")

        with gr.Row():
            bot_two_pfp = gr.Image(label=f"Avatar",
                                   type="filepath",
                                   value="media/robot_pfp02.png",
                                   show_fullscreen_button=False,
                                   show_download_button=False,
                                   height=128,
                                   scale=1)
            bot_two_name = gr.Textbox(label=f"Character Name", placeholder="Enter character's display name", scale=3)
        bot_two_description = gr.TextArea(label=f"Character Personality", placeholder="Describe the character's personality")
        save_bots_btn = gr.Button("\U0001F4BE Save")

    progress_btn.click(progress, [chatbot, nr_of_rounds], [chatbot])
    download_history.click(download)
    save_bots_btn.click(set_bots, [bot_one_pfp, bot_one_name, bot_one_description, bot_two_pfp, bot_two_name, bot_two_description])
        

def launch():
    demo.launch()

if __name__ == "__main__":
    demo.launch()
