import copy

class Point:
    """ Point class represent a point in 2D space.
    
    Attributes: x, y."""

class Rectange:
    """ Rectangle class represent a rectangle in 2D space.abs

    Attributes: width, height, left_bottom_corner."""



rect = Rectange()
rect.center = Point()
rect2 = copy.copy(rect)

print(rect is rect2)
print(rect.center is rect2.center)

rect2 = copy.deepcopy(rect)

print(rect is rect2)
print(rect.center is rect2.center)
