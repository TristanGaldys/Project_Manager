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

def project_info(project):
    """
    This functionw takes in a project_id and returns data in the following format

    param: project: This is the Primary Key of the project in the database
    type: int

    return: project_info: format below
    project_info:
    [0] : Project description
    [1] : Incompleted Tasks
    [2] : Completed Tasks
    [3] : Contributors
    [4] : Age in days
    type: list
    """
    project_info = [""]
    return project_info

def project_tasks(project, skill= None):
    """
    This function give the task id with the associated project
    In the future would be nice if it could only give tasks with the required skill that is entered

    param: project: This is the Primary Key of the project in the database
    type: int

    param: skill: This is the skill that is checked for if it is not None
    type: String

    return: task_ids: This is a list of task ids [1,2,3,4]
    type: list
    """
    task_ids = []
    return task_ids

def task_info(task):
    """
    This function takes in the task id and will return a list of task data

    param: task: This is the primary key of the task
    type: int

    return: task_data: This is a  list that is in the given format
    task_data:
    [0] : Task
    [1] : Task Description
    [2] : Required Skills
    [3] : Deadline
    [4] : Assigned User (In String form)
    type: list
    """
    task_data = [""]
    return task_data

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
