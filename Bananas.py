import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import time
import torch
import torch.nn as nn
from torchvision.utils import save_image
import random
from urllib.request import urlopen

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
navigation = st.sidebar.radio("Navigation", ["Generate Banana Text Art", "Information", "Code Resources", "About Us"])

# Create the text art generator page
if navigation == "Generate Banana Text Art":
    st.title("Banana Image Generator")
    st.write("Click the button to generate a random banana text art!")

    # Load the dataset of banana text art from textart.sh
    url = 'https://textart.sh/data/banana.txt'
    response = urlopen(url)
    dataset = response.read().decode('utf-8')
    text_lines = dataset.split('\n')

    # Define the DCGAN generator model
    latent_dim = 100
    img_shape = (32, 32)
    channels = 1
    generator = nn.Sequential(
        nn.Linear(latent_dim, 128),
        nn.LeakyReLU(0.2, inplace=True),
        nn.Linear(128, 256),
        nn.BatchNorm1d(256, 0.8),
        nn.LeakyReLU(0.2, inplace=True),
        nn.Linear(256, 512),
        nn.BatchNorm1d(512, 0.8),
        nn.LeakyReLU(0.2, inplace=True),
        nn.Linear(512, 1024),
        nn.BatchNorm1d(1024, 0.8),
        nn.LeakyReLU(0.2, inplace=True),
        nn.Linear(1024, int(img_shape[0] * img_shape[1] * channels)),
        nn.Tanh()
    )
    # Load the pre-trained weights for the generator
    generator.load_state_dict(torch.load('banana_generator.pth', map_location=torch.device('cpu')))
    generator.eval()

    # Generate a random banana text art
    if st.button("Generate"):
        with st.spinner("Generating image..."):
            # Generate a random noise vector
            noise = torch.randn(1, latent_dim)

            # Generate an image from the noise vector using the generator
            img = generator(noise).view(img_shape)

            # Convert the image tensor to a PIL image
