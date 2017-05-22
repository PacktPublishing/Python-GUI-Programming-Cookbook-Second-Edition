'''
May 2017
@author: Burkhard
'''
#======================
# imports
#======================
import tkinter as tk 
from tkinter import ttk, scrolledtext, Menu, Spinbox,\
                    filedialog as fd, messagebox as mBox 
from queue import Queue 
from os import path  
import Ch08_Code.ToolTip as tt 
from Ch08_Code.LanguageResources import I18N 
from Ch08_Code.Logger import Logger, LogLevel
from Ch08_Code.Callbacks_Refactored import Callbacks 

# Module level GLOBALS
GLOBAL_CONST = 42

#=================================================================== 
class OOP():
    def __init__(self, language='en'): 
        # Create instance
        self.win = tk.Tk()
        
        self.i18n = I18N(language)
#         self.i18n = I18N(language)

        # Add a title       
        self.win.title(self.i18n.title)   
        
        # Callback methods now in different module
        self.callBacks = Callbacks(self)
         
        # Disable resizing the window  
        self.win.resizable(0,0)  
        
        # Create a Queue
        self.guiQueue = Queue() 
                              
        self.createWidgets() 
        
        # populate Tab 2 Entries      
        self.callBacks.defaultFileEntries()
        
        # create MySQL instance
#         self.mySQL = MySQL()
        
        # create Logger instance
        fullPath = path.realpath(__file__)
        self.log = Logger(fullPath)
#         print(self.log)
        
        # create Log Level instance
        self.level = LogLevel()
          
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
        self.action = ttk.Button(self.mySQL, text="Insert Quote", command=self.callBacks.insertQuote)   
        self.action.grid(column=2, row=1)

        # Adding a Button
        self.action1 = ttk.Button(self.mySQL, text="Get Quotes", command=self.callBacks.getQuote)   
        self.action1.grid(column=2, row=2)
        
        # Adding a Button
        self.action2 = ttk.Button(self.mySQL, text="Mody Quote", command=self.callBacks.modifyQuote)   
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
        self.chVarUn.trace('w', lambda unused0, unused1, unused2 : self.callBacks.checkCallback())    
        self.chVarEn.trace('w', lambda unused0, unused1, unused2 : self.callBacks.checkCallback())   
#         self.chVarUn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())      # <= bug missing callBacks
#         self.chVarEn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback()) 
        
              
        # Radiobutton list
        colors = self.i18n.colors
        
        self.radVar = tk.IntVar()
        
        # Selecting a non-existing index value for radVar
        self.radVar.set(99)    
        
        # Creating all three Radiobutton widgets within one loop
        for col in range(3):
            self.curRad = 'rad' + str(col)  
            self.curRad = tk.Radiobutton(self.widgetFrame, text=colors[col], variable=self.radVar, value=col, command=self.callBacks.radCall)
            self.curRad.grid(column=col, row=6, sticky=tk.W, columnspan=3)
            # And now adding tooltips
            tt.create_ToolTip(self.curRad, 'This is a Radiobutton control.')
            
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
        self.combo.bind('<<ComboboxSelected>>', self.callBacks._combo) 
             
        # Adding a Spinbox widget using a set of values
        self.spin = Spinbox(self.widgetFrame, values=(1, 2, 4, 42, 100), width=5, bd=8, command=self.callBacks._spin) 
        self.spin.grid(column=2, row=7, sticky='W,', padx=6, pady=1)
        
        # Using a scrolled Text control    
        scrolW  = 40; scrolH = 1
        self.scr = scrolledtext.ScrolledText(self.widgetFrame, width=scrolW, height=scrolH, wrap=tk.WORD)
        self.scr.grid(column=0, row=8, sticky='WE', columnspan=3)      

        # Adding a TZ Button
        self.allTZs = ttk.Button(self.widgetFrame, text=self.i18n.timeZones, command=self.callBacks.allTimeZones)   
        self.allTZs.grid(column=0, row=9, sticky='WE')

        # Adding local TZ Button
        self.localTZ = ttk.Button(self.widgetFrame, text=self.i18n.localZone, command=self.callBacks.localZone)   
        self.localTZ.grid(column=1, row=9, sticky='WE')

        # Adding getTime TZ Button
        self.dt = ttk.Button(self.widgetFrame, text=self.i18n.getTime, command=self.callBacks.getDateTime)   
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
        fileMenu.add_command(label=self.i18n.exit, command=self.callBacks._quit)
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


#==============================================
if __name__ == '__main__':            
    #======================
    # Start GUI
    #======================
    oop = OOP()
    print(oop.log)
#     oop.log.setLoggingLevel(oop.level.DEBUG)        # this is the default logging level
    oop.log.setLoggingLevel(oop.level.MINIMUM)      # control logging level      
    oop.log.writeToLog('Test message')      
    oop.win.mainloop()
    
     
    
    

