import streamlit as st

def save_progress(weight, bmi):
    if "progress" not in st.session_state:
        st.session_state.progress = []
    st.session_state.progress.append({"weight": weight, "bmi": bmi})
