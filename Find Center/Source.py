
class Point:
    """ Point class represent a point in 2D space.
    
    Attributes: x, y."""

class Rectange:
    """ Rectangle class represent a rectangle in 2D space.abs

    Attributes: width, height, left_bottom_corner."""


def find_center(rect):
    center = Point()
    center.x = (rect.left_bottom_corner.x + rect.width) / 2
    center.y = (rect.left_bottom_corner.y + rect.height) / 2
    return center


rect = Rectange()
rect.left_bottom_corner = Point()
rect.left_bottom_corner.x = 0
rect.left_bottom_corner.y = 0
rect.height = 11
rect.width = 11

center = find_center(rect)

print(list((center.x, center.y)))