import tkinter as tk
from tkinter import ttk
import random

# Dictionary to store tasks for each project and details for each task
project_tasks = {}
task_details = {}
scheduled_animation = None

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

def slide_menu(target_x, step=True):
    """Helper function to slide the menu_canvas."""
    global scheduled_animation
    if step:
        step = menu_width/40
    current_x = menu_canvas.winfo_x()
    
    if current_x == target_x:  # If already at target, stop
        return

    if target_x < current_x:  # Sliding out
        new_x = current_x - step
        if new_x <= target_x:
            new_x = target_x
            menu_canvas.place(x=new_x, y=0, relheight=1, width=menu_width)
        else:
            menu_canvas.place(x=new_x, y=0, relheight=1, width=menu_width)
            scheduled_animation = root.after(10, slide_menu, target_x)
    else:  # Sliding in
        new_x = current_x + step
        if new_x >= target_x:
            new_x = target_x
            menu_canvas.place(x=new_x, y=0, relheight=1, width=menu_width)
        else:
            menu_canvas.place(x=new_x, y=0, relheight=1, width=menu_width)
            scheduled_animation = root.after(10, slide_menu, target_x)

def on_menu_leave(event):
    """Function to start closing the menu when the mouse leaves the menu."""
    global scheduled_animation
    if scheduled_animation:
        root.after_cancel(scheduled_animation)
        scheduled_animation = None
    hide_menu()

def show_menu():
    global menu_visible
    if not menu_visible:
        # Target x position for the menu_canvas to slide in
        target_x = root.winfo_width() - menu_width
        # Start the sliding animation
        slide_menu(target_x)
        menu_visible = True

def hide_menu():
    global menu_visible
    if menu_visible:
        # Target x position for the menu_canvas to slide out
        target_x = root.winfo_width()
        # Start the sliding animation
        slide_menu(target_x)
        menu_visible = False

def draw_menu():
    # Create a rounded rectangle with the desired color
    create_rounded_rectangle(menu_canvas, 0, 0, menu_width + 35, root.winfo_height(), 35, fill=menu_color)

def adjust_menu(event=None):
    global scheduled_animation
    global previous_width
    global previous_height
    if previous_height != root.winfo_height(): 
        draw_menu()
        previous_height = root.winfo_height()
    if previous_width == root.winfo_width(): return
    previous_width = root.winfo_width()
    if menu_visible:
        target_x = root.winfo_width() - menu_width
    else:
        target_x = root.winfo_width()
    if scheduled_animation:  # If there's an ongoing animation, cancel it
        root.after_cancel(scheduled_animation)
        scheduled_animation = None
    menu_canvas.place(x=target_x, y=0, relheight=1, width=menu_width)



root = tk.Tk()
root.geometry('1000x600')
root.title("Project Manager")
previous_width = root.winfo_width()
previous_height = root.winfo_height()

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
menu_button_frame = tk.Frame(content_frame,  bg='#2E2E2E')
menu_button_frame.pack(anchor='ne', pady=10, padx=10)

ham_hover = tk.Label(menu_button_frame, text="☰", bg='#2E2E2E', fg='white', relief=tk.FLAT, font=("Arial", 18))
ham_hover.bind("<Enter>", lambda event: show_menu())
ham_hover.pack()

# Main frame for projects and tasks
main_frame = tk.Frame(content_frame, bg='#2E2E2E')
main_frame.pack(fill=tk.BOTH, expand=True)

welcome_label = tk.Label(main_frame, text="Welcome to Project Manager!", bg='#2E2E2E', fg='white', font=('Arial', 30, 'bold'))
welcome_label.pack(anchor='w', pady=20, padx=200)

# Frame for projects canvas
projects_frame = tk.Frame(main_frame, bg='#2E2E2E')
projects_frame.pack(anchor='w', padx=(menu_width, 0), fill=tk.BOTH, expand=True)

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
tasks_frame.pack(anchor='w', padx=(menu_width, 0), fill=tk.BOTH, expand=True)

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

menu_color = '#2F4F4F'

# Side menu
menu_canvas = tk.Canvas(root, bg='#2E2E2E', bd=0, highlightthickness=0)  # Set the background color to blue
menu_canvas.bind("<Leave>", lambda event: hide_menu())
menu_canvas.place(x=1000, y=0, relheight=1, width=menu_width)

root.after(10, draw_menu)  # Schedule the drawing of the menu after the mainloop starts

# Hamburger button in the menu frame
hamburger_button_menu = tk.Label(menu_canvas, text="☰", bg=menu_color, fg='white', relief=tk.FLAT, font=("Arial", 18))
hamburger_button_menu.pack(anchor='ne', pady=(10, 40), padx=10)
root.bind('<Configure>', adjust_menu)

# Add options to the menu
options = ["Change User", "Add/Remove Skill", "Active Projects", "Assigned Tasks", "Create Project"]
for option in options:
    btn = tk.Button(menu_canvas, text=option, bg='#2F4F4F', fg='white', relief=tk.FLAT,
                     anchor='w', padx=20, activebackground='#1E3E3E', activeforeground='white'
                     , font=("Arial", 10, 'bold'))
    btn.pack(fill=tk.X, pady=0)

root.mainloop()

