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
st.set_page_config(page_title="Banana AI Image Generator", page_icon="🍌", layout="wide")
st.markdown(
    """
    <style>
        .stApp {
            background-image: url('https://i.imgur.com/lxJuCzk.png');
            background-size: cover;
            background-position: center;
        }
        .stTextInput input {
            color: red;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Banana AI Image Generator")
st.write("Please generate an image using Stable Diffusion!")

# Create the text input and Generate button
default_prompt = "Please write your prompt here."
prompt = st.text_input("Prompt:", default_prompt)
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

# Create the navigation bar
navigation = ["Chat", "Information", "Code Resource", "Terms"]
choice = st.sidebar.selectbox("Navigation", navigation)

# Create the pages
if choice == "Chat":
    st.write("Welcome to the chat page!")
    st.write("Here you can chat with our AI image generator and generate amazing images!")
elif choice == "Information":
    st.write("Welcome to the information page!")
    st.write("Here you can find information about our AI image generator and how it works.")
elif choice == "Code Resource":
    st.write("Welcome to the code resource page!")
    st.write("Here you can find the code for our AI image generator and other resources.")
elif choice == "Terms":
    st.write("Welcome to the terms page!")
    st.write("Here you can find the terms and conditions for using our AI image generator.")
