import Controller.View.user_login_view as View
import Controller.Model.user_login_model as Model
import tkinter as tk

class userLoginController:
    def __init__(self, root, control)->None:
        self.root = root
        self.control = control
        
        self.login_view = View.userLoginView(self.root, self)
        self.login_model = Model.loginModel('\PPDatabase.db')
        
    def run_prog(self):
        self.login_view.show()      
        
    def LoginAction(self, user, password):
        if(self.login_model.run_comparison(user, password)):
            pass
        
    def previous(self):
        self.control.root.deiconify()
        
            
        
    
if __name__ == '__main__':
    sample_class = tk.Tk()
    sample_program = userLoginController(sample_class, userLoginController)
    sample_program.run_prog()