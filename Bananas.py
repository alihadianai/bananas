import streamlit as st
import time
from PIL import Image

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
    # Display the image
    st.image(Image.open("https://thumb.ac-illust.com/a8/a8ccf142b92269fcccc3e8f92b5bba0e_t.jpeg"), use_column_width=True)
