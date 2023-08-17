import tkinter as tk
from tkinter import ttk
import random

# Dictionary to store tasks for each project and details for each task
project_tasks = {}
task_details = {}
scheduled_animation = None
project_displayed = None

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

def main_canvas_click(event):
    # Get the current item under the mouse pointer
    current_item = main_canvas.find_withtag(tk.CURRENT)
    
    if not current_item:
        return  # No item was clicked
    
    # Retrieve all tags of the clicked item
    tags = main_canvas.gettags(current_item[0])
    
    # Reconstruct the name from the tags
    name = " ".join(tag for tag in tags if tag != "current")
    
    if name.startswith("Project"):
        display_tasks_for_project(name)
    elif name.startswith("Task"):
        display_task_details(name)

def get_all_tags(canvas):
    all_tags = set()
    for item in canvas.find_all():
        tags = canvas.gettags(item)
        for tag in tags:
            all_tags.add(tag)
    return all_tags

def display_tasks_for_project(project_name):
    global project_displayed
    # Clear the main_canvas
    main_canvas.delete('all')

    # Redraw all projects and tasks, but insert tasks for the clicked project
    y_position = 10
    for project in project_names:
        # Draw the project
        create_rounded_rectangle(main_canvas, 25, y_position, root.winfo_width()*.9, y_position + height_of_item, 10, fill="#37465B", tag=project)
        main_canvas.create_text(35, y_position + height_of_item/2, text=project.replace('_', ' '), font=("Arial", 16), anchor='w', tags=project)
        y_position += height_of_item + spacing


        if project == project_name:
            if project_displayed == project_name: 
                project_displayed = None
                continue
            # Draw the tasks for this project
            for task in project_tasks[project_name]:
                create_rounded_rectangle(main_canvas, 25, y_position, root.winfo_width()*.9, y_position + height_of_item, 10, fill="#37465B", tag=task)
                main_canvas.create_text(35, y_position + height_of_item/2, text=task.replace('_', ' '), font=("Arial", 16), anchor='w', tags=task)
                y_position += height_of_item + spacing
            project_displayed = project_name
    main_canvas.config(scrollregion=main_canvas.bbox(tk.ALL))

def display_task_details(task_name):
    # Display task details
    description_label.config(text=f"Description: {task_details[task_name]['description']}")
    skills_label.config(text=f"Required Skills: {', '.join(task_details[task_name]['skills'])}")
    
    # Hide main frame and show task details frame
    main_frame.pack_forget()
    task_details_frame.pack(fill=tk.BOTH, expand=True)

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

def adjust_menu(event=None):
    global scheduled_animation
    global previous_width
    global previous_height
    if previous_height != root.winfo_height(): 
        create_rounded_rectangle(menu_canvas, 0, 0, menu_width + 35, root.winfo_height(), 35, fill=menu_color)
        previous_height = root.winfo_height()
    if previous_width == root.winfo_width(): return
    previous_width = root.winfo_width()
    display_projects(project_names)
    if menu_visible:
        target_x = root.winfo_width() - menu_width
    else:
        target_x = root.winfo_width()
    if scheduled_animation:  # If there's an ongoing animation, cancel it
        root.after_cancel(scheduled_animation)
        scheduled_animation = None
    menu_canvas.place(x=target_x, y=0, relheight=1, width=menu_width)

def display_projects(projects):
    y_position = 10
    height_of_item = 30
    spacing = 10
    for project_name in projects:
        # Create the rounded rectangle with the project name as the tag
        root.after(10, create_rounded_rectangle(main_canvas, 25, y_position, root.winfo_width()*.9, y_position + height_of_item, 10, fill="#37465B", tag=project_name))
        
        # Create the text with the project name as the tag
        main_canvas.create_text(35, y_position + height_of_item/2, text=project_name.replace('_', ' '), font=("Arial", 16), anchor='w', tags=project_name)
        
        # Increment the y_position for the next project
        y_position += height_of_item + spacing

    for project_name in project_names:
        tasks = [f"Task_{random.randint(1, 100)}" for _ in range(random.randint(3, 10))]
        project_tasks[project_name] = tasks
        
        for task in tasks:
            description = f"This is a description for {task.replace('_', ' ')}."
            skills = [f"Skill {random.randint(1, 5)}", f"Skill {random.randint(6, 10)}"]
            task_details[task] = {'description': description, 'skills': skills}

root = tk.Tk()
root.geometry('1000x600')
root.title("Project Manager")
previous_width = root.winfo_width()
previous_height = root.winfo_height()

menu_visible = False
menu_width = 200  # Adjusted width

style = ttk.Style()
style.theme_use('clam')

# Main content
content_frame = tk.Frame(root, bg='#2E2E2E')
content_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

# Hamburger button in the content frame
menu_button_frame = tk.Frame(content_frame,  bg='#2E2E2E')
menu_button_frame.pack(anchor='ne', pady=10, padx=10)

ham_button = tk.Button(menu_button_frame, text="☰", bg='#2E2E2E', fg='white', relief=tk.FLAT, font=("Arial", 18))
ham_button.bind("<Button-1>", lambda event: show_menu())
ham_button.pack()

# Main frame for projects and tasks
main_frame = tk.Frame(content_frame, bg='#2E2E2E')
main_frame.pack(fill=tk.BOTH, expand=True, padx=50)  # Adjusted padding

welcome_label = tk.Label(main_frame, text="Welcome to Project Manager!", bg='#2E2E2E', fg='white', font=('Arial', 30, 'bold'))
welcome_label.pack(anchor='w', pady=0, padx=10)  # Adjusted padding


project_frame = tk.Frame(main_frame, bg='#2E2E2E')
project_frame.pack(fill=tk.BOTH, expand=True)
# Single canvas for both projects and tasks
main_canvas = tk.Canvas(project_frame, bg='#2E2E2E', bd=0, highlightthickness=0, width=1000)
main_canvas.bind("<Button-1>", main_canvas_click)
main_canvas.bind("<MouseWheel>", lambda event, canvas=main_canvas: on_mousewheel(event, canvas))
main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
main_canvas.config(scrollregion=main_canvas.bbox(tk.ALL))
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
project_names = [f"Project_{random.randint(1, 100)}" for _ in range(10)]

menu_color = '#2F4F4F'

# Side menu
menu_canvas = tk.Canvas(root, bg='#2E2E2E', bd=0, highlightthickness=0)  # Set the background color to blue
menu_canvas.place(x=1000, y=0, relheight=1, width=menu_width)

root.after(10, create_rounded_rectangle(menu_canvas, 0, 0, menu_width + 35, root.winfo_height(), 35, fill=menu_color))  # Schedule the drawing of the menu after the mainloop starts
root.after(100, display_projects(project_names))

# Hamburger button in the menu frame
close_menu = tk.Button(menu_canvas, text="X", bg=menu_color, fg='white', relief=tk.FLAT, font=("Arial", 16))

close_menu.pack(anchor='ne', pady=(10, 40), padx=10)
close_menu.bind("<Button-1>", lambda event: hide_menu())
root.bind('<Configure>', adjust_menu)

# Add options to the menu
options = ["Change User", "Add/Remove Skill", "Active Projects", "Assigned Tasks", "Create Project"]
for option in options:
    btn = tk.Button(menu_canvas, text=option, bg='#2F4F4F', fg='white', relief=tk.FLAT,
                     anchor='w', padx=20, activebackground='#1E3E3E', activeforeground='white'
                     , font=("Arial", 10, 'bold'))
    btn.pack(fill=tk.X, pady=0)

root.mainloop()

