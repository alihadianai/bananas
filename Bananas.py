import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import time

# Translations
translations = {
    "en": {
        "title": "Banana Chatbot",
        "input_label": "Enter a prompt and the chatbot will respond!",
        "generate_button": "Generate",
        "response_message": "Your prompt: {}\n\nThis is a dummy response.",
        "image_warning": "Unable to display image.",
        "input_placeholder": "Prompt:"
    },
    "ja": {
        "title": "バナナチャットボット",
        "input_label": "プロンプトを入力すると、チャットボットが応答します！",
        "generate_button": "生成する",
        "response_message": "あなたのプロンプト：{}\n\nこれはダミーの応答です。",
        "image_warning": "画像を表示できません。",
        "input_placeholder": "プロンプト："
    }
}

# Define the function to generate the response
def generate_response(prompt):
    # Insert your code here to generate the response
    # You can use any language model or API you prefer
    time.sleep(5) # Simulate the response generation process
    response = translations[language]["response_message"].format(prompt)
    return response

# Set up the Streamlit app
st.set_page_config(page_title=translations[language]["title"], page_icon="🍌", layout="wide")

language = st.sidebar.selectbox("Select Language / 言語を選択", options=["en", "ja"])

st.title(translations[language]["title"])
st.write(translations[language]["input_label"])

# Create the text input and Generate button
prompt = st.text_input(translations[language]["input_placeholder"])
if st.button(translations[language]["generate_button"]):
    with st.spinner(translations[language]["generating_message"]):
        response = generate_response(prompt)
    st.success(translations[language]["done_message"])
    st.write(response)
    # Download the image and display it
    image_url = "https://thumb.ac-illust.com/a8/a8ccf142b92269fcccc3e8f92b5bba0e_t.jpeg"
    response = requests.get(image_url)
    try:
        img = Image.open(BytesIO(response.content))
        st.image(img, use_column_width=True)
    except:
        st.warning(translations[language]["image_warning"])
