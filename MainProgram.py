#THIS FILE IS THE MAIN PROGRAM OF PROGRESSPAL
import tkinter as tk
import Controller.user_login_controller as loginController
import View.user_login_view as loginView
import Model.User_Database_Model as  UserDatabase
import Controller.user_registration_controller as registerController
import View.user_register_view as registerView
import Controller.main_menu_controller as MainMenuController
import View.main_menu_view as MainMenuView


class MainProgram:
    def __init__(self, root):
        self.root = root
        self.root.geometry("750x750")
        self.root.resizable(False, False)
        
        self.control = None
        self.View = None
        self.Model = None
        
    def Login(self):
        self.control = loginController.userLoginController(self.root, self)
        self.View = loginView.userLoginView(self.root, self.control)
        self.Model = UserDatabase.userManagerModel()
        
        self.control.assignValues()
        self.control.LoginProg()
    
    def SignUp(self):
        self.control = registerController.userRegistrationController(self.root, self)
        self.View = registerView.userRegisterView(self.root, self.control)
        
        self.control.assignValues()
        self.control.RegProg()
    
    def MainMenu(self):
        self.control = MainMenuController.mainMenuController(self.root, self)
        self.View = MainMenuView.mainMenu(self.root, self.control)
        
        self.control.assignValues()
        self.control.MainMenuProg()
        
        
    
if __name__ == '__main__':
    mainRoot = tk.Tk()
    Program = MainProgram(mainRoot)
    Program.Login()