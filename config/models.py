import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


ROUTER_MODEL = "llama-3.1-8b-instant"

REASONING_MODEL = "llama-3.3-70b-versatile"