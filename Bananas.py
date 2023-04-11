# Create the home page
def home():
    st.title("Home")

    # Create a new project
    if st.button("Create Project"):
        name = st.text_input("Project Name")
        description = st.text_input("Project Description")
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        cur.execute("INSERT INTO Projects (Name, Description, Start_Date, End_Date) VALUES (%s, %s, %s, %s)", (name, description, start_date, end_date))
        conn.commit()
        st.success("Project created successfully")

    # List all projects
    cur.execute("SELECT * FROM Projects")
    projects = cur.fetchall()
    for project in projects:
        st.write(project)

# Create the app
def app():
    st.set_page_config(page_title="Project Management App", page_icon=":clipboard:")
    st
