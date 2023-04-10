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
            # Define the banana text art dataset
banana_text_art = [
    """
         _____
     .-'`     `'-.
    /  _      _   \\
   /   /      \   \\
  |   /        \   |
  |  |          |  |
  |  |          |  |
  |  |          |  |
   \  \        /  /
    \   `.__.'   /
     `-._____.-'`,
""",
    """
    ,-.      _,---._ __  / \
   /  )    ,'       `./ /   \
  (  (   ,\"`--.      / /     \\
   \  `-'      `,_  / /       \\
    `._           ` \"\\        :
       `\".          `.\\       |
        /      \"--._   \\       |
       /             `  \\      :
      /`._            |  |      \
     /               ||   \      \
    /                ||    \      \
  ,'                 ''     .     \
(_,-..__..._         .-\"`-._ `\"-._/ 
           `\"\"---~~`        `~~\"\"` 
""",
    """
   /\_/\
  ( o o )
 ( =^= ) 
  (\"_\"_) 
""",
    """
  .-^-.
 /_/_\_\
' ' | ` `
    J
   / \
  /   \
""",
]

# Define the function to generate the banana text art
def generate_banana_text_art():
    return random.choice(banana_text_art)
            try:
                img = Image.open(BytesIO(response.content))
                st.image(img, use_column_width=True)
            except:
                st.warning("Unable to display image.")

# Create the information page
elif navigation == "Information":
    st.title("Banana Information")
    st.write("Bananas are a great source of potassium and other nutrients.")

# Create the code resources page
elif navigation == "Code Resources":
    st.title("Banana Code Resources")
    st.write("Here are some helpful resources for coding with bananas.")

# Create the about us page
else:
    st.title("About Us")
    st.write("We are a team of banana enthusiasts who love creating images with bananas.")
