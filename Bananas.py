import streamlit as st
import pandas as pd

class ProjectManagementApp:
    def __init__(self):
        self.pages = {
            'Home': self.render_home_page,
            'Tasks': self.render_tasks_page,
            'Projects': self.render_projects_page,
        }
        self.current_page = 'Home'
        self.tasks_df = pd.DataFrame(columns=['Task name', 'Task description', 'Due date'])
        self.projects_df = pd.DataFrame(columns=['Project name', 'Project description', 'Status'])
        
    def render_home_page(self):
        st.title('Welcome to the home page')
        st.write('This is the home page of the project management app')
        
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
    
    def run(self):
        st.sidebar.title('Navigation')
        if self.current_page == 'Home':
            st.sidebar.selectbox('Select a page', list(self.pages.keys()), index=0)
            self.render_home_page()
        elif self.current_page == 'Tasks':
            st.sidebar.selectbox('Select a page', list(self.pages.keys()), index=1)
            self.render_tasks_page()
        elif self.current_page == 'Projects':
            st.sidebar.selectbox('Select a page', list(self.pages.keys()), index=2)
            self.render_projects_page()

if __name__ == '__main__':
    app = ProjectManagementApp()
    app.run()
