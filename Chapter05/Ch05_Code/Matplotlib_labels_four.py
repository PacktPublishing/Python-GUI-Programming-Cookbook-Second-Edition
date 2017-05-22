'''
May 2017
@author: Burkhard A. Meier
'''

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import tkinter as tk 
#-------------------------------------------------------------- 
fig = Figure(figsize=(12, 8), facecolor='white') 
xValues = [1,2,3,4] 
yValues = [5,7,6,8] 
#-------------------------------------------------------------- 
axis1 = fig.add_subplot(221)
axis2 = fig.add_subplot(222, sharex=axis1, sharey=axis1)
axis3 = fig.add_subplot(223, sharex=axis1, sharey=axis1)
axis4 = fig.add_subplot(224, sharex=axis1, sharey=axis1)
#-------------------------------------------------------------- 
axis1.plot(xValues, yValues) 
axis1.set_xlabel('Horizontal Label 1') 
axis1.set_ylabel('Vertical Label 1')  
axis1.grid(linestyle='-')        # solid grid lines 
#-------------------------------------------------------------- 
axis2.plot(xValues, yValues) 
axis2.set_xlabel('Horizontal Label 2') 
axis2.set_ylabel('Vertical Label 2')  
axis2.grid(linestyle='-')        # solid grid lines 
#-------------------------------------------------------------- 
axis3.plot(xValues, yValues) 
axis3.set_xlabel('Horizontal Label3') 
axis3.set_ylabel('Vertical Label 3')  
axis3.grid(linestyle='-')        # solid grid lines 
#-------------------------------------------------------------- 
axis4.plot(xValues, yValues) 
axis4.set_xlabel('Horizontal Label 4') 
axis4.set_ylabel('Vertical Label 4')  
axis4.grid(linestyle='-')        # solid grid lines 
#-------------------------------------------------------------- 

#-------------------------------------------------------------- 
def _destroyWindow(): 
    root.quit() 
    root.destroy()  
#-------------------------------------------------------------- 
root = tk.Tk()  
root.withdraw() 
root.protocol('WM_DELETE_WINDOW', _destroyWindow)    
#-------------------------------------------------------------- 
canvas = FigureCanvasTkAgg(fig, master=root) 
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1) 
#-------------------------------------------------------------- 
root.update() 
root.deiconify() 
root.mainloop() 



