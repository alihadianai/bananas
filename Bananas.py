import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Define the function to generate the response
def generate_response(prompt):
    # Insert your code here to generate the response
    # You can use any language model or API you prefer
    response = f"Your prompt: {prompt}\n\nThis is a dummy response."
    return response

# Set up the Streamlit app
st.set_page_config(page_title="Banana Chatbot", page_icon="🍌", layout="wide")

# Create the navigation bar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Chat", "Information", "Code Resources", "About Us"])

# Create the pages
if selection == "Chat":
    st.title("Banana Chatbot")
    st.write("Enter a prompt and the chatbot will respond!")
    
    # Create the text input and Generate button
    prompt = st.text_input("Prompt:")
    if st.button("Generate"):
        with st.spinner("Generating response..."):
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
            
elif selection == "Information":
    st.title("Information")
    st.write("This is the information page. Here you can find information about the chatbot.")
    st.write("Insert your text here.")
    
elif selection == "Code Resources":
    st.title("Code Resources")
    st.write("This is the code resources page. Here you can find helpful resources to create your own chatbot.")
    st.write("Insert your text here.")
    
elif selection == "About Us":
    st.title("About Us")
    st.write("This is the about us page. Here you can find information about the developers of the chatbot.")
    st.write("Insert your text here.")
