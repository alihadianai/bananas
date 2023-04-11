import streamlit as st
import pandas as pd

# Set up user authentication
users = {'user1': 'password1', 'user2': 'password2'}
def authenticate(username, password):
    if username in users and password == users[username]:
        return True
    return False

# Define the pages of the app
def main():
    page = st.sidebar.selectbox('Select a page', ['Home', 'Tasks', 'Projects'])
    
    if page == 'Home':
        st.title('Welcome to the project management app!')
        if st.button('Log in'):
            username = st.text_input('Username')
            password = st.text_input('Password', type='password')
            if authenticate(username, password):
                st.success('Logged in as {}'.format(username))
                st.stop()
            else:
                st.error('Incorrect username or password')
    
    elif page == 'Tasks':
        st.title('Task management')
        task_name = st.text_input('Task name')
        task_description = st.text_area('Task description')
        task_due_date = st.date_input('Due date')
        if st.button('Add task'):
            tasks_df = pd.DataFrame({'Task name': [task_name],
                                     'Task description': [task_description],
                                     'Due date': [task_due_date]})
            st.write('Task added:')
            st.write(tasks_df)
    
    elif page == 'Projects':
        st.title('Project tracking')
        project_name = st.text_input('Project name')
        project_description = st.text_area('Project description')
        project_status = st.selectbox('Status', ['Not started', 'In progress', 'Completed'])
        if st.button('Create project'):
            projects_df = pd.DataFrame({'Project name': [project_name],
                                        'Project description': [project_description],
                                        'Status': [project_status]})
            st.write('Project created:')
            st.write(projects_df)

if __name__ == '__main__':
    main()
