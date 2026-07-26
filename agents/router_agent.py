from groq import Groq
import os
from dotenv import load_dotenv

from config.models import ROUTER_MODEL
from agents.messages import AgentMessage

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def router_agent(state):

    question = state["question"]

    prompt = f"""
Classify this rice farming question.

Question:

{question}

Return ONLY one of these:

disease_information

treatment

prevention

nutrient_management

pest_management
"""

    response = client.chat.completions.create(

        model=ROUTER_MODEL,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    intent = response.choices[0].message.content.strip()

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