import streamlit as st
import pandas as pd

# Set up your data
team_df = pd.DataFrame({
    'Name': ['آلیس', 'باب', 'چارلی', 'دیوید'],
    'Role': ['مدیر', 'توسعه‌دهنده', 'توسعه‌دهنده', 'طراح']
})
project_df = pd.DataFrame({
    'Project Name': ['پروژه ۱', 'پروژه ۲', 'پروژه ۳'],
    'Assigned To': ['آلیس', 'باب', 'چارلی']
})

# Define your Streamlit app
st.title('ابزار مدیریت پروژه')

st.header('اعضای تیم')
st.dataframe(team_df)

st.header('پروژه‌ها')
st.dataframe(project_df)

# Add functionality for adding new team members
st.header('افزودن عضو جدید به تیم')
new_name = st.text_input('نام')
new_role = st.selectbox('نقش', ['مدیر', 'توسعه‌دهنده', 'طراح'])
if st.button('افزودن'):
    team_df = team_df.append({'Name': new_name, 'Role': new_role}, ignore_index=True)
    st.success('عضو تیم جدید اضافه شد!')
    st.dataframe(team_df)

# Add functionality for adding new projects
st.header('افزودن پروژه جدید')
new_project_name = st.text_input('نام پروژه')
new_assigned_to = st.selectbox('اختصاص داده شده به', team_df['Name'].tolist())
if st.button('افزودن'):
    project_df = project_df.append({'Project Name': new_project_name, 'Assigned To': new_assigned_to}, ignore_index=True)
    st.success('پروژه جدید اضافه شد!')
    st.dataframe(project_df)
