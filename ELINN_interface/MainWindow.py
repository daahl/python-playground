# Main window pane

# GUI lib
import tkinter as tk
# My libs
import SwitchFrame as sf
import TankFrame as tf

class MainWindow:
    def __init__(self):
        self.sfStatus = True
        self.debug = False
        self.root = tk.Tk()
        self.root.title("Water tank - Control panel")
        self.root.geometry("500x600")
        
        ################## Create text window
        self.text_window = tk.Frame(self.root, width=500, height=100, 
                                    bd=1, relief="solid", bg="red" if self.debug else None)
        self.text_window.grid_propagate(False)
        self.text_window.grid(row=0, column=0, columnspan=2)
        
        # Add text to text window
        self.text_breadtext = tk.Label(self.text_window, text="foobar")
        self.text_breadtext.grid(row=0, column=0, padx=10, pady=10)
        
        ################## Create switch window
        self.switch_window = tk.Frame(self.root, width=300, height=400, 
                                      bd=1, relief="groove", bg="green" if self.debug else None)
        self.switch_window.grid_propagate(False)
        self.switch_window.grid(row=1, column=0)
        
        # Add switch frames
        self.sf1 = sf.SwitchFrame(self.switch_window, "Switch 1")
        self.sf1.frame.grid(row=0, column=0, padx=20, pady=20)
        self.sf2 = sf.SwitchFrame(self.switch_window, "Switch 2")
        self.sf2.frame.grid(row=0, column=1, padx=20, pady=20)
        
        ################## Create tank window
        self.tank_window = tf.TankFrame(self.root, width=200, height=400, debug_mode=False)
        self.tank_window.frame.grid(row=1, column=1)
        
        ################## Test buttons
        self.bton = tk.Button(self.root, text="On", command=lambda:self.update())
        self.bton.grid(row=3, column=0, sticky="we")
        self.btoff = tk.Button(self.root, text="Tank level +", command=lambda:self.tank_window.set_status(+10))
        self.btoff.grid(row=4, column=0, sticky="we")
        self.btoff = tk.Button(self.root, text="Tank level -", command=lambda:self.tank_window.set_status(-10))
        self.btoff.grid(row=5, column=0, sticky="we")
        
        ################## Add all state objects to be updated to a dict
        self.objs = {"sf1":self.sf1, "sf2":self.sf2}
        
        
    def start(self):
        self.root.mainloop()
        
    def update(self):
        statusString = "sf1:1,sf2:1"
        
        for s in statusString.split(","):
            self.objs[s.split(":")[0]].set_status(s.split(":")[1])
