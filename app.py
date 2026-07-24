import streamlit as st

st.title("🌾 Rice Disease Advisory System")

question = st.text_area("Ask your question about rice diseases")

if st.button("Get Advice"):
    st.write("AI response will appear here.")