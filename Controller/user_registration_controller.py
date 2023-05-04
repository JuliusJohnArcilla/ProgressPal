import tkinter as tk

class userRegistrationController:
    def __init__(self, root, control=None)->None:
        self.root = root
        self.control = control
    
    def RegProg(self):
        self.view.show()
    
    def switchViewLogin(self):
        self.control.Login()
    
    def addUser(self, userInfo):
        self.model.add_user(userInfo)
    
    def assignValues(self):
        self.view = self.control.View
        self.model = self.control.Model

if __name__ == '__main__':
    sample = tk.Tk()
    program = userRegistrationController(sample)
    program.demo()
    print("gumana")
    
    
        