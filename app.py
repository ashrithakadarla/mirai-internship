import streamlit as st

st.title("Mirai Intern App")
st.write("Welcome to the Mirai Intern App! This application is designed to help interns navigate their tasks and resources efficiently. Please use the sidebar to access different sections of the app.")

# Take user input 
user_message=st.text_input("Enter your name")

if st.button("Submit"):
    st.write(f"You entered: {user_message}")