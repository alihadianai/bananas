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
st.title("Banana Chatbot")

# Set up the navigation bar
nav_options = ["Image Generator", "Code Resources", "About Us"]
nav_selection = st.sidebar.radio("", nav_options)

# Set the font and background color for the app
st.markdown('<style>body { font-family: "Press Start 2P", cursive; background-color: #ffc947;}</style>', unsafe_allow_html=True)

# Show the appropriate page based on the navigation selection
if nav_selection == "Image Generator":
    # Create the text input and Generate button
    with st.beta_container():
        st.markdown('<p style="color:red;">Enter a prompt and the image generator will create a response!</p>', unsafe_allow_html=True)
        prompt = st.text_input("", "")
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
elif nav_selection == "Code Resources":
    st.write("This is the code resources page.")
elif nav_selection == "About Us":
    st.write("This is the about us page.")
