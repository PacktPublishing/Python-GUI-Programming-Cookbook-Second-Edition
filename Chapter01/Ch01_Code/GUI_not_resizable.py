'''
May 2017
@author: Burkhard A. Meier
'''
#======================
# imports
#======================
import tkinter as tk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")

# Disable resizing the GUI by passing in False/False
win.resizable(False, False)   

# Enable resizing x-dimension, disable y-dimension 
# win.resizable(True, False)     

#======================
# Start GUI
#======================
win.mainloop()