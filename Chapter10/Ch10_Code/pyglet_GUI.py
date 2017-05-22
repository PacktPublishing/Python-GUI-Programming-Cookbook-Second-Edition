'''
May 2017
@author: Burkhard A. Meier
'''

import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *

WINDOW = 400
INCREMENT = 5

class Window(pyglet.window.Window):

    # Cube 3D start rotation
    xRotation = yRotation = 30    

    def __init__(self, width, height, title=''):
        super(Window, self).__init__(width, height, title)
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)    

    def on_draw(self):
        # Clear the current GL Window
        self.clear()
        
        # Push Matrix onto stack
        glPushMatrix()

        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)

        # Draw the six sides of the cube
        glBegin(GL_QUADS)
        
        # White
        glColor3ub(255, 255, 255)
        glVertex3f(50, 50, 50)

        # Yellow
        glColor3ub(255, 255, 0)
        glVertex3f(50, -50, 50)

        # Red
        glColor3ub(255, 0, 0)
        glVertex3f(-50, -50, 50)

        # Magenta
        glColor3ub(255, 0, 255)
        glVertex3f(-50, 50, 50)

        # Cyan
        glColor3f(0, 1, 1)
        glVertex3f(50, 50, -50)

        # Green
        glColor3f(0, 1, 0)
        glVertex3f(50, -50, -50)
        
        # Black
        glColor3f(0, 0, 0)
        glVertex3f(-50, -50, -50)

        # Blue
        glColor3f(0, 0, 1)
        glVertex3f(-50, 50, -50)
    
        # Cyan
        glColor3f(0, 1, 1)
        glVertex3f(50, 50, -50)

        # White
        glColor3f(1, 1, 1)
        glVertex3f(50, 50, 50)

        # Magenta
        glColor3f(1, 0, 1)
        glVertex3f(-50, 50, 50)

        # Blue
        glColor3f(0, 0, 1)
        glVertex3f(-50, 50, -50)

        # Green
        glColor3f(0, 1, 0)
        glVertex3f(50, -50, -50)

        # Yellow
        glColor3f(1, 1, 0)
        glVertex3f(50, -50, 50)

        # Red
        glColor3f(1, 0, 0)
        glVertex3f(-50, -50, 50)

        # Black
        glColor3f(0, 0, 0)
        glVertex3f(-50, -50, -50)

        # White
        glColor3f(1, 1, 1)
        glVertex3f(50, 50, 50)

        # Cyan
        glColor3f(0, 1, 1)
        glVertex3f(50, 50, -50)

        # Green
        glColor3f(0, 1, 0)
        glVertex3f(50, -50, -50)

        # Yellow
        glColor3f(1, 1, 0)
        glVertex3f(50, -50, 50)
    
        # Magenta
        glColor3f(1, 0, 1)
        glVertex3f(-50, 50, 50)

        # Blue
        glColor3f(0, 0, 1)
        glVertex3f(-50, 50, -50)

        # Black
        glColor3f(0, 0, 0)
        glVertex3f(-50, -50, -50)

        # Red
        glColor3f(1, 0, 0)
        glVertex3f(-50, -50, 50)
        
        glEnd()

        # Pop Matrix off stack
        glPopMatrix()


    def on_resize(self, width, height):
        # set the Viewport
        glViewport(0, 0, width, height)

        # using Projection mode
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = width / height
        gluPerspective(35, aspectRatio, 1, 1000)
         
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -400)
    

    def on_text_motion(self, motion): 
        if motion == key.UP:
            self.xRotation -= INCREMENT
        elif motion == key.DOWN:
            self.xRotation += INCREMENT
        elif motion == key.LEFT:
            self.yRotation -= INCREMENT
        elif motion == key.RIGHT:
            self.yRotation += INCREMENT
            

if __name__ == '__main__':
    Window(WINDOW, WINDOW, 'Pyglet Colored Cube')
    pyglet.app.run()
