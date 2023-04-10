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

# Define the sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("", ("Home", "Chat", "Information", "Code Resource", "About Us"))

# Define the pages
if page == "Home":
    st.title("Welcome to Banana Chatbot")
    st.write("This is a chatbot that generates responses to your prompts. Try it out in the Chat page!")
    # Set background color to yellow
    st.markdown(
        """
        <style>
        body {
            background-color: #ffff99;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
elif page == "Chat":
    st.title("Chat with Banana Chatbot")
    st.write("Enter a prompt and the chatbot will respond!")
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
elif page == "Information":
    st.title("Information")
    st.write("This page contains some information about Banana Chatbot.")
    st.write("Banana Chatbot is a fun chatbot that generates responses to your prompts. It uses advanced machine learning techniques to generate responses that are sometimes humorous, sometimes informative, and sometimes nonsensical. Try it out in the Chat page!")
    st.write("The chatbot was created by John Doe and Jane Smith, two developers who love bananas and chatbots.")
elif page == "Code Resource":
    st.title("Code Resource")
    st.write("This page contains some resources related to the development of Banana Chatbot.")
    st.write("The chatbot was developed using Python and Streamlit, an open-source app framework for machine learning and data science.")
    st.write("If you want to learn more about Streamlit, check out their website at https://streamlit.io/.")
    st.write("The code for Banana Chatbot is available on GitHub at https://github.com/johndoe/banana-chatbot.")
elif page == "About Us":
    st.title("About Us")
    st.write("This page contains some information about the creators of Banana Chatbot.")
    st.write("John Doe is a software developer who loves bananas, Python, and machine learning. He lives in San Francisco, California.")
    st.write("Jane Smith is a data scientist who loves bananas, statistics, and natural language processing. She lives in New York City, New York.")
