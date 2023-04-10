import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import time

# Define the function to generate the response
def generate_response(prompt):
    # Insert your code here to generate the response
    # You can use any language model or API you prefer
    time.sleep(5) # Simulate the response generation process
    response = f"Your prompt: {prompt}\n\nThis is a dummy response."
    return response

# Set up the Streamlit app
st.set_page_config(page_title="Banana Chatbot", page_icon="🍌", layout="wide")

# Set the background image and dot art
bg_image_url = "https://i.imgur.com/YsmU1l6.jpg"
st.set_page_bg_image(bg_image_url)
st.markdown(
    """
    <style>
        .stApp {
            background-color: rgba(255, 255, 255, 0.8);
        }
        .banana {
            position: absolute;
            top: 20px;
            left: 20px;
            font-size: 64px;
            line-height: 1;
            color: #FEE12B;
            text-shadow: 2px 2px #666;
            font-family: 'Press Start 2P', cursive;
            z-index: 1000;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Create the text input and Generate button
prompt = st.text_input("Prompt:")
if st.button("Generate"):
    with st.spinner("Generating response..."):
        response = generate_response(prompt)
    st.success("Done!")
    st.write(response)
    # Download the image and display it
    image_url = "https://thumb.ac-illust.com/a8/a8ccf142b92269fcccc3e8f92b5bba0e_t.jpeg"
    response = requests.get(image_url)
    try:
        img = Image.open(BytesIO(response.content))
        st.image(img, use_column_width=True)
    except:
        st.warning("Unable to display image.")
        
# Add the dot art of the small banana
st.markdown('<p class="banana">.</p>', unsafe_allow_html=True)
