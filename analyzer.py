import re

def analyze_text(text):
    issues = []
    score = 100

    if len(text.strip()) == 0:
        issues.append("Empty input — nothing to analyze.")
        return 0, issues

    if "print" in text and "if" not in text:
        issues.append("Looks like debug code or incomplete logic.")
        score -= 20

    if len(re.findall(r'\b(var|let|const)\b', text)) > 5:
        issues.append("Too many variable declarations — chaos detected.")
        score -= 15

    if len(text.split()) < 10:
        issues.append("Too short to make sense.")
        score -= 10

    if "Lorem" in text or "asdf" in text:
        issues.append("Nonsense detected.")
        score -= 25

    score = max(0, score)
    return score, issues
