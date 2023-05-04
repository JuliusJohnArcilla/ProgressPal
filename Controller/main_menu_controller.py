class mainMenuController:
    def __init__(self, root, control)->None:
        super(mainMenuController, self).__init__()
        self.root = root
        self.control = control
    
    def assignValues(self):
        self.view = self.control.View
        self.model = self.control.Model
    
    def MainMenuProg(self):
        self.view.show()
    
    def switchViewTasks(self):
        self.control.TaskManager()
    
    def switchViewProfile(self):
        self.control.Profile()
    
    def switchViewSchedule(self):
        self.control.Schedule()
    
    
        
        