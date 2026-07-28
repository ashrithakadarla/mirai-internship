import streamlit as st
import requests
import random

st.title("My AI Image Generator")

# Sidebar
art_style = st.sidebar.selectbox(
    "Select desired Art Style",
    ["Photorealistic", "Anime", "Vintage Victorian", "Sketch", "3D Render"]
)

width = st.sidebar.slider(
    "Image Width",
    min_value=256,
    max_value=1024,
    value=512
)

height = st.sidebar.slider(
    "Image Height",
    min_value=256,
    max_value=1024,
    value=512
)

magic_enhance = st.sidebar.checkbox("✨ Enable Magic Enhance")

# Creative prompts for Surprise Me
surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A dragon reading books in a futuristic library",
    "A giant octopus serving coffee underwater",
    "A floating castle above rainbow clouds"
]

user_prompt = st.text_input("Describe the image you want to generate:")

generate = st.button("Generate Image")
surprise = st.button("Surprise Me!")

# Decide which prompt to use
prompt = ""

if generate:
    prompt = user_prompt

elif surprise:
    prompt = random.choice(surprise_prompts)
    st.info(f"Surprise Prompt: **{prompt}**")

# Generate image
if prompt:

    with st.spinner("Rendering your image..."):

        full_prompt = f"{prompt}, make the art style: {art_style}"

        # Task 3: Magic Enhance
        if magic_enhance:
            full_prompt += ", masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render"

        # Task 1: Width & Height parameters
        url = (
            f"https://image.pollinations.ai/prompt/{full_prompt}"
            f"?width={width}&height={height}"
        )

        response = requests.get(url)

        if response.status_code == 200:

            st.success("Image Generated Successfully!")

            st.image(response.content, caption=full_prompt)

            # Task 2: Dynamic file name
            st.download_button(
                label="Download Image",
                data=response.content,
                file_name=f"{art_style}_image.png",
                mime="image/png"
            )

        else:
            st.error("API is not working.")

elif generate:
    st.warning("Please add an image description.")