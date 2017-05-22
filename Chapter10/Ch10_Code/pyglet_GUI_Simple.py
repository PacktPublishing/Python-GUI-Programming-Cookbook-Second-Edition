'''
May 2017
@author: Burkhard A. Meier
'''

import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label('PyGLet GUI',
                          font_size=42,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
