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
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: url("https://i.imgur.com/xKpokZu.png")
        }}
        .sidebar .sidebar-content {{
            background: url("https://i.imgur.com/kk4lzL9.png")
        }}
        .btn-outline-secondary {{
            color: #FFFFFF;
        }}
        .stTextInput > div > input {{
            color: red;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }}
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Banana Image Generator")
st.write("Enter a prompt and the image generator will respond!")

# Create the text input and Generate button
prompt = st.text_input("Prompt:")
if st.button("Generate"):
    with st.spinner("Generating image..."):
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
