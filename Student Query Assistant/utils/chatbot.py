import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def get_response(user_query):

    try:

        prompt = f"""
        You are a Student Query Assistant.

        Answer only questions related to:

        - Programming
        - Artificial Intelligence
        - Machine Learning
        - Career Guidance
        - Interview Preparation

        User Question:
        {user_query}
        """

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"
