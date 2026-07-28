import os
import streamlit as st

from groq import Groq
from dotenv import load_dotenv

from config.models import ROUTER_MODEL


load_dotenv()


if "GROQ_API_KEY" in st.secrets:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
else:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


client = Groq(
    api_key=GROQ_API_KEY
)

ROUTER_MODEL = "llama-3.1-8b-instant"

REASONING_MODEL = "llama-3.3-70b-versatile"