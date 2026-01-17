import streamlit as st

def apply_style():
    st.markdown("""
    <style>
    .block-container { padding: 2rem; }
    </style>
    """, unsafe_allow_html=True)
