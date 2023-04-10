import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import time

translations = {
    "English": {
        "title": "Banana Chatbot",
        "subtitle": "Enter a prompt and the chatbot will respond!",
        "generate_button": "Generate",
        "prompt_text": "Prompt:",
        "response_text": "Response:",
        "error_text": "Unable to display image.",
        "loading_text": "Generating response...",
    },
    "Japanese": {
        "title": "バナナチャットボット",
        "subtitle": "プロンプトを入力してください。チャットボットが応答します！",
        "generate_button": "生成する",
        "prompt_text": "プロンプト：",
        "response_text": "応答：",
        "error_text": "画像を表示できません。",
        "loading_text": "応答を生成しています...",
    }
}


# Define the function to generate the response
def generate_response(prompt):
    # Insert your code here to generate the response
    # You can use any language model or API you prefer
    time.sleep(5) # Simulate the response generation process
    response = f"あなたのプロンプト：{prompt}\n\nこれはダミーのレスポンスです。"
    return response

# Set up the Streamlit app
st.set_page_config(page_title="バナナチャットボット", page_icon="🍌", layout="wide")

# Define the translations for the app
translations = {
    "en": {
        "title": "Banana Chatbot",
        "prompt_label": "Enter a prompt and the chatbot will respond!",
        "generate_button": "Generate",
        "generating_message": "Generating response...",
        "done_message": "Done!",
        "image_warning": "Unable to display image.",
    },
    "ja": {
        "title": "バナナチャットボット",
        "prompt_label": "プロンプトを入力してください。チャットボットが返信します。",
        "generate_button": "生成する",
        "generating_message": "返信を生成しています...",
        "done_message": "完了！",
        "image_warning": "画像を表示できません。",
    },
}

# Set the default language to English
language = "en"

# Create the language selection dropdown
language_options = ["English", "日本語"]
language = st.sidebar.selectbox("Select language / 言語を選択してください", language_options, index=0)

# Translate the UI text based on the selected language
title = translations[language]["title"]
prompt_label = translations[language]["prompt_label"]
generate_button = translations[language]["generate_button"]
generating_message = translations[language]["generating_message"]
done_message = translations[language]["done_message"]
image_warning = translations[language]["image_warning"]

# Set the background image
bg_image_url = "https://i.ibb.co/bm44QV8/background.jpg"
bg_image_style = f"""
<style>
body {{
background-image: url('{bg_image_url}');
background-size: cover;
}}
</style>
"""
st.markdown(bg_image_style, unsafe_allow_html=True)

# Display the title and prompt input
st.title(title)
prompt = st.text_input(prompt_label)

# Create the Generate button
if st.button(generate_button):
    with st.spinner(generating_message):
        response = generate_response(prompt)
    st.success(done_message)
    st.write(response)
    # Download the image and display it
    image_url = "https://thumb.ac-illust.com/a8/a8ccf142b92269fcccc3e8f92b5bba0e_t.jpeg"
    response = requests.get(image_url)
    try:
        img = Image.open(BytesIO(response.content))
        st.image(img, use_column_width=True)
    except:
        st.warning(image_warning)
