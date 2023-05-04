import tkinter as tk
from tkinter import ttk
import re 

class userRegisterView():
    def __init__(self, root, control)->None:
        
        #ROOT AND CONTROL
        super(userRegisterView, self).__init__()
        self.root = root
        self.control = control
        
    def show(self):
        self.root.title("ProgressPal: Sign Up")

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
        
        #FRAME IN VIEW FRAME
        self.FrameinFrame = tk.Frame(self.viewFrame, background=color_rectangle)
        self.FrameinFrame.grid(row=1,column=1, sticky='nsew')

        self.ff1 = tk.Frame(self.FrameinFrame, height=25, width=25, background=color_rectangle)
        self.ff2 = tk.Frame(self.FrameinFrame, height=25, width=25, background=color_rectangle)
        self.ff3 = tk.Frame(self.FrameinFrame, height=25, width=25, background=color_rectangle)
        self.ff4 = tk.Frame(self.FrameinFrame, height=25, width=25, background=color_rectangle)
        
        self.bg = tk.Frame(self.FrameinFrame, background=color_rectangle)
        self.bg.grid(column=1,row=1, sticky='nsew')
        
        self.ff1.grid(column=0,row=0)
        self.ff2.grid(column=2,row=2)
        self.ff3.grid(column=2,row=0)
        self.ff4.grid(column=0,row=2)
        
        #FRAME CONFIGURATIONS

        self.viewFrame.grid_columnconfigure((1),weight=1)
        self.viewFrame.grid_rowconfigure((1),weight=1)  
        self.FrameinFrame.grid_columnconfigure((1),weight=1)
        self.FrameinFrame.grid_rowconfigure((1),weight=1)              
        
        #ENTRY FIELD
        self.entryField = tk.Frame(self.FrameinFrame, background=color_rectangle)
        self.entryField.grid(column=1,row=1, sticky='ns')
        
        #NAME FIELD
        self.nameField = tk.Frame(self.entryField, background=color_rectangle)
        self.nameField.grid(row=1,column=0)
        
        #LABELS
        self.Header = tk.Label(self.entryField, text = "Create Account",
                               font = ('Montserrat', 24),
                               anchor='center', width=15)
        
        #PADDING
        self.padx = (5,0)
        self.pady = (10,0)
        self.namex = (5,0)
        
        #LABEL IMPLEMENTATION
        self.Header.grid(row=0,column=0,
                         pady=(125, 25),
                         columnspan=2)

        #ENTRY FIELD
        self.choice = tk.StringVar()
        self.lastName_entry = ttk.Entry(self.nameField, 
                                        font=('Montserrat',12),
                                        width=15,
                                        )
        self.firstName_entry = ttk.Entry(self.nameField, 
                                        font=('Montserrat',12),
                                        width=15,
                                        )
        self.UseType_choice1 = tk.Radiobutton(self.nameField, text = 'Business', 
                                              variable=self.choice, 
                                             font=('Montserrat',12),
                                             value='Business', width=12)
        self.UseType_choice2 = tk.Radiobutton(self.nameField, text = 'Personal', 
                                              variable=self.choice,
                                              font=('Montserrat, 12',12),
                                              value='Personal', width=12)
        self.email_entry = ttk.Entry(self.entryField,
                                     font=('Montserrat',12),
                                     width=31)
        self.Username_entry = ttk.Entry(self.entryField,
                        font=('Montserrat',12),
                        width=31)
        self.Password_entry = ttk.Entry(self.entryField,
                        font=('Montserrat',12),
                        width=31)
        self.Password_reentry = ttk.Entry(self.entryField,
                                     font=('Montserrat',12),
                                     width=31)
        
        #BUTTONS
        self.back_button = tk.Button(self.FrameinFrame, text = '<',
                                     width=4, height=2, command = self.back)
        self.signup_button = tk.Button(self.entryField, text= "Sign Up",
                                       font=('Montserrat', 12),
                                       width=31, command = self.Register)
        
        #INSERT
        self.lastName_entry.insert(0,"Last Name")
        self.firstName_entry.insert(0,"First Name")
        self.email_entry.insert(0,"Email Address")
        self.Username_entry.insert(0,"Username")
        self.Password_entry.insert(0,"Enter Password")
        self.Password_reentry.insert(0,"Re-enter Password")
        
        #CONFIGURE
        self.lastName_entry.config(state='disabled')
        self.firstName_entry.config(state='disabled')   
        self.email_entry.config(state='disabled')
        self.Username_entry.config(state='disabled')
        self.Password_entry.config(state='disabled')
        self.Password_reentry.config(state='disabled')
        
        #ENTRY FIELD IMPLEMENTATION
        self.lastName_entry.grid(row=0,
                                 column=1,
                                 pady=self.pady,
                                 padx=self.namex,)
        self.firstName_entry.grid(row=0,
                                 column=0,
                                 pady=self.pady,
                                 padx=self.namex,)
        self.email_entry.grid(row=3,
                              column=0,
                              pady=self.pady,
                              padx=self.padx)
        self.Username_entry.grid(row=4,
                              column=0,
                              pady=self.pady,
                              padx=self.padx)
        self.Password_entry.grid(row=5,
                              column=0,
                              pady=self.pady,
                              padx=self.padx)
        self.Password_reentry.grid(row=6,
                              column=0,
                              pady=self.pady,
                              padx=self.padx)
        
        #CHOICE IMPLEMENTATION
        self.UseType_choice1.grid(row=2,
                                 column=0,
                                 pady=self.pady,
                                 padx=self.padx,
                                 sticky='w')
        self.UseType_choice2.grid(row=2,
                                 column=1,
                                 pady=self.pady,
                                 padx=self.padx,
                                 sticky='w')
        
        #BUTTON IMPLEMENTATION
        self.back_button.grid(column=0,row=0,
                              sticky='w',
                              padx=5,
                              pady=5)
        self.signup_button.grid(row=7,
                                column=0,
                                pady=self.pady,
                                padx=self.padx)
        
        #BINDS
        self.lastName_entry.bind('<Button-1>', lambda x: self.on_focus_in(self.lastName_entry, "Last Name"))
        self.lastName_entry.bind('<FocusOut>', lambda x: self.on_focus_out(self.lastName_entry, "Last Name"))
        self.firstName_entry.bind('<Button-1>', lambda x: self.on_focus_in(self.firstName_entry, "First Name"))
        self.firstName_entry.bind('<FocusOut>', lambda x: self.on_focus_out(self.firstName_entry, "First Name"))
        self.email_entry.bind('<Button-1>', lambda x: self.on_focus_in(self.email_entry, "Email Address"))
        self.email_entry.bind('<FocusOut>', lambda x: self.on_focus_out(self.email_entry, "Email Address"))
        self.Username_entry.bind('<Button-1>', lambda x: self.on_focus_in(self.Username_entry, "Username"))
        self.Username_entry.bind('<FocusOut>', lambda x: self.on_focus_out(self.Username_entry, "Username"))
        self.Password_entry.bind('<Button-1>', lambda x: self.on_focus_in_pass(self.Password_entry, "Enter Password"))
        self.Password_entry.bind('<FocusOut>', lambda x: self.on_focus_out_pass(self.Password_entry, "Enter Password"))
        self.Password_reentry.bind('<Button-1>', lambda x: self.on_focus_in_pass(self.Password_reentry, "Re-enter Password"))
        self.Password_reentry.bind('<FocusOut>', lambda x: self.on_focus_out_pass(self.Password_reentry, "Re-enter Password"))       
        
        self.root.mainloop()
    
    
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
    
    def back(self):
        self.viewFrame.destroy()
        self.control.switchViewLogin()
  
    def Register(self):
        if(self.Validate(self.email_entry.get(), self.Password_entry.get(), self.Password_reentry.get())):
            userInfo = (self.Username_entry.get(), self.Password_entry.get(), self.lastName_entry.get(), self.firstName_entry.get(), self.choice.get(), self.email_entry.get())
            self.control.addUser(userInfo)
            self.back()
        else:
            pass
        
    def Validate(self, email, password, rpassword):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, email)):
            if(password == rpassword):
                return True
            else:
                print("Password do not match.")
                return False
        else:
            print("Invalid Email.")
            return False
