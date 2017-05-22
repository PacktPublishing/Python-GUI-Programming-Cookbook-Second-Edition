'''
May 2017
@author: Burkhard
'''
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
#--------------------------------------------------------------               
fig = Figure(figsize=(12, 8), facecolor='white')
#--------------------------------------------------------------     
axis = fig.add_subplot(211)     # 2 rows, 1 column, Top graph       
#--------------------------------------------------------------
xValues = [1,2,3,4]
yValues0 = [5,7,6,8]
axis.plot(xValues, yValues0)

axis.set_xlabel('Horizontal Label')
axis.set_ylabel('Vertical Label')

axis.grid(linestyle='-')        # solid grid lines
#--------------------------------------------------------------
axis1 = fig.add_subplot(212)    # 2 rows, 1 column, Bottom graph       
#--------------------------------------------------------------
xValues1 = [1,2,3,4]
yValues1 = [7,5,8,6]
axis1.plot(xValues1, yValues1)
axis1.grid()                    # default line style 
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
