import streamlit as st

st.set_page_config(
    page_title="SuperFight",
    page_icon="🦸🏻‍♂️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Définir les pages pour la navigation
pages = [
    st.Page("noame.py", title="Analyses", icon="📊"),
    st.Page("character.py", title="Personnage", icon="🤹"),
    st.Page("chatbot.py", title="Fight", icon="🥊"),
]

# Activer la navigation
pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()