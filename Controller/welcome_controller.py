import View.welcome_view as welcome
import user_registration_controller as register
import tkinter as tk

class welcomeController:
    def __init__(self, root, control=None)->None:
        self.root = root
        self.control = control
    
    def run_prog(self):
        self.welcome_view = welcome.welcomeView(self.root, self)
        self.welcome_view.show()
    
    def gotoreg(self):
        self.root.withdraw()
        self.register_view = tk.Toplevel()
        self.register_view = register.userRegistrationController(self.register_view, control=self)
        self.register_view.demo()

if __name__ == "__main__":
    sample_class = tk.Tk()
    sample_program = welcomeController(sample_class)
    sample_program.run_prog()
    