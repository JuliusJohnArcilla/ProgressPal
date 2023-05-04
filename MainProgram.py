#THIS FILE IS THE MAIN PROGRAM OF PROGRESSPAL
import tkinter as tk
import Controller.user_login_controller as loginController
import View.user_login_view as loginView
import Controller.user_registration_controller as registerController
import View.user_register_view as registerView
import Controller.main_menu_controller as MainMenuController
import View.main_menu_view as MainMenuView
import Controller.task_manager_controller as TaskController
import View.task_manager_view as TaskView
import Controller.forget_password_controller as ForgetController
import View.forget_password_view as ForgetView 
import Controller.user_profile_controller as ProfileController
import View.user_profile_view as ProfileView
import Controller.schedule_controller as ScheduleController
import View.schedule_view as ScheduleView
import Model.User_Database_Model as  UserDatabase
import Model.Task_Database_Model as TaskDatabase

class MainProgram:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("750x750")
        self.root.resizable(False, False)
        
        self.control = None
        self.View = None
        self.Model = None
        self.TaskModel = None
        
    def Login(self):
        self.control = loginController.userLoginController(self.root, self)
        self.View = loginView.userLoginView(self.root, self.control)
        self.Model = UserDatabase.userManagerModel()
        self.TaskModel = TaskDatabase.taskManagerModel()
        
        self.control.assignValues()
        self.control.LoginProg()
    
    def SignUp(self):
        self.control = registerController.userRegistrationController(self.root, self)
        self.View = registerView.userRegisterView(self.root, self.control)
        
        self.control.assignValues()
        self.control.RegProg()
    
    def MainMenu(self):
        self.control = MainMenuController.mainMenuController(self.root, self)
        self.View = MainMenuView.mainMenuView(self.root, self.control)
        
        self.control.assignValues()
        self.control.MainMenuProg()
        
    def TaskManager(self):
        self.control = TaskController.TaskManagerController(self.root, self)
        self.View = TaskView.TaskManagerView(self.root, self.control)
        
        self.control.assignValues()
        self.control.TaskProg()
    
    def ForgetPassword(self):
        self.control = ForgetController.ForgetPasswordController(self.root, self)
        self.View = ForgetView.forgetPasswordView(self.root, self.control)
        
        self.control.assignValues()
        self.control.ForgetProg()
        
    def Profile(self):
        self.control = ProfileController.UserProfileController(self.root, self)
        self.View = ProfileView.UserProfileView(self.root, self.control)
        
        self.control.assignValues()
        self.control.ProfileProg()
        
    def Schedule(self):
        self.control = ScheduleController.ScheduleController(self.root, self)
        self.View = ScheduleView.ScheduleView(self.root, self.control)
        
        self.control.assignValues()
        self.control.ScheduleProg()
        
if __name__ == '__main__':
    mainRoot = tk.Tk()
    Program = MainProgram(mainRoot)
    Program.Login()