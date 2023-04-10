# Import the necessary libraries
import streamlit as st
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random
import time

# Define the function to generate the banana text art
def generate_banana_text(prompt):
    # Define the URL of the banana text art website
    url = f"https://textart.sh/topic/{prompt}"
    response = requests.get(url)
    # Check if the website returns a valid response
    if response.status_code != 200:
        return None
    # Parse the text art from the HTML response
    html = response.content.decode("utf-8")
    start_tag = "<div class=\"post_text\" itemprop=\"text\">"
    end_tag = "</div>"
    start_index = html.find(start_tag)
    end_index = html.find(end_tag, start_index)
    if start_index == -1 or end_index == -1:
        return None
    text_art = html[start_index + len(start_tag) : end_index]
    return text_art

# Define the function to generate the response
def generate_response(prompt):
    # Generate a random banana text art
    text_art = generate_banana_text(prompt)
    # If the text art is None, return an error message
    if text_art is None:
        return "Sorry, we could not generate a banana text art for that prompt."
    # Define the font and size for the text art
    font_path = "fonts/PressStart2P-Regular.ttf"
    font_size = 12
    font = ImageFont.truetype(font_path, font_size)
    # Define the width and height for the image
    width, height = font.getsize(text_art)
    width += 10
    height += 10
    # Create the image and draw the text art on it
    img = Image.new("RGB", (width, height), color="#151515")
    draw = ImageDraw.Draw(img)
    draw.text((5, 5), text_art, font=font, fill=(255, 191, 0))
    # Convert the image to bytes and return it
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    return img_bytes.getvalue()

# Set up the Streamlit app
st.set_page_config(page_title="Banana Text Art Generator", page_icon="🍌", layout="wide")

# Set the background color and style
page_bg_img = '''
<style>
body {
background-color: #151515;
color: white;
font-family: "Press Start 2P", cursive;
}
.stButton button {
background-color: #ffbf00;
}
.stTextInput>div>div>input {
color: red;
}
.stTextInput>div>label {
color: white;
}
.stTextInput>div>div>div {
background-color: #333333;
}
.stTextArea>div>div>textarea {
color: white;
}
.stTextArea>div>label {
color: white;
}
.stTextArea>div>div>div {
background-color: #333333;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Set up the navigation bar
navigation = st.sidebar.radio("Navigation", ["Generator", "Information", "Code Resources", "About Us"])

# Create the generator page
if navigation == "Generator":
    st.title("Banana Text Art Generator")
    st.write("Enter a prompt and we'll generate a random banana text art!")
    # Create the text input and Generate button
    prompt = st.text_input("Prompt:")
