class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%g,%g)' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            if len(other) == 2:
                return Point(self.x + other[0], self.y + other[1])
            else:
                raise ValueError("Then length of tuple cannot be greater that 2")

    def __radd__(self, other):
        return self.__add__(other)

def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)

def main():
    p1 = Point(3,4)
    p2 = Point (3,5)

    print p1+p2
    print p1 + (2,3)
    print (1,5)  + p2
    print_attributes(p1)

if __name__== '__main__':
    main()