if __name__ == '__main__':
    sample = tk.Tk()
    program = userRegisterView(root=sample, control=None)
    program.show()

# self.Sex_entry.grid(row=3+1,
#                          column=1,
#                          pady=self.pady,
#                          padx=self.padx,
#                          sticky='e')
# self.Email_entry.grid(row=4+1,
#                          column=1,
#                          pady=self.pady,
#                          padx=self.padx,)
# self.Phone_entry.grid(row=5+1,
#                          column=1,
#                          pady=self.pady,
#                          padx=self.padx,)
# self.Username_entry.grid(row=6+1,
#                          column=1,
#                          pady=self.pady,
#                          padx=self.padx,)
# self.Password_entry.grid(row=7+1,
#                          column=1,
#                          pady=self.pady,
#                          padx=self.padx,)
# self.RPassword_entry.grid(row=8+1,
#                          column=1,
#                          pady=self.pady,
#                          padx=self.padx,)   
    
# #LABEL FRAME
# self.userField = tk.LabelFrame(self.viewFrame, text = "Please complete the following information.")
# self.userField.grid(row=0, column=0, padx=20, pady=20)
    
# self.Sex_entry = ttk.Combobox(self.entryField, 
#                               values = ("Male","Female","Other"), 
#                               width=17,height=8, 
#                                 font=('Montserrat',12))
# self.Email_entry = ttk.Entry(self.entryField, 
#                                 font=('Montserrat',12))
# self.Phone_entry = ttk.Entry(self.entryField, 
#                                 font=('Montserrat',12))
# self.Username_entry = ttk.Entry(self.entryField, 
#                                 font=('Montserrat',12))
# self.Password_entry = ttk.Entry(self.entryField, 
#                                 font=('Montserrat',12))
# self.RPassword_entry = ttk.Entry(self.entryField, 
#                                 font=('Montserrat',12))


