from swampy.TurtleWorld import *
from math import pi, sin, cos, sqrt

def square(t, length):
    """ Draws a square given the length of the 
        side of the square and t is the turtle 
        object.
    """  
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):
    """ Draws n sided polygon with the given length and
    and t is the turtle object
    """  
    for i in range(n):
        fd(t, length)
        lt(t, (360/n))

def circle(t, r):
    """
    Draws a circle given the radius r
    where t is the turtle object.
    """
    cirf = 2*pi*r
    n = 120
    l = cirf/n
    polygon(t,l,n)

def arc(t, r, a):
    """
    Draws an arc having the radius r 
    and takes angle a used to determine
    arc length. t is the turtle object. 
    """ 
    rad_angle=a/360.0
    arc_len = rad_angle * 2 * pi* r
    n = int(arc_len / 3) + 1
    step_length = arc_len / n
    step_angle = float(a) / n
    
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)



world = TurtleWorld()
bob = Turtle()
print bob

for i in range(4):
    print 'Hello!'

square(bob, 60)
square(bob, 120)
#polygon(bob, 30, 6)
polygon(bob, 30, 12)
circle(bob, 50)
circle(bob, 100)
circle(bob, 30)
arc(bob, 6, 180)


wait_for_user()


