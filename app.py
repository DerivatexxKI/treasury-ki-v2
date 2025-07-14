import streamlit as st
import openai
import pandas as pd

# API-Key aus den Streamlit Secrets laden
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Treasury KI Agent", layout="wide")
st.title("🤖 Treasury KI-Agent: Mittelfristplanung & Zinsprognose")

# Auswahlmenü
mode = st.sidebar.selectbox("Wähle eine Funktion", [
    "Volkswirtschaftlicher Ausblick",
    "Zinsstrukturprognose",
    "Szenariengenerator",
    "ALCO-Bericht generieren",
    "Erklärung zu Annahmen"
])

PROMPTS = {
    "Volkswirtschaftlicher Ausblick": """
Erstelle einen volkswirtschaftlichen Ausblick für Deutschland (2025–2030) inkl. BIP, Inflation, Arbeitsmarkt und EZB-Leitzinsen. Tabellarisch und erläuternd.
""",
    "Zinsstrukturprognose": """
Prognostiziere Swap-Sätze (2Y, 5Y, 10Y) und EZB-Leitzins für 2025–2030. Begründe die Prognose.
""",
    "Szenariengenerator": """
Erstelle Basis-, Stress- und Positivszenario für Wachstum, Inflation und Zinsen (2025–2030).
""",
    "ALCO-Bericht generieren": """
Erstelle einen ALCO-Bericht zur volkswirtschaftlichen Lage anhand folgender Daten:
EZB: 3.5%→2.0%, Swap 5Y: 2.9%→2.2% (2025–2029).
""",
    "Erklärung zu Annahmen": """
Warum sinkt der EZB-Leitzins im Szenario ab 2026 auf 3.0 %?
"""
}

def call_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content

if st.button("🔍 Analyse starten"):
    with st.spinner("GPT denkt nach..."):
        result = call_gpt(PROMPTS[mode])
        st.subheader("📊 Ergebnis")
        st.markdown(result)

st.markdown("---")
st.markdown("App powered by OpenAI & Streamlit · [© Derivatexx.de]")