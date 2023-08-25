"""
This will be the file that all database information will be pulled from

These function below are a few of the required functions for this application to work
"""
import sqlite3

conn = sqlite3.connect('project.db')
cur = conn.cursor()


def verify_user(name, password=None):
    """
    This function will take in a String that is a User
    Should Return true if the user exists and false if it doesn't
    """
    cur.execute("SELECT EXISTS(SELECT 1 FROM users WHERE name = ?)", (name,))
    result = cur.fetchone()[0]
    return result == 1

user_to_verify = input("Please enter your name: ")
input_password = None
user_exists = verify_user(user_to_verify)
verify_user(user_to_verify, input_password)
def create_user(name, user_password=None, skills=None):
    """
    This function will take in a String that is a User
    Should Return false if the user exists and true if it doesn't
    """
    if skills is None:
        skills = []
    if verify_user(name):
        return False
    cur.execute("INSERT INTO users (name, password, skills) VALUES (?, ?, ?)", (name, user_password, ', '.join(skills)))
    conn.commit()
    return True
new_user_name = user_to_verify
new_user_password = input("Enter the user's password: ")
#new_user_skills_str = []
#new_user_skills = new_user_skills_str.split(",")
success = create_user(new_user_name, new_user_password)
if success:
    print(f"User '{new_user_name}' created successfully.")
else:
    print(f"Failed to create user '{new_user_name}'.")

def get_available_projects():
    """
    Get a list of available projects from the projects table.
    Returns a list of project names.
    """
    try:
        cur.execute("SELECT project FROM projects")
        projects = cur.fetchall()
        return projects
    except sqlite3.Error:
        return []

available_projects = get_available_projects()
print("Available Projects:")
for project in available_projects:
    print(project[0])
project_choice = input("Do you want to continue with old project or start a new one? (old/new): ")
if project_choice.lower() == "old":
    # if old and there are no projects add question one more time
    proj_list = get_available_projects()
    unique_project_names = list(set(project[0] for project in proj_list))
    if unique_project_names:
        print("Available projects:")
        for index, project_name in enumerate(unique_project_names, start=1):
            print(f"{index}. {project_name}")
        selected_project_index = input("Select a project by its index number: ")
        try:
            selected_project_index = int(selected_project_index) - 1
            if 0 <= selected_project_index < len(unique_project_names):
                selected_project_name = unique_project_names[selected_project_index]
                print(f"You selected project: {selected_project_name}")
            else:
                print("Invalid project index. Continuing with no project.")
                selected_project_name = None
        except ValueError:
            print("Invalid input. Continuing with no project.")
            selected_project_name = None
    else:
        print("No projects available to continue with.")
        selected_project_name = None
else:
    pass

def create_proj(user, project):
    """
    adds an empty project to the project table
    return true on success and false on failed
    """
    try:
        cur.execute("INSERT INTO projects (owner, project) VALUES (?, ?)", (user, project,))
        conn.commit()
        cur.execute("UPDATE projects SET project_id = ? WHERE owner = ?", (project, user))
        conn.commit()
        return True
    except sqlite3.Error as e:
        conn.rollback()
        return False

new_project_name = []
user_name = user_to_verify
#project_choice = input("Do you want to continue with old project or start a new one? (old/new): ")
if project_choice.lower() == "new":
    new_project_name = input("Enter the name of the new project: ")
    if create_proj(user_name, new_project_name):
        print(f"Project '{new_project_name}' created successfully.")
    else:
        print(f"Failed to create project '{new_project_name}'.")
else:
    pass

def add_skill(user, skill):
    """
    This function should add a skill or multiple to the user specified
    return true on success and false on failed
    """
    if not verify_user(user):
        return False
    if isinstance(skill, list):
        try:
            skills_str = ', '.join(skill)
            cur.execute("UPDATE users SET skills =? WHERE name=?", (skills_str, user))
            conn.commit()
            return True
        except sqlite3.Error as e:
            conn.rollback()
            print(f"Error adding skills for user '{user}': {e}")
            return False
    else:
        print("invalid input: 'skill' parameter should be a list")
        return False

