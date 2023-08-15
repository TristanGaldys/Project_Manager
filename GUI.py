import tkinter as tk
from tkinter import ttk
import random

# Dictionary to store tasks for each project and details for each task
project_tasks = {}
task_details = {}

def create_rounded_rectangle(canvas, x1, y1, x2, y2, corner_radius, **kwargs):
    # Draw the main rectangle
    canvas.create_polygon(
        x1 + corner_radius, y1,
        x1 + corner_radius, y1,
        x2 - corner_radius, y1,
        x2 - corner_radius, y1,
        x2, y1,
        x2, y1 + corner_radius,
        x2, y1 + corner_radius,
        x2, y2 - corner_radius,
        x2, y2 - corner_radius,
        x2, y2,
        x2 - corner_radius, y2,
        x2 - corner_radius, y2,
        x1 + corner_radius, y2,
        x1 + corner_radius, y2,
        x1, y2,
        x1, y2 - corner_radius,
        x1, y2 - corner_radius,
        x1, y1 + corner_radius,
        x1, y1 + corner_radius,
        x1, y1,
        x1 + corner_radius, y1,
        smooth=True,
        **kwargs
    )

def on_project_selected(event, project_name):
    # Clear the tasks canvas
    tasks_canvas.delete("all")

    # Populate the tasks canvas
    y_position = 10
    height_of_item = 30
    spacing = 10

    for task in project_tasks[project_name]:
        # Create the rounded rectangle with the task name as the tag
        create_rounded_rectangle(tasks_canvas, 10, y_position, 390, y_position + height_of_item, 10, fill="#37465B", tag=task)
        
        # Create the text with the task name as the tag
        tasks_canvas.create_text(20, y_position + height_of_item/2, text=task, font=("Arial", 16), anchor='w', tags=task)
        
        # Increment the y_position for the next task
        y_position += height_of_item + spacing

    tasks_canvas.config(scrollregion=tasks_canvas.bbox(tk.ALL))

def tasks_canvas_click(event):
    # Get the current item under the mouse pointer
    current_item = tasks_canvas.find_withtag(tk.CURRENT)
    
    if not current_item:
        return  # No item was clicked

    # Retrieve all tags of the clicked item
    tags = tasks_canvas.gettags(current_item[0])
    
    # Reconstruct the task name from the tags
    task_name = " ".join(tag for tag in tags if tag != "current" and not tag.startswith("task_"))
    
    if task_name.startswith("Task"):
        # Display task details
        description_label.config(text=f"Description: {task_details[task_name]['description']}")
        skills_label.config(text=f"Required Skills: {', '.join(task_details[task_name]['skills'])}")
        
        # Hide main frame and show task details frame
        main_frame.pack_forget()
        task_details_frame.pack(fill=tk.BOTH, expand=True)


def canvas_click(event):
    # Get the current item under the mouse pointer
    current_item = canvas.find_withtag(tk.CURRENT)
    
    if not current_item:
        return  # No item was clicked
    
    # Retrieve all tags of the clicked item
    tags = canvas.gettags(current_item[0])
    
    # Reconstruct the project name from the tags
    project_name = " ".join(tag for tag in tags if tag != "current")
    
    if project_name.startswith("Project"):
        on_project_selected(event, project_name)

