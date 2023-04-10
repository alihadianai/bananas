import streamlit as st
from PIL import Image, ImageDraw
import requests
from io import BytesIO

# Set page title
st.set_page_config(page_title="Banana Generator", page_icon=":banana:")

# Set background image
background_image = Image.open("https://i.ibb.co/b3DCgj1/background.jpg")
st.image(background_image, use_column_width=True)

# Set page layout
st.markdown("<h1 style='text-align: center; color: white;'>Banana Generator</h1>", unsafe_allow_html=True)
st.write("")

# Create space for user input
user_input = st.text_input("Write your prompt here:", "")

# Generate button
if st.button("Generate"):
    # Display loading message
    with st.spinner("Generating..."):
        # Get dot art of a small banana
        response = requests.get("https://thumbs.dreamstime.com/z/small-banana-icon-fruit-isolated-white-background-vector-illustration-154441025.jpg")
        img = Image.open(BytesIO(response.content))
        img = img.resize((100, 100))
        draw = ImageDraw.Draw(img)

        # Set dot art parameters
        color = (255, 255, 0)
        diameter = 10
        step = 2

        # Create dot art
        for x in range(step, img.width, step):
            for y in range(step, img.height, step):
                pixel = img.getpixel((x, y))
                if pixel == (0, 0, 0):
                    draw.ellipse((x - diameter, y - diameter, x + diameter, y + diameter), fill=color)

        # Display generated image
        st.image(img, use_column_width=True)
