import streamlit as st
from views import tentang_saya, tentang_project, prediction, kontak

st.set_page_config(page_title="Telco Customer Churn App", page_icon="📉", layout="wide")

def load_css():
    with open("style.css","r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.sidebar.markdown("<div class='card'><div class='h1'>📉 Churn App</div><p class='muted'>Telco Customer Churn </p></div>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Menu",
    ["Tentang Saya", "Tentang Project", "Prediction", "Kontak"],
    index=1
)

if menu == "Tentang Saya":
    tentang_saya.show()
elif menu == "Tentang Project":
    tentang_project.show()
elif menu == "Prediction":
    prediction.show()
else:
    kontak.show()
