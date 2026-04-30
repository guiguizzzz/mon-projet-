import streamlit as st
from input import import_json

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

st.markdown("<h1>Projet objet Python combinaison</h1>", unsafe_allow_html=True)

left, center, right = st.columns([1, 1.2, 1])

with center:
    col1, spacer, col2 = st.columns([1, 0.6, 1])

    with col1:
        fichier_1 = st.file_uploader("TEXTE 1", type=["json"], key="texte1")

    with col2:
        fichier_2 = st.file_uploader("TEXTE 2", type=["json"], key="texte2")

left, middle, right = st.columns(3, vertical_alignment="bottom")

middle.radio(
    "Stratégie de fusion",
    ["Union", "Intersection", "Priorité"]
)

left, middle, right = st.columns(3, vertical_alignment="bottom")
middle.button("Combiner", use_container_width=True)
middle.button("Exporter", use_container_width=True)