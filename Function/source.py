
import math

def degree_to_rad (degree):
    result = (degree * math.pi) / 180
    return result


print(math.sin(degree_to_rad(90)))
