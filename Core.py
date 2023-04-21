import Database as db
import GUI.RegistrationScreen as Registration
import GUI.WelcomeScreen as Welcome
import GUI.LoginScreen as Login

database = db.db("\Database\PPDatabase.py")
database.check()

class Program:
        
    def gotologin(self):
        self.current.window.destroy()
        self.current = Login.loginGUI()
        
    def gotoreg(self):
        self.current.window.destroy()
        self.current = Registration.registerGUI()
    
    def __init__(self):
        self.current = Welcome.welcomeGUI(Logincmd=self.gotologin(), Registercmd=self.gotoreg())
        
    current = Welcome.welcomeGUI()
            
if __name__ == '__main__':
    program = Program()