developer_skills = [
        "Python", "JavaScript", "Java", "C++", "C#", "HTML", "CSS", "SQL", "Ruby", "PHP", "Swift", "Kotlin",
        "TypeScript",
        "Go", "Rust", "Scala", "Perl", "R", "Shell Scripting", "Node.js", "React", "Angular", "Vue.js", "Django",
        "Flask", "Spring Boot", "Ruby on Rails", "Laravel", "ASP.NET", "GraphQL", "RESTful API Development",
        "WebSockets",
        "WebAssembly", "Bootstrap", "Tailwind CSS", "Sass/SCSS", "Docker", "Kubernetes", "AWS", "Azure",
        "Google Cloud Platform",
        "Serverless Architecture", "Firebase", "MongoDB", "PostgresSQL", "MySQL", "SQLite", "Redis", "Elasticsearch",
        "Git", "GitHub", "GitLab", "Bitbucket", "CI/CD", "Jenkins", "Travis CI", "Agile Development", "Scrum",
        "Kanban", "Test-Driven Development (TDD)", "Behavior-Driven Development (BDD)", "Unit Testing",
        "Integration Testing",
        "End-to-End Testing", "Jest", "Mocha", "Chai", "Selenium", "Cypress", "Performance Optimization",
        "Web Accessibility (WCAG)",
        "SEO Best Practices", "Responsive Web Design", "Mobile App Development", "Progressive Web Apps (PWA)",
        "WebVR/WebXR", "Three.js", "D3.js", "Game Development", "Unreal Engine", "Unity", "CryEngine",
        "Machine Learning",
        "TensorFlow", "PyTorch", "Natural Language Processing (NLP)", "Computer Vision", "Blockchain", "Ethereum",
        "Smart Contracts", "Solidity", "Raspberry Pi", "Arduino", "IoT Development", "Embedded Systems Programming",
        "Cybersecurity", "Penetration Testing", "Data Analysis", "Big Data", "Hadoop", "Spark", "Data Visualization",
        "VR/AR Development"
    ]

selected_skills_indices = []

user_skills = developer_skills
if user_skills:
    print("Choose your skills from the list below:")
    for index, skill in enumerate(developer_skills, start=1):
        print(f"{index}. {skill}")

    selected_skills_indices = input("Enter the indices of the skills you want to add (comma-separated): ")
    selected_skills_indices = [int(index) for index in selected_skills_indices.split(",")]
    new_user_skills = [developer_skills[index - 1] for index in selected_skills_indices]
    success = add_skill(new_user_name, new_user_skills)
    if success:
        print(f"Skills added successfully for user '{new_user_name}'.")
    else:
        print(f"Failed to add skills for user '{new_user_name}'.")
else:
    print(f"No additional skills to add for user '{new_user_name}'.")

#def add_task(project_id, task, skill):
#     """
#     This will add a task to a project and link the skill that is required
#     return true on success and false on failed
#     """
#     try:
#         cur.execute("INSERT INTO tasks (project_id, task, required_skills) VALUES (?, ?, ?)", (project_id, task, skill))
#         conn.commit()
#         return True
#     except sqlite3.Error as e:
#         conn.rollback()
#         print(e)
#         return False
#
# project_id = new_project_name
# new_task_name = selected_skills_indices  # input("Enter the task name: ")
# new_skill_required = None  # input("Enter the required skill: ")
# success = add_task(project_id, new_task_name, new_skill_required)
# if success:
#     print("Task added successfully.")
# else:
#     print("Failed to add the task.")

def find_tasks(user):
    """
    Uses the users name to find the tasks this person can work on based on their skills
    returns all tasks(This can be done either with an id or other method)
    """
    try:
        cur.execute("SELECT * FROM tasks WHERE task IN (SELECT task FROM projects Where owner=?) AND"
                    " required_skills IN (SELECT skills FROM users Where name = ?)", (user, user))
        tasks = cur.fetchall()
        return tasks
    except sqlite3.Error as e:
        print(e)
        return []

