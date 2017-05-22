'''
May 2017
@author: Burkhard
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
import Ch08_Code.ToolTip as tt
from threading import Thread
from time import sleep
from queue import Queue
from tkinter import filedialog as fd
from os import path 
from tkinter import messagebox as mBox
from Ch08_Code.LanguageResources import I18N
from datetime import datetime
from pytz import all_timezones, timezone

# Module level GLOBALS
GLOBAL_CONST = 42

#========================================================
class OOP():
    def __init__(self): 
        # Create instance
        self.win = tk.Tk()
        
        self.i18n = I18N('en')              # use English
        self.i18n = I18N('de')              # use German

        # Add a title       
        self.win.title(self.i18n.title)   
#         self.win.title("Python Graphical User Interface")    # w/out importing I18N
         
        # Disable resizing the window  
        self.win.resizable(0,0)  
        
        # Create a Queue
        self.guiQueue = Queue() 
                              
        self.createWidgets() 
        
        # populate Tab 2 Entries      
        self.defaultFileEntries()
        
        # create MySQL instance
#         self.mySQL = MySQL()
                
    def defaultFileEntries(self): 
        self.fileEntry.delete(0, tk.END)
        self.fileEntry.insert(0, 'Z:\\')        # bogus path
        self.fileEntry.config(state='readonly')         

        self.netwEntry.delete(0, tk.END)
        self.netwEntry.insert(0, 'Z:\\Backup')  # bogus path                      
    
    # Combobox callback 
    def _combo(self, val=0):
        value = self.combo.get()
        self.scr.insert(tk.INSERT, value + '\n')
    
    # Spinbox callback 
    def _spin(self):
        value = self.spin.get()
        self.scr.insert(tk.INSERT, value + '\n')
                
    # Checkbox callback  
    def checkCallback(self, *ignoredArgs):
        # only enable one checkbutton
        if self.chVarUn.get(): self.check3.configure(state='disabled')
        else:                  self.check3.configure(state='normal')
        if self.chVarEn.get(): self.check2.configure(state='disabled')
        else:                  self.check2.configure(state='normal') 
        
    # Radiobutton callback function
    def radCall(self):
        radSel=self.radVar.get()
        if   radSel == 0: self.widgetFrame.configure(text=self.i18n.WIDGET_LABEL + self.i18n.colorsIn[0])
        elif radSel == 1: self.widgetFrame.configure(text=self.i18n.WIDGET_LABEL + self.i18n.colorsIn[1])
        elif radSel == 2: self.widgetFrame.configure(text=self.i18n.WIDGET_LABEL + self.i18n.colorsIn[2])        

    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit() 
       
    def methodInAThread(self, numOfLoops=10):
        for idx in range(numOfLoops):
            sleep(1)
            self.scr.insert(tk.INSERT, str(idx) + '\n') 
        sleep(1)
        print('methodInAThread():', self.runT.isAlive())
            
    # Running methods in Threads
    def createThread(self, num):
        self.runT = Thread(target=self.methodInAThread, args=[num])
        self.runT.setDaemon(True)    
        self.runT.start()
        print(self.runT)
        print('createThread():', self.runT.isAlive())

        # textBoxes are the Consumers of Queue data
        writeT = Thread(target=self.useQueues, daemon=True)
        writeT.start()
    
    # Create Queue instance  
    def useQueues(self):
        # Now using a class member Queue        
        while True: 
            qItem = self.guiQueue.get()
            print(qItem)
            self.scr.insert(tk.INSERT, qItem + '\n') 

    # Button callback
    def insertQuote(self):
        title = self.bookTitle.get()
        page = self.pageNumber.get()
        quote = self.quote.get(1.0, tk.END)
        print(title)
        print(quote)
        self.mySQL.insertBooks(title, page, quote)     

    # Button callback
    def getQuote(self):
        allBooks = self.mySQL.showBooks()  
        print(allBooks)
        self.quote.insert(tk.INSERT, allBooks)

    # Button callback
    def modifyQuote(self):
        raise NotImplementedError("This still needs to be implemented for the SQL command.")
    
    # TZ Button callback
    def allTimeZones(self):
        for tz in all_timezones:
            self.scr.insert(tk.INSERT, tz + '\n')

    # TZ Local Button callback
    def localZone(self):   
        from tzlocal import get_localzone         
        self.scr.insert(tk.INSERT, get_localzone())

                    
    # Format local US time with TimeZone info
    def getDateTime(self):
        fmtStrZone = "%Y-%m-%d %H:%M:%S %Z%z"
        # Get Coordinated Universal Time
        utc = datetime.now(timezone('UTC'))
        print(utc.strftime(fmtStrZone))
         
        # Convert UTC datetime object to Los Angeles TimeZone
        la = utc.astimezone(timezone('America/Los_Angeles'))
        print(la.strftime(fmtStrZone))
 
        # Convert UTC datetime object to New York TimeZone
        ny = utc.astimezone(timezone('America/New_York'))
        print(ny.strftime(fmtStrZone))

        # update GUI label with local Time and Zone       
#         self.lbl2.set(la.strftime(fmtStrZone))
                 
        # update GUI label with NY Time and Zone       
        self.lbl2.set(ny.strftime(fmtStrZone))

    
          
    #####################################################################################    
    def createWidgets(self):    
        # Tab Control introduced here --------------------------------------
        tabControl = ttk.Notebook(self.win)     # Create Tab Control
        
        tab1 = ttk.Frame(tabControl)            # Create a tab 
#         tabControl.add(tab1, text='MySQL')    # Add the tab -- COMMENTED OUT FOR CH08
        
        tab2 = ttk.Frame(tabControl)            # Add a second tab
        tabControl.add(tab2, text='Widgets')    # Make second tab visible
        
        tabControl.pack(expand=1, fill="both")  # Pack to make visible
        # ~ Tab Control introduced here -----------------------------------------
        
        # We are creating a container frame to hold all other widgets
        self.mySQL = ttk.LabelFrame(tab1, text=' Python Database ')
        self.mySQL.grid(column=0, row=0, padx=8, pady=4)        
        
        # Creating a Label
        ttk.Label(self.mySQL, text="Book Title:").grid(column=0, row=0, sticky='W')
   
        # Adding a Textbox Entry widget
        book = tk.StringVar()
        self.bookTitle = ttk.Entry(self.mySQL, width=34, textvariable=book)
        self.bookTitle.grid(column=0, row=1, sticky='W')     

        # Adding a Textbox Entry widget
        book1 = tk.StringVar()
        self.bookTitle1 = ttk.Entry(self.mySQL, width=34, textvariable=book1)
        self.bookTitle1.grid(column=0, row=2, sticky='W')  
        
        # Adding a Textbox Entry widget
        book2 = tk.StringVar()
        self.bookTitle2 = ttk.Entry(self.mySQL, width=34, textvariable=book2)
        self.bookTitle2.grid(column=0, row=3, sticky='W')  
        
        # Creating a Label
        ttk.Label(self.mySQL, text="Page:").grid(column=1, row=0, sticky='W')
        
        # Adding a Textbox Entry widget
        page = tk.StringVar()
        self.pageNumber = ttk.Entry(self.mySQL, width=6, textvariable=page)
        self.pageNumber.grid(column=1, row=1, sticky='W')     
 
        # Adding a Textbox Entry widget
        page = tk.StringVar()
        self.pageNumber1 = ttk.Entry(self.mySQL, width=6, textvariable=page)
        self.pageNumber1.grid(column=1, row=2, sticky='W')    
        
        # Adding a Textbox Entry widget
        page = tk.StringVar()
        self.pageNumber2 = ttk.Entry(self.mySQL, width=6, textvariable=page)
        self.pageNumber2.grid(column=1, row=3, sticky='W')           
       
        # Adding a Button
        self.action = ttk.Button(self.mySQL, text="Insert Quote", command=self.insertQuote)   
        self.action.grid(column=2, row=1)

        # Adding a Button
        self.action1 = ttk.Button(self.mySQL, text="Get Quotes", command=self.getQuote)   
        self.action1.grid(column=2, row=2)
        
        # Adding a Button
        self.action2 = ttk.Button(self.mySQL, text="Mody Quote", command=self.modifyQuote)   
        self.action2.grid(column=2, row=3)
                
        # Add some space around each widget
        for child in self.mySQL.winfo_children(): 
            child.grid_configure(padx=2, pady=4)
            

        quoteFrame = ttk.LabelFrame(tab1, text=' Book Quotation ')
        quoteFrame.grid(column=0, row=1, padx=8, pady=4)    

        # Using a scrolled Text control    
        quoteW  = 40; quoteH = 6
        self.quote = scrolledtext.ScrolledText(quoteFrame, width=quoteW, height=quoteH, wrap=tk.WORD)
        self.quote.grid(column=0, row=8, sticky='WE', columnspan=3)   

        # Add some space around each widget
        for child in quoteFrame.winfo_children(): 
            child.grid_configure(padx=2, pady=4)
                            
        #======================================================================================================               
        # Tab Control 2 
        #======================================================================================================
        # We are creating a container frame to hold all other widgets -- Tab2
        self.widgetFrame = ttk.LabelFrame(tab2, text=self.i18n.WIDGET_LABEL)
        self.widgetFrame.grid(column=0, row=0, padx=8, pady=4)
        
        # Creating three checkbuttons
        self.chVarDis = tk.IntVar()
        self.check1 = tk.Checkbutton(self.widgetFrame, text=self.i18n.disabled, variable=self.chVarDis, state='disabled')
        self.check1.select()
        self.check1.grid(column=0, row=0, sticky=tk.W)               
        
        self.chVarUn = tk.IntVar()
        self.check2 = tk.Checkbutton(self.widgetFrame, text=self.i18n.unChecked, variable=self.chVarUn)
        self.check2.deselect()
        self.check2.grid(column=1, row=0, sticky=tk.W )                  
         
        self.chVarEn = tk.IntVar()
        self.check3 = tk.Checkbutton(self.widgetFrame, text=self.i18n.toggle, variable=self.chVarEn)
        self.check3.deselect()
        self.check3.grid(column=2, row=0, sticky=tk.W)                 
     
        # trace the state of the two checkbuttons
        self.chVarUn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())    
        self.chVarEn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())   
        
        # Radiobutton list
        colors = self.i18n.colors
        
        self.radVar = tk.IntVar()
        
        # Selecting a non-existing index value for radVar
        self.radVar.set(99)    
        
        # Creating all three Radiobutton widgets within one loop
        for col in range(3):
            curRad = 'rad' + str(col)  
            curRad = tk.Radiobutton(self.widgetFrame, text=colors[col], variable=self.radVar, value=col, command=self.radCall)
            curRad.grid(column=col, row=6, sticky=tk.W, columnspan=3)
            # And now adding tooltips
            tt.create_ToolTip(curRad, 'This is a Radiobutton control.')
            
        # Create a container to hold labels
        labelsFrame = ttk.LabelFrame(self.widgetFrame, text=self.i18n.labelsFrame)
        labelsFrame.grid(column=0, row=7, pady=6)
         
        # Place labels into the container element - vertically
        ttk.Label(labelsFrame, text=self.i18n.chooseNumber).grid(column=0, row=0)
        self.lbl2 = tk.StringVar()
        self.lbl2.set(self.i18n.label2)
        ttk.Label(labelsFrame, textvariable=self.lbl2).grid(column=0, row=1)
        
        # Add some space around each label
        for child in labelsFrame.winfo_children(): 
            child.grid_configure(padx=6, pady=1)
            
        number = tk.StringVar()
        self.combo = ttk.Combobox(self.widgetFrame, width=12, textvariable=number)
        self.combo['values'] = (1, 2, 4, 42, 100)
        self.combo.grid(column=1, row=7, sticky=tk.W)
        self.combo.current(0)       
        self.combo.bind('<<ComboboxSelected>>', self._combo) 
             
        # Adding a Spinbox widget using a set of values
        self.spin = Spinbox(self.widgetFrame, values=(1, 2, 4, 42, 100), width=5, bd=8, command=self._spin) 
        self.spin.grid(column=2, row=7, sticky='W,', padx=6, pady=1)
        
        # Using a scrolled Text control    
        scrolW  = 40; scrolH = 1
        self.scr = scrolledtext.ScrolledText(self.widgetFrame, width=scrolW, height=scrolH, wrap=tk.WORD)
        self.scr.grid(column=0, row=8, sticky='WE', columnspan=3)      

        # Adding a TZ Button
        self.allTZs = ttk.Button(self.widgetFrame, 
                                 text=self.i18n.timeZones, 
                                 command=self.allTimeZones)   
        self.allTZs.grid(column=0, row=9, sticky='WE')

        # Adding local TZ Button
        self.localTZ = ttk.Button(self.widgetFrame, 
                                  text=self.i18n.localZone, 
                                  command=self.localZone)   
        self.localTZ.grid(column=1, row=9, sticky='WE')

        # Adding getTime TZ Button
        self.dt = ttk.Button(self.widgetFrame, 
#                              text='Time',
                             text=self.i18n.getTime, 
                             command=self.getDateTime)   
        self.dt.grid(column=2, row=9, sticky='WE')
        
                                
        # Create Manage Files Frame ------------------------------------------------
        mngFilesFrame = ttk.LabelFrame(tab2, text=self.i18n.mgrFiles)
        mngFilesFrame.grid(column=0, row=1, sticky='WE', padx=10, pady=5)
        
        # Button Callback
        def getFileName():
            print('hello from getFileName')
            fDir  = path.dirname(__file__)
            fName = fd.askopenfilename(parent=self.win, initialdir=fDir)
            print(fName)
            self.fileEntry.config(state='enabled')
            self.fileEntry.delete(0, tk.END)
            self.fileEntry.insert(0, fName)
            
            if len(fName) > self.entryLen:
                self.fileEntry.config(width=len(fName) + 3)
                        
        # Add Widgets to Manage Files Frame
        lb = ttk.Button(mngFilesFrame, text=self.i18n.browseTo, command=getFileName)     
        lb.grid(column=0, row=0, sticky=tk.W) 
        
        #-----------------------------------------------------        
        file = tk.StringVar()
        self.entryLen = scrolW - 4
        self.fileEntry = ttk.Entry(mngFilesFrame, width=self.entryLen, textvariable=file)
        self.fileEntry.grid(column=1, row=0, sticky=tk.W)
              
        #-----------------------------------------------------
        logDir = tk.StringVar()
        self.netwEntry = ttk.Entry(mngFilesFrame, width=self.entryLen, textvariable=logDir)
        self.netwEntry.grid(column=1, row=1, sticky=tk.W) 

        
        def copyFile():
            import shutil   
            src = self.fileEntry.get()
            file = src.split('/')[-1]  
            dst = self.netwEntry.get() + '\\'+ file
            try:
                shutil.copy(src, dst)   
                mBox.showinfo('Copy File to Network', 'Succes: File copied.')     
            except FileNotFoundError as err:
                mBox.showerror('Copy File to Network', '*** Failed to copy file! ***\n\n' + str(err))
            except Exception as ex:
                mBox.showerror('Copy File to Network', '*** Failed to copy file! ***\n\n' + str(ex))   
        
        cb = ttk.Button(mngFilesFrame, text=self.i18n.copyTo, command=copyFile)     
        cb.grid(column=0, row=1, sticky=tk.E) 
                
        # Add some space around each label
        for child in mngFilesFrame.winfo_children(): 
            child.grid_configure(padx=6, pady=6)            
            
        # Creating a Menu Bar ==========================================================
        menuBar = Menu(tab1)
        self.win.config(menu=menuBar)
        
        # Add menu items
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label=self.i18n.new)
        fileMenu.add_separator()
        fileMenu.add_command(label=self.i18n.exit, command=self._quit)
        menuBar.add_cascade(label=self.i18n.file, menu=fileMenu)
        
        # Add another Menu to the Menu Bar and an item
        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label=self.i18n.about)
        menuBar.add_cascade(label=self.i18n.help, menu=helpMenu)
        
        # Change the main windows icon
        self.win.iconbitmap('pyc.ico')
        
        # Using tkinter Variable Classes
        strData = tk.StringVar()
        strData.set('Hello StringVar')
        
        # It is not necessary to create a tk.StringVar() 
        strData = tk.StringVar()
        strData = self.spin.get()
        
        # Place cursor into name Entry
        self.bookTitle.focus()        
      
        # Add a Tooltip to the Spinbox
        tt.create_ToolTip(self.spin, 'This is a Spin control.')         
        
        # Add Tooltips to more widgets
        tt.create_ToolTip(self.bookTitle, 'This is an Entry control.')  
        tt.create_ToolTip(self.action, 'This is a Button control.')                      
        tt.create_ToolTip(self.scr,    'This is a ScrolledText control.')   
          
#======================
# Start GUI
#======================
oop = OOP()
oop.win.mainloop()

