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
pages = {
    "Home": "This is the home page. Use the navigation bar to access other pages.",
    "Chat": "Enter a prompt and the chatbot will respond!",
    "Information": "This page contains information about the chatbot.",
    "Code Resource": "This page contains the code used to build the chatbot.",
    "Terms": "This page contains the terms of use for the chatbot.",
}

# Create the old-school navigation bar
st.markdown("""
<style>
nav {
    display: flex;
    background-color: black;
    padding: 10px 20px;
}
nav a {
    color: white;
    text-decoration: none;
    margin-right: 20px;
    font-size: 20px;
    font-weight: bold;
}
nav a:hover {
    color: yellow;
}
</style>
""", unsafe_allow_html=True)
navigation = st.sidebar.radio("Navigate", list(pages.keys()))

# Display the selected page
if navigation == "Home":
    st.title("Welcome to Banana Chatbot!")
    st.write(pages[navigation])
elif navigation == "Chat":
    st.title("Banana Chatbot")
    st.write(pages[navigation])
    # Create the text input and Generate button
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
elif navigation == "Information":
    st.title("Information")
    st.write(pages[navigation])
    st.write("This chatbot was created as a demo for educational purposes only.")
    st.write("The responses are generated using a simple algorithm and are not based on any AI or machine learning model.")
    st.write("The chatbot is for entertainment purposes only and should not be used as a substitute for professional advice.")
elif navigation == "Code Resource":
    st.title("Code Resource")
    st.write(pages[navigation])
    st.write("Here is the code used to build this chatbot:")
    with st.beta_expander("View Code"):
        with open("Bananas.py", "r") as f:
            st.code(f.read())
elif navigation == "Terms":
    st.title("Terms")
    st.write(pages[navigation])
    st.write("By using this chatbot, you agree to the following terms of use:")
    st.write("This chatbot is for entertainment purposes only and should not be used as a substitute for professional advice.")
    st.write("The creators of this chatbot are
