import streamlit as st
import pandas as pd
from datetime import datetime
from typing import List, Dict, Any

class ProjectManager:

    def __init__(self, db):
        self.db = db
        self.users = {'user1': 'password1', 'user2': 'password2'}
    
    def authenticate(self, username, password):
        if username in self.users and password == self.users[username]:
            return True
        return False
    
    def add_task(self, task_name, task_description, task_due_date):
        if not all([task_name, task_description, task_due_date]):
            st.error('Please fill in all fields.')
            return
        try:
            task_due_date = datetime.strptime(task_due_date, '%Y-%m-%d').date()
        except ValueError:
            st.error('Please enter a valid date format (YYYY-MM-DD).')
            return
        task_data = {'Task name': task_name,
                     'Task description': task_description,
                     'Due date': task_due_date}
        self.db.add_task(task_data)
        st.success('Task added.')
    
    def add_project(self, project_name, project_description, project_status):
        if not all([project_name, project_description]):
            st.error('Please fill in all fields.')
            return
        project_data = {'Project name': project_name,
                        'Project description': project_description,
                        'Status': project_status}
        self.db.add_project(project_data)
        st.success('Project added.')
    
    def view_tasks(self):
        tasks = self.db.get_tasks()
        if not tasks:
            st.warning('No tasks found.')
            return
        st.write(pd.DataFrame(tasks))
    
    def view_projects(self):
        projects = self.db.get_projects()
        if not projects:
            st.warning('No projects found.')
            return
        st.write(pd.DataFrame(projects))

class Database:

    def __init__(self):
        self.tasks = []
        self.projects = []
    
    def add_task(self, task_data: Dict[str, Any]):
        self.tasks.append(task_data)
    
    def add_project(self, project_data: Dict[str, Any]):
        self.projects.append(project_data)
    
    def get_tasks(self) -> List[Dict[str, Any]]:
        return self.tasks
    
    def get_projects(self) -> List[Dict[str, Any]]:
        return self.projects

def main():
    db = Database()
    project_manager = ProjectManager(db)
    page = st.sidebar.selectbox('Select a page', ['Home', 'Tasks', 'Projects'])
    
    if page == 'Home':
        st.title('Welcome to the project management app!')
        if st.button('Log in'):
            username = st.text_input('Username')
            password = st.text_input('Password', type='password')
            if project_manager.authenticate(username, password):
                st.success('Logged in as {}'.format(username))
                st.stop()
            else:
                st.error('Incorrect username or password')
    
    elif page == 'Tasks':
        st.title('Task management')
        task_name = st.text_input('Task name')
        task_description = st.text_area('Task description')
        task_due_date = st.date_input('Due date')
task_assigned_to = st.text_input('Assigned to')
if st.button('Add task'):
tasks_df = pd.DataFrame({'Task name': [task_name],
'Task description': [task_description],
'Due date': [task_due_date],
'Assigned to': [task_assigned_to]})
st.write('Task added:')
st.write(tasks_df)
