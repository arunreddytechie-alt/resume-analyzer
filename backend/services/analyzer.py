import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_resume(resume_text, job_text, question):
    print("question: ", question)


    prompt = f"""
    Resume:
    {resume_text}

    Job Description:
    {job_text}

    Question:
    {question}

    Provide:

    1. Fit Score (0–100%)
    2. Missing Skills
    3. Matching Skills
    4. Suggestions
    5. Interview Preparation Tips
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content