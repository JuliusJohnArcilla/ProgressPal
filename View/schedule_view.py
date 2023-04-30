import tkinter as tk

class SchedulView:
    def __init__(self, root, control)->None:
        super(SchedulView, self).__init__()
        self.root = root
        self.control = control
    
    def show(self):
        self.root.title("Schedule View")