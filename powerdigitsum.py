import math

x = pow(2, 1000)

print x

y = list(str(x))
z = map(int, y)

print z

v = sum(z)

print v