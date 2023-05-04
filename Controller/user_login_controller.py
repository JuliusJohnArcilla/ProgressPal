import tkinter as tk

class userLoginController:
    
    def __init__(self, root, control)->None:
        self.root = root
        self.control = control
    
    def assignValues(self):
        self.view = self.control.View
        self.model = self.control.Model
        
    def LoginProg(self):
        self.view.show()
        
    def switchViewSignUp(self):
        self.control.SignUp()
    
    def switchViewMain(self):
        self.control.MainMenu()
        
    def switchViewForgetPassword(self):
        self.control.ForgetPassword()
        
        
        
            
        
    
if __name__ == '__main__':
    sample_class = tk.Tk()
    sample_program = userLoginController(sample_class, userLoginController)
    sample_program.run_prog()