from swampy.World import World

class Point(object):
    """Represents a point in 2-D space."""
    pass

class Rectangle(object):
    """ Represents a rectangle
        having the attribute
        urp: Upper Right coordinate
        llp : Lower Left coordinates
    """
    pass





def draw_rectangle(rect, canvas, outline='black', width=1, color='green4'):
    assert isinstance(rect.llp, Point) and isinstance(rect.urp, Point)
    bbox = [ [rect.llp.x, rect.llp.x], [rect.urp.x, rect.urp.x]]
    canvas.rectangle(bbox,  fill=color, outline=outline, width=width)

world = World()
canvas = world.ca(width=500, height = 500, background = 'white')


rect = Rectangle()
rect.llp =Point()
rect.urp = Point()

rect.llp.x  = -225
rect.llp.y = -150

rect.urp.x  = 75
rect.urp.y = 50

draw_rectangle(rect, canvas, outline = 'black',color = 'white')

rect.llp.x  = -75
rect.llp.y = -50

rect.urp.x  = 225
rect.urp.y = 150

draw_rectangle(rect, canvas, outline = 'red',color = 'red')




#points = [[-150,-100], [150, 100], [150, -100]]
#canvas.polygon(points, fill='green4')



world.mainloop()



