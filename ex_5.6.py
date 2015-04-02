from swampy.TurtleWorld import *
from letters import skip

def koch(t, length):
    """
    function to draw koch curves using
    recursion.
    """
    if(length < 3):
        fd(t, length)
    else:
        koch(t, length/3)
        lt(t, 60)
        koch(t, length/3)
        rt(t, 120)
        koch(t, length/3)
        lt(t, 60)
        koch(t, length/3)



def koch_snow(t, length):
    """
    function to draw three koch curves
    """
    lt(t, 120)
    fd(t, length/3)
    rt(t, 120)
    fd(t, length/3)
    lt(t, 60)
    fd(t, length/3)
    rt(t, 120)
    fd(t, length/3)
    lt(t, 60)
    fd(t, length/3)
    rt(t,120)
    fd(t, length/3)

    """
    function to draw three koch curves in
    downward direction
    """
    lt(t, 60)
    fd(t, length/3)
    rt(t, 120)
    fd(t, length/3)
    lt(t, 60)
    fd(t, length/3)
    rt(t, 120)
    fd(t, length/3)
    lt(t, 60)
    fd(t, length/3)
    rt(t,120)
    fd(t, length/3)
    rt(t, 60)

def koch_snowflake(t, length, depth):
    if(depth == 0):
        fd(t, length)
    else:
        koch_snowflake(t, length/3, depth-1)
        lt(t, 60)
        koch_snowflake(t, length/3, depth-1)
        rt(t, 120)
        koch_snowflake(t, length/3, depth-1)
        lt(t, 60)
        koch_snowflake(t, length/3, depth-1)

def draw_koch_snowflake(t, length, depth):
    koch_snowflake(t, length, depth)
    rt(t, 120)
    koch_snowflake(t, length, depth)
    rt(t, 120)
    koch_snowflake(t, length,depth)



#main
world = TurtleWorld()
bob = Turtle()
print bob

bob.delay = 0.01

koch(bob, 200)
skip(bob, 100)
koch_snow(bob, 30)
skip(bob, 100)
draw_koch_snowflake(bob, 300,3)

wait_for_user()



