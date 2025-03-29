import streamlit as st

def apply_theme():
    st.markdown("""<style>
        body {
            background-color: #f0fff0;
        }
        .stButton>button {
            background-color: #66bb6a;
            color: white;
            font-weight: bold;
        }
        .stTextInput>div>input {
            background-color: #ffffff;
        }
    </style>""", unsafe_allow_html=True)
