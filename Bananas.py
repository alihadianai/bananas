import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class ProjectManagementApp:
    def __init__(self):
        self.pages = {
            'Home': self.render_home_page,
            'Tasks': self.render_tasks_page,
            'Projects': self.render_projects_page,
            'Project Progress': self.render_project_progress_page,
        }
        self.current_page = 'Home'
        self.tasks_df = pd.DataFrame(columns=['Task name', 'Task description', 'Due date'])
        self.projects_df = pd.DataFrame(columns=['Project name', 'Project description', 'Status'])
        self.project_progress_df = pd.DataFrame(columns=['Project name', 'Progress'])
        
    def render_home_page(self):
        st.title('Welcome to the project management app')
        st.write('This app allows you to manage your tasks and projects in one place.')
        
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
                
                # Add the project to the project progress dataframe
                self.project_progress_df.loc[len(self.project_progress_df)] = [project_name, 0]
                
            except:
                st.error('Error creating project')
    
    def render_project_progress_page(self):
        st.title('Project Progress')
        if len(self.project_progress_df) > 0:
            project_name = st.selectbox('Select a project', self.project_progress_df['Project name'])
            progress = st.slider('Progress', 0, 100)
            if st.button('Update progress'):
                self.project_progress_df.loc[self.project_progress_df['Project name'] == project_name, 'Progress'] = progress
                st.write('Progress updated:')
                st.write(self.project_progress_df)
        else:
            st.write('No projects to display progress for.')
            
        # Plot the progress of each project
        if not self.project_progress_df.empty:
            plt.figure(figsize=(10,6))
            for project_name in self.project_progress_df['Project name']:
                project_progress = self.project_progress_df[self.project_progress_df['Project name'] == project_name]['Progress']
                plt.plot(project_progress, label=project_name)
            plt.title('Project Progress')
            plt.xlabel('Time')
            plt.ylabel('Progress (%)')
            plt.legend()
            st.pyplot()
    
    def run(self):
        st.sidebar.title('Navigation')
        if self.current_page == 'Home':
            page_selection = st.sidebar.selectbox('Select a page', list(self.pages.keys()), index=0)
            if page_selection != self.current_page:
                self.current_page = page_selection
        elif self.current_page == 'Tasks':
            page_selection = st.sidebar.selectbox('Select a page', list(self.pages.keys()), index=1)
            if page_selection != self.current_page:
            self.current_page = page_selection
            elif self.current_page == 'Projects':
            page_selection = st.sidebar.selectbox('Select a page', list(self.pages.keys()), index=2)
            if page_selection != self.current_page:
            self.current_page = page_selection
            elif self.current_page == 'Team':
            page_selection = st.sidebar.selectbox('Select a page', list(self.pages.keys()), index=3)
            if page_selection != self.current_page:
            self.current_page = page_selection
            if self.current_page == 'Projects':
            self.render_projects_page()
            self.render_project_chart()
            elif self.current_page == 'Tasks':
            self.render_tasks_page()
            elif self.current_page == 'Team':
            self.render_team_page()
            else:
            self.render_home_page()
    def render_project_chart(self):
        st.title('Project Progress Chart')
        project_status_count = self.projects_df['Status'].value_counts()
        if not project_status_count.empty:
            chart_data = pd.DataFrame({
                'Status': project_status_count.index,
                'Count': project_status_count.values
            })
            st.bar_chart(chart_data)
        else:
            st.write('No projects found')

    def render_team_page(self):
        st.title('Team Page')
        st.write('This is the team page where team members can see the progress of the projects.')
        st.write('Here, you can see the progress chart of all projects.')
        self.render_project_chart()
        if name == 'main':
app = ProjectManagementApp()
app.run()
