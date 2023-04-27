import tkinter as tk
from tkinter import ttk

class userRegisterView():
    def __init__(self, root, control)->None:
        #INITIALIZE VARS
        super(userRegisterView, self).__init__()
        self.root = root
        self.control = control
        
    def show(self):
        self.root.title("Registration")
        self.root.geometry("400x500")
        
        self.viewFrame = tk.Frame(self.root)
        self.viewFrame.pack()
        
        #LABEL FRAME
        self.userField = tk.LabelFrame(self.viewFrame, text = "Please complete the following information.")
        self.userField.grid(row=0, column=0, padx=20, pady=20)
        
        #LABELS
        self.lastName_label = tk.Label(self.userField, text="Last Name:")
        self.lastName_label.grid(row=0,column=0, pady=(10,0), sticky='e')
        self.middleName_label = tk.Label(self.userField, text="Middle Name:")
        self.middleName_label.grid(row=1,column=0, pady=(10,0), sticky='e')
        self.firstName_label = tk.Label(self.userField, text="First Name:")
        self.firstName_label.grid(row=2,column=0, pady=(10,0), sticky='e')
        self.Sex_label = tk.Label(self.userField, text="Sex:")
        self.Sex_label.grid(row=3,column=0, pady=(10,0), sticky='e')
        self.Email_label = tk.Label(self.userField, text="Email:")
        self.Email_label.grid(row=4,column=0, pady=(10,0), sticky='e')
        self.Phone_label = tk.Label(self.userField, text="Phone:")
        self.Phone_label.grid(row=5,column=0, pady=(10,0), sticky='e')
        self.Username_label = tk.Label(self.userField, text="Username:")
        self.Username_label.grid(row=6,column=0, pady=(10,0), sticky='e')
        self.Password_label = tk.Label(self.userField, text="Password:")
        self.Password_label.grid(row=7,column=0, pady=(10,0), sticky='e')
        self.RPassword_label = tk.Label(self.userField, text="Re-enter Password:")
        self.RPassword_label.grid(row=8,column=0, pady=(10,0), sticky='e')
        
        #ENTRY FIELD
        self.lastName_entry = ttk.Entry(self.userField)
        self.lastName_entry.grid(row=0,column=1)
        self.middleName_entry = ttk.Entry(self.userField)
        self.middleName_entry.grid(row=1,column=1)
        self.firstName_entry = ttk.Entry(self.userField)
        self.firstName_entry.grid(row=2,column=1)
        self.Sex_entry = ttk.Combobox(self.userField, values = ("Male","Female","Other"), width=8,height=8)
        self.Sex_entry.grid(row=3,column=1)
        self.Email_entry = ttk.Entry(self.userField)
        self.Email_entry.grid(row=4,column=1)
        self.Phone_entry = ttk.Entry(self.userField)
        self.Phone_entry.grid(row=5,column=1)
        self.Username_entry = ttk.Entry(self.userField)
        self.Username_entry.grid(row=6,column=1)
        self.Password_entry = ttk.Entry(self.userField)
        self.Password_entry.grid(row=7,column=1)
        self.RPassword_entry = ttk.Entry(self.userField)
        self.RPassword_entry.grid(row=8,column=1)
        
        #BUTTONS
        self.backButton = tk.Button(self.viewFrame, text="Back", command=self.back)
        self.backButton.grid(row=1,column=0, sticky='e')
        self.submitButton = tk.Button(self.viewFrame, text="Submit", command=self.register)
        self.submitButton.grid(row=1,column=0, sticky='w')
        
        
        
        self.root.mainloop()
        
    def back(self):
        self.root.destroy()
        self.control.previous()
  
    def register(self):
        if(self.Password_entry.get()==self.RPassword_entry.get()):
            User_info = (self.Username_entry.get(), self.Password_entry.get(),
                         self.lastName_entry.get(), self.middleName_entry.get(), 
                         self.firstName_entry.get(), self.Sex_entry.get(), 
                         self.Email_entry.get(), int(self.Phone_entry.get()))
        
            self.control.addUser(User_info)
            
            
        else:
            print("Password and Re-enter Password does not match. Please try again.")
    
if __name__ == '__main__':
    sample = tk.Tk()
    program = userRegisterView(root=sample)
    program.show()
          
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
