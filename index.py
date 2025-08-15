import streamlit as st
from main import callOpenAI

st.title("GPT Summarizer App")

user_input = st.text_area("Text", placeholder="Gib hier deinen Text ein...")

if st.button("Zusammenfassen"):
    response = callOpenAI(user_input)
    st.text(response)