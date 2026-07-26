import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def reflection_agent(state):

    answer = state["answer"]
    question = state["question"]


    prompt = f"""
You are a quality reviewer for an AI rice disease advisor.

Check the following answer.

Question:
{question}

Answer:
{answer}


Evaluate:

1. Is the disease information correct?
2. Are symptoms clearly explained?
3. Are management recommendations practical for Sri Lankan farmers?
4. Is the answer safe and understandable?


If improvements are needed, rewrite the answer.

Return only the improved final answer.
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


    state["final_answer"] = (
        response
        .choices[0]
        .message
        .content
    )


    return state