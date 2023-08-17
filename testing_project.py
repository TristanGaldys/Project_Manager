import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

prev_width = 0

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

def get_all_tags(canvas):
    all_tags = set()
    for item in canvas.find_all():
        tags = canvas.gettags(item)
        for tag in tags:
            all_tags.add(tag)
    return all_tags

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

def project_tasks():
    """
    This will return the task ids that are apart of the project
    """
    task_ids = [1,2,3,4]
    return task_ids

def task_info(id):
    """
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
        lines[max_lines-1] = lines[max_lines-1][0:-1]
        lines[max_lines-1] += "..."
    if len(lines) == 1: lines = lines[0]
    return lines

def get_longest(texts, font):
    longest_length = 0
    for text in texts:
        text_width = font.measure(text)
        longest_length = max(longest_length, text_width)
    return longest_length

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
    project = project.replace(" ", "_")
    canvas.delete(project)
    create_rounded_rectangle(canvas, 10, y, root.winfo_width()-210, y+90, 20, outline= '#FFFFFF', fill='#18141C', tag=project)
    y+= 15
    font = tkFont.Font(font=("Arial", 18, 'bold', 'underline'))
    canvas.create_text(20, y, text = project.replace("_", " "), anchor='w', font=font, tag=project, fill='#69D7FF')
    canvas.create_text(font.measure(project) + 50, y+5, text = "Incomplete Tasks: " + project_info()[1], anchor='w', font=("Arial", 12, 'bold'), tag=project, fill='#69D7FF')
    canvas.create_text(root.winfo_width()-400, y, text = "Contributors: " + project_info()[3], anchor='w', font=("Arial", 12, 'bold'), tag=project, fill = '#69D7FF')
    canvas.create_text(root.winfo_width()-400, y+25, text = "Project Age: " + project_info()[4], anchor='w', font=("Arial", 12, 'bold'), tag=project, fill = '#69D7FF')
    canvas.create_text(root.winfo_width()-400, y+50, text = "Completed Tasks: " + project_info()[2], anchor='w', font=("Arial", 12, 'bold'), tag=project, fill = '#69D7FF')
    y+= 30
    wrapped_text = wrap_text(project_info()[0], tkFont.Font(font=("Arial", 12)), root.winfo_width()-450, 2)
    for line in wrapped_text:
        canvas.create_text(20, y, text=line, anchor='w', font=("Arial", 12), tag=project, fill = '#1193C2')
        y += 20
    return y

def display_task(canvas, task, y =0):
    y+= 10
    canvas.delete("task_"+str(task))
    create_rounded_rectangle(canvas, 20, y, root.winfo_width()-220, y+50, 15, outline= '#FFFFFF', fill='#18141C', tag="task_"+str(task))
    y+= 15
    font = tkFont.Font(font=("Arial", 10, 'bold'))
    right_offset = get_longest(["Assigned to: " + task_info(task)[4], "Deadline: " +  task_info(task)[3]],font)
    canvas.create_text(30, y, text = task_info(task)[0], anchor='w', font=("Arial", 12, 'bold'), tag="task_"+str(task), fill = '#69D7FF')
    canvas.create_text(root.winfo_width()-right_offset -230, y, text = "Assigned to: " + task_info(task)[4], anchor='w', font=font, tag="task_"+str(task), fill = '#69D7FF')
    y+= 20
    canvas.create_text(30, y, text = wrap_text(task_info(task)[1], font, root.winfo_width()-right_offset -300, 1), anchor='w', font=font, tag="task_"+str(task), fill = '#69D7FF')
    canvas.create_text(root.winfo_width()-right_offset -230, y, text = "Deadline: " +  task_info(task)[3], anchor='w', font=font, tag="task_"+str(task), fill = '#69D7FF')
    y+= 10
    return y


def display_tasks(canvas, project, y = 0):
    project = project.replace(" ", "_")
    canvas.delete(project+"taskdrop")
    create_rounded_rectangle(canvas, 10, y, root.winfo_width()-210, 315, 20, outline= '#FFFFFF', fill='#3B3147', tag=project+"taskdrop")
    y = display_project(canvas, project, y)
    y = display_task(canvas, 1, y)
    y = display_task(canvas, 2, y)
    y = display_task(canvas, 3, y)
    y = display_task(canvas, 4, y)


def update_scale():
    global prev_width
    if root.winfo_width() != prev_width:
        main_canvas.config(width=root.winfo_width())
        display_tasks(main_canvas, "Project Manager")

root = tk.Tk()
root.geometry('1000x600')
root.minsize(1000,600)
root.title("Project Manager")

style = ttk.Style()
style.theme_use('clam')

main_canvas = tk.Canvas(root, bg='#241E2B', bd=0, highlightthickness=0, width=1000)
main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
root.bind("<Configure>", lambda event: update_scale() if event.widget == root else None)


root.mainloop()