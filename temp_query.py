developer_skills = [
    "Python",
    "JavaScript",
    "Java",
    "C++",
    "C#",
    "HTML",
    "CSS",
    "SQL",
    "Ruby",
    "PHP",
    "Swift",
    "Kotlin",
    "TypeScript",
    "Go",
    "Rust",
    "Scala",
    "Perl",
    "R",
    "Shell Scripting",
    "Node.js",
    "React",
    "Angular",
    "Vue.js",
    "Django",
    "Flask",
    "Spring Boot",
    "Ruby on Rails",
    "Laravel",
    "ASP.NET",
    "GraphQL",
    "RESTful API Development",
    "WebSockets",
    "WebAssembly",
    "Bootstrap",
    "Tailwind CSS",
    "Sass/SCSS",
    "Docker",
    "Kubernetes",
    "AWS",
    "Azure",
    "Google Cloud Platform",
    "Serverless Architecture",
    "Firebase",
    "MongoDB",
    "PostgreSQL",
    "MySQL",
    "SQLite",
    "Redis",
    "Elasticsearch",
    "Git",
    "GitHub",
    "GitLab",
    "Bitbucket",
    "CI/CD",
    "Jenkins",
    "Travis CI",
    "Agile Development",
    "Scrum",
    "Kanban",
    "Test-Driven Development (TDD)",
    "Behavior-Driven Development (BDD)",
    "Unit Testing",
    "Integration Testing",
    "End-to-End Testing",
    "Jest",
    "Mocha",
    "Chai",
    "Selenium",
    "Cypress",
    "Performance Optimization",
    "Web Accessibility (WCAG)",
    "SEO Best Practices",
    "Responsive Web Design",
    "Mobile App Development",
    "Progressive Web Apps (PWA)",
    "WebVR/WebXR",
    "Three.js",
    "D3.js",
    "Game Development",
    "Unreal Engine",
    "Unity",
    "CryEngine",
    "Machine Learning",
    "TensorFlow",
    "PyTorch",
    "Natural Language Processing (NLP)",
    "Computer Vision",
    "Blockchain",
    "Ethereum",
    "Smart Contracts",
    "Solidity",
    "Raspberry Pi",
    "Arduino",
    "IoT Development",
    "Embedded Systems Programming",
    "Cybersecurity",
    "Penetration Testing",
    "Data Analysis",
    "Big Data",
    "Hadoop",
    "Spark",
    "Data Visualization",
    "VR/AR Development"
]

def project_info():
    """
    TEMP FUNCTION REAL will be in query.py
    The data that is returned is 
    project_info:
    [0] : Project description
    [1] : Incompleted Tasks
    [2] : Completed Tasks
    [3] : Contributors
    [4] : Age in days
    """
    project_info = [
         "This project delves deeply into the nuances of project management and exploration. Designed to not just manage tasks and milestones, it also acts as a comprehensive database visualizer. Users can effortlessly browse through various projects, understanding their core objectives and current statuses. This platform encourages collaboration and knowledge-sharing, serving as a beacon for those searching for projects where their skills and expertise can make a tangible difference. We believe that collective wisdom can push the boundaries of what's possible. Hence, we warmly invite individuals from all backgrounds and expertise levels to contribute. By collaborating, we can drive innovation, ensure the completion of projects, and bring about transformative change.",
         "5", "2", "3", "5"
    ]
    return project_info

def project_tasks(project):
    """
    TEMP FUNCTION REAL will be in query.py
    This will return the task ids that are apart of the project
    """
    task_ids = [5,4,3,2,1]
    return task_ids

def task_info(id):
    """
    TEMP FUNCTION REAL will be in query.py
    This gives task info based on the id
    """
    task_data = {
    1: [
        "Define Project Scope and Objectives",
        "Clearly outline the scope and objectives of the 'Project Manager' project. This includes identifying key features, target audience, and desired outcomes.",
        "Project management, Requirements gathering, Communication",
        "September 5th, 2023",
        "Emily J."
    ],
    2: [
        "Develop User Interface Mockups",
        "Create detailed mockups for the project's user interface. These mockups should reflect the database visualizer's layout and user interaction flow.",
        "UI/UX design, Wireframing, Creativity",
        "September 8th, 2023",
        "Alex C."
    ],
    3: [
        "Implement Backend Database Integration",
        "Integrate the backend database system into the project. Ensure smooth data retrieval and manipulation, considering scalability and security.",
        "Database management, Backend development, API integration",
        "September 12th, 2023",
        "Michael R."
    ],
    4: [
        "Implement User Authentication",
        "Develop a secure user authentication system for the project, allowing contributors to log in, manage their profiles, and access relevant project information.",
        "Security, Authentication protocols, Backend development",
        "September 10th, 2023",
        "Sarah P."
    ],
    5: [
        "Test and Bug Fixing",
        "Conduct thorough testing of the project, identifying and addressing any bugs, glitches, or inconsistencies. Ensure a smooth user experience before the official launch.",
        "Quality assurance, Troubleshooting, Attention to detail",
        "September 14th, 2023",
        "David W."
    ]
    }
    return task_data[id] 

def get_projects(user = None):
    if user != None: return ["Project Manager"]
    return ["Project Manager", "PETra", "Another Project", "Profitable Idea!", "Anything TBH"]

def get_all_skills():
    return developer_skills

def verify_user(user, password= None):
    if password != None:
        if user == 'admin' and password == 'password':
            return "admin"
        else:
            return False
    else:
        return user == "admin"

def create_user(user, password, skills = []):
    print(user)
    print(password)
    print(skills)
    return True

def add_skill(var):
    if isinstance(var, list):
        for i in var:
            add_skill(i)
    elif isinstance(var, str):
        print("Skill added: "+var)
