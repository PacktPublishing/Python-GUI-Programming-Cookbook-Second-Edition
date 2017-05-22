'''
May 2017
@author: Burkhard A. Meier
'''

import wx
BACKGROUNDCOLOR = (240, 240, 240, 255)
#====================================================================
class Widgets(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.panel = wx.Panel(self)
        self.createWidgetsFrame()
        self.createManageFilesFrame()
        self.addWidgets()
        self.addFileWidgets()
        self.layoutWidgets()
        
    #----------------------------------------------------------
    def createWidgetsFrame(self):
        staticBox = wx.StaticBox( self.panel, -1, "Widgets Frame", size=(285, -1) )   
        self.statBoxSizerV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)   
    
    #----------------------------------------------------------
    def createManageFilesFrame(self):
        staticBox = wx.StaticBox( self.panel, -1, "Manage Files", size=(285, -1) )   
        self.statBoxSizerMgrV = wx.StaticBoxSizer(staticBox, wx.VERTICAL) 
                                        
    #----------------------------------------------------------  
    def layoutWidgets(self):         
        boxSizerV = wx.BoxSizer( wx.VERTICAL )
        boxSizerV.Add( self.statBoxSizerV, 1, wx.ALL )
        boxSizerV.Add( self.statBoxSizerMgrV, 1, wx.ALL )
        
        self.panel.SetSizer( boxSizerV )
        boxSizerV.SetSizeHints( self.panel )                        
    #----------------------------------------------------------
    def addWidgets(self):
        self.addCheckBoxes()        
        self.addRadioButtons()
        self.addStaticBoxWithLabels()  
        self.addTextCtrl()
        self.addButtons()
        
    #----------------------------------------------------------
    def addCheckBoxes(self):
        # Regular Box Sizer 
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        chk1 = wx.CheckBox(self.panel, label='Disabled')
        chk1.SetValue(True)
        chk1.Disable()
        boxSizerH.Add(chk1)
        chk2 = wx.CheckBox(self.panel, label='UnChecked')
        boxSizerH.Add(chk2, flag=wx.LEFT, border=10)
        chk3 = wx.CheckBox(self.panel, label='Toggle')
        boxSizerH.Add(chk3, flag=wx.LEFT, border=10)
        chk3.SetValue(True)
        # Add Regular Box Sizer to StaticBox sizer
        self.statBoxSizerV.Add(boxSizerH, flag=wx.LEFT, border=10)
        self.statBoxSizerV.Add((0, 8))     
          
    #----------------------------------------------------------
    def addRadioButtons(self):         
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add((2, 0))
        boxSizerH.Add(wx.RadioButton(self.panel, -1, 'Blue', style=wx.RB_GROUP))
        boxSizerH.Add((33, 0)) 
        boxSizerH.Add(wx.RadioButton(self.panel, -1, 'Gold'))
        boxSizerH.Add((45, 0)) 
        boxSizerH.Add(wx.RadioButton(self.panel, -1, 'Red' ))        
        self.statBoxSizerV.Add(boxSizerH, 0, wx.ALL, 8)                  

    #----------------------------------------------------------
    def addStaticBoxWithLabels(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        staticBox = wx.StaticBox( self.panel, -1, "Labels within a Frame" )
        staticBoxSizerV = wx.StaticBoxSizer( staticBox, wx.VERTICAL )
        boxSizerV = wx.BoxSizer( wx.VERTICAL )
        staticText1 = wx.StaticText( self.panel, -1, " Choose a number:" )
        boxSizerV.Add( staticText1, 0, wx.ALL)
        staticText2 = wx.StaticText( self.panel, -1, "           Label 2")
        boxSizerV.Add( staticText2, 0, wx.ALL )
        #------------------------------------------------------
        staticBoxSizerV.Add( boxSizerV, 0, wx.ALL )
        boxSizerH.Add(staticBoxSizerV)
        #------------------------------------------------------
        boxSizerH.Add(wx.ComboBox(self.panel, size=(70, -1)))
        #------------------------------------------------------
        boxSizerH.Add(wx.SpinCtrl(self.panel, size=(50, -1), style=wx.BORDER_RAISED))             
        
        # Add local boxSizer to main frame
        self.statBoxSizerV.Add( boxSizerH, 1, wx.ALL )

    #----------------------------------------------------------
    def addTextCtrl(self):   
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add(wx.TextCtrl(self.panel, size=(275, -1), style= wx.TE_MULTILINE))     
        self.statBoxSizerV.Add( boxSizerH, 1, wx.ALL )
 
    #----------------------------------------------------------
    def addButtons(self):   
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add(wx.Button(self.panel, label='All Time Zones'))   
        boxSizerH.Add(wx.Button(self.panel, label='Local Zone')) 
        boxSizerH.Add(wx.Button(self.panel, label='New York'))     
        self.statBoxSizerV.Add( boxSizerH, 1, wx.ALL )

    #----------------------------------------------------------
    def addFileWidgets(self):   
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add(wx.Button(self.panel, label='Browse to File...'))   
        boxSizerH.Add(wx.TextCtrl( self.panel, size=(174, -1), value= "Z:\\" ))
        
        boxSizerH1 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH1.Add(wx.Button(self.panel, label='Copy File To:    ')) 
        boxSizerH1.Add(wx.TextCtrl( self.panel, size=(174, -1), value= "Z:\\Backup" ))    
        
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(boxSizerH)
        boxSizerV.Add(boxSizerH1)        
        
        self.statBoxSizerMgrV.Add( boxSizerV, 1, wx.ALL )        
        
#====================================================================
class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.createWidgets()
        self.Show()
    #----------------------------------------------------------
    def exitGUI(self, event):       # callback
        self.Destroy()
    #----------------------------------------------------------  
    def createWidgets(self):   
        self.CreateStatusBar()      # wxPython built-in method
        self.createMenu()
        self.createNotebook()
    #----------------------------------------------------------
    def createMenu(self):      
        menu= wx.Menu()
        menu.Append(wx.ID_NEW, "New", "Create something new")
        menu.AppendSeparator()
        _exit = menu.Append(wx.ID_EXIT, "Exit", "Exit the GUI")
        self.Bind(wx.EVT_MENU, self.exitGUI, _exit)
        menuBar = wx.MenuBar()
        menuBar.Append(menu, "File")   
        menu1= wx.Menu()    
        menu1.Append(wx.ID_ABOUT, "About", "wxPython GUI")
        menuBar.Append(menu1, "Help")     
        self.SetMenuBar(menuBar)  
    #----------------------------------------------------------
    def createNotebook(self):
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)
        widgets = Widgets(notebook)
        notebook.AddPage(widgets, "Widgets")
        notebook.SetBackgroundColour(BACKGROUNDCOLOR) 
        # layout
        boxSizer = wx.BoxSizer()
        boxSizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizerAndFit(boxSizer)  
               
#======================
# Start GUI
#======================
app = wx.App()
MainFrame(None, title="Python GUI using wxPython", size=(350,450))
app.MainLoop()