import tkinter as tk

class welcomeView():
    def __init__(self, root, control=None)->None:
        self.root = root
        self.control = control
        
    def show(self):
        self.root.title("Welcome to ProgressPal!")
        self.root.geometry("400x500")
        
        self.view = tk.Frame(self.root)
        self.view.pack()
        
        #LABEL
        self.field = tk.LabelFrame(self.view, text = "Welcome to ProgressPal!\nWe are glad to have you join us!")
        self.field.grid(row=0,column=0)
        
        #BUTTONS
        self.login = tk.Button(self.field, text = "Login", command = self.login_action)
        self.login.grid(row=0, column=0)
        self.register = tk.Button(self.field, text = "Register", command = self.register_action)
        self.register.grid(row=0,column=1)
        
        self.root.mainloop()
        
    def login_action(self):
        self.root.withdraw()
        self.control.show()
        
    def register_action(self):
        self.control.gotoreg()
        
        
if __name__ == '__main__':
    sample_root = tk.Tk()
    sample_control = ""
    program = welcomeView(sample_root, sample_control)
    program.show()