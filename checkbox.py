import tkinter as tk

developer_skills = [
    "Python",
    "JavaScript",
    "Java",
    "C++",
    "C#",
    "HTML",
    "CSS",
    "SQL",
    "Ruby",
    "PHP",
    "Swift",
    "Kotlin",
    "TypeScript",
    "Go",
    "Rust",
    "Scala",
    "Perl",
    "R",
    "Shell Scripting",
    "Node.js",
    "React",
    "Angular",
    "Vue.js",
    "Django",
    "Flask",
    "Spring Boot",
    "Ruby on Rails",
    "Laravel",
    "ASP.NET",
    "GraphQL",
    "RESTful API Development",
    "WebSockets",
    "WebAssembly",
    "Bootstrap",
    "Tailwind CSS",
    "Sass/SCSS",
    "Docker",
    "Kubernetes",
    "AWS",
    "Azure",
    "Google Cloud Platform",
    "Serverless Architecture",
    "Firebase",
    "MongoDB",
    "PostgreSQL",
    "MySQL",
    "SQLite",
    "Redis",
    "Elasticsearch",
    "Git",
    "GitHub",
    "GitLab",
    "Bitbucket",
    "CI/CD",
    "Jenkins",
    "Travis CI",
    "Agile Development",
    "Scrum",
    "Kanban",
    "Test-Driven Development (TDD)",
    "Behavior-Driven Development (BDD)",
    "Unit Testing",
    "Integration Testing",
    "End-to-End Testing",
    "Jest",
    "Mocha",
    "Chai",
    "Selenium",
    "Cypress",
    "Performance Optimization",
    "Web Accessibility (WCAG)",
    "SEO Best Practices",
    "Responsive Web Design",
    "Mobile App Development",
    "Progressive Web Apps (PWA)",
    "WebVR/WebXR",
    "Three.js",
    "D3.js",
    "Game Development",
    "Unreal Engine",
    "Unity",
    "CryEngine",
    "Machine Learning",
    "TensorFlow",
    "PyTorch",
    "Natural Language Processing (NLP)",
    "Computer Vision",
    "Blockchain",
    "Ethereum",
    "Smart Contracts",
    "Solidity",
    "Raspberry Pi",
    "Arduino",
    "IoT Development",
    "Embedded Systems Programming",
    "Cybersecurity",
    "Penetration Testing",
    "Data Analysis",
    "Big Data",
    "Hadoop",
    "Spark",
    "Data Visualization",
    "VR/AR Development"
]

import tkinter as tk

def checkbox(parent, options, bg = '#241E2B', fg='#FFF'):
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(frame_id, width=event.width)

    def on_search(*args):
        query = search_var.get().lower()
        for checkbutton, option in zip(checkbuttons, options):
            if query in option.lower():
                checkbutton.pack(anchor='w', padx=10, pady=2)
            else:
                checkbutton.pack_forget()
        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def on_mousewheel(event, direction='y'):
        canvas.focus_set()
        if direction == 'y':
            canvas.yview_scroll(-1*(event.delta//120), "units")
        else:
            canvas.xview_scroll(-1*(event.delta//120), "units")

    # Entry for searching
    search_var = tk.StringVar()
    search_var.trace_add('write', on_search)
    entry = tk.Entry(parent, textvariable=search_var, bg=bg, fg=fg)
    entry.pack(pady=10, padx=10, fill=tk.X)

    # Create a Canvas
    canvas = tk.Canvas(parent, bg=bg, borderwidth=0, highlightthickness=0)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a frame to hold the Checkbuttons and add it to the Canvas
    frame = tk.Frame(canvas, bg=bg, borderwidth=0, highlightthickness=0)
    frame_id = canvas.create_window((0,0), window=frame, anchor='nw')

    # Populate the frame with Checkbuttons
    checkbutton_vars = []
    checkbuttons = []
    for option in options:
        var = tk.IntVar()
        checkbutton = tk.Checkbutton(frame, 
                                     text=option, 
                                     variable=var, 
                                     bg=bg, 
                                     fg=fg, 
                                     selectcolor='#000',
                                     activebackground='#241E2F')
        checkbutton.pack(anchor='w', padx=10, pady=2)
        checkbutton_vars.append(var)
        checkbuttons.append(checkbutton)


    frame.bind("<Configure>", on_frame_configure)
    parent.bind("<MouseWheel>", lambda event: on_mousewheel(event))

root = tk.Tk()
root.title("Checkbox Test")
root.configure(bg= '#241E2B')

checkbox(root, developer_skills)

root.mainloop()