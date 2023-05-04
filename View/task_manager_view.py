import tkinter as tk
from tkinter import ttk
import tkcalendar as tkc

class TaskManagerView:
    def __init__(self, root, control)->None:
        super(TaskManagerView, self).__init__()
        self.root = root
        self.control = control
        
    def show(self):
        self.root.title("Task Manager")
        
        self.color_background='#2D3033'
        self.color_toggleMenu='#868C96'
        self.color_mainScreen ='black'
        self.color_rectangle = '#636E72'
        self.color_button = '#B2BEC3'
        
        #TOGGLE MENU
        self.mainScreenFrame = tk.Frame(self.root, background=self.color_mainScreen)
        self.viewField = tk.Frame(self.mainScreenFrame, background = self.color_rectangle, )
        
        #FRAME IMPLEMENTATION
        self.mainScreenFrame.pack(expand=True, fill='both')
        self.viewField.grid(column=1,row=1, sticky='nsew')
        
        #FILLERS
        self.m1 = tk.Frame(self.mainScreenFrame, background=self.color_mainScreen, width=25, height=25)
        self.m2 = tk.Frame(self.mainScreenFrame, background=self.color_mainScreen, width=25, height=25)
        self.m3 = tk.Frame(self.mainScreenFrame, background=self.color_mainScreen, width=25, height=25)
        self.m4 = tk.Frame(self.mainScreenFrame, background=self.color_mainScreen, width=25, height=25)
        self.v1 = tk.Frame(self.viewField, background=self.color_rectangle, width=25, height=25)
        self.v2 = tk.Frame(self.viewField, background=self.color_rectangle, width=25, height=25)
        self.v3 = tk.Frame(self.viewField, background=self.color_rectangle, width=25, height=25)
        self.v4 = tk.Frame(self.viewField, background=self.color_rectangle, width=25, height=25)
        
        #FILLER IMPLEMENTATION
        self.m1.grid(column=0,row=0)
        self.m2.grid(column=0,row=2)
        self.m3.grid(column=2,row=0)
        self.m4.grid(column=2,row=2)
        
        self.v1.grid(column=0,row=0)
        self.v2.grid(column=0,row=2)
        self.v3.grid(column=2,row=0)
        self.v4.grid(column=2,row=2)
        
        #widgetField
        self.widgetFrame = tk.Frame(self.viewField, background=self.color_rectangle)
        self.widgetFrame.grid(column=1,row=1,sticky='nsew')
        
        self.MenuControlFrame = tk.Frame(self.widgetFrame, background = self.color_rectangle)
        self.MenuControlFrame.grid(column=0, row=0, sticky='nsew')
        
        self.mainFrame = tk.Frame(self.widgetFrame, background=self.color_rectangle)
        self.mainFrame.grid(column=1, row=0, sticky='nsew')
        
        #FRAME CONFIGS
        self.mainScreenFrame.grid_columnconfigure((1),weight=1)
        self.mainScreenFrame.grid_rowconfigure((1),weight=1)
        self.viewField.grid_columnconfigure((1),weight=1)
        self.viewField.grid_rowconfigure((1),weight=1)
        self.MenuControlFrame.grid_columnconfigure((1), weight=1)
        
        #LABEL
        self.PriorityLabel = tk.Label(self.MenuControlFrame, font=('Montserrat', 14, 'bold'), text='Priority', background=self.color_rectangle)
        self.CalendarLabel = tk.Label(self.MenuControlFrame, font=('Montserrat', 13, 'bold'), text = 'Please choose a deadline', background=self.color_rectangle)
        
        #ENTRY FIELDS
        self.TaskNameEntryField = tk.Entry(self.MenuControlFrame, font=('Montserrat', 20), width = 16)
        self.DescriptionEntryField = tk.Text(self.MenuControlFrame, width = 30, height= 6, background = self.color_rectangle, borderwidth=1)
        self.PriorityEntryField = tk.Entry(self.MenuControlFrame, font=('Montserrat', 15), width = 2)
        
        #BUTTONS
        self.toggleButtonOpen = tk.Button(self.mainScreenFrame, text='>', width=4, height=2, command = self.toggleMenu, background=self.color_toggleMenu, border = 0)
        self.AddTaskButton = tk.Button(self.MenuControlFrame, text = 'Add Task', width=20, height=1,
                                       font=('Montserrat', 14, 'bold'), border=0,background=self.color_background, foreground=self.color_rectangle)
        self.CalendarButton = tk.Button(self.MenuControlFrame, text = '📅', command = self.calendarPicker, background=self.color_rectangle, border=1)
        self.RemoveTaskButton = tk.Button(self.mainFrame, text = 'Remove Task', width=32, height=1,
                                       font=('Montserrat', 14, 'bold'), border=0,background=self.color_background, foreground=self.color_rectangle)
        
        #LIST BOX
        self.TaskList = tk.Listbox(self.mainFrame, width=30, height=50,
                                   font=("Montserrat", 18), border=0, 
                                   foreground='#464646', highlightthickness=0,
                                   selectbackground='#a6a6a6', activestyle="none")
        
        
        #LIST BOX IMPLEMENTATION
        self.TaskList.grid(column=1,row=1,sticky='nsew', padx=(25,0))
        
        #LABEL IMPLEMENTATION
        self.PriorityLabel.grid(column=0,row=4, sticky='w', pady=(0,5), padx=(0,0))
        self.CalendarLabel.grid(column=0,row=3, sticky='w', pady=(5,5), padx = (30,0))
        
        #ENTRY IMPLEMENTATION
        self.TaskNameEntryField.grid(column=0,row=1, sticky='w', pady=(0,5))
        self.DescriptionEntryField.grid(column=0, row=2, sticky='w', pady=(0,5))
        self.PriorityEntryField.grid(column=0, row=4, sticky='w', pady=(0,5), padx=(80,0))

        #BUTTON IMPLEMENTATION
        self.toggleButtonOpen.place(x=5,y=5)
        self.AddTaskButton.grid(column=0, row=0, sticky='w', pady=(0,5))
        self.CalendarButton.grid(column=0, row=3, sticky='w', pady=(1,0))
        self.RemoveTaskButton.grid(column=1,row=0, pady=(0,5), stick='n', padx=(25,0))
        
        self.root.mainloop()
        
    def calendarPicker(self):
        self.calendarWindow = tk.Toplevel()    
        self.calendarWindow.grab_set()
        self.calendarWindow.title("Set Deadline:")
        self.calendarWindow.geometry("250x220+590+370")
        self.cal = tkc.Calendar(self.calendarWindow, selectmode="day", date_pattern="mm/dd/y")
        self.cal.place(x=0,y=0)
        
        submitButton = tk.Button(self.calendarWindow, text = "Submit", command = self.grabDate)
        submitButton.place(x=80, y=190)
    
    def grabDate(self):
        self.CalendarLabel.configure(text=self.cal.get_date())
        self.calendarWindow.destroy()
        
    def ToggleClose(self):
        self.toggleMenuFrame.destroy()
    
    def switchViewMainMenu(self):
        self.mainScreenFrame.destroy()
        self.toggleMenuFrame.destroy()
        self.control.switchViewMainMenu()
    
    def toggleMenu(self):
        
        #TOGGLE MENU
        self.toggleMenuFrame = tk.Frame(self.root, width = 400, height = 750, background=self.color_toggleMenu)
        
        def ToggleButtons(x, y, name, bcolor, cmd):
            toggleButton = tk.Button(self.toggleMenuFrame, text = name, 
                                     width = 65, height = 3, 
                                     background = bcolor, 
                                     foreground = self.color_background, 
                                     command = cmd, 
                                     border=0,
                                     font=('Montserrat',8))
            
            toggleButton.place(x=x,y=y)
        
        def placeholdercmd(self):
            self.ToggleClose()
            pass
        
        #TOGGLE BUTTON
        self.toggleButtonClose = tk.Button(self.toggleMenuFrame, text='<', width=4, height=2, command = self.ToggleClose, background=self.color_toggleMenu, border = 0)
        self.toggleMenu1 = ToggleButtons(0,80, name='H O M E', bcolor=self.color_toggleMenu, cmd= self.switchViewMainMenu)
        self.toggleMenu2 = ToggleButtons(0,131, name='M A N A G E   T A S K', bcolor=self.color_toggleMenu, cmd=self.ToggleClose)
        self.toggleMenu3 = ToggleButtons(0,182, name='S C H E D U L E', bcolor=self.color_toggleMenu, cmd=self.switchViewSchedule)
        self.toggleMenu4 = ToggleButtons(0,233, name='P R O F I L E', bcolor=self.color_toggleMenu, cmd=self.switchViewProfile)
        
        #IMPLEMENTATION
        self.toggleMenuFrame.place(x=0,y=0)
        self.toggleButtonClose.place(x=5,y=5)
        
    def switchViewProfile(self):
        self.mainScreenFrame.destroy()
        self.toggleMenuFrame.destroy()
        self.control.switchViewProfile()
    
    def switchViewSchedule(self):
        self.mainScreenFrame.destroy()
        self.toggleMenuFrame.destroy()
        self.control.switchViewSchedule()
        
if __name__ == '__main__':
    sampleRoot = tk.Tk()
    sampleProg = TaskManagerView(sampleRoot, None)
    sampleProg.root.geometry("750x750")
    sampleProg.show()