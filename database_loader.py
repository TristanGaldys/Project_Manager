"""
This is a file to load the database with User data for testing of the Project
"""

import sqlite3

conn = sqlite3.connect("project.db")
cur = conn.cursor()

# Create Table USERS
cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    password TEXT,
    skills TEXT
    )
    ''')
# Create Table PROJECTS
cur.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner INTEGER,
        project TEXT,
        project_id INTEGER,
        tasks TEXT,
        start_date TEXT,
        description TEXT,
        completed_tasks INTEGER,
        uncompleted_tasks INTEGER
    )
''')
# Create Table TASKS
cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        user_id TEXT,
        project_id TEXT,
        task INTEGER,
        description TEXT,
        deadline INTEGER,
        required_skills,
        FOREIGN KEY (task) references projects (projects_id)        
    )
''')

# Adding data into users table
users_data =[]

# Adding data into projects table
projects_data = []

# Adding data into tasks table
tasks_data = [
    # ('user_id', 'project_id', 'task', 'description', 'deadline', 'required skills'),
    ('1', '', '', '', None, ''),
    ('2', '', '', '', None, ''),
    ('3', '', '', '', None, ''),
    ('4', '', '', '', None, ''),
    ('5', '', '', '', None, ''),
    ('6', '', '', '', None, ''),
    ('7', '', '', '', None, ''),
    ('8', '', '', '', None, ''),
    ('9', '', '', '', None, ''),
    ('10', '', '', '', None, ''),
    ('11', '', '', '', None, ''),
    ('12', '', '', '', None, ''),
    ('13', '', '', '', None, ''),
    ('14', '', '', '', None, ''),
    ('15', '', '', '', None, ''),
    ('16', '', '', '', None, ''),
    ('17', '', '', '', None, ''),
    ('18', '', '', '', None, ''),
]


cur.executemany("INSERT INTO users (name, skills) VALUES (?, ?)", users_data)

cur.executemany("INSERT INTO projects (owner, project, project_id, tasks, start_date, description, completed_tasks, uncompleted_tasks) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", projects_data)

#cur.executemany("INSERT INTO tasks (user_id, project_id, task, description, deadline, required_skills) VALUES ( ?, ?, ?, ?, ?, ?)", tasks_data)

print("Users, Project and Tasks Table has been created.")

# CHECK
# Query and print data from 'users' table
print("Users Table:")
cur.execute("SELECT * FROM users")
for row in cur.fetchall():
    print(row)

print("\n")

# Query and print data from 'projects' table
print("Projects Table:")
cur.execute("SELECT * FROM projects")
for row in cur.fetchall():
    print(row)

print("\n")
#
# # Query and print data from 'tasks' table
# print("Task Table:")
# cur.execute("SELECT * FROM tasks")
# for row in cur.fetchall():
#     print(row)

cur.execute("SELECT project from projects")
for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
