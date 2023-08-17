import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

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

def project_info():
    """
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

def wrap_text(text, font, max_width, max_lines = None):
    lines = []
    words = text.split()
    
    while words:
        line = ''
        while words and font.measure(line + words[0]) <= max_width:
            line += (words.pop(0) + ' ')
        lines.append(line)
    if max_lines != None and len(lines) > max_lines:
        lines = lines[0:max_lines]
        lines[max_lines-1] += "..."
    return lines

def display_project(canvas, project, y= 0):
    """
    This Method Creates a Project that is well visualized and shows all important pieces of data for the Project

    param: canvas: This is a tk object that this project should be placed into
    type: tk.Canvas

    param: project: This is the name of the project but might soon be changed to Proj_id
    type: String

    param: y: this is the y location that this project display should be placed at
    type: int
    """
    y+= 10
    canvas.delete('all')
    create_rounded_rectangle(canvas, 10, y, root.winfo_width()-210, 70, 20, outline= '#000000', fill='#FFFFFF', tag=project)
    y+= 15
    font = tkFont.Font(font=("Arial", 16, 'bold', 'underline'))
    canvas.create_text(20, y, text = project, anchor='w', font=("Arial", 16, 'bold', 'underline'), tag=project)
    canvas.create_text(font.measure(project) + 50, y, text = "Incomplete Tasks: " + project_info()[1], anchor='w', font=("Arial", 10, 'bold'), tag=project)
    canvas.create_text(root.winfo_width()-350, y-2, text = "Contributors: " + project_info()[3], anchor='w', font=("Arial", 10, 'bold'), tag=project)
    canvas.create_text(root.winfo_width()-350, y+15, text = "Project Age: " + project_info()[4], anchor='w', font=("Arial", 10, 'bold'), tag=project)
    canvas.create_text(root.winfo_width()-350, y+32, text = "Completed Tasks: " + project_info()[2], anchor='w', font=("Arial", 10, 'bold'), tag=project)
    y+= 20
    wrapped_text = wrap_text(project_info()[0], tkFont.Font(font=("Arial", 10)), root.winfo_width()-400, 2)
    for line in wrapped_text:
        canvas.create_text(20, y, text=line, anchor='w', font=("Arial", 10), tag=project)
        y += 15

def update_scale():
    main_canvas.config(width=root.winfo_width())
    display_project(main_canvas, "Project Manager")

root = tk.Tk()
root.geometry('1000x600')
root.minsize(1000,600)
root.title("Project Manager")

style = ttk.Style()
style.theme_use('clam')

main_canvas = tk.Canvas(root, bg='#2E2E2E', bd=0, highlightthickness=0, width=root.winfo_width())
main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
root.bind("<Configure>", lambda event: update_scale() if event.widget == root else None)


root.mainloop()