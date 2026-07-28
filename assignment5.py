import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
from google import genai
from gtts import gTTS
import tempfile

load_dotenv()

st.set_page_config(
    page_title="AI Visual Novel",
    page_icon="📖",
    layout="wide"
)

st.title("AI Multi-Modal Visual Novel")

@st.cache_resource
def get_client():
    return genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

client = get_client()

st.sidebar.header("Story Settings")

genre = st.sidebar.selectbox(
    "Story Genre",
    [
        "Fantasy",
        "Sci-Fi",
        "Mystery",
        "Horror",
        "Adventure"
    ]
)

art_style = st.sidebar.selectbox(
    "Art Style",
    [
        "Anime",
        "Photorealistic",
        "Fantasy Art",
        "Pixel Art",
        "Sketch"
    ]
)

if "story" not in st.session_state:
    st.session_state.story = []

if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(
        model="gemini-2.5-flash"
    )

if "current_options" not in st.session_state:
    st.session_state.current_options = []

def generate_story(user_choice):
    prompt = f"""
You are an AI Visual Novel Engine.

Story Genre: {genre}
Art Style: {art_style}

The player's latest action is:
"{user_choice}"

Continue the story.

IMPORTANT:
Return ONLY a valid JSON object.

Format:

{{
    "story_text":"Write an interesting story paragraph.",
    "image_prompt":"Describe an image for an AI image generator.",
    "options":[
        "Choice 1",
        "Choice 2",
        "Choice 3"
    ]
}}

Do NOT include markdown.
Do NOT include ```json.
Do NOT explain anything.
Return ONLY the JSON.
"""

    try:
        response = st.session_state.chat.send_message(prompt)
        return response.text
    except Exception:
        st.error("Gemini is unavailable. Please try again.")
        return None

def parse_story(json_text):

    try:
        return json.loads(json_text)

    except json.JSONDecodeError:

        st.error("Gemini returned invalid JSON.")

        st.code(json_text)

        return None

def generate_image(image_prompt):

    try:
        url = f"https://image.pollinations.ai/prompt/{image_prompt}"

        response = requests.get(url, timeout=30)

        if response.status_code == 200:
            return response.content

    except Exception:
        st.toast("Image server is busy, skipping visual...")

    return None

def generate_audio(story_text):

    try:

        tts = gTTS(text=story_text, lang="en")

        temp_audio = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        tts.save(temp_audio.name)

        return temp_audio.name

    except Exception:

        st.toast("Unable to generate narration.")

        return None

if st.button("Start Story"):
    raw = generate_story("Begin the story")
    if raw:
        data = parse_story(raw)
        if data:
            st.session_state.story.append(data)
            st.session_state.current_options = data["options"]

if st.sidebar.button("Restart Story"):

    st.session_state.story = []

    st.session_state.current_options = []

    st.session_state.chat = client.chats.create(
        model="gemini-2.5-flash"
    )

    st.rerun()

for scene in st.session_state.story:

    st.markdown("---")

    st.subheader("Story")

    st.write(scene["story_text"])

    image = generate_image(scene["image_prompt"])

    if image:
        st.image(image, width="content")

    audio = generate_audio(scene["story_text"])

    if audio:
        st.audio(audio)

if st.session_state.current_options:
    st.subheader("What will you do next?")
    for option in st.session_state.current_options:
        if st.button(option):
            raw = generate_story(option)
            if raw:
                data = parse_story(raw)
                if data:
                    st.session_state.story.append(data)
                    st.session_state.current_options = data["options"]
                    st.rerun()

st.divider()
st.caption("AI Multi-Modal Visual Novel | Built with Streamlit, Gemini, Pollinations AI & gTTS")