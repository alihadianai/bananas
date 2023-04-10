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
st.set_page_config(page_title="AI Image Generator", page_icon="🎨", layout="wide")

# Set up the navigation bar
st.markdown("""
<style>
nav {
    display: flex;
    justify-content: space-between;
    padding: 10px;
    background-color: #330033;
    color: white;
}

nav a {
    color: white;
    text-decoration: none;
}

nav a:hover {
    text-decoration: underline;
}

</style>
""", unsafe_allow_html=True)

nav_pages = {
    "Chat": "chat",
    "Information": "info",
    "Code Resources": "code",
    "About Us": "about"
}

page = st.sidebar.selectbox("Select a page", list(nav_pages.keys()))

nav_html = "<nav>"
for name, url in nav_pages.items():
    if url == page:
        nav_html += f'<strong>{name}</strong>'
    else:
        nav_html += f'<a href="/{url}">{name}</a>'
nav_html += "</nav>"

st.markdown(nav_html, unsafe_allow_html=True)

# Create the page content based on the selected page
if page == "chat":
    st.title("AI Image Generator")
    st.write("Enter a prompt and the AI will generate an image!")
    st.write("For example: 'Generate a sci-fi animation with Spielberg's director style'")
    # Create the text input and Generate button
    prompt = st.text_input("Prompt:", value="Generate a sci-fi animation with Spielberg's director style", max_chars=None, key=None, type='default', help=None, placeholder=None, on_change=None, args=None, kwargs=None)
    prompt_text = prompt_css = '<p style="color:red;">' + prompt + '</p>'
    if st.button("Generate"):
        with st.spinner("Generating image..."):
            response = generate_response(prompt)
        st.success("Done!")
        st.write(response)
        # Download the image and display it
        image_url = "https://imgtr.ee/images/2023/04/10/nQda2.png"
        response = requests.get(image_url)
        try:
            img = Image.open(BytesIO(response.content))
            st.image(img, use_column_width=True)
        except:
            st.warning("Unable to display image.")
elif page == "info":
    st.title("Information")
    st.write("This is the information page.")
    st.write("Here you can find information about the AI image generator.")
elif page == "code":
    st.title("Code Resources")
    st.write("This is the code resources page.")
    st.write("Here you can find links to the code used to build the AI image generator.")
elif page == "about":
    st.title("About Us")
    st.write("This is the about us page.")
    st.write("Here you can find information about the creators of the AI image generator.")
