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

def verify_user(user):
    """
    This function will take in a String that is a User
    Should Return true if the user exists and false if it doesnt
    """

def create_user(user):
    """
    This function will take in a String that is a User
    Should Return false if the user exists and true if it doesnt
    """

def add_skill(user, skills):
    """
    This function should add a skill or multiple to the user specified
    return true on success and false on failed
    """

def find_tasks(user):
    """
    Uses the users name to find the tasks this person can work on based on their skills
    returns all tasks(This can be done either with an id or other method)
    """

def assign_task(user, task):
    """
    Adds this to the tasks this user has assigned to them
    return true on success and false on failed
    """

def create_proj(project):
    """
    adds a empty project to the project table
    return true on success and false on failed
    """

def add_task(project, task, skill):
    """
    This will add a task to a project and link the skill that is required
    return true on success and false on failed
    """

def complete_task(project, task):
    """
    This will move a task from todo to done
    return true on success and false on failed
    """