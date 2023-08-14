"""
This is a file to load the database with User data for testing of the Project
"""

import sqlite3

conn = sqlite3.connect("project.db")
cur = conn.cursor()

# # Create Table USERS
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY,
#     user TEXT,
#     skill TEXT
#     )
#     ''')
#
# # Create Table PROJECTS
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS projects (
#         id INTEGER PRIMARY KEY,
#         project TEXT,
#         task TEXT
#     )
# ''')
#
#
# # Adding data into users table
# users_data = [
#     ('Michael', 'Developer'),
#     ('Tod', 'Data Analyst'),
#     ('Maria', 'Data Engineer'),
#     ('Tristan', 'Software Engineer'),
#     ('Ana', 'Web Developer')
# ]
#
# # Adding data into projects table
# projects_data = [
#     ('Game-Predator', 'Graphics'),
#     ('Data Science', 'Machine Learning'),
#     ('Data Base Management', 'RDBM'),
#     ('Analytics-Finance', 'Scraping and Cleaning'),
#     ('Mobile App', 'testing')
# ]
#
# cur.executemany("INSERT INTO users (user, skill) VALUES (?, ?)", users_data)
#
# cur.executemany("INSERT INTO projects (project, task) VALUES (?, ?)", projects_data)
#
# print("Users and Project Table has been created.")

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


conn.commit()
conn.close()
