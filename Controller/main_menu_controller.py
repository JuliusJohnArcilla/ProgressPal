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
        
        