import streamlit as st

st.set_page_config(
    page_title="Rice Disease Advisory System",
    page_icon="🌾"
)

st.title("🌾 Agentic AI-Powered Rice Disease Advisory System")

st.write(
    "AI assistant for Sri Lankan farmers to get advice about rice diseases."
)

question = st.text_area(
    "Ask your question about rice diseases:"
)

if st.button("Get Advice"):

    if question:
        st.success("Question received!")
        st.write("AI agent response will appear here.")

    else:
        st.warning("Please enter a question.")