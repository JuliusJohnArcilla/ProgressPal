import Controller.View.user_register_view as view
import Controller.Model.user_registration_model as model
import tkinter as tk

class userRegistrationController:
    def __init__(self, root, control=None)->None:
        self.root = root
        self.control = control
    
    def demo(self):
        self.view = view.userRegisterView(self.root, self)
        self.model = model.registerModel("\PPDatabase.db")
        
        
        self.view.show()
    
    def addUser(self, userInfo):
        self.model.insertUser(userInfo)
    
    def previous(self):
        self.control.root.deiconify()

if __name__ == '__main__':
    sample = tk.Tk()
    program = userRegistrationController(sample)
    program.demo()
    print("gumana")
    
    
        