tasks = find_tasks(new_user_name)
print("Tasks that", new_user_name, "can work on:")
for task in tasks:
    print("Task ID:", task[0], "Task:", task[3])

def assign_task(user, task_id):
    """
    Adds this to the tasks this user has assigned to them
    return true on success and false on failed
    """
    try:
        cur.execute("UPDATE tasks set user_id = ? WHERE id = ?", (user, task_id))
        conn.commit()
        cur.execute("UPDATE projects SET tasks = ? WHERE id = ?", (user, task_id))
        conn.commit()
        return True
    except sqlite3.Error as e:
        conn.rollback()
        print(e)
        return False

user_name = user_to_verify
task_id = 1
success = assign_task(user_name, task_id)
if success:
    print("Task assigned successfully")
else:
    print("Failed to assign the task.")


def complete_task(project_id, task_id):
    """
    This will move a task from todo to done
    return true on success and false on failed
    """
    try:
        # Retrieve the task information from the projects table
        cur.execute("SELECT tasks FROM projects WHERE project_id = ? AND id = ?", (project_id, task_id))
        task_to_complete = cur.fetchone()

        if task_to_complete:
            # Move the task to the completed_tasks column
            cur.execute("UPDATE projects SET completed_tasks = tasks, tasks = NULL WHERE project_id = ? AND id = ?",
                        (project_id, task_id))
            conn.commit()
            return True
        else:
            print("Task not found.")
            return False
    except sqlite3.Error as e:
        conn.rollback()
        print(e)
        return False

user_input_project_id = new_project_name
user_input_task_id = new_project_name  # project_id
success = complete_task(user_input_project_id, user_input_task_id)
if success:
    print("Task marked as completed.")
else:
    print("Failed to mark the task as completed.")

