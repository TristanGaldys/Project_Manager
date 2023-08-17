"""
This will be the file that all database information will be pulled from

These function below are a few of the required functions for this application to work

These require a bit of a change of the database
New collumns in projects:
    DOB (Start date)
    description
    completed tasks (these should just hold IDs to link to task table)
    incomplete tasks (these should just hold IDs to link to task table)

New Table for tasks:
    assigned user
    description
    deadline
    required skills
"""
import sqlite3

conn = sqlite3.connect('project.db')
cursor = conn.cursor()
def verify_user(user):
    """
    This function will take in a String that is a User
    Should Return true if the user exists and false if it doesnt
    """
    cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE name = ?)", (user,))
    result = cursor.fetchone()[0]
    return result == 1

def create_user(user):
    """
    This function will take in a String that is a User
    Should Return false if the user exists and true if it doesnt
    """
    if verify_user(user):
        return False
    cursor.execute("INSERT INTO users (name) VALUES (?)", (user,))
    conn.commit()
    return True
def add_skill(user, skills):
    """
    This function should add a skill or multiple to the user specified
    return true on success and false on failed
    """
    pass
def find_tasks(user):
    """
    Uses the users name to find the tasks this person can work on based on their skills
    returns all tasks(This can be done either with an id or other method)
    """
    pass
def assign_task(user, task):
    """
    Adds this to the tasks this user has assigned to them
    return true on success and false on failed
    """
    pass
def create_proj(project):
    """
    adds a empty project to the project table
    return true on success and false on failed
    """
    pass
def add_task(project, task, skill):
    """
    This will add a task to a project and link the skill that is required
    return true on success and false on failed
    """
    pass
def complete_task(project, task):
    """
    This will move a task from todo to done
    return true on success and false on failed
    """
    pass

user_to_verify = "John Doe"
if verify_user(user_to_verify):
    print(f"User '{user_to_verify}' exists.")
else:
    print(f"User '{user_to_verify}' does not exist.")

new_user = "Jane Smith"
if create_user(new_user):
    print(f"User '{new_user}' created successfully.")
else:
    print(f"User '{new_user}' already exists.")

user = "John Doe"
skills = ["Python", "Database Management"]
if add_skill(user, skills):
    print(f"Skills added for user '{user}'.")
else:
    print(f"Failed to add skills for user '{user}'.")

# Continue calling other functions as needed
