import tkinter as tk
from tkinter import ttk

class taskView:
    def __init__(self, root, control)->None:
        super(taskView, self).__init__()
        self.root = root
        self.control = control
    
    def show(self):
        #SCREEN WIDTH AND HEIGHT
        Width = self.root.winfo_screenwidth()
        Height = self.root.winfo_screenheight()
        
        
        #GET RID OF TITLE BAR AND BUTTONS
        self.root.overrideredirect(True)
        
        #WINDOW CONFIGURATIONS
        self.root.geometry("%sx%s+%s+%s" % (300, 600,Width-310,10))
        self.root.resizable(True, True)
        
        #TURN WINDOW TO CANVAS
        self.viewWindow = tk.Canvas(self.root)
        self.viewWindow.pack()
        
        #GRIDS
        self.gridView = tk.LabelFrame(self.viewWindow)
        self.gridView.grid()
        
        #TASKS
        self.task = tk.StringVar()
        self.task_entry = tk.Entry(self.gridView)
        self.task_entry.grid(row=0,column=0)
        self.task_entry.focus
        
        #TASKLIST
        self.taskList = tk.Listbox(self.viewWindow)
        self.taskList.grid()
        
        
        
        
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    sample = ""
    program = taskView(root, sample)
    program.show()