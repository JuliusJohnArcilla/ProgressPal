import tkinter as tk
from tkinter import ttk

class mainMenu:
    def __init__(self, root, control)->None:
        
        #DEFINE ROOT AND CONTROL
        super(mainMenu, self).__init__()
        self.root = root
        self.control = control
    
    def show(self):
        self.root.title("ProgressPal: Main Menu")
    
        self.color_background='#2D3033'
        self.color_toggleMenu='#868C96'
        self.color_mainScreen ='black'
        
        self.root.configure(background = self.color_background)
        
        #TOGGLE MENU
        self.mainScreenFrame = tk.Frame(self.root, background=self.color_mainScreen)
        
        #FRAME IMPLEMENTATION
        self.mainScreenFrame.pack(expand=True, fill='both')
        
        #LABELS
        
        #BUTTONS
        self.toggleButtonOpen = tk.Button(self.mainScreenFrame, text='>', width=4, height=2, command = self.toggleMenu, background=self.color_toggleMenu, border = 0)
        
        #BUTTON IMPLEMENTATION
        self.toggleButtonOpen.place(x=5,y=5)
        
        self.root.mainloop()
    
    def toggleMenu(self):
        
        #TOGGLE MENU
        self.toggleMenuFrame = tk.Frame(self.root, width = 400, height = 750, background=self.color_toggleMenu)
        
        def ToggleClose():
            self.toggleMenuFrame.destroy()
        
        def ToggleButtons(x, y, name, bcolor, cmd):
            toggleButton = tk.Button(self.toggleMenuFrame, text = name, 
                                     width = 65, height = 3, 
                                     background = bcolor, 
                                     foreground = self.color_background, 
                                     command = cmd, 
                                     border=0,
                                     font=('Montserrat',8))
            
            toggleButton.place(x=x,y=y)
        
        def placeholdercmd():
            ToggleClose()
            pass
        
        #TOGGLE BUTTON
        self.toggleButtonClose = tk.Button(self.toggleMenuFrame, text='<', width=4, height=2, command = ToggleClose, background=self.color_toggleMenu, border = 0)
        self.toggleMenu1 = ToggleButtons(0,80, name='S C H E D U L E', bcolor=self.color_toggleMenu, cmd=placeholdercmd)
        self.toggleMenu2 = ToggleButtons(0,131, name='M A N A G E   T A S K', bcolor=self.color_toggleMenu, cmd=placeholdercmd)
        self.toggleMenu3 = ToggleButtons(0,182, name='P R O F I L E', bcolor=self.color_toggleMenu, cmd=placeholdercmd)
        
        #IMPLEMENTATION
        self.toggleMenuFrame.place(x=0,y=0)
        self.toggleButtonClose.place(x=5,y=5)
    
    
    
        
        

    
if __name__ == '__main__':
    sample = tk.Tk()
    program = mainMenu(root=sample, control=None)
    program.show()
