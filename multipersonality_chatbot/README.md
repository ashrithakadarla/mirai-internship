#  Multiverse of Chatbots – Memory Vault

A Streamlit-based AI chatbot powered by Google's Gemini API that allows users to chat with different AI personalities. This project upgrades the chatbot from a **stateless** application to a **stateful** chatbot using **Streamlit Session State**, enabling it to remember conversation history throughout the session.

## Features

- Multiple AI personalities
  - An Expert Hacker
  - Iron Man
  - Any Random Personality
  - An Angry Ravi Shastri
  - A Crazy Ronaldo Fan
  - Donald Trump
- Adjustable personality intensity
- Interactive chat interface using `st.chat_input()`
- Chat memory using `st.session_state`
- Conversation history persists across Streamlit reruns
- Powered by Google Gemini 2.5 Flash

---

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- python-dotenv

---

## Project Structure

```
.
├── app.py
├── README.md
└── demo.mp4
```

---

## Running the Application

Start the Streamlit app with:

```bash
streamlit run app.py
```

---

## Memory Vault Implementation

This project uses **Streamlit Session State** to maintain chat history.

Implemented features:
- Initialize `st.session_state.messages`
- Display previous chat messages
- Use `st.chat_input()` for user input
- Store user messages
- Store AI responses
- Preserve conversation during reruns

---

## 🎥 Demo Video

The demonstration video is included in this repository.

[▶ Watch Demo Video](demo.mp4)


---

## Author

**Ashritha Kadarla**

Virtual Summer Internship 2026

MirAI School of Technology