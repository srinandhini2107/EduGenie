from ai_client import ask_ai_json


def generate_quiz(topic: str):

    if not topic.strip():
        return {
            "error": "Please enter a topic."
        }

    prompt = f"""
Create a quiz about:

{topic}

Create exactly 3 multiple-choice questions.

Each question must have exactly 4 options.

Return JSON in exactly this format:

{{
    "quiz": [
        {{
            "question": "Question here",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "answer": "Correct option",
            "explanation": "Short explanation"
        }}
    ]
}}

Do not add anything outside the JSON.
"""

    return ask_ai_json(
        prompt,
        "You are an educational quiz generator."
    )