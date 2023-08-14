import pandas as pd

database = {'project.db'}

projects = {"Back-end Developer": [["Project Manager", "Stock Analysis"]],
            "Web Developer": ["Project Manager"],
            "Data Analyst": [["Project Manager", "Stock Analysis"]],
            "Data Engineer": [["Project Manager", "Stock Analysis"]]}
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df_projects = pd.DataFrame(projects)

tasks = {"Project Manager": {"Data Engineer": "Create Database", "Back-end Developer": "Implement Database Usage"},
         "Stock Analysis": ["Import Dataset", "Scrap Data", "Create Database"]}

description = {"Project ManagerCreate Database": "This task is meant to create the database that will \
                                                    house all the data for this project..ect",
               "Project ManagerImplement Database Usage": "Description"}

name = input("Please enter your name: ")
print('Hi,', name)
occupation = input("Please choose your occupation (Back-end Developer, Web Developer, Data Analyst, Data Engineer): ")
print()
if occupation == 'Back-end Developer':
    print("Very nice", name)
if occupation == 'Web Developer':
    print("Awesome", name)
if occupation == 'Data Analyst':
    print("Great", name)
if occupation == 'Data Engineer':
    print("Cool", name)

print("This is our list of current projects. What project would you be interested to work on?")
print()
print(df_projects)

proj = str(input("Which project do you want to dive into: "))

print()
task = input("What task would you like, choose one (Import Dataset, Scrap Data, Create Database): ")
print()
print(description)
