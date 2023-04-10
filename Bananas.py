import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Set page configuration
st.set_page_config(
    page_title="Banana Generator",
    page_icon=":banana:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load background image
bg_image = Image.open("https://i.imgur.com/KiTSzRD.png")
page_bg = st.image(bg_image, use_column_width=True)

# Set sidebar
st.sidebar.header("Parameters")
prompt = st.sidebar.text_input("Enter prompt:", "A pixelated banana")
generate = st.sidebar.button("Generate")

# Set main page
st.title("Banana Generator")
st.markdown("---")

if generate:
    # Generate banana image
    banana_url = "https://thumb.ac-illust.com/a8/a8ccf142b92269fcccc3e8f92b5bba0e_t.jpeg"
    response = requests.get(banana_url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((200, 200))
    st.image(img, caption="Pixelated banana", use_column_width=True)

# Add footer
st.markdown("---")
st.write("Built with Streamlit")
