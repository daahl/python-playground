# 

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
        
        # Water container
        self.container = tk.Frame(self.frame, width=self.width-20, height=self.height-20)
        self.container.grid(row=0, column=0, padx=10)
        
        # Water level
        self.water = tk.Frame(self.frame, width=self.width-20, height=self.tank_level, bg="blue")
        self.water.grid(row=0, column=0, padx=10, sticky="S")
    
    def set_status(self, level):
        self.tank_level = self.tank_level + level
        self.water.config(height=self.tank_level)