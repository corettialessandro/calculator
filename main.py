import numpy as np

from std_operations import Add, Subtract, Inverse
from linalg import ScalProd

a = -1
b = 3.14

c = Add(a, b)
d = Subtract(a, b)

print("{} + {} = {}\n{} - {} = {}".format(a, b, c, a, b, d))

u = np.array([1, 0.5, -3.14])
v = np.array([-4, 0, 6.73])

udotv = ScalProd(u, v)

print("{} dot {} = {}".format(u, v, udotv))

print("The Inverse of {} is {}".format(b, Inverse(b)))
