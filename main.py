"""
This is the main file for the Project Management Project

The goal of this project is for anyone to be able to open to Application and be able to select their Occupation and then be shown all the projects that are avaliable for the said Occupation
Every task will have  a set of occupations that can work on it
We will be using SQL to manage all the data
"""

import sqlite3

database = {}

projects = {"Back-end Developer": ["Project Manager", "Stock Analysis"],
             "Web Developer": ["Project Manager"],
             "Data Analyst" : ["Project Manager", "Stock Analysis"],
             "Data Engineer" : ["Project Manager", "Stock Analysis"]}

tasks = {"Project Manager" : {"Data Engineer" : "Create Database", "Back-end Developer" : "Implement Database Usage"},
         "Stock Analysis" : ["Import Dataset", "Scrap Data", "Create Database"]}

description = {"Project ManagerCreate Database" : "This task is meant to create the database that will house all the data for this project..ect",
               "Project ManagerImplement Database Usage" : "Description"}

occupation = str(input("Please Enter Your Occupation: "))

print(projects[occupation])

proj = input("Which project do you want to look into: ")

print(tasks[proj][occupation])

task = input("What task would look like to look into: ")

print(description[proj+task])