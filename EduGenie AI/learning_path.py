from ai_client import ask_ai_json

def generate_learning_path(topic: str):
    system_prompt = "Generate a structured learning roadmap with sub-topics, estimated time, and key outcomes."
    prompt = f"Create a step-by-step learning roadmap for learning: {topic}"
    return ask_ai_json(prompt=prompt, system_prompt=system_prompt)