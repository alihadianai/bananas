import streamlit as st
import pandas as pd

class ProjectManagementApp:
    def __init__(self):
        self.pages = {
            'Home': self.render_home_page,
            'Tasks': self.render_tasks_page,
            'Projects': self.render_projects_page,
        }
        self.current_user = None
        self.tasks_df = pd.DataFrame(columns=['Task name', 'Task description', 'Due date'])
        self.projects_df = pd.DataFrame(columns=['Project name', 'Project description', 'Status'])
        
    def authenticate(self, username, password):
        # Replace with database or file system lookup for user credentials
        users = {'user1': 'password1', 'user2': 'password2'}
        if username in users and password == users[username]:
            self.current_user = username
            return True
        return False
    
    def require_login(self):
        if self.current_user is None:
            st.error('Please log in to access this page')
            st.stop()
    
    def render_home_page(self):
        st.title('Welcome to the home page, {}'.format(self.current_user))
        st.write('This is the home page of the project management app')
        
    def render_tasks_page(self):
        self.require_login()
        st.title('Task management')
        task_name = st.text_input('Task name')
        task_description = st.text_area('Task description')
        task_due_date = st.date_input('Due date')
        if st.button('Add task'):
            try:
                self.tasks_df.loc[len(self.tasks_df)] = [task_name, task_description, task_due_date]
                st.write('Task added:')
                st.write(self.tasks_df)
            except:
                st.error('Error adding task')
    
    def render_projects_page(self):
        self.require_login()
        st.title('Project tracking')
        project_name = st.text_input('Project name')
        project_description = st.text_area('Project description')
        project_status = st.selectbox('Status', ['Not started', 'In progress', 'Completed'])
        if st.button('Create project'):
            try:
                self.projects_df.loc[len(self.projects_df)] = [project_name, project_description, project_status]
                st.write('Project created:')
                st.write(self.projects_df)
            except:
                st.error('Error creating project')
    
    def run(self):
        st.sidebar.title('Navigation')
        current_page_name = st.sidebar.selectbox('Select a page', list(self.pages.keys()))
        current_page = self.pages[current_page_name
    if self.current_user is None:
        self.render_login_page()

    elif self.current_page == 'Home':
        st.title('Welcome to the home page, {}'.format(self.current_user))

    elif self.current_page == 'Tasks':
        self.render_tasks_page()

    elif self.current_page == 'Projects':
        self.render_projects_page()

def render_login_page(self):
    st.title('Welcome to the project management app!')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Log in'):
        if self.authenticate(username, password):
            st.success('Logged in as {}'.format(username))
            self.current_page = self.pages['Home']
        else:
            st.error('Incorrect username or password')

def render_tasks_page(self):
    st.title('Task management')
    task_name = st.text_input('Task name')
    task_description = st.text_area('Task description')
    task_due_date = st.date_input('Due date')
    if st.button('Add task'):
        try:
            self.tasks_df.loc[len(self.tasks_df)] = [task_name, task_description, task_due_date]
            st.write('Task added:')
            st.write(self.tasks_df)
        except:
            st.error('Error adding task')

def render_projects_page(self):
    st.title('Project tracking')
    project_name = st.text_input('Project name')
    project_description = st.text_area('Project description')
    project_status = st.selectbox('Status', ['Not started', 'In progress', 'Completed'])
    if st.button('Create project'):
        try:
            self.projects_df.loc[len(self.projects_df)] = [project_name, project_description, project_status]
            st.write('Project created:')
            st.write(self.projects_df)
        except:
            st.error('Error creating project')

