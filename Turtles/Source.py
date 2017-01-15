import turtle
import time
import math

bob = turtle.Turtle()
print(bob)

# draw a house
width = 100

bob.fd(width)
bob.lt(90)
bob.fd(width)
bob.lt(90)
bob.fd(width)
bob.lt(90)
bob.fd(width)
bob.pu()
bob.bk(width)
bob.lt(150)
bob.pd()
bob.fd(width)
bob.rt(120)
bob.fd(width)


time.sleep(30)
