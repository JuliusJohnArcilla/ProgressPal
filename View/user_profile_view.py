import tkinter as tk

class UserProfileView:
    def __init__(self, root, control)->None:
        self.root = root
        self.control = control
        self.count = 0 
        
        
    def show(self):
        self.root.title("ProgressPal: Profile")
        
        #COLORS
        self.window_color = '#333333'
        self.toggle_color = '#BBBBBB'
        self.screen_color = '#888888'
        
        #WINDOW
        self.window = tk.Frame(self.root, background=self.window_color)
        self.window.pack(fill='both',expand=True)
        
        self.screen = tk.Frame(self.window, background=self.screen_color)
        self.screen.pack(fill='both', expand=True, padx=25, pady=25)
        
        self.screen.grid_columnconfigure((1), weight=1)
        self.screen.grid_rowconfigure((1), weight=1)
        
        #EMPTY FRAMES
        self.empty1 = tk.Frame(self.screen, width = 25, height = 25, background=self.screen_color)
        self.empty2 = tk.Frame(self.screen, width = 25, height = 25, background=self.screen_color)
        self.empty3 = tk.Frame(self.screen, width = 25, height = 25, background=self.screen_color)
        self.empty4 = tk.Frame(self.screen, width = 25, height = 25, background=self.screen_color)
        
        #EMPTY FRAMES IMPLEMENTATION
        self.empty1.grid(column=0,row=0)
        self.empty2.grid(column=2,row=0)
        self.empty3.grid(column=0,row=2)
        self.empty4.grid(column=2,row=2)
        
        #PROFILE LABELS
        self.Name_Label = tk.Label(self.screen, text = 'Name', 
                                   font=('Montserrat', 12))
        self.Email_Label = tk.Label(self.screen, text = 'Email', 
                                   font=('Montserrat', 12))
        self.Username_Label = tk.Label(self.screen, text = 'Username', 
                                   font=('Montserrat', 12))
        self.Password_Label = tk.Label(self.screen, text = 'Password', 
                                   font=('Montserrat', 12))
        
        #USER LABELS
        self.User_Name_Label = tk.Label(self.screen, font = ('Montserrat', 12), text = '****************')
        self.User_Email_Label = tk.Label(self.screen, font = ('Montserrat', 12), text = '****************')
        self.User_Username_Label = tk.Label(self.screen, font = ('Montserrat', 12), text = '****************')
        self.User_Password_Label = tk.Label(self.screen, font = ('Montserrat', 12), text = '****************')
        
        #LABEL IMPLEMENTATION
        self.Name_Label.grid(sticky='n', column=1,row=1, pady=(125, 25), padx = (100, 221))
        self.Email_Label.grid(sticky='n', column=1,row=1, pady=(163, 0), padx = (100, 221))
        self.Username_Label.grid(sticky='n', column=1,row=1, pady=(201, 0), padx = (100, 250))
        self.Password_Label.grid(sticky='n', column=1,row=1, pady=(239, 25), padx = (100, 250))
        
        self.User_Name_Label.grid(sticky='nw', column=1,row=1, pady = (125, 25), padx = (300,75))
        self.User_Email_Label.grid(sticky='nw', column=1,row=1, pady = (163, 0), padx = (300,75))
        self.User_Username_Label.grid(sticky='nw', column=1,row=1, pady = (201, 0), padx = (300,75))
        self.User_Password_Label.grid(sticky='nw', column=1,row=1, pady = (239, 0), padx = (300,75))
        
        #TOGGLE SCREEN
        self.toggleButtonOpen = tk.Button(self.root, text='>', width=4, height=2, command = self.toggleMenu, background=self.toggle_color, border = 0)
        self.toggleButtonOpen.place(x=5,y=5)
        
        #VIEW BUTTON
        self.viewbutton = tk.Button(self.screen, text = 'V I E W', height=2, command= self.viewButton, background=self.screen_color, border=0)
        self.viewbutton.grid(sticky='nwe', column=1, row=1, pady=(75,25))
        self.root.mainloop()
        
    def toggleMenu(self):
        
        #TOGGLE MENU
        self.toggleMenuFrame = tk.Frame(self.root, width = 400, height = 750, background=self.toggle_color)
        
        def ToggleClose():
            self.toggleMenuFrame.destroy()
        
        def ToggleButtons(x, y, name, bcolor, cmd):
            toggleButton = tk.Button(self.toggleMenuFrame, text = name, 
                                     width = 65, height = 3, 
                                     background = bcolor, 
                                     foreground = self.window_color, 
                                     command = cmd, 
                                     border=0,
                                     font=('Montserrat',8))
            
            toggleButton.place(x=x,y=y)
        
        def placeholdercmd():
            ToggleClose()
            pass
        
        #TOGGLE BUTTON
        self.toggleButtonClose = tk.Button(self.toggleMenuFrame, text='<', width=4, height=2, command = ToggleClose, background=self.toggle_color, border = 0)
        self.toggleMenu1 = ToggleButtons(0,80, name='H O M E', bcolor=self.toggle_color, cmd=self.SwitchViewHome)
        self.toggleMenu2 = ToggleButtons(0,131, name='M A N A G E   T A S K', bcolor=self.toggle_color, cmd=self.SwitchViewTasks)
        self.toggleMenu3 = ToggleButtons(0,182, name='S C H E D U L E', bcolor=self.toggle_color, cmd=self.switchViewSchedule)
        self.toggleMenu4 = ToggleButtons(0,233, name='P R O F I L E', bcolor=self.toggle_color, cmd=ToggleClose)


        #IMPLEMENTATION
        self.toggleMenuFrame.place(x=0,y=0)
        self.toggleButtonClose.place(x=5,y=5)
        
    def SwitchViewHome(self):
        self.window.destroy()
        self.toggleMenuFrame.destroy()
        self.control.switchViewHome()
    
    def SwitchViewTasks(self):
        self.window.destroy()
        self.toggleMenuFrame.destroy()
        self.control.switchViewTasks()
        
    def switchViewSchedule(self):
        self.window.destroy()
        self.toggleMenuFrame.destroy()
        self.control.switchViewSchedule()

    
    def viewButton(self):
        
        #LABEL CONFIGURATIONS
        
        if(self.count == 0):
            self.User_Name_Label.configure(text = self.control.model.getName(self.control.model.loginUser))
            self.User_Email_Label.configure(text = self.control.model.searchEmail(self.control.model.loginUser))
            self.User_Username_Label.configure(text = self.control.model.getUser(self.control.model.loginUser))
            self.User_Password_Label.configure(text = self.control.model.getPassword(self.control.model.loginUser))
            self.count = 1
            self.viewbutton.configure(text = 'H I D E')
        elif(self.count == 1):
            self.User_Name_Label.configure(text = '****************')
            self.User_Email_Label.configure(text = '****************')
            self.User_Username_Label.configure(text = '****************')         
            self.User_Password_Label.configure(text = '****************')
            self.count = 0
            self.viewbutton.configure(text = 'V I E W')
        
        
        
if __name__ == '__main__':
    sample_root = tk.Tk()
    sample_program = UserProfileView(sample_root, None)
    sample_program.root.geometry("750x750")
    sample_program.show()