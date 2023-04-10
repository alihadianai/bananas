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
st.set_page_config(page_title="Banana Chatbot", page_icon=":banana:", layout="wide")
background_color = '#F5B7B1'
text_color = '#212F3D'
font = 'monospace'
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background-color: {background_color};
            color: {text_color};
            font-family: {font};
        }}
        .stButton button {{
            background-color: #E74C3C;
            color: white;
            border-radius: 8px;
        }}
        .stTextInput {{
            background-color: white;
            border-radius: 8px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Banana Chatbot")
st.subheader("An old-school American AI chatbot")

# Set up the image for the header
header_url = "https://imgtr.ee/images/2023/04/10/nQda2.png"
header_response = requests.get(header_url)
header_img = Image.open(BytesIO(header_response.content))

# Display the header image
st.image(header_img, use_column_width=True)

# Create the text input and Generate button
prompt = st.text_input("You say:", "")
if st.button("Banana say:"):
    with st.spinner("Thinking..."):
        response = generate_response(prompt)
    st.success("Done!")
    st.write("Banana say:", response)
    # Download the image and display it
    image_url = "https://thumb.ac-illust.com/a8/a8ccf142b92269fcccc3e8f92b5bba0e_t.jpeg"
    response = requests.get(image_url)
    try:
        img = Image.open(BytesIO(response.content))
        st.image(img, use_column_width=True)
    except:
        st.warning("Unable to display image.")
