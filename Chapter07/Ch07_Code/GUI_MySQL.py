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
import Ch07_Code.ToolTip as tt
from threading import Thread
from time import sleep
from queue import Queue
from tkinter import filedialog as fd
from os import path, makedirs
from tkinter import messagebox as mBox
from Ch07_Code.GUI_MySQL_class import MySQL 

# Module level GLOBALS
GLOBAL_CONST = 42
fDir   = path.dirname(__file__)
netDir = fDir + '\\Backup' 
if not path.exists(netDir):
    makedirs(netDir, exist_ok = True) 
WIDGET_LABEL = ' Widgets Frame '

#=================================================================== 
class OOP():
    def __init__(self): 
        # Create instance
        self.win = tk.Tk()           

        # Add a title       
        self.win.title("Python GUI")   
         
        # Disable resizing the window  
        self.win.resizable(0,0)  
        
        # Create a Queue
        self.guiQueue = Queue() 
                              
        self.createWidgets() 
        
        # populate Tab 2 Entries      
        self.defaultFileEntries()
        
        # create MySQL instance
        self.mySQL = MySQL()
                
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
        else:             self.check3.configure(state='normal')
        if self.chVarEn.get(): self.check2.configure(state='disabled')
        else:             self.check2.configure(state='normal') 
        
    # Radiobutton callback function
    def radCall(self):
        radSel=self.radVar.get()
        if   radSel == 0: self.mySQL2.configure(text=WIDGET_LABEL + 'in Blue')
        elif radSel == 1: self.mySQL2.configure(text=WIDGET_LABEL + 'in Gold')
        elif radSel == 2: self.mySQL2.configure(text=WIDGET_LABEL + 'in Red')        

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
          
    #####################################################################################    
    def createWidgets(self):    
        # Tab Control introduced here --------------------------------------
        tabControl = ttk.Notebook(self.win)     # Create Tab Control
        
        tab1 = ttk.Frame(tabControl)            # Create a tab 
        tabControl.add(tab1, text='MySQL')      # Add the tab 
        
        tab2 = ttk.Frame(tabControl)            # Add a second tab
        tabControl.add(tab2, text='Widgets')      # Make second tab visible
        
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
        self.mySQL2 = ttk.LabelFrame(tab2, text=WIDGET_LABEL)
        self.mySQL2.grid(column=0, row=0, padx=8, pady=4)
        
        # Creating three checkbuttons
        self.chVarDis = tk.IntVar()
        self.check1 = tk.Checkbutton(self.mySQL2, text="Disabled", variable=self.chVarDis, state='disabled')
        self.check1.select()
        self.check1.grid(column=0, row=0, sticky=tk.W)               
        
        self.chVarUn = tk.IntVar()
        self.check2 = tk.Checkbutton(self.mySQL2, text="UnChecked", variable=self.chVarUn)
        self.check2.deselect()
        self.check2.grid(column=1, row=0, sticky=tk.W )                  
         
        self.chVarEn = tk.IntVar()
        self.check3 = tk.Checkbutton(self.mySQL2, text="Toggle", variable=self.chVarEn)
        self.check3.deselect()
        self.check3.grid(column=2, row=0, sticky=tk.W)                 
     
        # trace the state of the two checkbuttons
        self.chVarUn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())    
        self.chVarEn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())   
        
        # Radiobutton list
        colors = ["Blue", "Gold", "Red"]
        
        self.radVar = tk.IntVar()
        
        # Selecting a non-existing index value for radVar
        self.radVar.set(99)    
        
        # Creating all three Radiobutton widgets within one loop
        for col in range(3):
            curRad = 'rad' + str(col)  
            curRad = tk.Radiobutton(self.mySQL2, text=colors[col], variable=self.radVar, value=col, command=self.radCall)
            curRad.grid(column=col, row=6, sticky=tk.W, columnspan=3)
            # And now adding tooltips
            tt.create_ToolTip(curRad, 'This is a Radiobutton control.')
            
        # Create a container to hold labels
        labelsFrame = ttk.LabelFrame(self.mySQL2, text=' Labels within a Frame ')
        labelsFrame.grid(column=0, row=7, pady=6)
         
        # Place labels into the container element - vertically
        ttk.Label(labelsFrame, text="Choose a number:").grid(column=0, row=0)
        ttk.Label(labelsFrame, text="Label 2").grid(column=0, row=1)
        
        # Add some space around each label
        for child in labelsFrame.winfo_children(): 
            child.grid_configure(padx=6, pady=1)
            
        number = tk.StringVar()
        self.combo = ttk.Combobox(self.mySQL2, width=12, textvariable=number)
        self.combo['values'] = (1, 2, 4, 42, 100)
        self.combo.grid(column=1, row=7, sticky=tk.W)
        self.combo.current(0)       
        self.combo.bind('<<ComboboxSelected>>', self._combo) 
             
        # Adding a Spinbox widget using a set of values
        self.spin = Spinbox(self.mySQL2, values=(1, 2, 4, 42, 100), width=5, bd=8, command=self._spin) 
        self.spin.grid(column=2, row=7, sticky='W,', padx=6, pady=1)
        
        # Using a scrolled Text control    
        scrolW  = 40; scrolH = 1
        self.scr = scrolledtext.ScrolledText(self.mySQL2, width=scrolW, height=scrolH, wrap=tk.WORD)
        self.scr.grid(column=0, row=8, sticky='WE', columnspan=3)      
                
        # Create Manage Files Frame ------------------------------------------------
        mngFilesFrame = ttk.LabelFrame(tab2, text=' Manage Files: ')
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
        lb = ttk.Button(mngFilesFrame, text="Browse to File...", command=getFileName)     
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
        
        cb = ttk.Button(mngFilesFrame, text="Copy File To :   ", command=copyFile)     
        cb.grid(column=0, row=1, sticky=tk.E) 
                
        # Add some space around each label
        for child in mngFilesFrame.winfo_children(): 
            child.grid_configure(padx=6, pady=6)            
            
        # Creating a Menu Bar ==========================================================
        menuBar = Menu(tab1)
        self.win.config(menu=menuBar)
        
        # Add menu items
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._quit)
        menuBar.add_cascade(label="File", menu=fileMenu)
        
        # Add another Menu to the Menu Bar and an item
        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About")
        menuBar.add_cascade(label="Help", menu=helpMenu)
        
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

