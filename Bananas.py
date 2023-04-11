import streamlit as st
import psycopg2

# Connect to the database
conn = psycopg2.connect(database="your_database_name", user="your_username", password="your_password", host="your_host", port="your_port")

# Create a cursor
cur = conn.cursor()

# Create the sign-up page
def signup():
    st.title("Sign Up")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        # Check if the username already exists
        cur.execute("SELECT * FROM Users WHERE Username = %s", (username,))
        result = cur.fetchone()
        if result:
            st.error("Username already exists")
        else:
            # Insert the new user into the database
            cur.execute("INSERT INTO Users (Username, Email, Password) VALUES (%s, %s, %s)", (username, email, password))
            conn.commit()
            st.success("You have successfully signed up")

# Create the login page
def login():
    st.title("Log In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        # Check if the username and password are correct
        cur.execute("SELECT * FROM Users WHERE Username = %s AND Password = %s", (username, password))
        result = cur.fetchone()
        if result:
            st.success("You have successfully logged in")
        else:
            st.error("Invalid username or password")

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
