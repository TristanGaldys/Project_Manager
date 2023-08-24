from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import temp_query as query

class AbstractTab(ABC):
    def __init__(self, parent, button, tab_canvas, classkeys, select = False):
        self.notebook = parent
        self.frame = tk.Frame(parent, bg="#241E2B")
        classkeys[str(self.frame)] = self
        self.classkeys = classkeys
        self.button = button
        self.tab = tab_canvas
        self.button.bind("<Button-1>", lambda event: self.select_tab())
        self.width = 1000
        if parent.winfo_width() > 1000: self.width = parent.winfo_width()
        self.height = 500
        if parent.winfo_height() > 500: self.height = parent.winfo_height()
        self.frame.bind("<Configure>", lambda event: self.update_tab() if self.notebook.select() == str(self.frame) else None)
        parent.add(self.frame, text=button.cget("text"))
        if select: self.select_tab()
        self.create_styles()

    def create_styles(self):
        self.style = ttk.Style()
        self.style.configure("Custom.TButton",
                background="#282828",
                foreground="white",
                bordercolor="#282828",
                darkcolor="#282828",
                lightcolor="#282828",
                relief="flat")
        self.style.map("Custom.TButton",
            background=[('active', '#282828')],
            foreground=[('active', 'white')])
        self.style.configure('Custom.TEntry', 
                foreground='white',
                font=('Arial', 12),
                background="#282828",
                fieldbackground="#282828",
                insertcolor='white',  # Color of the insertion cursor
                borderwidth=0,
                highlightbackground='#241E2B',
                highlightthickness=3
               )

    def __del__(self):
        self.classkeys[self.past].select_tab()
        self.button.destroy()
        self.frame.destroy()

    def create_tab(self, label, Tab, delete = False):
        new_tab = Tab(self.notebook, self.classkeys[self.notebook].create_tab(label), self.tab, self.classkeys, True)
        if delete: 
            self.past = str(new_tab.frame)
            self.__del__()

    def select_tab(self):
        x1, x2 = self.button.winfo_x(), self.button.winfo_x() + self.button.winfo_width()
        if str(self.frame) == self.notebook.select() and int(self.tab.coords("selected")[0]) == x1:
            return False
        self.past = self.notebook.select()
        self.notebook.select(self.frame)
        
        # Calculate the actual visible region of the canvas in terms of content coordinates
        visible_x1 = self.tab.xview()[0] * self.tab.winfo_width()
        visible_x2 = self.tab.xview()[1] * self.tab.winfo_width()
        
        # Check if the button's x-coordinates are outside the visible region
        if x1 < visible_x1 or x2 > visible_x2:
            self.tab.xview_moveto(x1 / self.tab.winfo_width())
        
        self.tab.delete("selected")
        self.tab.create_line(x1, 45, x2, 45, fill="blue", width=4, tag='selected')
        return True

    def create_rounded_rectangle(self, canvas, x1, y1, x2, y2, corner_radius, **kwargs):
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

    def wrap_text(self, text, font, max_width, max_lines = None):
        if font == "":
            font = tkFont.Font(font="TkDefaultFont")

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

    def get_longest(self, texts, font = ""):
        if font == "":
            font = tkFont.Font(font="TkDefaultFont")
        longest_length = 0
        for text in texts:
            text_width = font.measure(text)
            longest_length = max(longest_length, text_width)
        return longest_length
    
    def on_mousewheel(self,event, canvas, dir = 'y'):
        """
        This allows the canvas to be scrolled through
        """
        canvas.focus_set()
        if dir == 'y':
            canvas.yview_scroll(-1*(event.delta//120), "units")
        else:
            canvas.xview_scroll(-1*(event.delta//120), "units")
    
    def on_var_change(self, var):
        #print(var.get())
        pass

    def get_selected(self, checkbutton_vars):
        selected = []
        for key, value in checkbutton_vars.items():
            if value.get() != 0:
                selected.append(key)
        return selected

    def unbind_mousewheel_from_children(self, widget):
        """Recursively unbind an event from a widget and its children."""
        widget.unbind("<MouseWheel>")
        for child in widget.winfo_children():
            self.unbind_mousewheel_from_children(child, "<MouseWheel>")

    def bind_mousewheel(self, widget, canvas , dir = 'y'):
        widget.bind("<MouseWheel>", lambda e, canvas=canvas: self.on_mousewheel(e, canvas, dir))
        for child in widget.winfo_children():
            self.bind_mousewheel(child, canvas, dir)

    def checkbox(self, parent, options, height = 200, width = 300, print_sel = True, sel_label = "You've Selected: "):
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
        
        def print_selection(*args):
            for line in printed_sel:
                line.place_forget()
            printed_sel.clear()
            text = ""
            for skill in self.get_selected(checkbutton_vars):
                if text == "":
                    text = sel_label + skill
                else:
                    text += ", " + skill
            text = self.wrap_text(text, "", width-framewidth)
            if isinstance(text, list):
                spacing = 0
                for line in text:
                    temp = tk.Label(canvas, text=line, bg='#241E2B', fg='white')
                    temp.place(x= framewidth, y = spacing)
                    printed_sel.append(temp)
                    spacing += 20
            else:
                temp = tk.Label(canvas, text=text, bg='#241E2B', fg='white')
                temp.place(x= framewidth, y = 0)
                printed_sel.append(temp)

        def add_option():
            if search_var.get() not in options:
                var = tk.IntVar()
                var.trace_add('write', print_selection)
                checkbutton = tk.Checkbutton(frame, 
                                            text=search_var.get(), 
                                            variable=var, 
                                            bg='#241E2B', 
                                            fg='#FFF', 
                                            selectcolor='#000',
                                            activebackground='#241E2F')
                checkbutton.pack(anchor='w', padx=10, pady=2)
                checkbutton_vars[search_var.get()] = var
                checkbuttons.append(checkbutton)
                options.append(search_var.get())
            if checkbutton_vars[search_var.get()].get() == 0:
                checkbutton_vars[search_var.get()].set(1)
            else:
                checkbutton_vars[search_var.get()].set(0)

        printed_sel = []
        framewidth = width
        if print_sel:
            framewidth = self.get_longest(options)+ 25
            if width/2 > framewidth:
                framewidth = width/2

        # Entry for searching
        search_var = tk.StringVar()
        search_var.trace_add('write', on_search)
        entry = tk.Entry(parent, textvariable=search_var, bg='#241E2B', fg='#FFF')
        entry.pack(pady=0, padx=(0, width- framewidth), fill=tk.X)
        entry.bind("<Return>", lambda event: add_option())

        # Create a Canvas
        canvas = tk.Canvas(parent, bg='#241E2B', borderwidth=0, highlightthickness=0, height=height, width = width)
        canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a frame to hold the Checkbuttons and add it to the Canvas
        frame = tk.Frame(canvas, bg='#241E2B', borderwidth=0, highlightthickness=0)
        frame_id = canvas.create_window((0,0), window=frame, anchor='nw', width= framewidth)

        # Populate the frame with Checkbuttons
        checkbutton_vars = {}
        checkbuttons = []
        for option in options:
            var = tk.IntVar()
            var.trace_add('write', print_selection)
            checkbutton = tk.Checkbutton(frame, 
                                        text=option, 
                                        variable=var, 
                                        bg='#241E2B', 
                                        fg='#FFF', 
                                        selectcolor='#000',
                                        activebackground='#241E2F')
            checkbutton.pack(anchor='w', padx=0, pady=2)
            checkbutton_vars[option] = var
            checkbuttons.append(checkbutton)

        frame.bind("<Configure>", on_frame_configure)
        self.bind_mousewheel(frame, canvas)
        return checkbutton_vars

    @abstractmethod
    def update_tab(self):
        if self.frame.winfo_height() != self.height:
            self.height = self.frame.winfo_height()
        self.select_tab()

class ExploreTab(AbstractTab):
    def __init__(self, parent, button, tab_canvas, classkeys, select = False):
        super().__init__(parent, button, tab_canvas, classkeys, select)
        self.selected = None

        if not hasattr(self, "user"): 
            self.user = None
            self.noProjects = "Seems like there are no Projects :(, Please log in if you'd like to make one!"

        canvas = tk.Canvas(self.frame, bg='#241E2B', bd=0, highlightthickness=0, width=1000)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a top frame to contain the 'avail' label and 'entry' widget
        self.top_frame = tk.Frame(canvas, bg='#241E2B')
        self.top_frame.pack(pady=20, fill='x')  # pad in the y direction to provide spacing

        self.avail = tk.Label(self.top_frame, text="Available Projects", bg='#241E2B', fg='white', font=('Arial', 18, 'bold'))
        self.avail.pack(side='left', padx=20)

        # Create a StringVar for your entry
        entry_var = tk.StringVar()
        entry_var.set("🔍 Search For Projects")  # initial value

        # Set a trace on the StringVar
        entry_var.trace_add("write", lambda *args: self.on_var_change(entry_var))

        self.entry = tk.Entry(self.top_frame, textvariable=entry_var, fg='white', font=('Arial', 12), bg="#282828", width=30, bd=0, highlightbackground='#18141D', highlightthickness=3)
        self.entry.pack(side='right', padx=20)

        self.main_canvas = tk.Canvas(canvas, bg='#241E2B', bd=0, highlightthickness=0, width=1000)
        self.main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 0))
        self.projects = query.get_projects(self.user)
        self.display_all_proj()
        self.main_canvas.bind("<Button-1>", lambda event: self.click(event))
        self.entry.bind("<FocusIn>", lambda event: self.remove_placeholder(self.entry, "🔍 Search For Projects"))
        self.entry.bind("<FocusOut>", lambda event: self.restore_placeholder(self.entry, "🔍 Search For Projects"))

    def update_tab(self):
        super().update_tab()
        self.update_scrolling()
        if self.width != self.frame.winfo_width():
            self.width = self.frame.winfo_width()
            self.entry.pack(side='left', padx=(self.width-500 , 10))
            self.display_all_proj()

    def display_project(self, project, y= 0):
        """
        This Method Creates a Project that is well visualized and shows all important pieces of data for the Project

        param: canvas: This is a tk object that this project should be placed into
        type: tk.Canvas

        param: project: This is the name of the project but might soon be changed to Proj_id
        type: String

        param: y: this is the y location that this project display should be placed at
        type: int
        """
        #Making project name into a single tagable name
        project = project.replace(" ", "_")

        #Determining how much space to give on the right side
        font = tkFont.Font(font=("Arial", 12, 'bold'))
        right_offset = self.get_longest(["Contributors: " + query.project_info()[3], "Project Age: " + query.project_info()[4], "Completed Tasks: " + query.project_info()[2]],font)+50

        #Creating background for the project
        self.create_rounded_rectangle(self.main_canvas, 10, y, self.width-40, y+90, 20, outline= '#FFFFFF', fill='#18141C', tag=project)
        y+= 20

        #font for measurement
        font = tkFont.Font(font=("Arial", 18, 'bold', 'underline'))
        #Writing Project Name
        self.main_canvas.create_text(20, y, text = project.replace("_", " "), anchor='w', font=font, tag=[project, 'header'], fill='#69D7FF')
        #Writing Incomplete Tasks
        self.main_canvas.create_text(font.measure(project) + 50, y+5, text = "Incomplete Tasks: " + query.project_info()[1], anchor='w', font=("Arial", 12, 'bold'), tag=project, fill='#69D7FF')
        #Writing Amount of Contributors
        self.main_canvas.create_text(self.width-right_offset, y, text = "Contributors: " + query.project_info()[3], anchor='w', font=("Arial", 12, 'bold'), tag=project, fill = '#69D7FF')
        #Writing the Projects Age
        self.main_canvas.create_text(self.width-right_offset, y+25, text = "Project Age: " + query.project_info()[4], anchor='w', font=("Arial", 12, 'bold'), tag=project, fill = '#69D7FF')
        #Writing amount of tasks completed
        self.main_canvas.create_text(self.width-right_offset, y+50, text = "Completed Tasks: " + query.project_info()[2], anchor='w', font=("Arial", 12, 'bold'), tag=project, fill = '#69D7FF')

        #shifting down to write the description
        y+= 32
        #Wrapping the text for the description into 2 lines
        wrapped_text = self.wrap_text(query.project_info()[0], tkFont.Font(font=("Arial", 12)), self.width-right_offset -50, 2)
        #Looping to write it down
        for line in wrapped_text:
            self.main_canvas.create_text(20, y, text=line, anchor='w', font=("Arial", 12), tag=project, fill = '#1193C2')
            y += 20
        return y

    def display_task(self, canvas, task, y =0):
        """
        This function is meant to display a singlar task

        param: canvas: This determines what canvas to draw onto
        type: tk.Canvas

        param: tasks: This is the Primary key of the task from the database
        type: int

        param: y: This is determines the y axis location to draw onto
        type: int

        return: y: This is the bottom of the task so it can easily be passed on and not be drawn onto
        type: int    
        """
        #Clearing this task so just in case it doesnt ever have 2 versions
        canvas.delete("task_"+str(task))

        font = tkFont.Font(font=("Arial", 10, 'bold')) #most used font

        #Determining how much space to give on the right side
        right_offset = self.get_longest(["Assigned to: " + query.task_info(task)[4], "Deadline: " +  query.task_info(task)[3]],font) +60

        #Determining how much space there is to write the required skills
        skill_space = self.width - right_offset - tkFont.Font(font=("Arial", 12, 'bold')).measure(query.task_info(task)[0]) -100
        skill = self.wrap_text("Required Skills: " + query.task_info(task)[2], font, skill_space, 1)

        #Creating the Task background
        self.create_rounded_rectangle(canvas, 20, y, self.width-50, y+50, 15, outline= '#FFFFFF', fill='#18141C', tag="task_"+str(task))
        
        y+= 15 # Moving down to the first line of text
        #Writing Task Name
        canvas.create_text(30, y, text = query.task_info(task)[0], anchor='w', font=("Arial", 12, 'bold'), tag="task_"+str(task), fill = '#FFFFFF')
        #Writing Assigned User 
        canvas.create_text(self.width-right_offset, y, text = "Assigned to: " + query.task_info(task)[4], anchor='w', font=font, tag="task_"+str(task), fill = '#FFFFFF')
        #Writng the Required Skills
        canvas.create_text(tkFont.Font(font=("Arial", 12, 'bold')).measure(query.task_info(task)[0])+ 50, y, text = skill, anchor='w', font=font, tag="task_"+str(task), fill = '#FFFFFF')

        y+= 20 #Moving down to second line of text
        #Wrinting down the task description
        canvas.create_text(30, y, text = self.wrap_text(query.task_info(task)[1], font, self.width-right_offset -140, 1), anchor='w', font=font, tag="task_"+str(task), fill = '#FFFFFF')
        #Writing the deadline down
        canvas.create_text(self.width-right_offset, y, text = "Deadline: " +  query.task_info(task)[3], anchor='w', font=font, tag="task_"+str(task), fill = '#FFFFFF')

        y+= 15 #moving the y to the bottom of the task section 
        return y

    def display_proj_tasks(self, project, y = 0):
        #This allows the tags to work well while allowing users to have spaces in their project names
        project = project.replace(" ", "_")

        #cuts the tasks amount down to a max of 4
        tasks = query.project_tasks(project)
        if len(tasks) > 4: tasks = tasks[0:4]

        #Creates the "Dropdown"
        self.create_rounded_rectangle(self.main_canvas, 10, y, self.width-40, y + 95 + len(tasks)*55, 20, outline= '#FFFFFF', fill='#3B3147', tag="taskdrop")

        #Displays the Project
        y = self.display_project(project, y)
        spacing = 5
        #Display the Tasks
        for task in tasks:
            y = self.display_task(self.main_canvas, task, y +spacing)
        y += 5
        return y

    def display_all_proj(self, y = 0):
        """
        This function displays all projects and whichever projects tasks that are selected
        """
        self.main_canvas.delete('all')
        if self.projects == []:
            text = self.wrap_text(self.noProjects, tkFont.Font(font=("Arial", 20, 'bold')), self.width-200)
            i = 0
            if isinstance(text, str): text = [text]
            for line in text:
                self.main_canvas.create_text(self.width/2, 150+i, text= line, fill="white", anchor='c', font=("Arial", 20, 'bold'), tag='NoProj')
                i+= 30
        else:
            for project in self.projects:
                if project == self.selected:
                    y = self.display_proj_tasks(project, y+10)
                else:
                    y = self.display_project(project, y+10)
        self.main_canvas.update()   
        #After creating the projects making sure the scrolling region is set right
        self.main_canvas.config(scrollregion=self.main_canvas.bbox(tk.ALL))

    def click(self, event):
        # Get the current item under the mouse pointer
        self.main_canvas.focus_set()
        current_item = self.main_canvas.find_withtag(tk.CURRENT)
        
        if not current_item:
            return  # No item was clicked
        
        # Retrieve all tags of the clicked item
        tags = self.main_canvas.gettags(current_item[0])
        
        # Reconstruct the name from the tags
        name = " ".join(tag for tag in tags if tag != "current")
        if name == "taskdrop": 
            pass
        elif name.startswith("task_"):
            pass
        else:
            name = name.replace("_", " ")
            self.main_canvas.delete('all')
            if name == self.selected:
                self.selected = None
            else:
                self.selected = name.replace("_", " ")
            self.display_all_proj()
        #elif name.endswith("header"):
        #    print("Open Project Tab")

    def remove_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)

    def restore_placeholder(self, entry, placeholder):
        if entry.get().strip() == "":
            entry.insert(0, placeholder)

    def update_scrolling(self):
        if len(self.projects)*100 < self.height-80:
            self.main_canvas.unbind("<MouseWheel>")
        else:
            self.main_canvas.bind("<MouseWheel>", lambda event, canvas=self.main_canvas: self.on_mousewheel(event, canvas))

class UserProjectsTab(ExploreTab):
    def __init__(self, parent, button, tab_canvas, classkeys, select=False):
        self.classkeys = classkeys
        self.noProjects = "Seems like you arent a part of any projects, You can either find one to join or create one!"
        self.user = classkeys[parent].user
        super().__init__(parent, button, tab_canvas, classkeys, select)
        self.avail.configure(text= "Your Projects")
        newProj = ttk.Button(self.top_frame, text="Create Project", style="Custom.TButton")
        newProj.pack(side= 'right', padx=0)
    
    def update_tab(self):
        if not hasattr(self, "projects"):
            return
        return super().update_tab()

class LoginTab(AbstractTab):
    def __init__(self, parent, button, tab_canvas, classkeys, select = False):
        super().__init__(parent, button, tab_canvas, classkeys, select)
        self.canvas = tk.Canvas(self.frame, bg='#241E2B', bd=0, highlightthickness=0, width=self.width)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.fail_label = tk.Label(self.canvas, text="", bg='#241E2B', fg='red', font=('Arial', 12))
        self.fail_label.place(rely= 0.3, x= self.width/2 -50)

        # Sign in message
        sign = tk.Label(self.canvas, text="Sign In", bg='#241E2B', fg='white', font=('Arial', 18, 'bold'))
        sign.place(relx = .5, rely=0.25, anchor='c')

        self.user = tk.StringVar()

        # Username label & entry
        self.username_label = tk.Label(self.canvas, text="Username:", bg='#241E2B', fg='white')
        self.username_label.place(x= self.width/2 -150, rely=0.4, anchor='e')

        self.username_entry = ttk.Entry(self.canvas, textvariable=self.user, style='Custom.TEntry', width=60)
        self.username_entry.place(x= self.width/2 -150, rely=0.4, anchor='w')

        self.password = tk.StringVar()

        # Password label & entry
        self.password_label = tk.Label(self.canvas, text="Password:", bg='#241E2B', fg='white')
        self.password_label.place(x= self.width/2 - 150, rely=0.5, anchor='e')

        self.password_entry = ttk.Entry(self.canvas, textvariable=self.password, style='Custom.TEntry', width=60, show="*")
        self.password_entry.place(x= self.width/2 - 150, rely=0.5, anchor='w')

        self.password_entry.bind("<Return>", lambda event: self.on_submit())
        login_button = ttk.Button(self.canvas, text="Login", style="Custom.TButton", command=self.on_submit)
        login_button.place(relx=0.45, rely=0.65, anchor='c')

        signup_button = ttk.Button(self.canvas, text="Sign Up", style="Custom.TButton")
        signup_button.place(relx=0.55, rely=0.65, anchor='c')
        signup_button.bind("<Button-1>", lambda event: self.create_tab("Sign Up", SignUpTab, True))     

    def on_submit(self):
        user = query.verify_user(self.user.get(), self.password.get())
        if isinstance(user, str):
            for widget in self.canvas.winfo_children():
                widget.destroy()
            success_label = tk.Label(self.canvas, text="Successfully Logged In!", bg='#241E2B', fg='white', font=('Arial', 14))
            success_label.place(relx=0.5, rely=0.5, anchor='c')
            self.classkeys[self.notebook].user = user
            self.create_tab("Your Projects", UserProjectsTab, True)
        else:
            self.fail_label.config(text="Failed to login")

    def authenticate(self):
        if self.user.get() == "admin" and self.password.get() == "password":
            return True
        return False

    def update_tab(self):
        super().update_tab()
        if self.width != self.frame.winfo_width() and self.frame.winfo_width() >= 1000:
            self.width = self.frame.winfo_width()
            self.username_label.place(x= self.width/2 -150, rely=0.4, anchor='e')
            self.username_entry.place(x= self.width/2 -150, rely=0.4, anchor='w')
            self.password_label.place(x= self.width/2 - 150, rely=0.5, anchor='e')
            self.password_entry.place(x= self.width/2 - 150, rely=0.5, anchor='w')
     
class SignUpTab(AbstractTab):
    def __init__(self, parent, button, tab_canvas, classkeys, select=False):
        super().__init__(parent, button, tab_canvas, classkeys, select)

        self.valid_pass = False
        self.valid_user = False

        self.canvas = tk.Canvas(self.frame, bg='#241E2B', bd=0, highlightthickness=0, width=self.width)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        sign = tk.Label(self.canvas, text="Sign Up", bg='#241E2B', fg='white', font=('Arial', 18, 'bold'))
        sign.place(relx = .5, rely=0.05, anchor='c')

        self.user = tk.StringVar()

        # Username label & entry
        self.username_label = tk.Label(self.canvas, text="Username:", bg='#241E2B', fg='white')
        self.username_label.place(x= self.width/2 -150, rely=0.15, anchor='e')

        self.username_entry = ttk.Entry(self.canvas, textvariable=self.user, style='Custom.TEntry', width=60)
        self.username_entry.place(x= self.width/2 -150, rely=0.15, anchor='w')

        self.password = tk.StringVar()

        # Password label & entry
        self.password_label = tk.Label(self.canvas, text="Password:", bg='#241E2B', fg='white')
        self.password_label.place(x= self.width/2 - 150, rely=0.25, anchor='e')

        self.password_entry = ttk.Entry(self.canvas, textvariable=self.password, style='Custom.TEntry', width=60, show="*")
        self.password_entry.place(x= self.width/2 - 150, rely=0.25, anchor='w')

        self.confirm= tk.StringVar()

        self.confirm_label = tk.Label(self.canvas, text="Confirm Password:", bg='#241E2B', fg='white')
        self.confirm_label.place(x= self.width/2 - 150, rely=0.35, anchor='e')

        self.confirm_entry = ttk.Entry(self.canvas, textvariable=self.confirm, style='Custom.TEntry', width=60, show="*")
        self.confirm_entry.place(x= self.width/2 - 150, rely=0.35, anchor='w')

        self.user.trace_add("write", lambda *args: self.on_var_change(self.user))
        self.confirm.trace_add("write", lambda *args: self.on_var_change(self.confirm))
        self.match = tk.Label(self.canvas, text="Passwords do not match", bg='#241E2B', fg='red')
        self.user_check = tk.Label(self.canvas, text="Looks good! This username is available.", bg='#241E2B', fg='green')

        self.skill_label = tk.Label(self.canvas, text="Your Skills:", bg='#241E2B', fg='white')
        self.skill_label.place(x= self.width/2 - 190, rely=0.46, anchor='e')

        self.skills = tk.Frame(self.canvas, bg='#241E2B', width = self.width/2, height= self.height*.3)
        self.selected_skills = self.checkbox(self.skills, query.get_all_skills(), height = self.height*.3, width = 500)
        self.skills.place(x= self.width/2 - 190, rely= 0.45)

        signup_button = ttk.Button(self.canvas, text="Sign Up", style="Custom.TButton")
        signup_button.place(relx=0.50, rely=0.85, anchor='c')
        signup_button.bind("<Button-1>", lambda event: self.signup() if self.valid_pass and self.valid_user else None)    

    def signup(self):
        skills = self.get_selected(self.selected_skills)
        query.create_user(self.user.get(), self.password.get(), skills)
        self.__del__()

    def update_tab(self):
        super().update_tab()
        if self.width != self.frame.winfo_width():
            self.width = self.frame.winfo_width()
            self.username_label.place(x= self.width/2 -150, rely=0.15, anchor='e')
            self.username_entry.place(x= self.width/2 -150, rely=0.15, anchor='w')
            self.password_label.place(x= self.width/2 - 150, rely=0.25, anchor='e')
            self.password_entry.place(x= self.width/2 - 150, rely=0.25, anchor='w')
            self.confirm_label.place(x= self.width/2 - 150, rely=0.35, anchor='e')
            self.confirm_entry.place(x= self.width/2 - 150, rely=0.35, anchor='w')
            self.skill_label.place(x= self.width/2 - 150, rely=0.4, anchor='e')
            self.skills.place(x= self.width/2 - 150, rely= 0.4)
    
    def on_var_change(self, var):
        if var == self.confirm:
            if self.password.get() != var.get():
                self.match.place(relx = .5, rely=0.30, anchor='c')
                self.valid_pass = False
            else:
                self.valid_pass = True
                self.match.place_forget()
        if var == self.user:
            if query.verify_user(var.get()):
                self.user_check.config(fg='red', text= "Oops! That username is taken. Try another one.")
                self.user_check.place(relx = .5, rely=0.10, anchor='c')
                self.valid_user = False
            else:
                self.user_check.config(fg='green',  text="Looks good! This username is available.")
                self.user_check.place(relx = .5, rely=0.10, anchor='c')
                self.valid_user = True

class ProjectManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x600')
        self.root.minsize(1000,600)
        self.root.title("Project Manager")
        self.root.iconbitmap('GUI_Design/Project_Manager.ico')
        self.root.configure(bg="#2C2634")
        self.root.bind("<Configure>", lambda event: self.update())

        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook', background="#2C2634", borderwidth=0, tabmargins=[0, 0, -1000, 0])
        style.configure('TNotebook.Tab', background="#2C2634", foreground="white", padding=0)
        style.layout('TNotebook.Tab', [])

        self.width = 1000
        self.classkeys = {}
        self.user = None
        
        self.create_header()

        self.notebook = ttk.Notebook(self.root)
        self.classkeys[self.notebook] = self
        ExploreTab(self.notebook, self.create_tab("Explore"), self.tab_canvas, self.classkeys)
        LoginTab(self.notebook, self.create_tab("Login"), self.tab_canvas, self.classkeys, True)

        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.root.mainloop()

    def update(self):
        if self.width != self.root.winfo_width():
            self.width = self.root.winfo_width()
            self.update_scrolling()

    def create_header(self):
        header = tk.Canvas(self.root, bg='#18141D', bd=0, highlightthickness=0, width=1000)
        header.pack(side=tk.TOP, fill=tk.BOTH)

        menu_button = tk.Button(
            header,
            text="☰",
            bg='#18141D',
            activebackground='#2C2634',
            fg='white',
            font=('Arial', 18, 'bold'),
            borderwidth=0,
            highlightthickness=0,
        )
        menu_button.pack(side='right', padx=10, pady=0)

        welcome = tk.Label(header, text="Project Manager", bg='#18141D', fg='white', font=('Arial', 0, 'bold'))
        welcome.pack(side='left', pady =(5, 5), padx= (20,0))

        self.tab_canvas = tk.Canvas(header, bg='#18141D', highlightthickness=0, height=45)
        self.tab_canvas.pack(side='left', fill=tk.X, expand=True)

        self.tab_frame = tk.Frame(self.tab_canvas, bg='#18141D')
        self.tab_canvas.create_window((0,0), window=self.tab_frame, anchor='nw')
        self.bind_mousewheel(self.tab_frame, "<MouseWheel>", self.tab_canvas)
    
    def create_tab(self, label):
        button = tk.Button(
            self.tab_frame,
            text=label,
            bg='#18141D',
            activebackground='#2C2634',  
            fg='#5C596D',
            font=('Arial', 12, 'bold'),
            borderwidth=0,
            highlightthickness=0,
            width = 10 
        )
        button.pack(anchor='w', pady=(10,5), padx=10, side='left')
        self.update_scrolling()
        return button

    def on_mousewheel(self, event, canvas, direction = 'y'):
        """
        This allows the canvas to be scrolled through
        """
        if direction == 'y':
            canvas.yview_scroll(-1*(event.delta//120), "units")
        else:
            canvas.xview_scroll(-1*(event.delta//120), "units")
    
    def unbind_mousewheel_from_children(self, widget, event):
        """Recursively unbind an event from a widget and its children."""
        widget.unbind(event)
        for child in widget.winfo_children():
            self.unbind_mousewheel_from_children(child, event)

    def bind_mousewheel(self, widget, event, canvas):
        widget.bind(event, lambda e, canvas=canvas: self.on_mousewheel(e, canvas, 'x'))
        for child in widget.winfo_children():
            self.bind_mousewheel(child, event, canvas)

    def update_scrolling(self):
        # Force update of pending geometry management tasks
        self.tab_canvas.update_idletasks()
        
        # Calculate the total width of the buttons
        total_width = sum(btn.winfo_width() for btn in self.tab_frame.winfo_children())
        
        # Compare to the width of the tab_canvas
        canvas_width = self.tab_canvas.winfo_width()
        if canvas_width == 1: canvas_width = 757
        
        # Enable or disable scrolling based on the comparison
        if total_width <= canvas_width:
            self.tab_canvas.config(scrollregion=())
            # Unbind the MouseWheel event from tab_canvas and all its children
            self.unbind_mousewheel_from_children(self.tab_canvas, "<MouseWheel>")
        else:
            self.tab_canvas.config(scrollregion=self.tab_canvas.bbox('all'))
            self.bind_mousewheel(self.tab_frame, "<MouseWheel>", self.tab_canvas)

app = ProjectManager()



