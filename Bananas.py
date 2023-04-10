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
st.markdown("""
<style>
body {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Crect fill='%23fc0' width='50' height='50'/%3E%3Crect fill='%23fc0' x='50' y='50' width='50' height='50'/%3E%3Crect fill='%23f80' x='50' width='50' height='50'/%3E%3Crect fill='%23f80' y='50' width='50' height='50'/%3E%3C/svg%3E");
}
</style>
""", unsafe_allow_html=True)

PAGES = {
    "Home": st.markdown("# Home\n\nWelcome to the Banana Chatbot!"),
    "Chat": st.markdown("# Chat\n\nEnter a prompt and the chatbot will respond!"),
    "About": st.markdown("# About\n\nThis app was created by John Doe.")
}

# Create the text input and Generate button
page = st.sidebar.selectbox("Select a page", ["Home", "Chat", "About"])

if page == "Home":
    st.sidebar.markdown("This is the home page")
elif page == "Chat":
    prompt = st.text_input("Prompt:")
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
else:
    st.sidebar.markdown("This is the about page")
