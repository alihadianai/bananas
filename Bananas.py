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
st.title("Banana Chatbot")

# Set background image
bg_image = Image.open("https://i.imgur.com/6dXHfu8.png")
st.image(bg_image, use_column_width=True)

# Set up input form
form = st.form(key='my_form')
prompt = form.text_input('Prompt')
submit_button = form.form_submit_button(label='Generate')

if submit_button:
    with st.spinner("Generating response..."):
        response = generate_response(prompt)
    st.success("Done!")
    st.write(response)

    # Download the image and display it
    image_url = "https://thumb.ac-illust.com/a8/a8ccf142b92269fcccc3e8f92b5bba0e_t.jpeg"
    response = requests.get(image_url)
    try:
        img = Image.open(BytesIO(response.content))
        st.image(img, width=200, caption='Generated Image')
    except:
        st.warning("Unable to display image.")
