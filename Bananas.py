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
st.set_page_config(page_title="Banana Image Generator", page_icon="🍌", layout="wide")
st.title("Banana Image Generator")
st.write("Enter a prompt and the image generator will create an image!")

# Set the background color and font
page_bg_color = '''
<style>
body {
background-color: #e6e6e6;
font-family: "Brush Script MT", cursive;
}
</style>
'''
st.markdown(page_bg_color, unsafe_allow_html=True)

# Create the text input and Generate button
prompt = st.text_input("Prompt:", key="prompt_input")
prompt_style = "<style> .css-1yqbge4 { color: red; font-size: 24px; }</style>"
st.markdown(prompt_style, unsafe_allow_html=True)

if st.button("Generate"):
    with st.spinner("Generating image..."):
        # Insert your code here to generate the image
        # You can use any image generation model or API you prefer
        image_url = "https://thumb.ac-illust.com/a8/a8ccf142b92269fcccc3e8f92b5bba0e_t.jpeg"
        response = requests.get(image_url)
        try:
            img = Image.open(BytesIO(response.content))
            st.image(img, use_column_width=True)
        except:
            st.warning("Unable to display image.")

# Create the navigation bar
menu = ["Image Generator", "Information", "Code Resources", "About Us"]
choice = st.sidebar.selectbox("Select a page", menu)

# Display the selected page
if choice == "Image Generator":
    st.write("Enter a prompt and the image generator will create an image!")
    prompt = st.text_input("Prompt:", key="prompt_input")
    prompt_style = "<style> .css-1yqbge4 { color: red; font-size: 24px; }</style>"
    st.markdown(prompt_style, unsafe_allow_html=True)

    if st.button("Generate"):
        with st.spinner("Generating image..."):
            # Insert your code here to generate the image
            # You can use any image generation model or API you prefer
            image_url = "https://thumb.ac-illust.com/a8/a8ccf142b92269fcccc3e8f92b5bba0e_t.jpeg"
            response = requests.get(image_url)
            try:
                img = Image.open(BytesIO(response.content))
                st.image(img, use_column_width=True)
            except:
                st.warning("Unable to display image.")
                
elif choice == "Information":
    st.write("This is the information page.")
    st.write("Here you can find more information about our image generator.")
    
elif choice == "Code Resources":
    st.write("This is the code resources page.")
    st.write("Here you can find resources and examples of code for creating your own image generator.")
    
elif choice == "About Us":
    st.write("This is the about us page.")
    st.write("Here you can learn more about our team and the development of this image generator.")
