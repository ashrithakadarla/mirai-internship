# MirAI School of Technology — AI Builder Internship

This repository documents my learning journey through the MirAI School of Technology Virtual Summer Internship 2026 — AI Builder Track. It contains session-based learning, assignments, practical experiments, and application work completed during the internship.

## About

This repository captures my internship progress through hands-on exercises, AI application development, and assignment work during the program.

## Internship Sessions

### Session 1 — Google Gemini API Foundations

- File: `internship.py`
- Learned to use the Google Gemini API with Python to generate AI responses.

### Session 2 — Streamlit Basics and User Interaction

- Files: `app.py`, `Calculator.py`, `identity_echo_interface.py`
- Explored Streamlit basics, user input, and interactive UI design.
- Built a basic calculator and the Assignment 1 project: Identity Echo Interface.
- Identity Echo Interface collected user details, validated input, and estimated token usage for the entered text or message.

### Session 3 — Google Gemini / AI Chatbot

- File: `session3.py`
- Built a Streamlit AI chatbot using the Google Gemini API.
- Managed the API key using environment variables and local `.env`-style configuration.

### Session 4 — AI Image Generation and Stateful Chatbot

- Files: `session4.py`, `multipersonality_chatbot/app.py`
- Worked with Pollinations AI to generate images from text prompts.
- Built a stateful multi-personality chatbot using Streamlit Session State to preserve chat history and state.

### Session 5 — AI Image Generation and Improvements

- Files: `session5.py`, `assignment4.py`
- Continued working with Pollinations AI for image generation.
- Explored customizable art styles and image dimensions.
- Improved the image generation flow with Magic Enhance, Surprise Me, and dynamic downloads.

### Session 6 — Stateful AI and Visual Novel Concepts

- Files: `session6.py`, `assignment5.py`
- Built a stateful Gemini chatbot with chat history and downloadable conversation output.
- Worked on AI storytelling concepts with structured JSON responses, dynamic story choices, Pollinations AI visuals, and gTTS narration.

### Session 7 — Git, GitHub, Version Control, and Deployment

- Covered Git, GitHub, version control, repository workflow, deployment basics, and Streamlit Community Cloud.

### Session 8 — Speech-to-Text

- File: `session8.py`
- Built a simple speech-to-text application in Streamlit using `streamlit-mic-recorder`.

### Session 9 — Sports Analytics Dashboard

- File: `session9.py`
- Built a Streamlit sports analytics dashboard with player selection, KPI cards, and a run-rate chart.
- Used Pandas and NumPy to generate a simple data view and visualize performance trends.

### Session 10 — Streamlit Forms and Data Interaction

- File: `session10.py`
- Explored Streamlit loading states, forms, expanders, and user interaction patterns.
- Built a small dashboard showing API latency simulation, form inputs, and editable tabular data using `st.data_editor`.

### Session 11 — Interactive Web Development with DOM & APIs

This session was part of the internship curriculum. No separate implementation file from this session is included in this repository.

### Session 12 — Build the Frontend of an AI Resume Optimizer and Connect It to an LLM API

This session was part of the internship curriculum. No separate implementation file from this session is included in this repository.

### Session 13 — Build the Frontend of an AI Resume Optimizer and Connect It to an LLM API

This session was part of the internship curriculum. No separate implementation file from this session is included in this repository.

### Session 14 — Capstone Project

## Assignments

| Assignment | Description | Technologies |
|---|---|---|
| Assignment 1 — Identity Echo Interface | Streamlit interface for collecting user details, validating input, and estimating token usage for entered text or messages. | Streamlit, Python |
| Assignment 2 — Gemini AI Chatbot | Streamlit-based chatbot using the Google Gemini API with environment-variable-based API management. | Streamlit, Google Gemini API, Python |
| Assignment 3 — Multi-Personality Chatbot | Stateful chatbot that preserves conversation history and personality-based responses using Streamlit Session State. | Streamlit, Python |
| Assignment 4 — Enhanced AI Image Generator | AI image generation workflow with art-style controls, image sizing, Magic Enhance, Surprise Me, and dynamic downloads. | Streamlit, Pollinations AI |
| Assignment 5 — AI Multi-Modal Visual Novel | Story-driven AI application using structured JSON responses, dynamic choices, Pollinations visuals, and gTTS narration. | Streamlit, Gemini, Pollinations AI, gTTS, JSON |
| Assignment 6 — GitHub Terminal-Style Profile | Built a terminal-inspired GitHub profile README using Markdown, ASCII art, stats, and contribution-style visuals. | GitHub, Markdown |
| Assignment 7 — Life-OS Wellbeing Dashboard | Streamlit wellbeing dashboard using screen-time data, Pandas, visualizations, and Gemini-powered coaching. | Streamlit, Pandas, Gemini, Python |

## Capstone Project — Tech Roast

Tech Roast is an AI-powered resume critique and review application that uses Google Gemini to analyze resume content and provide recruiter-style feedback. It helps identify weaknesses in a resume and improve positioning for technical roles.

- GitHub Repository: [Tech Roast GitHub Repository](https://github.com/ashrithakadarla/tech-roast)
- Live Demo: [Tech Roast Live Demo](https://tech-roast-bfxaxv4qvoirenmelkstul.streamlit.app/)

## Technologies & Skills

| Technology / Skill | Usage |
|---|---|
| Python | Core application development |
| Streamlit | Interactive AI and dashboard apps |
| Google Gemini API / `google-genai` | AI response generation and coaching |
| Pollinations AI | AI image generation |
| Pandas | Data processing and dashboard aggregation |
| Requests | API requests |
| gTTS | Text-to-speech narration |
| `streamlit-mic-recorder` | Speech-to-text input |
| `python-dotenv` | Environment variable management |
| JSON | Structured output parsing |
| Git | Version control |
| GitHub | Repository and profile workflow |
| Streamlit Community Cloud | App deployment |

## Repository Structure

```text
mirai-intern/
├── assignment7/
│   ├── README.md
│   ├── app.py
│   ├── requirements.txt
│   └── screentime.csv
├── multipersonality_chatbot/
│   └── app.py
├── .gitignore
├── README.md
├── Calculator.py
├── app.py
├── assignment4.py
├── assignment5.py
├── identity_echo_interface.py
├── internship.py
├── session3.py
├── session4.py
├── session5.py
├── session6.py
├── session8.py
├── session9.py
├── session10.py
└── .gitignore
```

## Learning Outcomes

This repository reflects practical learning in:

- Gemini API integration
- Prompt engineering
- Streamlit development
- Session state
- Stateful AI applications
- AI image generation
- API integration
- JSON parsing
- Multimodal AI development
- Text-to-speech
- Speech-to-text
- Pandas and data visualization
- Environment variable management
- Git and GitHub
- Deployment basics

## Security

API keys and other sensitive values were managed locally through environment variables and `.env` files. These secrets were not committed to GitHub and should never be stored directly in repository files.

## Author

**Ashritha Kadarla**