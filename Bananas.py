import streamlit as st
from PIL import Image
import time

# Define the background image
background_image_url = "https://imgtr.ee/images/2023/04/10/nQda2.png"

# Define the function to generate the pixelated banana
def generate_pixelated_banana(pixel_size):
    # Insert your code here to generate the pixelated banana
    # You can use any image processing library you prefer
    time.sleep(5) # Simulate the image generation process
    banana_image_url = "https://imgtr.ee/images/2023/04/10/nQda2.png"
    return banana_image_url

# Set up the Streamlit app
st.set_page_config(page_title="Pixelated Banana Generator", page_icon="🍌")
st.markdown(f'<style>body{{background-image: url("{background_image_url}"); background-size: cover;}}</style>', unsafe_allow_html=True)

# Create the parameter input and Generate button
with st.container():
    st.image(Image.open("https://imgtr.ee/images/2023/04/10/nQda2.png"), use_column_width=True)
    pixel_size = st.slider("Pixel size", 1, 100, 10, 1)
    if st.button("Generate"):
        with st.spinner("Generating pixelated banana..."):
            banana_image_url = generate_pixelated_banana(pixel_size)
        st.success("Done!")
        st.image(banana_image_url, use_column_width=True)
