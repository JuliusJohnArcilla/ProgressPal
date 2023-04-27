import Controller.View.welcome_view as welcome
import Controller.user_registration_controller as register
import Controller.user_login_controller as login
import tkinter as tk

class welcomeController:
    def __init__(self, control=None)->None:
        self.root = tk.Tk()
        self.control = control
    
    def run_prog(self):
        self.welcome_view = welcome.welcomeView(self.root, self)
        self.welcome_view.show()
    
    def gotoreg(self):
        self.root.withdraw()
        self.register_view = tk.Toplevel()
        self.register_view = register.userRegistrationController(self.register_view, control=self)
        self.register_view.demo()
        
    def gotologin(self):
        self.root.withdraw()
        self.login_view = tk.Toplevel()
        self.login_view = login.userLoginController(self.login_view, control=self)
        self.login_view.run_prog()

if __name__ == "__main__":
    sample_program = welcomeController()
    sample_program.run_prog()
    