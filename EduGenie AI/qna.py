from ai_client import generate_ai_response


def answer_question(question: str, context: str = "") -> str:

    if not question or not question.strip():
        return "Please enter a valid question."

    prompt = f"""
You are EduGenie, an expert educational tutor.

Answer the student's question clearly,
accurately, and in an easy-to-understand way.

Question:
{question}

Context:
{context}
"""

    try:
        return generate_ai_response(prompt)

    except Exception as e:
        return f"Error generating answer: {str(e)}"