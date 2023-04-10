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

# Define the function to show the Home page
def show_home():
    st.write("Welcome to the Banana Chatbot!")
    st.write("This app generates responses to your prompts using a language model.")
    st.write("Click on the Chat button to start chatting!")
    
# Define the function to show the Chat page
def show_chat():
    # Create the text input and Generate button
    prompt = st.text_input("Prompt:")
    if st.button("Generate"):
        with st.spinner("Generating response..."):
            response = generate_response(prompt)
        st.success("Done!")
        st.write(response)
        # Download the image and display it
        image_url = "https://imgtr.ee/images/2023/04/10/nQda2.png"
        response = requests.get(image_url)
        try:
            img = Image.open(BytesIO(response.content))
            st.image(img, use_column_width=True)
        except:
            st.warning("Unable to display image.")
    
# Define the function to show the About page
def show_about():
    st.write("This app was created by [Your Name Here].")
    st.write("It uses Streamlit and a language model to generate responses to your prompts.")

# Create the navigation buttons
nav = st.sidebar.radio("Select a page:", ["Home", "Chat", "About"])

# Show the appropriate page based on the user's selection
if nav == "Home":
    show_home()
elif nav == "Chat":
    show_chat()
elif nav == "About":
    show_about()
