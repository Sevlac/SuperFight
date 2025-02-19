import streamlit as st
import google.generativeai as genai
import pandas as pd
import data
import functions as fun

# /chatbot?tm1=Batman&tm2=Indiana%20Jones&o1=Venom&detail=ils%20ont%203%20grammes%20dans%20le%20sang&o2=none&o3=None

character_df = data.characters_df
query_params = st.query_params
query_params_dict = query_params.to_dict()
teammate_list = []
oponent_list = []
details = ""
for key, val in query_params_dict.items():
        if "tm" in key:
            if val is not None:
                if val.lower() != 'none':
                    teammate_list.append(val)
        elif "o" in key:
            if val is not None:
                if val.lower() != 'none':
                    oponent_list.append(val)
        elif "detail" in key:
            if val is not None:
                if val.lower() != 'none':
                    details = val

# Création du prompt système
system_prompt = f"""
Je vais te donner un ou plusieurs perssonnage fictif qui vont se battre contre un ou plusieurs personnage fictif, je veux que tu me réponde en français qui gagne et pourquoi

"""

team1 = st.multiselect("Sélectionnez le ou les noms de la Team 1", character_df['Name'].tolist(), teammate_list)

st.write("VS")

team2 = st.multiselect("Sélectionnez le ou les noms de la Team 2", character_df['Name'].tolist(), oponent_list)

addons = st.text_area("Ajouter des details pour le combat",details)

if st.button("Validez"):

    st.write(fun.fightbot(team1,team2,addons))


