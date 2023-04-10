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
st.set_page_config(page_title="Banana Chatbot", page_icon="🍌")
st.markdown(
"""
<style>
body {
    background-image: url('https://i.imgur.com/sJtNWjK.png');
    background-repeat: repeat;
}
.sidebar-content {
    background-image: url('https://i.imgur.com/Wq3fVUU.png');
    background-repeat: repeat;
}
.css-2trqyj, .st-bw, .st-cv, .st-d6, .st-df, .st-dg, .st-hv, .st-it, .st-jh, .st-ki, .st-lf, .st-ly, .st-m1, .st-ni, .st-nt, .st-o3, .st-q7, .st-qw, .st-sf, .st-tq, .st-u9, .st-vh, .st-wy {
    background-color: #FFFFFF;
    border-radius: 25px;
}
.css-hby737, .css-1vdfo4t {
    border-radius: 25px;
}
.st-dz {
    padding: 1rem;
}
.st-cu {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 18px;
    line-height: 24px;
}
.st-cx {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 24px;
    line-height: 32px;
}
.st-cs {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 16px;
    line-height: 20px;
}
.st-cp {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 14px;
    line-height: 18px;
}
.st-cz {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 20px;
    line-height: 24px;
}
.st-dd {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 12px;
    line-height: 16px;
}
.st-cl {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 28px;
    line-height: 36px;
}
.st-ce {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 22px;
    line-height: 28px;
}
.st-ck {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 32px;
    line-height: 40px;
}
.st-ct {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 26px;
    line-height: 32px;
}
.st-cv > .st-cw {
    margin-top: 1rem;
    margin-bottom: 1rem;
}
.css
