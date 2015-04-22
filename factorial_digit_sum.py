import math

x = math.factorial(100)
print x
y = map(int, str(x))
print y

print sum(y)

print reduce(lambda x, y: x + y, y)                                               