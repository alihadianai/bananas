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
st.set_page_config(
    page_title="Banana Chatbot",
    page_icon=":banana:",
    layout="wide"
)

# Set background color and font
st.markdown("""
    <style>
    body {
        background-color: #0041C2;
        color: white;
        font-family: 'Press Start 2P', cursive;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Set up title and subtitle
st.title("Banana Chatbot")
st.markdown("<h4 style='text-align: center; color: #FFC300'>Enter a prompt and the chatbot will respond!</h4>", unsafe_allow_html=True)

# Set up the text input and Generate button
prompt = st.text_input("Prompt:")
if st.button("Generate", key="generate_btn"):
    with st.spinner("Generating response..."):
        response = generate_response(prompt)
    st.success("Done!")
    st.markdown(f"<p>{response}</p>", unsafe_allow_html=True)
    # Download the image and display it
    image_url = "https://imgtr.ee/images/2023/04/10/nQda2.png"
    response = requests.get(image_url)
    try:
        img = Image.open(BytesIO(response.content))
        st.image(img, use_column_width=True)
    except:
        st.warning("Unable to display image.")
