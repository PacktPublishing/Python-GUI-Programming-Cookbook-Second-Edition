'''
May 2017
Example translated into Python from: 
"OpenGL SuperBible Fourth Edition" starting at page 54
@author: Burkhard A. Meier
'''

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def RenderScene():                      # display callback function
    glClear(GL_COLOR_BUFFER_BIT)        # clear window with color defined in SetupRC    
    #          R    G    B              # set drawing color to Red
    glColor3f(1.0, 0.0, 0.0)            # function expects 3 f(loats)    
    glRectf(-25.0, 25.0, 25.0, -25.0)   # draw a filled rectangle with above color
    glFlush()                           # flush/execute the OpenGL drawing command(s)

def SetupRC():                          # rendering context setup
    glClearColor(0.0, 0.0, 1.0, 1.0)    # RGBA: R=0.0, G=0.0, B=1.0=white => becomes Blue

def ChangeSize(w, h):                   # callback when window size changes
    if h == 0: h =1                     # prevent divide by zero        
    glViewport(0, 0, w, h)              # set Viewport to Window dimensions
    glMatrixMode(GL_PROJECTION)         # define the viewing volume
    glLoadIdentity()                    # reset coordinate system
    aspectRatio = GLfloat(w).value / GLfloat(h).value   # establish clipping volume
                                                        # GLfloat becomes ctypes.c_float 
                                                        # Use the value attribute before dividing       
    if w <= h: glOrtho(-100.0, 100.0, -100.0 / aspectRatio, 100.0 / aspectRatio, 1.0, -1.0)      
    else:      glOrtho(-100.0 * aspectRatio, 100.0 * aspectRatio, -100.0, 100.0, 1.0, -1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)    # single buffer; RGBA color mode
    glutCreateWindow(b"GLRect")                     # Python 3: bytes instead of string for Title
    glutDisplayFunc(RenderScene)  
    glutReshapeFunc(ChangeSize)  
    SetupRC()
    glutMainLoop()  
#=================
main()
