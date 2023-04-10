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

# Define the pages
pages = ["Home", "Chat", "About"]

# Define the contents of each page
home_content = """
## Welcome to Banana Chatbot!

This app allows you to chat with a banana and get some fun responses.
"""

chat_content = """
## Banana Chat

Enter a prompt and the chatbot will respond!
"""

about_content = """
## About Banana Chatbot

This app was created by John Doe as a fun project to showcase Streamlit.
"""

# Add a navigation menu to switch between pages
selection = st.sidebar.radio("Go to", pages)

# Display the content based on the user's selection
if selection == "Home":
    st.write(home_content)
elif selection == "Chat":
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
elif selection == "About":
    st.write(about_content)
