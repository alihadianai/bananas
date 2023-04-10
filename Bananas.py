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

# Set the background color and style
page_bg_img = '''
<style>
body {
background-color: #151515;
color: white;
font-family: 'Press Start 2P', cursive;
}
.stButton button {
background-color: #ffbf00;
}
.stTextInput>div>div>input {
color: red;
}
.stTextInput>div>label {
color: white;
}
.stTextInput>div>div>div {
background-color: #333333;
}
.stTextArea>div>div>textarea {
color: white;
}
.stTextArea>div>label {
color: white;
}
.stTextArea>div>div>div {
background-color: #333333;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Set up the navigation bar
navigation = st.sidebar.radio("Navigation", ["Generate", "Information", "Code Resources", "About Us"])

# Create the generate page
if navigation == "Generate":
    st.title("Banana Image Generator")
    st.write("Enter a prompt and an image of a banana will be generated based on it!")
    # Create the text input and Generate button
    prompt = st.text_input("Prompt:")
    if st.button("Generate"):
        with st.spinner("Generating image..."):
            # Insert your code here to generate the image
            # You can use any image generation model or API you prefer
            # For this example, we'll just use a simple dot art banana
            banana = Image.new('RGB', (300, 300), color = '#F7DC6F')
            banana_pixels = banana.load()
            for i in range(0, 300, 10):
                for j in range(0, 300, 10):
                    if (i in range(30, 270) and j in range(30, 270)) or (i in range(0, 60) and j in range(70, 200)):
                        banana_pixels[i, j] = (255, 255, 255)
                    elif i in range(90, 210) and j in range(120, 210):
                        banana_pixels[i, j] = (255, 255, 255)
            response_bytes = BytesIO()
            banana.save(response_bytes, format='PNG')
            response_bytes.seek(0)
            st.image(response_bytes, use_column_width=True)
        st.success("Done!")

# Create the information page
elif navigation == "Information":
    st.title("Banana Information")
    st.write("Bananas are a great source of potassium and other nutrients.")

# Create the code resources page
elif navigation == "Code Resources":
    st.title("Banana Code Resources")
    st.write("Here are some helpful resources for coding with bananas.")

# Create the about us page
else:
    st.title("About Us")
    st.write("We are a team of banana enthusiasts who love creating art and technology!")
