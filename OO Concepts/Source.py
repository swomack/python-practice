class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "%.2f, %.2f" %(self.x, self.y)

    def __add__(self, other):

        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def add_point(self, point):
        p = Point()
        p.x = self.x + point.x
        p.y = self.y + point.y
        return p

    def add_tuple(self, t):
        p = Point()
        p.x = self.x + t[0]
        p.y = self.y + t[1]
        return p


p = Point(10, 20)
v = Point(30, 40)

t = tuple([-30, -40])

print(p + v)

print(p + t)