'''
May 2017
Example translated into Python from: 
"OpenGL SuperBible Fourth Edition" starting at page 62
@author: Burkhard A. Meier
'''

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# initial position and size
x = GLfloat(0.0).value
y = GLfloat(0.0).value
rect_size = GLfloat(25.0).value

# number of pixels to move each step
xstep = GLfloat(1.0).value
ystep = GLfloat(1.0).value

# initialize bouncing window
windowWidth  = GLfloat(133).value       # 800/600 = 1.33
windowHeight = GLfloat(100).value


def RenderScene():                      # display callback function
    dRadius = 0.1
    dAngle  = 0.0
    
    glClearColor(0.0, 0.0, 1.0, 0.0)  # Clear blue window
    
    # Use 0 for clear stencil, enable stencil test
    glClearStencil(0)
    glEnable(GL_STENCIL_TEST)
    
    # Clear color and stencil buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
  
    # All drawing commands fail the stencil test, and are not
    # drawn, but increment the value in the stencil buffer. 
    glStencilFunc(GL_NEVER, 0x0, 0x0)
    glStencilOp(GL_INCR, GL_INCR, GL_INCR)
                
    # Spiral pattern will create stencil pattern
    # Draw the spiral pattern with white lines. We 
    # make the lines  white to demonstrate that the 
    # stencil function prevents them from being drawn
    glColor3f(1.0, 1.0, 1.0)
    
    glBegin(GL_LINE_STRIP)
    for _ in range(400):
        glVertex2d(dRadius * math.cos(dAngle), dRadius * math.sin(dAngle))
        dRadius *= 1.002
        dAngle += 0.1
    glEnd()                
                  
    # Now, allow drawing, except where the stencil pattern is 0x1
    # and do not make any further changes to the stencil buffer
    glStencilFunc(GL_NOTEQUAL, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)  

    # Now draw red bouncing square
    # (x and y) are modified by a timer function
    glColor3f(1.0, 0.0, 0.0)
    glRectf(x, y, x + rect_size, y - rect_size)
              
    glutSwapBuffers()                   # flush and swap double buffers


def TimerFunction(value):
    global x, xstep, y, ystep
    
    # reverse direction left/right
    if ((x > windowWidth - rect_size) or (x < -windowWidth)):
        xstep = -xstep
        
    # reverse direction top/bottom
    if ((y > windowHeight) or (y < -windowHeight + rect_size)):
        ystep = -ystep

    # Check bounds. This is in case the window is made
    # smaller while the rectangle is bouncing and the 
    # rectangle suddenly finds itself outside the new
    # clipping volume
    if (x > windowWidth - rect_size):
        x = windowWidth - rect_size-1

    if (y > windowHeight):
        y = windowHeight-1
            
    # move the red square
    x += xstep
    y += ystep
            
    # redraw the scene
    glutPostRedisplay()
    glutTimerFunc(33, TimerFunction, 1)     # recursive call
        
        
def SetupRC():                          # rendering context setup
    glClearColor(0.0, 0.0, 1.0, 1.0)    # RGBA: R=0.0, G=0.0, B=1.0=white => becomes Blue
  
  
def ChangeSize(w, h):                   
    if h == 0: h =1                     # prevent divide by zero
        
    glViewport(0, 0, w, h)              # set Viewport to Window dimensions
    
    glMatrixMode(GL_PROJECTION)         # define the viewing volume
    glLoadIdentity()                    # reset coordinate system
    
    aspectRatio = GLfloat(w).value / GLfloat(h).value   # establish clipping volume
                                                        # GLfloat becomes ctypes.c_float 
                                                        # Use the value attribute before dividing      
    if w <= h:
        windowWidth = 100
        windowHeight = 100 / aspectRatio
        glOrtho(-100.0, 100.0, -windowHeight, windowHeight, 1.0, -1.0)      
    else:
        windowWidth = 100 * aspectRatio
        windowHeight = 100
        glOrtho(-windowWidth, windowWidth, -100.0, 100.0, 1.0, -1.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_STENCIL)     # Double buffer, using Stencil
    glutInitWindowSize(800, 600)                    # window size
    glutCreateWindow(b"Bouncing Red Square")        # Python 3: bytes instead of string for Title
    glutDisplayFunc(RenderScene)  
    glutReshapeFunc(ChangeSize)  
    glutTimerFunc(33, TimerFunction, 1)
    
#     SetupRC()
    
    glutMainLoop()
    
#=================
main()
