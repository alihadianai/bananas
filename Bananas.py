import requests
from requests.structures import CaseInsensitiveDict

import json

QUERY_URL = "https://api.openai.com/v1/images/generations"

def generate_image(prompt, api_key):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {api_key}"

    data = """
    {
        """
    data += f'"model": "image-alpha-001",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":1,
        "size":"512x512",
        "response_format":"url"
    }
    """

    resp = requests.post(QUERY_URL, headers=headers, data=data)

    if resp.status_code != 200:
        raise ValueError("Failed to generate image "+resp.text)

    response_text = json.loads(resp.text)
    return response_text['data'][0]['url']

# Set up the Streamlit app
st.set_page_config(page_title="Banana Image Generator", page_icon="🍌", layout="wide")

# Set the background color and style
page_bg_img = '''
<style>
body {
background-color: #5b5b5b;
color: white;
font-family: 'Press Start 2P', cursive;
}
.stButton button {
background-color: #ffbf00;
}
.stTextInput>div>div>input {
color: red;
font-family: 'Press Start 2P', cursive;
}
.stTextInput>div>label {
color: white;
font-family: 'Press Start 2P', cursive;
}
.stTextInput>div>div>div {
background-color: #333333;
}
.stTextArea>div>div>textarea {
color: white;
font-family: 'Press Start 2P', cursive;
}
.stTextArea>div>label {
color: white;
font-family: 'Press Start 2P', cursive;
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
    st.write("Enter a prompt and the image generator will create an image based on the prompt!")
    # Create the text input and Generate button
    prompt = st.text_input("Prompt:")
    if st.button("Generate"):
        with st.spinner("Generating image..."):
            # Generate the image
            image_url = generate_image(prompt, 'your_api_key_here')
            try:
                img = Image.open(BytesIO(requests.get(image_url).content))
                st.image(img, use_column_width=True)
            except:
                st.warning("Unable to display image.")
