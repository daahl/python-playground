# Class for each switch

import tkinter as tk

class SwitchFrame():
    def __init__(self, parent, label):
        self.label = label
        self.status = False
        
        self.frame = tk.Frame(parent, width=100, height=50, bg="red")
        self.frame.grid_propagate(False)
        
        self.label = tk.Label(self.frame, text=label)
        self.label.grid(row=0, column=0, padx=5, pady=5)
        
    def set_status(self, status):
        self.status = status
        
        # Change color based on status
        if status == False:
            self.frame.config(bg="red")
        else:
            self.frame.config(bg="green")
        