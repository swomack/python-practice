
import math

class Point:
    """Represent a point in 2D space""" 


def distance(p1, p2):
    return math.sqrt(math.fabs(p1.x - p2.x) ** 2 + math.fabs(p1.y - p2.y) ** 2)


inp_1 = input()
inp_2 = input()

inps_1 = inp_1.split()
inps_2 = inp_2.split()

point_1 = Point()
point_1.x = int(inps_1[0])
point_1.y = int(inps_1[1])

point_2 = Point()
point_2.x = int(inps_2[0])
point_2.y = int(inps_2[1])


print(distance(point_1, point_2))
