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

# Query and print data from 'users' table
print("Users Table:")
# Print the column names
cur.execute("PRAGMA table_info(users)")
column_names = [row[1] for row in cur.fetchall()]
print("Column names:", column_names)
cur.execute("SELECT * FROM users")
for row in cur.fetchall():
    print(row)

print("\n")

# Query and print data from 'projects' table
print("Projects Table:")
# Print the column names
cur.execute("PRAGMA table_info(projects)")
column_names = [row[1] for row in cur.fetchall()]
print("Column names:", column_names)
cur.execute("SELECT * FROM projects")
for row in cur.fetchall():
    print(row)

print("\n")

# Query and print data from 'tasks' table
print("Task Table:")
# Print the column names
cur.execute("PRAGMA table_info(tasks)")
column_names = [row[1] for row in cur.fetchall()]
print("Column names:", column_names)
cur.execute("SELECT * FROM tasks")
for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
