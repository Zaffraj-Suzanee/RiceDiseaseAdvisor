import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def reasoning_agent(state):

    question = state["question"]

    context = "\n\n".join(
        state["documents"]
    )


    prompt = f"""
You are an expert rice disease advisor
for Sri Lankan farmers.

Use the provided knowledge.

Question:
{question}

Retrieved information:
{context}

Provide:
1. Disease identification
2. Symptoms
3. Causes
4. Recommended management
5. Prevention advice

Answer in simple farmer-friendly language.
"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]

    )


    state["answer"] = (
        response
        .choices[0]
        .message
        .content
    )


    return state