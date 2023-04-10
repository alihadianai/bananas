import streamlit as st
import random

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

# Set up the Streamlit app
st.set_page_config(page_title="Banana Text Art Generator", page_icon="🍌", layout="wide")

# Set the background color and style
page_bg_img = '''
<style>
body {
background-color: #151515;
color: white;
}
.stButton button {
background-color: #ffbf00;
}
.stTextInput>div>div>input {
color: red;
}
.stTextInput>div>label {
color: white;
}
.stTextInput>div>div>div {
background-color: #333333;
}
.stTextArea>div>div>textarea {
color: white;
}
.stTextArea>div>label {
color: white;
}
.stTextArea>div>div>div {
background-color: #333333;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Set up the navigation bar
navigation = st.sidebar.radio("Navigation", ["Generate Banana Text Art", "About Us"])

# Create the generate banana text art page
if navigation == "Generate Banana Text Art":
    st.title("Banana Text Art Generator")
    st.write("Click the button below to generate a random banana text art!")
    if st.button("Generate"):
        banana_text_art = generate_banana_text_art()
        st.code(banana_text_art)

# Create the about us page
else:
    st.title("About Us")
    st.write("We are a team of banana enthusiasts who love creating text art!")
