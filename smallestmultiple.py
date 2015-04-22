def factors(n):    
    return (reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#print factors(2520)

#print factors(99999)

a =[1, 2, 3, 4, 5,6, 7,8, 9, 10, 11, 12, 13,14, 15, 16, 17, 18, 19, 20]

# z = 2520 *11 * 13 * 17*19

# print z

# print factors(zz)

for j in range(1, 1000000000):
	b = factors(j)
	if a in b:
		print j
# print a
# print b
print j



