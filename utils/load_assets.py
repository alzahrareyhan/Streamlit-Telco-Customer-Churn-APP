import pickle
import streamlit as st

@st.cache_resource
def load_assets():

    with open("model.pkl", "rb") as f:
        data = pickle.load(f)

    model = data["model"]

    with open("encoders.pkl", "rb") as f:
        encoders = pickle.load(f)

    with open("scalers.pkl", "rb") as f:
        scalers = pickle.load(f)

    return model, encoders, scalers
