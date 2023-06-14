# https://docs.python.org/3/library/tkinter.html
# https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/
# https://robotic-controls.com/learn/python-guis/python-gui-broken-multiple-files
#
# GUI for the ELINN water tank.
#
# By Marcus Dahlström 2023

# TODO
# - write serial interface
# - string decoder to update interface. Kinda works now, need to add all states
# - v1.0 layout
# - get tank level UI to work. could make it prettier with which parts of the tank is on?

from MainWindow import *

main = MainWindow()
main.start()