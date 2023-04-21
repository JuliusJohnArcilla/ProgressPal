import tkinter as tk
from tkinter import ttk
import calendar, datetime

class registerGUI:
    
    def __init__(self, WIDTH=400, HEIGHT=500):
        #INITIALIZE PAGE
        win = tk.Tk()
        win.title("Registration")
        
        self.frame = tk.Frame(win)
        self.frame.pack()
        
        #WIDGETS
        self.user_info_field = tk.LabelFrame(self.frame, text = "Please complete the following information.")
        self.user_info_field.grid(row=0, column=0, padx=20, pady=20)
        
        #LABELS
        self.first_name_label = tk.Label(self.user_info_field, text = "First Name:")
        self.first_name_label.grid(sticky="w", row=0,column=0, padx=15, pady=(10,0))
        
        self.middle_name_label = tk.Label(self.user_info_field, text = "Middle Name:")
        self.middle_name_label.grid(sticky="w", row=1,column=0, padx=15, pady=(10,0))
        
        self.last_name_label = tk.Label(self.user_info_field, text = "Last Name:")
        self.last_name_label.grid(row=2,column=0, padx=15, pady=(10,0))
        
        self.Birthdate_label = tk.Label(self.user_info_field, text = "Birthday:")
        self.Birthdate_label.grid(row=3,column=0, padx=15, pady=(10,0))
        
        self.Sex_label = tk.Label(self.user_info_field, text = "Sex:")
        self.Sex_label.grid(row=4,column=0, padx=15, pady=(10,0))
        
        self.Email_label = tk.Label(self.user_info_field, text = "Email:")
        self.Email_label.grid(row=5,column=0, padx=15, pady=(10,0))
        
        self.Phone_label = tk.Label(self.user_info_field, text = "Phone:")
        self.Phone_label.grid(row=6,column=0, padx=15, pady=(10,0))
        
        self.Username_label = tk.Label(self.user_info_field, text = "Username:")
        self.Username_label.grid(row=7,column=0, padx=15, pady=(10,0))
        
        self.Password_label = tk.Label(self.user_info_field, text = "Password")
        self.Password_label.grid(row=8,column=0, padx=15, pady=(10,0))
        
        #ENTRY FIELDS
        self.first_name_entry = tk.Entry(self.user_info_field)
        self.first_name_entry.grid(sticky="w", row=0,column=1, padx = 15, pady = (10,0))
        
        self.middle_name_entry = tk.Entry(self.user_info_field)
        self.middle_name_entry.grid(sticky="w", row=1,column=1, padx = 15, pady = (10,0))
        
        self.last_name_entry = tk.Entry(self.user_info_field)
        self.last_name_entry.grid(row=2,column=1, padx = 15, pady = (10,0))
        
        self.Email_entry = tk.Entry(self.user_info_field)
        self.Email_entry.grid(row=5,column=1, padx = 15, pady = (10,0))
        
        self.Phone_entry = tk.Entry(self.user_info_field)
        self.Phone_entry.grid(row=6,column=1, padx = 15, pady = (10,0))
        
        self.Username_entry = tk.Entry(self.user_info_field)
        self.Username_entry.grid(row=7,column=1, padx = 15, pady = (10,0))
        
        self.Password_entry = tk.Entry(self.user_info_field)
        self.Password_entry.grid(row=8,column=1, padx = 15, pady = (10,10))
        
        #COMBOBOXES
        self.Birthdate_Frame = tk.Frame(self.user_info_field)
        self.Birthdate_Frame.grid(row=3,column=1)
        self.Birthdate_Month = ttk.Combobox(self.Birthdate_Frame, values = tuple(calendar.month_name))
        self.Birthdate_Month.grid(row=0,column=0)
        self.Birthdate_Year = ttk.Combobox(self.Birthdate_Frame, values = tuple(range(1900,(datetime.datetime.now().year+1)))) 
        self.Birthdate_Year.grid(row=0,column=2)
        self.Birthdate_Day = ttk.Combobox(self.Birthdate_Frame, values = calendar.monthrange(self.Birthdate_Year, self.Birthdate_Month))
        self.Birthdate_Day.grid(row=0,column=1)

        
        self.Sex_entry = tk.Entry(self.user_info_field)
        self.Sex_entry.grid(row=4,column=1, padx = 15, pady = (10,0))
        
        
        win.mainloop()
        
        
if __name__ =='__main__':
    register = registerGUI()
