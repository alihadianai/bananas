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
st.set_option('deprecation.showfileUploaderEncoding', False)

# Set up the background image
bg_image = Image.open("banana_bg.png")
bg_image = bg_image.resize((700,500))
page_bg = '''
<style>
body {
background-image: url("data:image/png;base64,%s");
background-size: cover;
}
</style>
''' % base64.b64encode(bg_image.getvalue()).decode('utf-8')
st.markdown(page_bg, unsafe_allow_html=True)

# Set up the header
st.image("banana_title.png")
st.subheader("Enter a prompt and the chatbot will respond!")

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

# Set up the Information section
st.subheader("Information")
st.write("This app is a demonstration of how a chatbot can be used to respond to prompts. In this case, a dummy response is generated after a delay of 5 seconds to simulate the response generation process. The chatbot can be modified to use any language model or API of your choice to generate responses. The app also displays an image in response to the prompt. You can modify the app to display any image of your choice.") 
st.write("This app was created by [Your Name Here]. © 2023. All rights reserved.")
