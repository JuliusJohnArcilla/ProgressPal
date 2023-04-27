import tkinter as tk
from tkinter import ttk
import webbrowser as wb

class userLoginView():
    def __init__(self, root, control)->None:
        
        #INITIALIZE ROOT AND CONTROL
        super(userLoginView, self).__init__()
        self.root = root
        self.control = control
        
    def show(self):
        self.root.title("Login")
        self.root.geometry("400x500")
        r = 0
        c = 0
        
        self.viewFrame = tk.Frame(self.root)
        self.viewFrame.pack()
        
        self.entryField = tk.LabelFrame(self.viewFrame) 
        self.entryField.pack(pady=(100,0))
        
        #LABEL
        self.Welcome_Label = tk.Label(self.entryField, text= "Welcome back to ProgressPal!", anchor= 'center').grid(row=0,columnspan=2)
        self.Username_Label = tk.Label(self.entryField, text = "Username:")
        self.Username_Label.grid(row = 1, column = 0)
        self.Password_Label = tk.Label(self.entryField, text = "Password: ")
        self.Password_Label.grid(row=2,column=0)
        self.ForgetPassword_Label = tk.Label(self.entryField, text = "Forget Password?", cursor='hand2')
        self.ForgetPassword_Label.grid(row=4, columnspan=2)
        
        
        #CONFIGS
        self.ForgetPassword_Label.configure(anchor='center')
        self.ForgetPassword_Label.bind('<Button-1>', lambda x: self.forget_password())
     
        
        #ENTRY
        self.Username_Entry = ttk.Entry(self.entryField)
        self.Username_Entry.grid(row=1, column=1)
        self.Password_Entry = ttk.Entry(self.entryField)
        self.Password_Entry.grid(row=2,column=1)
        
        #BUTTON
        self.Login_button = ttk.Button(self.entryField, text = "Login", command = self.control.LoginAction(self.Username_Entry.get(), self.Password_Entry.get()))
        self.Login_button.grid(row=3, columnspan=2) 
        
        self.back_button = ttk.Button(self.entryField, text = "Back", command = self.back())             
        self.back_button.grid(row=5,column=1, sticky='e')
        self.root.mainloop()
    
    def back(self):
        self.root.destroy()
        self.control.previous()
        pass

if __name__ == "__main__":
    sample_root = tk.Tk() 
    sample_control = ""
    program = userLoginView(sample_root, sample_control)
    program.show()