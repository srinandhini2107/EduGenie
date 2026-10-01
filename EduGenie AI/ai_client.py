import json
import time

from google import genai
from google.genai import types

from config import GEMINI_API_KEY, GEMINI_MODEL


client = genai.Client(api_key=GEMINI_API_KEY)


ENGLISH_RULES = """
IMPORTANT LANGUAGE RULES:
- Respond ONLY in English.
- Never use Tamil.
- Never use Hindi.
- Never use Telugu.
- Never use Malayalam.
- Never use any language other than English.
- Use simple and clear English.
- Explain things so students can easily understand.
"""


def generate_ai_response(
    prompt: str,
    system_prompt: str = "You are EduGenie, an expert educational AI tutor."
):

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt + ENGLISH_RULES,
                    temperature=0.7
                )
            )

            return response.text

        except Exception as e:

            error_message = str(e)

            print("GEMINI ERROR:", error_message)

            if "503" in error_message or "UNAVAILABLE" in error_message:

                if attempt < 2:
                    time.sleep(3)
                    continue

                return "Gemini AI is temporarily busy. Please try again."

            return f"AI Error: {error_message}"


def ask_ai(
    prompt: str,
    system_prompt: str = "You are EduGenie, an expert educational AI tutor."
):

    return generate_ai_response(
        prompt,
        system_prompt
    )


def ask_ai_json(
    prompt: str,
    system_prompt: str = "You are EduGenie, an expert educational AI tutor."
):

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        system_prompt
                        + ENGLISH_RULES
                        + """
Return ONLY valid JSON.
Do not use markdown.
Do not add explanations outside the JSON.
"""
                    ),
                    response_mime_type="application/json",
                    temperature=0.7
                )
            )

            return json.loads(response.text)

        except Exception as e:

            error_message = str(e)

            print("GEMINI JSON ERROR:", error_message)

            if "503" in error_message or "UNAVAILABLE" in error_message:

                if attempt < 2:
                    time.sleep(3)
                    continue

                return {
                    "error": "Gemini AI is temporarily busy. Please try again."
                }

            return {
                "error": error_message
            }