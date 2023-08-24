from Tabs import *

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