import turtle
import time
import math



def draw_square(width, bob):
    for i in range(4):
        bob.fd(width)
        bob.lt(90)


def draw_polygon(side, length, bob):
    angle = 360 / side;
    for i in range(side):
        bob.fd(length)
        bob.lt(angle)


def draw_circle(radius, bob):
    total_sides = 200
    side_length = (2 * math.pi * radius) / total_sides
    draw_polygon(total_sides, side_length, bob)


def draw_arc(angle, radius, bob):
    total_sides = 200
    side_length = (2 * math.pi * radius) / total_sides
    draw_side = int((total_sides * angle) / 360)
    draw_polygon(draw_side, side_length, bob)



bob = turtle.Turtle()
# draw square
draw_square(150, bob)
draw_polygon(5, 100, bob)
#draw_circle(50, bob)
draw_arc(90, 50, bob)







time.sleep(30)
