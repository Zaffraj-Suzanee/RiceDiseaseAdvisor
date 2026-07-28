import os
import streamlit as st

from groq import Groq
from dotenv import load_dotenv

from agents.messages import AgentMessage
from config.models import ROUTER_MODEL


load_dotenv()


if "GROQ_API_KEY" in st.secrets:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
else:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


client = Groq(
    api_key=GROQ_API_KEY
)

def router_agent(state):

    question = state["question"]

    prompt = f"""
Classify the following rice agriculture question into one of these intents:

1. disease_information
2. disease_management
3. disease_prevention
4. general_rice_information

Question:
{question}

Return ONLY one intent label.
Do not provide an explanation.
"""

    response = client.chat.completions.create(
        model=ROUTER_MODEL,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a rice agriculture intent-classification agent. Return only one valid intent label."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    intent = response.choices[0].message.content.strip()

    valid_intents = [
        "disease_information",
        "disease_management",
        "disease_prevention",
        "general_rice_information"
    ]

    if intent not in valid_intents:
        intent = "disease_information"

    message: AgentMessage = {

        "sender": "router_agent",

        "receiver": "retrieval_agent",

        "task": "retrieve_documents",

        "content": {

            "intent": intent,

            "query": question

        },

        "status": "completed"

    }

    state["messages"].append(message)

    state["intent"] = intent

    return state