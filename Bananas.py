import pandas as pd
import numpy as np

# Expander section
with st.expander("About"):
  st.write("""Trying to add a data table, chart, sidebar button with 
          ballons, an image, text input & exploring tabs!""")

# Sidebar section
with st.sidebar:
  st.subheader('This is a Sidebar')
  st.write('Button with Balloons 🎈')
  if st.button('Click me!✨'):
    st.balloons()
  else:
    st.write(' ')

# Dataframe and Chart display section
st.subheader('Interactive Data Table')
df = pd.DataFrame(
    np.random.randn(50, 3),  # generates random numeric values!
    columns=["a", "b", "c"])
st.dataframe(df) 

st.subheader('Bar Chart 📊')
st.bar_chart(df)

# Image upload and text input section
st.subheader('An Image')
st.image('https://www.scoopbyte.com/wp-content/uploads/2019/12/tom-and-jerry.jpg')

st.subheader('Text Input')
greet = st.text_input('Write your name, please!')
st.write('👋 Hey!', greet)


# Tabs section
st.subheader('Tabs')
tab1, tab2 = st.tabs(["TAB 1", "TAB 2"])

with tab1:
  st.write('WOW!')
  st.image("https://i.gifer.com/DJR3.gif", width=400)

with tab2:
  st.write('Do you like ice cream? 🍨')
  agree = st.checkbox('Yes! I love it')
  disagree = st.checkbox("Nah! 😅")
  if agree:
    st.write('Even I love it 🤤')
  if disagree:
    st.write('You are boring 😒')
Here’s the code breakdown:

Libraries
pandas — for writing a dataframe

numpy — to generate random numbers

Containers
st.expander — to add an “About” section

st.sidebar — for passing Streamlit elements by using with notation

st.tabs — separated tabs to pass Streamlit elements by using with notation

Widgets
st.button and st.balloons — a button for throwing balloons 🎈

st.text_input — a single-line text input

st.checkbox — to select multiple options

Data Display Elements
st.dataframe — displays pandas dataframe as a data table

st.bar_chart— displays a beautiful bar chart

st.image — displays an image
