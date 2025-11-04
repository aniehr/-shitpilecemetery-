import gradio as gr
from analyzer import analyze_text
from epitaph_generator import generate_epitaph

def process_input(text):
    score, issues = analyze_text(text)
    epitaph = generate_epitaph(text, score, issues)
    return f"💀 Score: {score}/100\n\nIssues:\n- " + "\n- ".join(issues) + "\n\nEpitaph:\n" + epitaph

iface = gr.Interface(fn=process_input, inputs="text", outputs="text",
                     title="🪦 Shitpile Cemetery",
                     description="Bury your cursed code or text here.",
                     theme="gradio/soft")

if __name__ == "__main__":
    iface.launch()
