import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# App Title
st.title("MULTIVERSE OF CHATBOTS")

# Sidebar
personality = st.sidebar.selectbox(
    "Who do you want to talk to?",
    [
        "An Expert Hacker",
        "Iron Man",
        "Any Random Personality",
        "An Angry Ravi Shastri",
        "A Crazy Ronaldo Fan",
        "Donald Trump"
    ]
)

intensity = st.sidebar.slider(
    "Personality Intensity",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

# ==========================
# Task 1: Initialize Memory
# ==========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================
# Task 2: Display Chat History
# ==========================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================
# Task 3: Chat Input
# ==========================
if user_message := st.chat_input("Say something..."):

    # Display User Message
    with st.chat_message("user"):
        st.markdown(user_message)

    # ==========================
    # Task 4: Save User Message
    # ==========================
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    ai_instructions = f"""
You are acting as {personality}.
Your personality intensity is {intensity}/10.
Always stay completely in character.

User Message:
{user_message}
"""

    with st.chat_message("assistant"):
        with st.spinner("Connecting to the Multiverse..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_instructions
            )

            st.markdown(response.text)

    # Save AI Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )