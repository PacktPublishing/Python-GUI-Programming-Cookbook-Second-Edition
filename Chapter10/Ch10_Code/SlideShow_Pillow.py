'''
May 2017
@author: Burkhard A. Meier
'''

from tkinter import Tk, Label
from itertools import cycle
from os import listdir, path, chdir

# using Pillow instead of PIL (2.7) for Python 3.6
# Installation is: >pip install Pillow
from PIL import ImageTk 


class SlideShow(Tk):
    # inherit GUI framework extending tkinter
    def __init__(self, msShowTimeBetweenSlides=1500):
        # initialize tkinter super class
        Tk.__init__(self)
        
        # time each slide will be shown
        self.showTime = msShowTimeBetweenSlides
        
        # look for images in current working directory where this module lives
        chapter_folder = path.realpath(path.dirname(__file__))
        resources_folder = path.join(chapter_folder, 'Resources')
        listOfSlides = [slide for slide in listdir(resources_folder) if slide.endswith('gif') or slide.endswith('jpg')]

        # endlessly read in the slides so we can show them on the tkinter Label 
        chdir(resources_folder)
        self.iterableCycle = cycle((ImageTk.PhotoImage(file=slide), slide) for slide in listOfSlides)
        
        # create tkinter Label widget which can also display images
        self.slidesLabel = Label(self)
        
        # create the Frame widget
        self.slidesLabel.pack()
 
 
    def slidesCallback(self):
        # get next slide from iterable cycle
        currentInstance, nameOfSlide = next(self.iterableCycle)
        
        # assign next slide to Label widget
        self.slidesLabel.config(image=currentInstance)
        
        # update Window title with current slide
        self.title(nameOfSlide)
        
        # recursively repeat the Show
        self.after(self.showTime, self.slidesCallback)

 
#=================================
# Start GUI
#=================================               
win = SlideShow()
win.after(0, win.slidesCallback())
win.mainloop()
