
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_remarks(glucose, haemoglobin, cholesterol):
    try:
        prompt = f"""
        You are providing general health information, not a diagnosis.

        Glucose: {glucose}
        Haemoglobin: {haemoglobin}
        Cholesterol: {cholesterol}

        Explain these values briefly in simple language.
        Do not diagnose any disease or prescribe medicine.
        Recommend consulting a qualified healthcare professional.
        """

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI service error: {e}"
