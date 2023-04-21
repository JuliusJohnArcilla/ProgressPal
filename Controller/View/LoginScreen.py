import tkinter as tk

class loginGUI:
    
    def __init__(self, WIDTH=400, HEIGHT=500):
        win = tk.Tk()
        win.title("Login")
        
        self.frame = tk.Frame(win)
        self.frame.pack()
        
        #
        
if __name__ =='__main__':
    login = loginGUI()
