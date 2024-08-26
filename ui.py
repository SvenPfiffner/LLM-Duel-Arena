import gradio as gr

def echo(message, history):
    return message["text"]

demo = gr.ChatInterface(
    fn=echo,
    title="LLM Duel Arena",
    multimodal=False,
)
demo.launch()