'''
May 2017
@author: Burkhard
'''
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
#--------------------------------------------------------------               
fig = Figure(figsize=(12, 5), facecolor='white')
#--------------------------------------------------------------          
axis  = fig.add_subplot(111)                  # 1 row, 1 column

xValues  = [1,2,3,4]

yValues0 = [6,7.5,8,7.5]
yValues1 = [5.5,6.5,8,6]
yValues2 = [6.5,7,8,7]

# the commas after t0, t1 and t2 are required
t0 = axis.plot(xValues, yValues0)               # no comma here
t1, = axis.plot(xValues, yValues1)
t2, = axis.plot(xValues, yValues2)

# t0, = axis.plot(xValues, yValues0, color = 'purple')  # change the color of the plotted line to purple
# t0, = axis.plot(xValues, yValues0, color = 'r')  # change the color of the plotted line
# t1, = axis.plot(xValues, yValues1, color = 'b')
# t2, = axis.plot(xValues, yValues2, color = 'purple')

axis.set_ylabel('Vertical Label')
axis.set_xlabel('Horizontal Label')

axis.grid()
          
fig.legend((t0, t1, t2), ('First line', 'Second line', 'Third line'), 'upper right')

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
