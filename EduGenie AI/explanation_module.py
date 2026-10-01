from ai_client import ask_ai

def generate_explanation(topic: str, target_audience: str = "Beginner") -> str:
    system_prompt = f"""
    Explain the topic: '{topic}' tailored for a {target_audience} level.
    Structure your answer with:
    - Simple Analogy / Real-world Example (உதாரணம்)
    - Sub-topics & Core Ideas
    - Key Terminology
    - Summary
    """
    return ask_ai(prompt=topic, system_prompt=system_prompt)