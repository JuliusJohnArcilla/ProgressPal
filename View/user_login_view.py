import tkinter as tk
from tkinter import ttk

class userLoginView():
    def __init__(self, root, control)->None:
        
        #INITIALIZE ROOT AND CONTROL
        super(userLoginView, self).__init__()
        self.root = root
        self.control = control
        
    def show(self):
        self.root.title("Welcome to ProgressPal!")
                
        color_background='#2D3033'
        color_rectangle='#868C96'
        
        self.viewFrame = tk.Frame(self.root, background=color_background)
        self.viewFrame.pack(expand=True, fill="both")

        self.f1 = tk.Frame(self.viewFrame, height=25, width=25, background=color_background)
        self.f2 = tk.Frame(self.viewFrame, height=25, width=25, background=color_background)
        self.f3 = tk.Frame(self.viewFrame, height=25, width=25, background=color_background)
        self.f4 = tk.Frame(self.viewFrame, height=25, width=25, background=color_background)
        
        self.bg = tk.Frame(self.viewFrame, background=color_rectangle)
        self.bg.grid(column=1,row=1, sticky='nsew')
        
        self.f1.grid(column=0,row=0)
        self.f2.grid(column=2,row=2)
        self.f3.grid(column=2,row=0)
        self.f4.grid(column=0,row=2)
        
        #VIEW FIELD
        self.viewFrame.grid_columnconfigure((1),weight=1)
        self.viewFrame.grid_rowconfigure((1),weight=1)
        
        #ENTRY FIELD
        self.entryField = tk.Frame(self.viewFrame, background = color_rectangle)
        self.entryField.grid(column=1,row=1, sticky='ns')
        
        #SIGN UP FIELD
        self.SignUpField = tk.Frame(self.entryField, background = color_rectangle)
        self.SignUpField.grid(row=5, column=1)
        
        #LABEL
        self.Signin_Label = tk.Label(self.entryField, text= "Sign in", 
                                      background=color_rectangle,
                                      anchor='n',
                                      font=('Montserrat', 30))
        self.Description_Label = tk.Label(self.entryField, text = "Sign in now and start\norganizing your schedule.",
                                      background=color_rectangle,
                                      font=('Montserrat', 12))
        
        #ENTRY FIELDS
        self.Username_Entry = ttk.Entry(self.entryField,width=25,
                                       font=('Montserrat', 15),
                                       foreground='black',
                                       )
        
        self.Password_entry = ttk.Entry(self.entryField,width=25,
                                        font=('Montserrat', 15),
                                        foreground='black',
                                        )
        
        #INSERT
        self.Username_Entry.insert(0,'Username')
        self.Password_entry.insert(0,'Password')
        
        #CONFIGURE
        self.Username_Entry.config(state='disabled')
        self.Password_entry.config(state='disabled')
        
        #BUTTONS
        self.Login_Button = tk.Button(self.entryField, text = "Login", command = self.LoginButton,
                                      font=('Montserrat', 15),
                                      background=color_background,
                                      foreground='white',
                                      width=20)
        self.SignUp_Label = tk.Label(self.SignUpField, text = "New to ProgressPal?",
                                     font=('Montserrat',15),
                                     background=color_rectangle)
        self.SignUp_Button = tk.Label(self.SignUpField, text = "Sign Up",
                                      cursor='hand2',
                                      background=color_rectangle,
                                      foreground='blue',
                                      font=('Montserrat',15,'underline'))
        self.ForgotPassword_Button = tk.Label(self.entryField, text="Forgot Password",
                                              font=('Montserrat',15,'underline'),
                                              background=color_rectangle,
                                              foreground='blue',
                                              cursor='hand2')
        
        #LABEL IMPLEMENT
        self.Signin_Label.grid(row=0,column=1,
                                pady=(150,0))
        self.Description_Label.grid(row=1,column=1,
                                pady=(15,25))
        self.SignUp_Label.grid(row=0,column=0)
        
        
        #ENTRY FIELDS IMPLEMENTATION
        self.Username_Entry.grid(row=2,column=1,
                                pady=(0,10))
        self.Password_entry.grid(row=3,column=1,
                                 pady=(0,25))
        
        #BUTTON IMPLEMENT
        self.Login_Button.grid(row=4,column=1, pady=(0,12))
        self.SignUp_Button.grid(row=0,column=1)
        self.ForgotPassword_Button.grid(row=6,column=1)
        
        #BIND
        self.Username_Entry.bind('<Button-1>', lambda x: self.on_focus_in(self.Username_Entry, "Username"))
        self.Username_Entry.bind('<FocusOut>', lambda x: self.on_focus_out(self.Username_Entry, "Username"))
        self.Password_entry.bind('<Button-1>', lambda x: self.on_focus_in_pass(self.Password_entry, "Password"))
        self.Password_entry.bind('<FocusOut>', lambda x: self.on_focus_out_pass(self.Password_entry, "Password"))
        self.SignUp_Button.bind('<Button-1>', lambda x: self.switchViewSignUp())
        self.ForgotPassword_Button.bind('<Button-1>', lambda x: self.switchForgetPassword())
                        
        self.root.mainloop()
    
    def back(self):
        self.root.destroy()
        self.control.previous()
        pass

    
    def on_focus_in(self, entry, placeholder):
        if entry.cget('state') != 'normal':
            entry.configure(state='normal')
            if entry.get() != "": 
                if entry.get() != placeholder:
                    return
                else:
                    entry.delete(0,'end')
            else:
                entry.delete(0, 'end')


    def on_focus_out(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.configure(state='disabled')

    def on_focus_in_pass(self, entry, placeholder):
        if entry.cget('state') != 'normal':
            entry.configure(state='normal', show='*')
            if entry.get() != "": 
                if entry.get() != placeholder:
                    return
                else:
                    entry.delete(0,'end')
            else:
                entry.delete(0, 'end')

    def on_focus_out_pass(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.configure(state='disabled', show='')
    
    def LoginButton(self):
        try:
            self.checkDatabase()
        except:
            print("Invalid Username or Password.")
            return
    
    def switchViewMainMenu(self):
        self.viewFrame.destroy()
        self.control.switchViewMain()
    
    def switchViewSignUp(self):
        self.viewFrame.destroy() 
        self.control.switchViewSignUp()
    
    def switchForgetPassword(self):
        self.viewFrame.destroy()
        self.control.switchViewForgetPassword()
    
    def checkDatabase(self):
        username = self.Username_Entry.get()
        password = self.Password_entry.get()
        
        if(len(self.control.model.getUser(username))>0):
            if(password == self.control.model.getPassword(self.control.model.getUser(username))):
                if(self.control.model.run_comparison(username, password)):
                    self.switchViewMainMenu()
                
        
    
        
if __name__ == "__main__":
    sample_root = tk.Tk() 
    sample_control = ""
    program = userLoginView(sample_root, sample_control)
    program.show()
    
#OLD CODES

    # self.Username_Label = tk.Label(self.entryField, text = "Username:")
    # 
    # self.Password_Label = tk.Label(self.entryField, text = "Password: ")
    # self.Password_Label.grid(row=2,column=0)
    # self.SignUp_Label = tk.Label(self.entryField, text="New User? Click here!", cursor = 'hand2')
    # self.SignUp_Label.grid(row=4,columnspan=2)
    # self.ForgetPassword_Label = tk.Label(self.entryField, text = "Forget Password?", cursor='hand2')
    # self.ForgetPassword_Label.grid(row=5, columnspan=2)        

    # #CONFIGS
    # self.ForgetPassword_Label.configure(anchor='center')
    # self.ForgetPassword_Label.bind('<Button-1>', lambda x: self.forget_password())

    # #ENTRY
    # self.Username_Entry = ttk.Entry(self.entryField)
    # self.Username_Entry.grid(row=1, column=1)
    # self.Password_Entry = ttk.Entry(self.entryField)
    # self.Password_Entry.grid(row=2,column=1)

    # #BUTTON
    # self.Login_button = ttk.Button(self.entryField, text = "Login", command = self.implement)#self.control.LoginAction(self.Username_Entry.get(), self.Password_Entry.get()))
    # self.Login_button.grid(row=3, columnspan=2) 

    # self.back_button = ttk.Button(self.entryField, text = "Back", command = self.implement)             
    # self.back_button.grid(row=5,column=1, sticky='e')