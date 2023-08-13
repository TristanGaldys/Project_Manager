import tkinter as tk
import random

# Dictionary to store tasks for each project and details for each task
project_tasks = {}
task_details = {}

def on_project_selected(event):
    selection = listbox.curselection()
    if selection:
        project = listbox.get(selection[0])
        tasks_listbox.delete(0, tk.END)
        for task in project_tasks[project]:
            tasks_listbox.insert(tk.END, task)

def on_task_selected(event):
    selection = tasks_listbox.curselection()
    if selection:
        task = tasks_listbox.get(selection[0])
        
        # Update task details labels
        description_label.config(text=f"Description: {task_details[task]['description']}")
        skills_label.config(text=f"Required Skills: {', '.join(task_details[task]['skills'])}")
        
        # Hide main frame and show task details frame
        main_frame.pack_forget()
        task_details_frame.pack(fill=tk.BOTH, expand=True)

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
root.geometry('1000x600')  # Adjusted size
root.title("Project_Manager")

menu_visible = False
menu_width = 200

# Main content
content_frame = tk.Frame(root, bg='#2E2E2E')
content_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

# Hamburger button in the content frame
hamburger_button_content = tk.Button(content_frame, text="☰", command=toggle_menu, bg='#2E2E2E', fg='white', relief=tk.FLAT)
hamburger_button_content.pack(anchor='ne', pady=10, padx=10)

# Main frame for projects and tasks
main_frame = tk.Frame(content_frame, bg='#2E2E2E')
main_frame.pack(fill=tk.BOTH, expand=True)

welcome_label = tk.Label(main_frame, text="Welcome", bg='#2E2E2E', fg='white', font=('Arial', 24, 'bold'))
welcome_label.pack(pady=20)

projects_label = tk.Label(main_frame, text="Available Projects", bg='#2E2E2E', fg='white', font=('Arial', 16))
projects_label.pack(pady=10)

listbox = tk.Listbox(main_frame, bg='#2E2E2E', fg='white', 
                     bd=0, highlightthickness=0, 
                     selectbackground='#4A4A4A', selectforeground='cyan',
                     font=('Arial', 12), width=50, height=10)
listbox.pack(pady=10)

tasks_label = tk.Label(main_frame, text="Tasks", bg='#2E2E2E', fg='white', font=('Arial', 16))
tasks_label.pack(pady=10)

tasks_listbox = tk.Listbox(main_frame, bg='#2E2E2E', fg='white', 
                           bd=0, highlightthickness=0, 
                           selectbackground='#4A4A4A', selectforeground='cyan',
                           font=('Arial', 12), width=50, height=10)
tasks_listbox.pack(pady=10)
tasks_listbox.bind("<<ListboxSelect>>", on_task_selected)

# Frame for task details
task_details_frame = tk.Frame(content_frame, bg='#2E2E2E')

description_label = tk.Label(task_details_frame, bg='#2E2E2E', fg='white', font=('Arial', 14))
description_label.pack(pady=20)

skills_label = tk.Label(task_details_frame, bg='#2E2E2E', fg='white', font=('Arial', 14))
skills_label.pack(pady=20)

back_button = tk.Button(task_details_frame, text="Back", command=go_back)
back_button.pack(pady=20)

# Populate projects and tasks
for _ in range(10):
    project_name = f"Project {random.randint(1, 100)}"
    listbox.insert(tk.END, project_name)
    
    tasks = [f"Task {random.randint(1, 100)}" for _ in range(random.randint(3, 10))]
    project_tasks[project_name] = tasks
    
    for task in tasks:
        description = f"This is a description for {task}."
        skills = [f"Skill {random.randint(1, 5)}", f"Skill {random.randint(6, 10)}"]
        task_details[task] = {'description': description, 'skills': skills}

listbox.bind("<<ListboxSelect>>", on_project_selected)

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
