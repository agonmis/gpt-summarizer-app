# main.py
from openai import OpenAI
import os

def _get_api_key() -> str:
    # 1) Streamlit Cloud: st.secrets
    try:
        import streamlit as st
        if "OPENAI_API_KEY" in st.secrets:
            return st.secrets["OPENAI_API_KEY"]
    except Exception:
        pass

    # 2) ENV (lokal via export / Windows setx oder .env mit python-dotenv)
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key

    # 3) .env als Fallback (optional)
    try:
        from dotenv import load_dotenv
        load_dotenv()
        key = os.getenv("OPENAI_API_KEY")
        if key:
            return key
    except Exception:
        pass

    raise RuntimeError("OPENAI_API_KEY ist nicht gesetzt (weder st.secrets, ENV noch .env).")


# WICHTIG: Key direkt an den Client übergeben
client = OpenAI(api_key=_get_api_key())

def callOpenAI(prompt: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Du bist ein exzellenter Zusammenfasser. Bitte den vorgegebenen Text in maximal zwei Sätzen zusammenfassen."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )
    return resp.choices[0].message.content
