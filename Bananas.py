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
st.set_page_config(page_title="Banana Chatbot", page_icon=":banana:", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
    <style>
        .main {
            background-color: #292A2D;
            background-image: url('https://i.imgur.com/YxQm46M.png');
            background-size: cover;
            background-position: center center;
        }
        .stTextInput {
            background-color: #3C3D3F;
            color: #F1F1F1;
            font-family: 'Press Start 2P', cursive;
        }
        .stButton>button {
            background-color: #FECE4E;
            color: #292A2D;
            font-weight: bold;
            font-family: 'Press Start 2P', cursive;
        }
        .stSuccess {
            color: #FECE4E;
        }
        .stWarning {
            color: #FF5F5F;
        }
        .stImage {
            margin-top: 20px;
        }
        .stText {
            color: #F1F1F1;
            font-family: 'Press Start 2P', cursive;
            font-size: 20px;
            line-height: 1.5;
        }
    </style>
""", unsafe_allow_html=True)

# Set up the sidebar
st.sidebar.markdown("<h1 style='color: #F1F1F1; font-family: \"Press Start 2P\", cursive;'>Banana Chatbot</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<hr style='border-top: 2px solid #FECE4E; margin: 10px 0;'>", unsafe_allow_html=True)
st.sidebar.write("Enter a prompt and the chatbot will respond!")
prompt = st.sidebar.text_input("", "", max_chars=50)
if st.sidebar.button("Generate"):
    with st.spinner("Generating response..."):
        response = generate_response(prompt)
    st.success("Done!")
    st.markdown(f"<p class='stText'>{response}</p>", unsafe_allow_html=True)
    # Download the image and display it
    image_url = "https://i.imgur.com/nDCKhJd.png"
    response = requests.get(image_url)
    try:
        img = Image.open(BytesIO(response.content))
        st.image(img, use_column_width=True, caption="Banana Chatbot")
    except:
        st.warning("Unable to display image.")
