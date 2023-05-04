class UserProfileController:
    def __init__(self, root, control)->None:
        super(UserProfileController, self).__init__()
        self.root = root
        self.control = control
        self.User = None
        
    def assignValues(self):
        self.view = self.control.View
        self.model = self.control.Model
        
    def ProfileProg(self):
        self.view.show()
        
    def switchViewHome(self):
        self.control.MainMenu()
    
    def switchViewSchedule(self):
        self.control.Schedule()
    
    def switchViewTasks(self):
        self.control.TaskManager()
        
    