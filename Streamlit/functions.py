import streamlit as st
import google.generativeai as genai
import pandas as pd
import data

characters_df = data.characters_df

def fightbot(team1,team2, addons, GOOGLE_API_KEY):

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')

    system_prompt = f"""
    Je vais te donner un ou plusieurs perssonnage fictif qui vont se battre contre un ou plusieurs personnage fictif, je veux que tu me réponde en français qui gagne et pourquoi

    """
    Team1_df = characters_df[characters_df["Name"].isin(team1)]
    Team2_df = characters_df[characters_df["Name"].isin(team2)]

    chat = model.start_chat(history=[{'role': 'user', 'parts': [system_prompt]}])

    response = chat.send_message(f" details = {addons}; Team 1 = {Team1_df.to_json()}; VS Team 2 = {Team2_df.to_json()}; ")

    return response.text




        