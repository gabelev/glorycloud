import numpy
import math
from sympy.solvers import solve
from sympy import symbols

# m, n = symbols('m n', integer=True)

# z = solve(m*n + m**2 - 500, n, m)

# print z

def pyth_triplets(n=1000):
    "Version 1"
    for x in xrange(1, n):
        x2= x*x # time saver
        for y in xrange(x+1, n): # y > x
            z2= x2 + y*y
            zs= int(z2**.5)
            if zs*zs == z2:
                yield x, y, zs


test = list(pyth_triplets(500))

print test[319]

print sum(test[319])

answer = 200 * 375 *425
print answer
# for i in test:
#  	print sum(test[i])