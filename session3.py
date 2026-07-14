import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from google import genai

st.title("MULTIVERSE OF CHATBOTS")
personality=st.sidebar.selectbox("Who do you want to talk to?",[
    "An Expert Hacker","Iron man","Any random personality","An angry Ravi Sastri","A crazy Ronaldo fan", "Donald Trump"
    ])

intensity=st.sidebar.slider("SOME NAME",min_value=1,max_value=10,value=5,step=1)

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

user_message=st.text_input("Say something:")
if st.button("SEND"):
    if user_message:
        ai_instructions=f"You are acting as {personality} with an intensity level of {intensity}. Respond to the message sent by the user staying completely in character"
        with st.spinner("Connecting to the multiverse!...."):
            response=client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_instructions
            )
            
            st.success("Message received!")
            st.write(response.text)
    else:
        st.warning("Please type a message first!")