def project_info(project):
    """
    This function takes in a project_id and returns data in the following format

    param: project: This is the Primary Key of the project in the database
    type: int

    return: project_info: format below
    project_info:
    [0] : Project description
    [1] : Uncompleted Tasks
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

# user_to_verify = input("Please enter your name: ")
# user_exists = verify_user(user_to_verify)

# if user_exists:
#     print(f"Welcome, {user_to_verify}!")
#     projects = get_available_projects()
#     if projects:
#         print("Available projects:")
#         for index, project in enumerate(projects, start=0):
#             print(f"{index}. {project[0]}")
#     else:
#         new_user = user_to_verify
#         if create_user(new_user):
#             print(f"User '{new_user}' created successfully.")
#         else:
#             pass
#
# developer_skills = [
#             "Python", "JavaScript", "Java", "C++", "C#", "HTML", "CSS", "SQL", "Ruby", "PHP", "Swift", "Kotlin",
#             "TypeScript",
#             "Go", "Rust", "Scala", "Perl", "R", "Shell Scripting", "Node.js", "React", "Angular", "Vue.js", "Django",
#             "Flask", "Spring Boot", "Ruby on Rails", "Laravel", "ASP.NET", "GraphQL", "RESTful API Development",
#             "WebSockets",
#             "WebAssembly", "Bootstrap", "Tailwind CSS", "Sass/SCSS", "Docker", "Kubernetes", "AWS", "Azure",
#             "Google Cloud Platform",
#             "Serverless Architecture", "Firebase", "MongoDB", "PostgresSQL", "MySQL", "SQLite", "Redis", "Elasticsearch",
#             "Git", "GitHub", "GitLab", "Bitbucket", "CI/CD", "Jenkins", "Travis CI", "Agile Development", "Scrum",
#             "Kanban", "Test-Driven Development (TDD)", "Behavior-Driven Development (BDD)", "Unit Testing",
#             "Integration Testing",
#             "End-to-End Testing", "Jest", "Mocha", "Chai", "Selenium", "Cypress", "Performance Optimization",
#             "Web Accessibility (WCAG)",
#             "SEO Best Practices", "Responsive Web Design", "Mobile App Development", "Progressive Web Apps (PWA)",
#             "WebVR/WebXR", "Three.js", "D3.js", "Game Development", "Unreal Engine", "Unity", "CryEngine",
#             "Machine Learning",
#             "TensorFlow", "PyTorch", "Natural Language Processing (NLP)", "Computer Vision", "Blockchain", "Ethereum",
#             "Smart Contracts", "Solidity", "Raspberry Pi", "Arduino", "IoT Development", "Embedded Systems Programming",
#             "Cybersecurity", "Penetration Testing", "Data Analysis", "Big Data", "Hadoop", "Spark", "Data Visualization",
#             "VR/AR Development"
# ]
# if not user_exists:
#     new_user = user_to_verify
#     if create_user(new_user, password=None):
#         print(f"Welcome '{new_user}'.")
#     else:
#         print(f"New user '{new_user}' already exists.")
#
#     if add_skill(new_user, developer_skills):
#         selected_skills = []
#         print("Add all your skills from our list:")
#         for index, skill in enumerate(developer_skills, start=1):
#             print(f"{index}. {skill}")
#
#         selected_skill = None  # Initialize selected_skill outside the loop
#         while selected_skill != 'done':
#             selected_skill = input("Select a skill by its number (or 'done' to finish selecting): ")
#             if selected_skill.lower() == 'done':
#                 break
#
#             try:
#                 skill_index = int(selected_skill) - 1
#                 if 0 <= skill_index < len(developer_skills):
#                     selected_skills.append(developer_skills[skill_index])
#                     print(f"Selected skill: {developer_skills[skill_index]}")
#                 else:
#                     print("Invalid skill number. Please try again.")
#             except ValueError:
#                 print("Invalid input. Please enter a valid skill number or 'done'.")
#
#         if selected_skills:
#             if add_skill(new_user, selected_skills):
#                 pass
#             else:
#                 print(f"Failed to add skills for user '{new_user}'.")
#     else:
#         print(f"Failed to add skills for user '{new_user}'.")
#
# project_choice = input("Do you want to continue with old project or start a new one? (old/new): ")
# if project_choice.lower() == "old":
#     proj_list = get_available_projects()
#     unique_project_names = list(set(project[0] for project in proj_list))
#     if unique_project_names:
#         print("Available projects:")
#         for index, project_name in enumerate(unique_project_names, start=1):
#             print(f"{index}. {project_name}")
#         selected_project_index = input("Select a project by its index number: ")
#         try:
#             selected_project_index = int(selected_project_index) - 1
#             if 0 <= selected_project_index < len(unique_project_names):
#                 selected_project_name = unique_project_names[selected_project_index]
#                 print(f"You selected project: {selected_project_name}")
#             else:
#                 print("Invalid project index. Continuing with no project.")
#                 selected_project_name = None
#         except ValueError:
#             print("Invalid input. Continuing with no project.")
#             selected_project_name = None
#     else:
#         print("No projects available to continue with.")
#         selected_project_name = None
#
# elif project_choice.lower() == "new":
#     new_project_name = input("Enter the name of the new project: ")
#     if create_proj(user_to_verify, new_project_name):
#         print(f"Project '{new_project_name}' created successfully.")
#     else:
#         print(f"Failed to create project '{new_project_name}'.")
# else:
#     print("No projects available at the moment. You can start a new Project.")
#     create_new_project = input("Would you like to create a new project? (yes/no): ")
#     if create_new_project.lower() == "yes":
#         new_project_name = input("Enter the name of the new project: ")
#         if create_proj(user_to_verify, new_project_name):
#             print(f"Project '{new_project_name}' created successfully.")
#         else:
#             print(f"Failed to create project '{new_project_name}'.")

# find_task


