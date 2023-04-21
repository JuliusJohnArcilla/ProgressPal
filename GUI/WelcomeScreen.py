import tkinter as tk
import LoginScreen as Login
import RegistrationScreen as Reg

class welcomeGUI():
    window = tk.Tk()
    
    def __init__(self, WIDTH=400, HEIGHT=500):
        self.window.title("Welcome to ProgressPal!")
        self.window.minsize(WIDTH, HEIGHT)
        
        text1 = tk.Label(self.window, text = "Welcome to ProgressPal!")
        text2 = tk.Label(self.window, text = "Please choose either of the\ntwo options!")
        text1.pack(pady=(100,0))
        text2.pack(pady=(12.5,0))
        
        button1 = tk.Button(self.window, text = "Login", command = self.Logincmd)
        button2 = tk.Button(self.window, text = "Register", command = self.Registercmd)
        button1.pack(pady=(25,0))
        button2.pack(pady=(12.5,0))
    
    def Logincmd(self):
        self.window.withdraw()
        self.window = Login.loginGUI()
        
    def Registercmd(self):
        self.window.destroy()
        self.window = Reg.registerGUI()
        
if __name__ == '__main__':
    test = welcomeGUI()
    test.window.mainloop()
    
        



# Create the main window
# class welcomeGUI(tk.Toplevel):
#     _WIDTH = None
#     _HEIGHT = None
    
#     def __init__(self, WIDTH=400, HEIGHT=500):
#         super().__init__()
#         self._WIDTH = WIDTH
#         self._HEIGHT = HEIGHT
#         self.title("ProgressPal")
#         self.minsize(self._WIDTH,self._HEIGHT)
        
#         #Label Widgets
#         text1 = tk.Label(self, text = "Welcome to ProgressPal!")
#         text2 = tk.Label(self, text = "Please choose either of the\ntwo options below to continue.")
#         text1.pack(pady=(100,0))
#         text2.pack(pady=(12.5,0))
        
#         #Button Widgets
#         button1 = tk.Button(self, text = "Login", command = self.Logincmd)
#         button2 = tk.Button(self, text = "Registration", command = None)
#         button1.pack(pady = (25, 0))
#         button2.pack(pady = (12.5, 0))
        
#     def Logincmd(self):
#         self.destroy()
#         W2 = Login.loginGUI()
        
        
# if __name__ == '__main__':
#     st = tk.Tk()
#     st = welcomeGUI()
#     st.mainloop()