# #BUTTONS
# self.backButton = tk.Button(self.viewFrame, text="Back", command=self.back)
# self.backButton.grid(row=1,column=0, sticky='e')
# self.submitButton = tk.Button(self.viewFrame, text="Submit", command=self.register)
# self.submitButton.grid(row=1,column=0, sticky='w')
    
# self.lastName_label.grid(row=1,column=0, 
#                         pady=self.pady,
#                         padx=self.padx, 
#                         sticky='e')
# self.middleName_label.grid(row=1,column=0, 
#                         pady=self.pady,
#                         padx=self.padx, 
#                         sticky='e')
# self.firstName_label.grid(row=1,column=0, 
#                         pady=self.pady,
#                         padx=self.padx, 
#                         sticky='e')
# self.Sex_label.grid(row=3+1,column=0, 
#                         pady=self.pady,
#                         padx=self.padx,
#                         sticky='e')
# self.Email_label.grid(row=4+1,column=0, 
#                         pady=self.pady,
#                         padx=self.padx, 
#                         sticky='e')
# self.Phone_label.grid(row=5+1,column=0, 
#                         pady=self.pady,
#                         padx=self.padx, 
#                         sticky='e')
# self.Username_label.grid(row=6+1,column=0, 
#                         pady=self.pady,
#                         padx=self.padx, 
#                         sticky='e')
# self.Password_label.grid(row=7+1,column=0, 
#                         pady=self.pady,
#                         padx=self.padx, 
#                         sticky='e')
# self.RPassword_label.grid(row=8+1,column=0, 
#                         pady=self.pady,
#                         padx=self.padx, 
#                         sticky='e')

#         #WIDGETS
#         self.user_info_field = tk.LabelFrame(self.frame, text = "Please complete the following information.")
#         self.user_info_field.grid(row=0, column=0, padx=20, pady=20)
        
#         #LABELS
#         self.first_name_label = tk.Label(self.user_info_field, text = "First Name:")
#         self.first_name_label.grid(sticky="w", row=0,column=0, padx=15, pady=(10,0))
        
#         self.middle_name_label = tk.Label(self.user_info_field, text = "Middle Name:")
#         self.middle_name_label.grid(sticky="w", row=1,column=0, padx=15, pady=(10,0))
        
#         self.last_name_label = tk.Label(self.user_info_field, text = "Last Name:")
#         self.last_name_label.grid(row=2,column=0, padx=15, pady=(10,0))
                
#         self.Sex_label = tk.Label(self.user_info_field, text = "Sex:")
#         self.Sex_label.grid(sticky="w",row=3,column=0, padx=15, pady=(10,0))
        
#         self.Email_label = tk.Label(self.user_info_field, text = "Email:")
#         self.Email_label.grid(sticky="w",row=4,column=0, padx=15, pady=(10,0))
        
#         self.Phone_label = tk.Label(self.user_info_field, text = "Phone:")
#         self.Phone_label.grid(sticky="w",row=5,column=0, padx=15, pady=(10,0))
        
#         self.Username_label = tk.Label(self.user_info_field, text = "Username:")
#         self.Username_label.grid(sticky="w",row=6,column=0, padx=15, pady=(10,0))
        
#         self.Password_label = tk.Label(self.user_info_field, text = "Password")
#         self.Password_label.grid(sticky="w",row=7,column=0, padx=15, pady=(10,0))
        
#         #ENTRY FIELDS
#         self.first_name_entry = tk.Entry(self.user_info_field)
#         self.first_name_entry.grid(sticky="w", row=0,column=1, padx = 15, pady = (10,0))
        
#         self.middle_name_entry = tk.Entry(self.user_info_field)
#         self.middle_name_entry.grid(sticky="w", row=1,column=1, padx = 15, pady = (10,0))
        
#         self.last_name_entry = tk.Entry(self.user_info_field)
#         self.last_name_entry.grid(sticky="w",row=2,column=1, padx = 15, pady = (10,0))
        
#         self.Sex_entry = ttk.Combobox(self.user_info_field, values = ('Male','Female'))
#         self.Sex_entry.grid(sticky="w",row=3,column=1, padx = 15, pady = (10,0))
        
#         self.Email_entry = tk.Entry(self.user_info_field)
#         self.Email_entry.grid(sticky="w",row=4,column=1, padx = 15, pady = (10,0))
        
#         self.Phone_entry = tk.Entry(self.user_info_field)
#         self.Phone_entry.grid(sticky="w",row=5,column=1, padx = 15, pady = (10,0))
        
#         self.Username_entry = tk.Entry(self.user_info_field)
#         self.Username_entry.grid(sticky="w",row=6,column=1, padx = 15, pady = (10,0))
        
#         self.Password_entry = tk.Entry(self.user_info_field)
#         self.Password_entry.grid(sticky="w",row=7,column=1, padx = 15, pady = (10,10))
        
#         #SUBMIT BUTTON
#         self.complete = tk.Button(self.frame, text="Submit", command = self.submit_button)
#         self.complete.grid(stick='center')
        

            
#         win.mainloop()
        
#     def submit_button():
        
    
#     # def submit_button(self):
        
        

# if __name__ =='__main__':
#     register = registerGUI()

