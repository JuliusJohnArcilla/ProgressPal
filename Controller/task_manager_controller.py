class TaskManagerController:
    def __init__(self, root, control)->None:
        super(TaskManagerController, self).__init__()
        self.root = root
        self.control = control
    
    def assignValues(self):
        self.view = self.control.View
        self.model = self.control.Model
    
    def TaskProg(self):
        self.view.show()
        
    def switchViewMainMenu(self):
        self.control.MainMenu()
    
    def switchViewProfile(self):
        self.control.Profile()
    
    def switchViewSchedule(self):
        self.control.Schedule()
        
    