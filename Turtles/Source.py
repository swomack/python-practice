import turtle
import time


def draw_edge(width, bob):
    for i in range(3):
        bob.fd(width)
        bob.lt(90)
    bob.fd(width)

def draw_roof(width, bob):
    bob.lt(150)
    bob.pd()
    bob.fd(width)
    bob.rt(120)
    bob.fd(width)

bob = turtle.Turtle()
print(bob)

# draw a house
width = 100
draw_edge(width, bob)
bob.pu()
bob.bk(width)
draw_roof(width, bob)




time.sleep(30)
