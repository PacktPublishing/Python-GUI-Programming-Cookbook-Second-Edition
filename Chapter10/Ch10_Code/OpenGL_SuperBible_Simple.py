'''
May 2017
Example translated into Python from: 
"OpenGL SuperBible Fourth Edition" starting at page 48
@author: Burkhard A. Meier
'''

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


def RenderScene():                      # display callback function
    glClear(GL_COLOR_BUFFER_BIT)        # clear window with color defined in SetupRC
    glFlush()                           # flush/execute the OpenGL drawing command(s)

def SetupRC():                          # rendering context
    glClearColor(0.0, 0.0, 1.0, 1.0)    # RGBA: R=0.0, G=0.0, B=1.0 => becomes Blue

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)    # single buffer; RGBA color mode
    glutCreateWindow(b"Simple")                     # Python 3: bytes instead of string for Title
    glutDisplayFunc(RenderScene)    
    SetupRC()

    glutMainLoop()
    
#=================
main()
