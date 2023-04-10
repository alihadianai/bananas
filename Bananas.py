import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Set up the Streamlit app
st.set_page_config(page_title="Banana Dot Art Generator", page_icon="🍌", layout="wide")

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

# Define the function to generate the dot art image
def generate_dot_art(prompt):
    # Define the size of the image
    size = (400, 400)

    # Create a new image with a white background
    img = Image.new("RGB", size, "white")

    # Get a drawing context for the image
    draw = ImageDraw.Draw(img)

    # Define the font and font size for the dots
    font = ImageFont.truetype("arial.ttf", 10)

    # Loop through each character in the prompt
    for i, c in enumerate(prompt):
        # Get the x and y coordinates for the dot based on the index of the character
        x = (i % 20) * 20 + 10
        y = (i // 20) * 20 + 10

        # Draw a dot on the image using the character as the color
        draw.rectangle([x, y, x+10, y+10], fill=c)

    return img

# Set up the navigation bar
navigation = st.sidebar.radio("Navigation", ["Dot Art Generator", "Information", "Code Resources", "About Us"])

# Create the dot art generator page
if navigation == "Dot Art Generator":
    st.title("Banana Dot Art Generator")
    st.write("Enter a prompt and the dot art generator will create an image based on the prompt!")
    # Create the text input and Generate button
    prompt = st.text_input("Prompt:")
    if st.button("Generate"):
        with st.spinner("Generating image..."):
            # Generate the dot art image
            img = generate_dot_art(prompt)
            st.image(img, use_column_width=True)
