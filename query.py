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

def create_user(name,  password=None, skills=[]):
    """
    This function will take in a String that is a User
    Should Return false if the user exists and true if it doesn't
    """
    if verify_user(name):
        return False
    cur.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    return True

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


def add_skill(user, skill):
    """
    This function should add a skill or multiple to the user specified
    return true on success and false on failed
    """
    if not verify_user(user):
        return False
    developer_skills = [
        "Python", "JavaScript", "Java", "C++", "C#", "HTML", "CSS", "SQL", "Ruby", "PHP", "Swift", "Kotlin",
        "TypeScript",
        "Go", "Rust", "Scala", "Perl", "R", "Shell Scripting", "Node.js", "React", "Angular", "Vue.js", "Django",
        "Flask", "Spring Boot", "Ruby on Rails", "Laravel", "ASP.NET", "GraphQL", "RESTful API Development",
        "WebSockets",
        "WebAssembly", "Bootstrap", "Tailwind CSS", "Sass/SCSS", "Docker", "Kubernetes", "AWS", "Azure",
        "Google Cloud Platform",
        "Serverless Architecture", "Firebase", "MongoDB", "PostgreSQL", "MySQL", "SQLite", "Redis", "Elasticsearch",
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
    if isinstance(developer_skills, list):

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
def create_proj(user, project):
    """
    adds a empty project to the project table
    return true on success and false on failed
    """
    try:
        cur.execute("INSERT INTO projects (owner, project) VALUES (?, ?)", (user, project,))
        conn.commit()
        # cur.execute("INSERT INTO projects SET project = ? WHERE owner = ?", (project, user))
        # conn.commit()
        return True
    except sqlite3.Error as e:
        conn.rollback()
        return False
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

user_to_verify = input("Please enter your name: ")
user_exists = verify_user(user_to_verify)

if user_exists:
    print(f"Welcome, {user_to_verify}!")
    projects = get_available_projects()
    if projects:
        print("Available projects:")
        for index, project in enumerate(projects, start=0):
            print(f"{index}. {project[0]}")
    else:
        new_user = user_to_verify
        if create_user(new_user):
            print(f"User '{new_user}' created successfully.")
        else:
            pass

developer_skills = [
            "Python", "JavaScript", "Java", "C++", "C#", "HTML", "CSS", "SQL", "Ruby", "PHP", "Swift", "Kotlin",
            "TypeScript",
            "Go", "Rust", "Scala", "Perl", "R", "Shell Scripting", "Node.js", "React", "Angular", "Vue.js", "Django",
            "Flask", "Spring Boot", "Ruby on Rails", "Laravel", "ASP.NET", "GraphQL", "RESTful API Development",
            "WebSockets",
            "WebAssembly", "Bootstrap", "Tailwind CSS", "Sass/SCSS", "Docker", "Kubernetes", "AWS", "Azure",
            "Google Cloud Platform",
            "Serverless Architecture", "Firebase", "MongoDB", "PostgreSQL", "MySQL", "SQLite", "Redis", "Elasticsearch",
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
if not user_exists:
    new_user = user_to_verify
    if create_user(new_user, password=None):
        print(f"Welcome '{new_user}'.")
    else:
        print(f"New user '{new_user}' already exists.")

    if add_skill(new_user, developer_skills):
        selected_skills = []
        print("Add all your skills from our list:")
        for index, skill in enumerate(developer_skills, start=1):
            print(f"{index}. {skill}")

        selected_skill = None  # Initialize selected_skill outside the loop
        while selected_skill != 'done':
            selected_skill = input("Select a skill by its number (or 'done' to finish selecting): ")
            if selected_skill.lower() == 'done':
                break

            try:
                skill_index = int(selected_skill) - 1
                if 0 <= skill_index < len(developer_skills):
                    selected_skills.append(developer_skills[skill_index])
                    print(f"Selected skill: {developer_skills[skill_index]}")
                else:
                    print("Invalid skill number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid skill number or 'done'.")

        if selected_skills:
            if add_skill(new_user, selected_skills):
                pass
            else:
                print(f"Failed to add skills for user '{new_user}'.")
    else:
        print(f"Failed to add skills for user '{new_user}'.")

project_choice = input("Do you want to continue with old project or start a new one? (old/new): ")
if project_choice.lower() == "old":
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

elif project_choice.lower() == "new":
    new_project_name = input("Enter the name of the new project: ")
    if create_proj(user_to_verify, new_project_name):
        print(f"Project '{new_project_name}' created successfully.")
    else:
        print(f"Failed to create project '{new_project_name}'.")
else:
    print("No projects available at the moment. You can start a new Project.")
    create_new_project = input("Would you like to create a new project? (yes/no): ")
    if create_new_project.lower() == "yes":
        new_project_name = input("Enter the name of the new project: ")
        if create_proj(user_to_verify, new_project_name):
            print(f"Project '{new_project_name}' created successfully.")
        else:
            print(f"Failed to create project '{new_project_name}'.")

# developer_skills = [
#             "Python", "JavaScript", "Java", "C++", "C#", "HTML", "CSS", "SQL", "Ruby", "PHP", "Swift", "Kotlin",
#             "TypeScript",
#             "Go", "Rust", "Scala", "Perl", "R", "Shell Scripting", "Node.js", "React", "Angular", "Vue.js", "Django",
#             "Flask", "Spring Boot", "Ruby on Rails", "Laravel", "ASP.NET", "GraphQL", "RESTful API Development",
#             "WebSockets",
#             "WebAssembly", "Bootstrap", "Tailwind CSS", "Sass/SCSS", "Docker", "Kubernetes", "AWS", "Azure",
#             "Google Cloud Platform",
#             "Serverless Architecture", "Firebase", "MongoDB", "PostgreSQL", "MySQL", "SQLite", "Redis", "Elasticsearch",
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



