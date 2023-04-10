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

# Set background color and font
page_bg = '''
<style>
body {
background-color: #c0c0c0;
font-family: Arial, sans-serif;
}
</style>
'''
st.markdown(page_bg, unsafe_allow_html=True)

# Set up the header
st.write("<h1 style='text-align: center; color: purple;'>Banana Chatbot</h1>", unsafe_allow_html=True)

# Set up the left and right columns
col1, col2 = st.columns(2)
with col1:
    # Create the text input and Generate button
    prompt = st.text_input("Prompt:", key='prompt')
    if st.button("Generate", key='generate'):
        with st.spinner("Generating response..."):
            response = generate_response(prompt)
        st.success("Done!")
        st.write(response)
with col2:
    # Display the banana image
    image_url = "https://thumb.ac-illust.com/a8/a8ccf142b92269fcccc3e8f92b5bba0e_t.jpeg"
    response = requests.get(image_url)
    try:
        img = Image.open(BytesIO(response.content))
        st.image(img, width=300)
    except:
        st.warning("Unable to display image.")
        
# Set up the footer
st.write("<p style='text-align: center; color: white;'>Created with love by Bananas Corp © 1995</p>", unsafe_allow_html=True)
