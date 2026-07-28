import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

from config.models import REASONING_MODEL

load_dotenv()

if "GROQ_API_KEY" in st.secrets:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
else:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


client = Groq(
    api_key=GROQ_API_KEY
)


def reasoning_agent(state):

    question = state["question"]

    context = "\n\n".join(state["documents"][:3])

    prompt = f"""
You are an expert agricultural extension officer specializing in rice diseases in Sri Lanka.

Use ONLY the retrieved knowledge below.

Question:
{question}

Retrieved Knowledge:
{context}

Return ONLY valid JSON.

Return exactly:

{{
    "disease":"",
    "symptoms":"",
    "causes":"",
    "management":"",
    "prevention":""
}}

Rules:

- Fill ALL fields.
- Never leave any field empty.
- Each field should contain one complete paragraph.
- Return ONLY JSON.
- Do not use markdown.
- Do not write anything outside the JSON.
"""

    response = client.chat.completions.create(
        model=REASONING_MODEL,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "Return ONLY valid JSON. Never return explanations outside JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    print("=" * 60)
    print(answer)
    print("=" * 60)

    state["answer"] = answer

    return state