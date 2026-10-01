from ai_client import ask_ai

def generate_summary(text: str) -> str:
    system_prompt = """
    You are an AI Education Assistant. Summarize the user's input text clearly with sub-topics:
    1. Key Concepts (முக்கிய கருத்துகள்)
    2. Detailed Breakdown (விரிவான விளக்கம்)
    3. Takeaway Points (முக்கிய குறிப்புகள்)
    Use clear Markdown headings, bullet points, and clean formatting.
    """
    return ask_ai(prompt=text, system_prompt=system_prompt)