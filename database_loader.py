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
        project TEXT,
        task TEXT,
        start date TEXT,
        description TEXT,
        completed tasks INTEGER,
        incomplete tasks INTEGER
    )
''')
# Create Table TASKS
cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        assigned_user TEXT,
        task INTEGER,
        description TEXT,
        deadline INTEGER,
        required_skills,
        FOREIGN KEY (task) references users (id)        
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
    # ('projects', 'tasks', 'start date', 'description', 'completed tasks', 'incomplete tasks')
    ('Regression', 'Data Collection and Preparation', '09-00-2023', "Gather the necessary datasets, ensuring they're relevant and high-quality", 'yes', 'no'),
    ('Classification', 'Model Deployment and Testing', '09-00-2023', 'Deploy the trained model to a production environment or create a prediction pipeline', 'no', 'yes'),
    ('Clustering', 'Problem Definition ', '09-00-2023', "Define the problem you're trying to solve with regression", 'yes', 'no'),
    ('Sentiment Analysis', 'Documentation and Reporting', '09-10-2023', 'Document the entire process, including data preprocessing, feature engineering, model selection, and evaluation metrics', 'yes', 'no'),
    ('Recommender System', 'Model Evaluation', '09-12-2023', 'Evaluate models using appropriate evaluation metrics such as Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), R-squared', 'no', 'yes'),
    ('NLP', 'Model Training', '09-13-2023', 'Train the selected models on the training dataset', 'no', 'yes'),
    ('Artificial Neural Network', 'Model Selection', '09-12-2023', 'Choose appropriate regression algorithms based on the problem type (linear, polynomial, etc.) and dataset size', 'yes', 'no'),
    ('Electricity Bill Management System', 'Requirement Gathering and Analysis', '08-22-2023', 'Understand the requirements of the management system, including user needs and business goals', 'yes', 'no'),
    ('Online Retail Application Database', 'Database Design', '08-22-2023', 'Create an Entity-Relationship Diagram (ERD) to visualize the database structure', 'yes', 'no'),
    ('Inventory Control Management', 'Schema Creation', '08-22-2023', 'Use a Database Management System (DBMS) to define tables, fields, data types, constraints, and relationships', 'yes', 'no'),
    ('Library Management System', 'Data Population', '09-30-2023', 'Develop scripts or use tools to insert data into the tables', 'yes', 'no'),
    ('Student Database Management', 'User Interface Design', '09-30-2023', 'Create mockups or wireframes to visualize the layout and functionalities', 'no', 'yes'),
    ('Payroll Management System', 'Front-End Development', '09-01-2023', 'Integrate the front-end with the back-end to fetch and display data from the database', 'no', 'yes'),
    ('Voice-based Transport Enquiry System', 'Database Connectivity', '09-01-2023', 'Establish a connection between the back-end server and the database', 'no', 'yes'),
    ('SMS-based Remote Server Monitoring System', 'Authentication and Authorization', '09-01-2023', 'Implement user authentication to ensure secure access to the system', 'no', 'yes'),
    ('E-Learning Platform', 'System Design', '09-01-2023', 'Architect the overall system, including database structure, backend services, and user interfaces', 'no', 'yes'),
    ('Advanced Employment Management System', 'User Management', '09-01-2023', 'Implement user authentication and authorization mechanisms', 'yes', 'no'),
    ('Image Encryption using AES', 'User Management', '09-01-2023', 'Manage roles and permissions for different user types ', 'no', 'yes'),
    ('Data Leak Detector', 'Job Posting and Recruitment', '08-30-2023', 'Design a module for posting job vacancies', 'yes', 'no'),
    ('Face Detector AI-Based Model', 'Performance Management', '08-30-2023', 'Develop mechanisms for setting employee goals and KPIs', 'yes', 'no'),
    ('Smart Health Prediction System', 'Leave and Attendance Management', '08-30-2023', 'Design a system for employees to apply for leaves', 'no', 'yes'),
    ('Weather Forecasting Application', 'Payroll and Compensation', '08-30-2023', 'Design a payroll module that calculates employee salaries based on attendance and other factors', 'no', 'yes'),
    ('E-Parking Challenge Generation System', 'Reporting and Analytics', '08-30-2023', 'Allow custom queries and filters for generating specific reports', 'no', 'yes'),
    ('Portfolio Website', 'UI/UX Design', '08-30-2023', 'Design the user interface elements, including buttons, forms, navigation, etc', 'yes', 'no'),
    ('To-Do App', 'Responsive Design', '08-30-2023', 'Ensure the application is responsive and works well on various screen sizes (desktop, tablet, mobile)', 'yes', 'no'),
    ('Virtual Keyboard', 'HTML/CSS Development', '08-30-2023', 'Write clean and semantic HTML code for the structure', 'no', 'yes'),
    ('Meme Generator', 'Cross-Browser Compatibility', '08-27-2023', 'Test and ensure the application works correctly across different web browsers (Chrome, Firefox, Safari, Edge, etc.)', 'no', 'yes'),
    ('Spotify Clone', 'Performance Optimization', '08-27-2023', 'Optimize images, scripts, and styles to improve page loading times', 'yes', 'no'),
    ('Chat App', 'Code Review and Testing', '08-27-2023', 'Conduct code reviews to ensure code quality and consistency', 'no', 'yes'),
    ('E-Commerce Website', 'Deployment', '08-27-2023', 'Deploy the front-end code to a web server or a content delivery network (CDN).', 'no', 'yes'),
    ('A User Authentication System. Image Source ', 'Requirements Gathering and Analysis', '08-27-2023', "Understand the project's objectives and requirements", 'no', 'yes'),
    ('Build a Landing Page. Image Source', 'Architecture and Design', '08-27-2023', 'Design the overall system architecture', 'no', 'yes'),
    ('Build Your Own Web Server', 'Database Design and Development', '08-23-2023', 'Set up the database server and create tables', 'yes', 'no'),
    ('Build a Finance Application', 'Server-Side Development', '08-23-2023', 'Develop backend APIs for communication with the frontend.', 'yes', 'no'),
    ('Create a Text Analyzer', 'API Development', '08-23-2023', 'Design RESTful or GraphQL APIs for communication with clients', 'no', 'yes'),
    ('Build a To-Do App', 'Middleware and Services', '08-23-2023', 'Integrate with third-party services like payment gateways or APIs', 'no', 'yes'),
    ('Build a CLI App', 'Security', '08-23-2023', 'Implement encryption for data at rest and in transit', 'no', 'yes'),
    ('Web Scraping Internet Movie', 'Defining the Problem and Objectives', '08-23-2023', 'Clearly define the goals and objectives of the data analysis project', 'no', 'yes'),
    ('Exploratory Data Analysis, Global suicide rates', 'Data Collection and Acquisition', '08-22-2023', 'Identify the data sources that are relevant to your analysis', 'yes', 'no'),
    ('Exploratory Data Analysis, World Happiness Report', 'Data Cleaning and Preprocessing', '08-22-2023', 'Handle missing data by imputing or removing it', 'yes', 'no'),
    ('Data visualization, Healthy food and sport', 'Exploratory Data Analysis (EDA):', '08-22-2023', 'Perform data visualization to understand the distribution of variables', 'yes', 'no'),
    ('Data visualization, Covid-19', 'Feature Engineering', '08-22-2023', 'Create new features that might provide more meaningful insights', 'no', 'yes'),
    ('Data visualization, Most followed on Instagram', 'Model Building and Prediction ', '08-22-2023', 'Train and validate the models using appropriate techniques', 'no', 'yes'),
    ('Data cleaning, World Software Engineers db', 'Interpretation and Insights', '08-22-2023', 'Address the initial questions or objectives set at the beginning of the project', 'yes', 'no'),
    ('Data cleaning, Banking data sets', 'Documentation and Code Cleanup', '08-22-2023', 'Archive and store your code, datasets, and any other resources used in the project', 'no', 'yes'),
]

# Adding data into tasks table
tasks_data = [
    # ('assigned user', 'task', 'description', 'deadline', 'required skills'),
    ('John Brzenk', '1', "Gather the necessary datasets, ensuring they're relevant and high-quality", '01-01-2024', 'Data Science'),
    ('Denis Cyplenkov', '2', 'Archive and store your code, datasets, and any other resources used in the project', '03-01-2024', 'Data Analysis'),
    ('Dave Chaffee', '3', 'Create new features that might provide more meaningful insights', '01-01-2024', 'Data Analysis'),
    ('Georgi Tsvetkov', '4', 'Clearly define the goals and objectives of the data analysis project', '03-01-2024', 'Data Analysis'),
    ('Levan Saginashvili', '5', 'Design RESTful or GraphQL APIs for communication with clients', '01-01-2024', 'Back end software development'),
    ('Artyom Morozov', '6', 'Write clean and semantic HTML code for the structure', '03-01-2024', 'Front end software development'),
    ('David Dadikyan', '7', 'Implement user authentication and authorization mechanisms', '01-07-2024', 'data base'),
    ('Ermes Gasparini', '8', 'Create mockups or wireframes to visualize the layout and functionalities', '01-01-2024', 'data base'),
    ('Vitaly Laletin', '9', 'Choose appropriate regression algorithms based on the problem type (linear, polynomial, etc.) and dataset size', '01-07-2024', 'Data Science'),
    ('Jerry Cadorette', '10', "Define the problem you're trying to solve with regression", '01-01-2024', 'Data Science'),
    ('Tobias Sporrong', '11', 'Deploy the trained model to a production environment or create a prediction pipeline', '01-07-2024', 'Data Science'),
    ('Devon Larratt', '12', 'Train the selected models on the training dataset', '01-07-2024', 'Data Science'),
    ('Dmitry Silaev', '13', 'Manage roles and permissions for different user types', '01-01-2024', 'Software Engineering'),
    ('Evgeny Prudnik', '14', 'Use a Database Management System (DBMS) to define tables, fields, data types, constraints, and relationships', '01-07-2024', 'Database'),
    ('Eglė Vaitkutė', '15', 'Develop scripts or use tools to insert data into the tables', '03-01-2024', 'Database'),
    ('Gabriela Vasconcelos', '16', 'Clearly define the goals and objectives of the data analysis project', '01-01-2024', 'Data Analysis'),
    ('Sarah Bäckman', '17', 'Allow custom queries and filters for generating specific reports', '01-07-2024', 'Software Engineering'),
    ('Barbora Bajciova', '18', 'Implement user authentication to ensure secure access to the system', '03-01-2024', 'Database'),
]

#cur.executemany("INSERT INTO users (name, skill) VALUES (?, ?)", users_data)

#cur.executemany("INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?)", projects_data)

#cur.executemany("INSERT INTO tasks (assigned_user, 'task', description, deadline, required_skills) VALUES (?, ?, ?, ?, ?)", tasks_data)

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
