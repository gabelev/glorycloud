from math import factorial

def factors(n):    
    return (reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def sum_int(n):
	x = 0
	for i in range(0, n+1):
		x += i
	return x

# def make_tri():
# 	x_list = []
# 	y_list = []
# 	n = 100000
# 	x = sum_int(n)
# 	z = factors(x)
# 	y = len(z)
# 	if y > 50:
# 		x_list.append(x)
# 		y_list.append(y)
# 	else:
# 		yield n
# 		n += 1
# 	print x_list
# 	print y_list

def guess_tri(number):
	print sum_int(number)
	print len(factors(sum_int(number)))

# def find_tri(number):
# 	x = sum_int(number)
# 	y = len(factors(x))
# 	answer = []
# 	if y > 500:
# 		number += 1
# 	else:
# 		yield number
# 		number += 1

# def print_num_fact(num):
# 	fact_list = []
# 	for i in range(10000000, 10000000 + num):
# 		x = len(factors(i))
# 		fact_list.append(x)
# 	fact_list.sort()
# 	print fact_list

# (199980010499500, 576) from (19999000, 19999001)
#(19989000, 19998001)
#guess_tri(19989000) 19988990

# for i in xrange(19988975, 19988975+1):
# 	x = sum_int(i)
# 	if len(factors(x)) > 500:
# 		print(i, x, len(factors(x)))
# 		break
# 	else:
# 		print "none"

for i in xrange(1, 1000000):
	x = sum_int(i)
	if len(factors(x)) > 500:
		print(i, x, len(factors(x)))
		break

