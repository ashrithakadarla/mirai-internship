import streamlit as st
from streamlit_mic_recorder import speech_to_text


st.title("Internship STT")

user_voice=speech_to_text(
    language="en",
    use_container_width=False,
    just_once=True,
    key="STT",
)

if user_voice:
    st.write(user_voice)