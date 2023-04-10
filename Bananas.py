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
st.set_page_config(page_title="Banana Chatbot", page_icon=":banana:", layout="wide")

# Set the background color and font
page_bg = """
<style>
body {
    background-color: #FF9900;
    font-family: 'Comic Sans MS', sans-serif;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Add the header
st.image("https://i.imgur.com/3Mq6g8U.gif", use_column_width=True)
st.subheader("Welcome to the Banana Chatbot!")

# Create the text input and Generate button
prompt = st.text_input("Say something to the chatbot...")
if st.button("Generate"):
    with st.spinner("Generating response..."):
        response = generate_response(prompt)
    st.success("Done!")
    st.write(response)

    # Add a retro graphic
    image_url = "https://i.imgur.com/j9E07Kf.png"
    response = requests.get(image_url)
    try:
        img = Image.open(BytesIO(response.content))
        st.image(img, use_column_width=True)
    except:
        st.warning("Unable to display image.")
