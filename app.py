import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="SQL Quest",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Remove margens padrão do Streamlit para o HTML ocupar tela cheia
st.markdown("""
    <style>
        .block-container { padding: 0 !important; }
        header { visibility: hidden; }
        footer { visibility: hidden; }
        #MainMenu { visibility: hidden; }
        </style>
""", unsafe_allow_html=True)


# Carrega o arquivo HTML do jogo
html_file = os.path.join(os.path.dirname(__file__), "sql-game.html")

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# Renderiza o HTML com altura total da tela
components.html(html_content, height=900, scrolling=True)

st.markdown(
    '<p style="text-align:center; color:gray; font-size:20px; font-weight:bold;">Criado por Osmar Gurgel</p>',
    unsafe_allow_html=True
)
