class ScheduleController:
    def __init__(self, root, control)->None:
        super(ScheduleController, self).__init__()
        self.root = root
        self.control = control
    
    def ScheduleProg(self):
        self.view.show()
    
    def assignValues(self):
        self.view = self.control.View
        self.model = self.control.Model
    
    def switchViewHome(self):
        self.control.MainMenu()
        
    def switchViewTasks(self):
        self.control.TaskManager()
    
    def switchViewProfile(self):
        self.control.Profile()