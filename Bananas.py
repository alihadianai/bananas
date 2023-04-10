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
st.title("Banana Chatbot")
st.write("Enter a prompt and the chatbot will respond!")

# Create the text input and Generate button
prompt = st.text_input("Prompt:")
if st.button("Generate"):
    with st.spinner("Generating response..."):
        response = generate_response(prompt)
    st.success("Done!")
    st.write(response)
    # Download the image and display it
    image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    st.image(img, use_column_width=True)
