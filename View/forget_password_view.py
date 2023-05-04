import tkinter as tk
import re
import smtplib
from email.mime.text import MIMEText

class forgetPasswordView:
    def __init__(self, root, control)->None:
        super(forgetPasswordView, self).__init__()
        self.root = root
        self.control = control
    
    def show(self):
        self.root.title("Forget Pasword")
    
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
        self.entryField = tk.Frame(self.viewFrame, background=color_rectangle)
        self.entryField.grid(column=1,row=1,sticky='ns')
        
        #LABEL
        self.label1 = tk.Label(self.entryField, text='Forget Password',
                               background=color_rectangle,
                               font=('Montserrat',30,'bold'))
        self.label2 = tk.Label(self.entryField, text='Please fill up the following field to reset your password.',
                               background=color_rectangle,
                               font=('Montserrat', 18, 'bold'))
        self.emailLabel = tk.Label(self.entryField,
                                   background=color_rectangle,
                                   font=('Montserrat', 18, 'bold'))
        
        #ENTRIES
        self.EmailEntry = tk.Entry(self.entryField, background=color_rectangle,
                                   font=('Montserrat', 15))
        
        #BUTTONS
        self.back_button = tk.Button(self.viewFrame, text = '<',
                                     width=4, height=2, command = self.back)
        self.emailButton = tk.Button(self.entryField, text = '✓',
                                     width=3, height=1, command = self.emailSearch)
        
        #LABEL IMPLEMENTATION
        self.label1.grid(row=0, pady=(30, 0))
        self.label2.grid(row=0, pady=(120, 0))   
        self.emailLabel.grid(row=2, pady=(30, 0))        

        #ENTRY IMPLEMENTATION
        self.EmailEntry.grid(column=0,row=1,
                             pady=25, sticky='n',
                             padx=(0,25))
        
        #BUTTON IMPLEMENTATION
        self.back_button.place(x=5, y=5)
        self.emailButton.grid(column=0,row=1,
                              pady=(26,0),
                              padx=(250,0),
                              sticky='n')
             
        
        self.root.mainloop()
        
    def back(self):
        self.viewFrame.destroy()
        self.control.switchViewLogin()
        
    def emailSearch(self):
        email = self.EmailEntry.get()
        print(self.control.model.searchEmail(email))
        if(self.Validate(email)):
            if(email == self.control.model.searchEmail(email)):
                smtp_server = 'smtp-mail.outlook.com'
                smtp_port = 587
                smtp_username = 'ProgressPal123@yahoo.com'
                smtp_password = 'gmasqxhieostiqdc'
                
                message = "TEST"
                
                msg = MIMEText(message)
                msg['Subject'] = 'ProgressPal Forget Password'
                msg['From'] = smtp_username
                msg['To'] = email
                
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username,smtp_password)
                    server.sendmail(smtp_username,email,msg.as_string())
            else:
                return
                
            

    def Validate(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, email)):
            return True
        else:
            print("Invalid Email.")
            return False    
        
        
if __name__ == '__main__':
    sample = tk.Tk()
    program = forgetPasswordView(root=sample, control=None)
    program.root.geometry("750x750")
    program.show()