import math


def potatoes(p0, w0, p1):
    return math.floor(w0 * (100 - p0) / (100 - p1))


# Without library
def potatoes(p0, w0, p1):
    return w0 * (100 - p0) // (100 - p1)


print(potatoes(82, 127, 80))
print(potatoes(99, 100, 98))
