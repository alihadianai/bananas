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

# Set up the background image
page_bg_img = '''
<style>
body {
background-image: url("https://i.imgur.com/Lf0vOM4.png");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Set up the header
st.write("<h1 style='text-align: center; color: red; font-family: Courier;'>Banana Chatbot</h1>", unsafe_allow_html=True)

# Create the text input and Generate button
prompt = st.text_input("Prompt:", key="prompt")
if st.button("Generate"):
    with st.spinner("Generating response..."):
        response = generate_response(prompt)
    st.success("Done!")
    st.write("<p style='color: blue; font-family: American Typewriter;'>Response:</p>", unsafe_allow_html=True)
    st.write(f"<p style='font-family: American Typewriter;'>{response}</p>", unsafe_allow_html=True)

    # Download the image and display it
    image_url = "https://thumb.ac-illust.com/a8/a8ccf142b92269fcccc3e8f92b5bba0e_t.jpeg"
    response = requests.get(image_url)
    try:
        img = Image.open(BytesIO(response.content))
        st.image(img, use_column_width=True)
    except:
        st.warning("Unable to display image.")
