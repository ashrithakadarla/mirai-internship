import streamlit as st
import requests

st.title("My AI IMAGE GENERATOR")
art_style=st.sidebar.selectbox(
    "Select desired Art Style", 
    ["Photorealistic", "Anime", "Vintage Victorian", "Sketch", "3D Render"]
)
width=st.sidebar.slider("Image width",min_value=256,max_value=1024,value=512)
height=st.sidebar.slider("Image height",min_value=256,max_value=1024,value=512)

user_prompt=st.text_input("Describe the image you want to generate:")

if st.button("Generate Image"):
    if user_prompt:
        with st.spinner("Rendering your image..."):
            # Call the API to generate the image
            full_prompt = f"{user_prompt}, make the art style: {art_style}"
            url=f"https://image.pollinations.ai/prompt/{full_prompt}"
            response = requests.get(url)
            
            if response.status_code == 200:
                st.success("Image Generated")
                #st.write(response)
                st.image(response.content, caption=full_prompt)
                st.download_button(
                    label="Download Image",
                    data=response.content,
                    file_name="generated_image.png",
                    mime="image/*"   
                )                                     
            else:
                st.error("API is not working")
    else:
        st.warning("Please add an image description")