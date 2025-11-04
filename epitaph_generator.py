import random

def generate_epitaph(text, score, issues):
    templates = [
        "Here lies a piece of code that tried its best.",
        "Gone too soon — may its syntax rest in peace.",
        "Once compiled, never again.",
        "A valiant attempt at logic, buried with honor.",
        "Here rests a text beyond salvation."
    ]

    if score < 40:
        templates.append("It lived fast, crashed hard, and died young.")
    if score < 20:
        templates.append("A true monument to chaos itself.")

    base = random.choice(templates)
    detail = f" ({len(issues)} sins committed.)"
    return base + detail
