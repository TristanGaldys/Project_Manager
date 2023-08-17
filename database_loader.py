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
    skill TEXT
    )
    ''')
# Create Table PROJECTS
cur.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner INTEGER,
        project TEXT,
        project_id TEXT,
        tasks TEXT,
        start_date TEXT,
        description TEXT,
        completed_tasks TEXT,
        uncompleted_tasks TEXT
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
users_data = [
    ('John Brzenk', 'Data Science'),
    ('Denis Cyplenkov', 'Data Analysis'),
    ('Dave Chaffee', 'Data Analysis'),
    ('Georgi Tsvetkov', 'Data Analysis'),
    ('Levan Saginashvili', 'Back end software development'),
    ('Artyom Morozov', 'Front end software development'),
    ('David Dadikyan', 'Database'),
    ('Ermes Gasparini', 'Database'),
    ('Vitaly Laletin', 'Data Science'),
    ('Jerry Cadorette', 'Data Science'),
    ('Tobias Sporrong', 'Data Science'),
    ('Devon Larratt', 'Data Science'),
    ('Dmitry Silaev', 'Software Engineering'),
    ('Evgeny Prudnik', 'Database'),
    ('Eglė Vaitkutė', 'Database'),
    ('Gabriela Vasconcelos', 'Data Analysis'),
    ('Sarah Bäckman', 'Software Engineering'),
    ('Barbora Bajciova', 'Database')
]

# Adding data into projects table
projects_data = [
    # ('id', 'owner', 'project', 'project_id', 'tasks', 'start date', 'description', 'completed tasks', 'uncompleted tasks')
    ('1', 'Regression', '', 'Data Collection and Preparation', '09-00-2023', "Gather the necessary datasets, ensuring they're relevant and high-quality", '', ''),
    ('3', 'Classification', '', 'Model Deployment and Testing', '09-00-2023', 'Deploy the trained model to a production environment or create a prediction pipeline', '', ''),
    ('6', 'Clustering', '', 'Problem Definition ', '09-00-2023', "Define the problem you're trying to solve with regression", '', ''),
    ('8', 'Sentiment Analysis', '', 'Documentation and Reporting', '09-10-2023', 'Document the entire process, including data preprocessing, feature engineering, model selection, and evaluation metrics', '', ''),
    ('10', 'Recommender System', '', 'Model Evaluation', '09-12-2023', 'Evaluate models using appropriate evaluation metrics such as Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), R-squared', '', ''),
    ('2', 'NLP', 'Model Training',  '', '09-13-2023', 'Train the selected models on the training dataset', '', ''),
    ('4', 'Artificial Neural Network',  '', 'Model Selection', '09-12-2023', 'Choose appropriate regression algorithms based on the problem type (linear, polynomial, etc.) and dataset size', '', ''),
    ('9', 'Electricity Bill Management System',  '', 'Requirement Gathering and Analysis', '08-22-2023', 'Understand the requirements of the management system, including user needs and business goals', '', ''),
    ('7', 'Online Retail Application Database',  '', 'Database Design', '08-22-2023', 'Create an Entity-Relationship Diagram (ERD) to visualize the database structure', '', ''),
    ('5', 'Inventory Control Management',  '', 'Schema Creation', '08-22-2023', 'Use a Database Management System (DBMS) to define tables, fields, data types, constraints, and relationships', '', ''),
    ('20', 'Library Management System',  '', 'Data Population', '09-30-2023', 'Develop scripts or use tools to insert data into the tables', '', ''),
    ('18', 'Student Database Management',  '', 'User Interface Design', '09-30-2023', 'Create mockups or wireframes to visualize the layout and functionalities', '', ''),
    ('11', 'Payroll Management System',  '', 'Front-End Development', '09-01-2023', 'Integrate the front-end with the back-end to fetch and display data from the database', '', ''),
    ('15', 'Voice-based Transport Enquiry System',  '', 'Database Connectivity', '09-01-2023', 'Establish a connection between the back-end server and the database', '', ''),
    ('17', 'SMS-based Remote Server Monitoring System',  '', 'Authentication and Authorization', '09-01-2023', 'Implement user authentication to ensure secure access to the system', '', ''),
    ('12', 'E-Learning Platform',  '', 'System Design', '09-01-2023', 'Architect the overall system, including database structure, backend services, and user interfaces', '', ''),
    ('13', 'Advanced Employment Management System',  '', 'User Management', '09-01-2023', 'Implement user authentication and authorization mechanisms', '', ''),
    ('19', 'Image Encryption using AES',  '', 'User Management', '09-01-2023', 'Manage roles and permissions for different user types ', '', ''),
    ('14', 'Data Leak Detector',  '', 'Job Posting and Recruitment', '08-30-2023', 'Design a module for posting job vacancies', '', ''),
    ('16', 'Face Detector AI-Based Model',  '', 'Performance Management', '08-30-2023', 'Develop mechanisms for setting employee goals and KPIs', '', ''),
    ('40', 'Smart Health Prediction System',  '', 'Leave and Attendance Management', '08-30-2023', 'Design a system for employees to apply for leaves', '', ''),
    ('31', 'Weather Forecasting Application',  '', 'Payroll and Compensation', '08-30-2023', 'Design a payroll module that calculates employee salaries based on attendance and other factors', '', ''),
    ('37', 'E-Parking Challenge Generation System',  '', 'Reporting and Analytics', '08-30-2023', 'Allow custom queries and filters for generating specific reports', '', ''),
    ('21', 'Portfolio Website',  '', 'UI/UX Design', '08-30-2023', 'Design the user interface elements, including buttons, forms, navigation, etc', '', ''),
    ('23', 'To-Do App', 'Responsive Design',  '', '08-30-2023', 'Ensure the application is responsive and works well on various screen sizes (desktop, tablet, mobile)', '', ''),
    ('27', 'Virtual Keyboard',  '', 'HTML/CSS Development', '08-30-2023', 'Write clean and semantic HTML code for the structure', '', ''),
    ('33', 'Meme Generator',  '', 'Cross-Browser Compatibility', '08-27-2023', 'Test and ensure the application works correctly across different web browsers (Chrome, Firefox, Safari, Edge, etc.)', '', ''),
    ('32', 'Spotify Clone',  '', 'Performance Optimization', '08-27-2023', 'Optimize images, scripts, and styles to improve page loading times', '', ''),
    ('24', 'Chat App',  '', 'Code Review and Testing', '08-27-2023', 'Conduct code reviews to ensure code quality and consistency', '', ''),
    ('34', 'E-Commerce Website',  '', 'Deployment', '08-27-2023', 'Deploy the front-end code to a web server or a content delivery network (CDN).', '', ''),
    ('26', 'A User Authentication System. Image Source ',  '', 'Requirements Gathering and Analysis', '08-27-2023', "Understand the project's objectives and requirements", '', ''),
    ('25', 'Build a Landing Page. Image Source',  '', 'Architecture and Design', '08-27-2023', 'Design the overall system architecture', '', ''),
    ('39', 'Build Your Own Web Server',  '', 'Database Design and Development', '08-23-2023', 'Set up the database server and create tables', '', ''),
    ('38', 'Build a Finance Application',  '', 'Server-Side Development', '08-23-2023', 'Develop backend APIs for communication with the frontend.', '', ''),
    ('28', 'Create a Text Analyzer',  '', 'API Development', '08-23-2023', 'Design RESTful or GraphQL APIs for communication with clients', '', ''),
    ('35', 'Build a To-Do App',  '', 'Middleware and Services', '08-23-2023', 'Integrate with third-party services like payment gateways or APIs', '', ''),
    ('36', 'Build a CLI App',  '', 'Security', '08-23-2023', 'Implement encryption for data at rest and in transit', '', ''),
    ('22', 'Web Scraping Internet Movie',  '', 'Defining the Problem and Objectives', '08-23-2023', 'Clearly define the goals and objectives of the data analysis project', '', ''),
    ('26', 'Exploratory Data Analysis, Global suicide rates',  '', 'Data Collection and Acquisition', '08-22-2023', 'Identify the data sources that are relevant to your analysis', '', ''),
    ('29', 'Exploratory Data Analysis, World Happiness Report',  '', 'Data Cleaning and Preprocessing', '08-22-2023', 'Handle missing data by imputing or removing it', '', ''),
    ('30', 'Data visualization, Healthy food and sport',  '', 'Exploratory Data Analysis (EDA):', '08-22-2023', 'Perform data visualization to understand the distribution of variables', '', ''),
    ('44', 'Data visualization, Covid-19',  '', 'Feature Engineering', '08-22-2023', 'Create new features that might provide more meaningful insights', '', ''),
    ('41', 'Data visualization, Most followed on Instagram',  '', 'Model Building and Prediction ', '08-22-2023', 'Train and validate the models using appropriate techniques', '', ''),
    ('43', 'Data cleaning, World Software Engineers db',  '', 'Interpretation and Insights', '08-22-2023', 'Address the initial questions or objectives set at the beginning of the project', '', ''),
    ('42', 'Data cleaning, Banking data sets',  '', 'Documentation and Code Cleanup', '08-22-2023', 'Archive and store your code, datasets, and any other resources used in the project', '', ''),
]

# Adding data into tasks table
# tasks_data = [
#     # ('id', 'user_id', 'project_id', 'task', 'description', 'deadline', 'required skills'),
#     ('', '1', '', '', '', '', ''),
#     ('', '2', '', '', '', '', ''),
#     ('', '3', '', '', '', '', ''),
#     ('', '4', '', '', '', '', ''),
#     ('', '5', '', '', '', '', ''),
#     ('', '6', '', '', '', '', ''),
#     ('', '7', '', '', '', '', ''),
#     ('', '8', '', '', '', '', ''),
#     ('', '9', '', '', '', '', ''),
#     ('', '10', '', '', '', '', ''),
#     ('', '11', '', '', '', '', ''),
#     ('', '12', '', '', '', '', ''),
#     ('', '13', '', '', '', '', ''),
#     ('', '14', '', '', '', '', ''),
#     ('', '15', '', '', '', '', ''),
#     ('', '16', '', '', '', '', ''),
#     ('', '17', '', '', '', '', ''),
#     ('', '18', '', '', '', '', ''),
# ]
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


#cur.executemany("INSERT INTO users (name, skill) VALUES (?, ?)", users_data)

#cur.executemany("INSERT INTO projects (owner, project, project_id, tasks, start_date, description, completed_tasks, uncompleted_tasks) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", projects_data)

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

# Query and print data from 'tasks' table
print("Task Table:")
cur.execute("SELECT * FROM tasks")
for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
