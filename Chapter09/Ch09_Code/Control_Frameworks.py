'''
May 2017
@author: Burkhard A. Meier
'''

#==================================================================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from threading import Thread

win = tk.Tk()    
     
win.title("Python GUI")
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)    
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)
scrolW  = 30
scrolH  =  3
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)
nameEntered.focus()  

#==================================================================     
## working           
def wxPythonApp():
    import wx
    app = wx.App()
    frame = wx.Frame(None, -1, "wxPython GUI", size=(200,150))
    frame.SetBackgroundColour('white')
    frame.CreateStatusBar()
    menu= wx.Menu()
    menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
    menuBar = wx.MenuBar()
    menuBar.Append(menu,"File") 
    frame.SetMenuBar(menuBar)     
    frame.Show()
    
    runT = Thread(target=app.MainLoop)
    runT.setDaemon(True)    
    runT.start()
    print(runT)
    print('createThread():', runT.isAlive())

action = ttk.Button(win, text="Call wxPython GUI", command=wxPythonApp) 
action.grid(column=2, row=1)
#================================================================== 


## NOT working - CRASHES Python -----------------------------------
# def wxPythonApp():
#     import wx
#     app = wx.App()
#     frame = wx.Frame(None, -1, "wxPython GUI", size=(200,150))
#     frame.SetBackgroundColour('white')
#     frame.CreateStatusBar()
#     menu= wx.Menu()
#     menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
#     menuBar = wx.MenuBar()
#     menuBar.Append(menu,"File") 
#     frame.SetMenuBar(menuBar)     
#     frame.Show()
#     app.MainLoop()
# 
# def tryRunInThread():
#     runT = Thread(target=wxPythonApp)
#     runT.setDaemon(True)    
#     runT.start()
#     print(runT)
#     print('createThread():', runT.isAlive())    
#         
# action = ttk.Button(win, text="Call wxPython GUI", command=tryRunInThread) 
# action.grid(column=2, row=1)
##-----------------------------------------------------------------
    
#======================
# Start GUI
#======================
win.mainloop()