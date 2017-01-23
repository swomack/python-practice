
def histogram(str):
    d = dict()
    for element in str:
        d[element] = d.get(element, 0) + 1

    return d

hist = histogram("hello world")
print(hist)