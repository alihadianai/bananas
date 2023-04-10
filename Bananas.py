import streamlit as st
import requests
from PIL import Image, ImageOps
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
navigation = st.sidebar.radio("Navigation", ["Image Generator", "Information", "Code Resources", "About Us"])

# Create the image generator page
if navigation == "Image Generator":
    st.title("Banana Image Generator")
    st.write("Enter a prompt and an image of a banana will be generated in dot art style!")
    # Create the text input and Generate button
    prompt = st.text_input("Prompt:")
    if st.button("Generate"):
        with st.spinner("Generating image..."):
            # Download the image and convert it to dot art
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Banana-Single.jpg/480px-Banana-Single.jpg"
            response = requests.get(image_url)
            try:
                img = Image.open(BytesIO(response.content))
                img = ImageOps.invert(img.convert("L")).resize((80, 80))
                dots = ["." if px < 128 else "*" for px in img.getdata()]
                dots = [dots[i:i+img.width] for i in range(0, len(dots), img.width)]
                dots = "\n".join([" ".join(row) for row in dots])
                # Generate the response and display it along with the dot art image
                response = generate_response(prompt)
                st.success("Done!")
                st.write(response)
                st.write(dots)
            except:
                st.warning("Unable to generate image.")

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
    st.write("We are a team of banana enthusiasts who love creating dot art images.")
