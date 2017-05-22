'''
May 2017
@author: Burkhard
'''

from pylab import show, arange, sin, plot, pi

t = arange(0.0, 2.0, 0.01)
s = sin( 2 * pi * t )
plot(t, s)

show()
