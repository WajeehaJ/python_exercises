from swampy.TurtleWorld import *
from math import pi, sin, cos, sqrt


def vertical_line(t, n):
    """
    Draws a vertical line of size n and t is the 
    turtle object.
    """
    lt(t)
    fd(t,n)
    rt(t)

def horizontal_line(t,n, h):
    """
    Draws a horizontal line of size n at the 
    given height h and t is the turtle object. 
    """
    lt(t)
    pu(t)
    fd(t,h)
    pd(t)
    lt(t)
    fd(t,n)
    rt(t)
def skip(t, n):
    """lift the pen and move"""
    pu(t)
    fd(t, n)
    pd(t)

def fdbk(t, n):
    """forward and back, ending at the original position"""
    fd(t, n)
    bk(t, n)

def move_back(t,n):
    """ move left and then backward direction and then right 
    """
    lt(t)
    bk(t, n)
    rt(t)

def draw_a(t, n):
    vertical_line(t, n)
    fd(t, n/2)
    vertical_line(t, -n)
    horizontal_line(t, n/2, n/2)
    bk(t, n/2)
    rt(t)

def draw_b(t, n):
    draw_a(t, n)
    fdbk(t, n/2)

def draw_c(t, n):
    fdbk(t, n/2)
    vertical_line(t, n)
    fdbk(t, n/2)
    move_back(t, n)

def draw_d(t,n):
    draw_c(t, n)
    skip(t, n/2)
    vertical_line(t,n)
    move_back(t, n)
    bk(t,n/2)    

def draw_e(t, n):
    vertical_line(t,n)
    fdbk(t, n/2)
    move_back(t, n/2)
    fdbk(t, n/2)
    rt(t)
    fd(t, n/2)
    lt(t)
    fdbk(t, n/2)

#Main function

world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.01

size = 50

for f in [draw_a, draw_b, draw_c, draw_d, draw_e]:
    f(bob, size)
    skip(bob, size)

wait_for_user()

