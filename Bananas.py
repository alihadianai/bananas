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

# Add a background image
background_image = Image.open("bananas_bg.png")
st.image(background_image, use_column_width=True)

# Create the navigation menu
menu = ["Home", "Chat", "About"]
choice = st.sidebar.selectbox("Select a page", menu)

# Display the appropriate page
if choice == "Home":
    st.title("Welcome to the Banana Chatbot!")
    st.write("This chatbot is designed to generate responses based on your prompts. Simply enter a prompt and click the 'Generate' button to get started!")
    
elif choice == "Chat":
    st.title("Banana Chatbot")
    st.write("Enter a prompt and the chatbot will respond!")
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
            
elif choice == "About":
    st.title("About the Banana Chatbot")
    st.write("The Banana Chatbot is a simple web application designed to showcase how to build a chatbot using Streamlit. It was built by John Doe as a fun project and is not intended for production use.")
    st.write("If you have any questions or feedback, feel free to contact John at john.doe@example.com.")