def on_mousewheel(event, canvas):
    canvas.yview_scroll(-1*(event.delta//120), "units")

def go_back():
    # Hide task details frame and show main frame
    task_details_frame.pack_forget()
    main_frame.pack(fill=tk.BOTH, expand=True)

def toggle_menu():
    global menu_visible
    if menu_visible:
        menu_frame.place_forget()  # Hide the menu
    else:
        menu_frame.place(x=root.winfo_width() - menu_width, y=0, relheight=1, width=menu_width)  # Show the menu
    menu_visible = not menu_visible

root = tk.Tk()
root.geometry('1000x600')
root.title("Project Manager")

menu_visible = False
menu_width = 200  # Adjusted width

style = ttk.Style()
style.theme_use('clam')

style.configure("TScrollbar",
                gripcount=0,
                background='#4A4A4A',
                troughcolor='#2E2E2E',
                bordercolor='#4A4A4A',
                darkcolor='#4A4A4A',
                lightcolor='#4A4A4A',
                arrowcolor='white')

style.map("TScrollbar",
          background=[('active', '#6A6A6A')],
          arrowcolor=[('pressed', 'red'), ('active', 'white')])

# Main content
content_frame = tk.Frame(root, bg='#2E2E2E')
content_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

# Hamburger button in the content frame
hamburger_button_content = tk.Button(content_frame, text="☰", command=toggle_menu, bg='#2E2E2E', fg='white', relief=tk.FLAT)
hamburger_button_content.pack(anchor='ne', pady=10, padx=10)

# Main frame for projects and tasks
main_frame = tk.Frame(content_frame, bg='#2E2E2E')
main_frame.pack(fill=tk.BOTH, expand=True)

welcome_label = tk.Label(main_frame, text="Welcome", bg='#2E2E2E', fg='white', font=('Arial', 30, 'bold'))
welcome_label.pack(anchor='w', pady=20, padx=200)

# Frame for projects canvas
projects_frame = tk.Frame(main_frame, bg='#2E2E2E')
projects_frame.pack(anchor='w', padx=200, fill=tk.BOTH, expand=True)

projects_label = tk.Label(projects_frame, text="Available Projects", bg='#2E2E2E', fg='white', font=('Arial', 20, 'bold'))
projects_label.pack(anchor='w', pady=(0, 2))

canvas = tk.Canvas(projects_frame, bg='#2E2E2E', bd=0, highlightthickness=0, width=400, height=200)
canvas.bind("<Button-1>", canvas_click)
canvas.bind("<MouseWheel>", lambda event, canvas=canvas: on_mousewheel(event, canvas))
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# For the projects scrollbar:
vbar = ttk.Scrollbar(projects_frame, orient=tk.VERTICAL, style="TScrollbar")
vbar.pack(side=tk.RIGHT, fill=tk.Y)
vbar.config(command=canvas.yview)
canvas.config(yscrollcommand=vbar.set)


# Frame for tasks canvas
tasks_frame = tk.Frame(main_frame, bg='#2E2E2E')
tasks_frame.pack(anchor='w', padx=200, fill=tk.BOTH, expand=True)

tasks_label = tk.Label(tasks_frame, text="Tasks", bg='#2E2E2E', fg='white', font=('Arial', 20, 'bold'))
tasks_label.pack(anchor='w', pady=(0, 2))

tasks_canvas = tk.Canvas(tasks_frame, bg='#2E2E2E', bd=0, highlightthickness=0, width=400, height=200)
tasks_canvas.bind("<Button-1>", tasks_canvas_click)
tasks_canvas.bind("<MouseWheel>", lambda event, canvas=tasks_canvas: on_mousewheel(event, canvas))

tasks_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# For the tasks scrollbar:
tasks_scrollbar = ttk.Scrollbar(tasks_frame, orient="vertical", command=tasks_canvas.yview, style="TScrollbar")
tasks_canvas.config(yscrollcommand=tasks_scrollbar.set)
tasks_scrollbar.pack(side="right", fill="y")

# Frame for task details
task_details_frame = tk.Frame(content_frame, bg='#2E2E2E')

description_label = tk.Label(task_details_frame, bg='#2E2E2E', fg='white', font=('Arial', 14))
description_label.pack(pady=20)

skills_label = tk.Label(task_details_frame, bg='#2E2E2E', fg='white', font=('Arial', 14))
skills_label.pack(pady=20)

back_button = tk.Button(task_details_frame, text="Back", command=go_back)
back_button.pack(pady=20)

# Populate projects and tasks
y_position = 10
height_of_item = 30
spacing = 10
project_names = [f"Project {random.randint(1, 100)}" for _ in range(10)]

for project_name in project_names:
    # Create the rounded rectangle with the project name as the tag
    create_rounded_rectangle(canvas, 10, y_position, 390, y_position + height_of_item, 10, fill="#37465B", tag=project_name)
    
    # Create the text with the project name as the tag
    canvas.create_text(20, y_position + height_of_item/2, text=project_name, font=("Arial", 16), anchor='w', tags=project_name)
    
    # Increment the y_position for the next project
    y_position += height_of_item + spacing

canvas.config(scrollregion=canvas.bbox(tk.ALL))

for project_name in project_names:
    tasks = [f"Task {random.randint(1, 100)}" for _ in range(random.randint(3, 10))]
    project_tasks[project_name] = tasks
    
    for task in tasks:
        description = f"This is a description for {task}."
        skills = [f"Skill {random.randint(1, 5)}", f"Skill {random.randint(6, 10)}"]
        task_details[task] = {'description': description, 'skills': skills}


# Side menu
menu_frame = tk.Frame(root, width=menu_width, bg='#4A4A4A')

# Hamburger button in the menu frame
hamburger_button_menu = tk.Button(menu_frame, text="☰", command=toggle_menu, bg='#4A4A4A', fg='white', relief=tk.FLAT)
hamburger_button_menu.pack(anchor='ne', pady=10, padx=10)

# Add options to the menu
options = ["Add/Change Skills", "Change Name", "View Projects"]
for option in options:
    btn = tk.Button(menu_frame, text=option, bg='#5A5A5A', fg='white', relief=tk.FLAT, anchor='w', padx=20)
    btn.pack(fill=tk.X, pady=10)

root.mainloop()
