import streamlit as st
import google.generativeai as genai
from IPython.display import display, Markdown
import pandas as pd
import data
import ast
import functions as fun

characters_df = data.characters_df

selected_character = st.selectbox("Select a character", characters_df['Name'].tolist(), index=None)

if selected_character != None:
    character_df = characters_df[characters_df['Name'] == selected_character]
    col1, col2 = st.columns([0.3,0.7])
    name = character_df['Name'].iloc[0]
    full_name = character_df['Full Name'].iloc[0]
    desc = character_df['Deck'].iloc[0]
    aliases = character_df['Aliases'].iloc[0].replace("[","").replace("]","").replace("'","").replace(",",", ")
    creators = character_df['Creators'].iloc[0].replace("[","").replace("]","").replace("'","").replace(",",", ")
    gender = character_df['Gender'].iloc[0]
    publisher = character_df['Publisher'].iloc[0]
    race = character_df['Race'].iloc[0]
    image = ast.literal_eval(character_df['Image'].iloc[0])

    with col1:
        st.image(image['medium_url'])
    
    with col2:
        st.header(f"{name} ({full_name})")

        st.subheader("Aliases")
        st.write(aliases)
        
        st.subheader("Creators")
        st.write(creators)

        st.subheader("Publisher")
        st.write(publisher)

        st.subheader("Gender & Race")
        st.write(f"{gender}, {race}")

        st.subheader("Short description")
        st.write(desc)
    
    st.subheader("Combat")

    team1 = st.multiselect("Sélectionnez des coéquipier ou laissez vide", characters_df['Name'].tolist())

    st.write("VS")

    team2 = st.multiselect("Sélectionnez un ou plusieurs adversaire", characters_df['Name'].tolist())

    addons = st.text_area("Ajouter des details pour le combat")

    GOOGLE_API_KEY = st.text_input("Entrez une clé API valide",type='password')

    if st.button("Combattez!"):
        st.write(fun.fightbot(team1+[name],team2,addons,GOOGLE_API_KEY))


