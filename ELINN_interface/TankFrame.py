import tkinter as tk

class TankFrame:
    def __init__(self, parent, width, height, debug_mode):
        self.debug = debug_mode
        self.width = width
        self.height = height
        self.tank_level = 100
        
        self.frame = tk.Frame(parent, width=self.width, height=self.height, 
                                    bd=1, relief="groove", bg="pink" if self.debug else None)
        self.frame.grid_propagate(False)
        
        self.water = tk.Frame(self.frame, width=self.width-20, height=self.tank_level, bg="blue")
        self.water.grid(row=0,column=0, padx=10, pady=100)