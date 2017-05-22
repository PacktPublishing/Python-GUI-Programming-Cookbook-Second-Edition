'''
May 2017
@author: Burkhard A. Meier
'''

#==================================================================
import tkinter as tk
from tkinter import ttk
from threading import Thread

win = tk.Tk()       
win.title("Python GUI")   
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()  

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

text = tk.Text(win, height=10, width=40, borderwidth=2, wrap='word')
text.grid(column=0, sticky='WE', columnspan=3)

#==================================================================  
from multiprocessing import Queue  
# from queue import Queue                  
sharedQueue = Queue()
dataInQueue = False

def putDataIntoQueue(data):
    global dataInQueue
    dataInQueue =  True
    sharedQueue.put(data)
    
def readDataFromQueue():
    global dataInQueue
    dataInQueue = False
    return sharedQueue.get()
     
#==================================================================      
import wx               
class GUI(wx.Panel):    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        parent.CreateStatusBar() 
        menu= wx.Menu()
        menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
        menuBar = wx.MenuBar()
        menuBar.Append(menu, "File") 
        parent.SetMenuBar(menuBar)  
        button = wx.Button(self, label="Print", pos=(0,60))
        self.Bind(wx.EVT_BUTTON, self.writeToSharedQueue, button)
        self.textBox = wx.TextCtrl(self, size=(280,50), style=wx.TE_MULTILINE)   

    #-----------------------------------------------------------------
    def writeToSharedQueue(self, event):
        self.textBox.AppendText(
                        "The Print Button has been clicked!\n") 
        putDataIntoQueue('Hi from wxPython via Shared Queue.\n')
        if dataInQueue: 
            data = readDataFromQueue()
            self.textBox.AppendText(data)
            
            text.insert('0.0', data) # insert data into tkinter GUI

#==================================================================        
def wxPythonApp():
        app = wx.App()      
        frame = wx.Frame(
            None, title="Python GUI using wxPython", size=(300,180))
        GUI(frame)          
        frame.Show()        
        runT = Thread(target=app.MainLoop)
        runT.setDaemon(True)    
        runT.start()
        print(runT)
        print('createThread():', runT.isAlive())
        
#================================================================== 
action = ttk.Button(win, text="Call wxPython GUI", command=wxPythonApp) 
action.grid(column=2, row=1)

#======================
# Start GUI
#======================
win.mainloop()