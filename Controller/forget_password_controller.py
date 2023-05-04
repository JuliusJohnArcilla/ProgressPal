class ForgetPasswordController:
    def __init__(self, root, control)->None:
        super(ForgetPasswordController, self).__init__()
        self.root = root
        self.control = control
    
    def assignValues(self):
        self.view = self.control.View
        self.model = self.control.Model
    
    def ForgetProg(self):
        self.view.show()
        
    def switchViewLogin(self):
        self.control.Login()
        
    