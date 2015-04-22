def sequence(n):
	seq_list = []
	while n > 1:
		if n % 2 == 0:
			seq_list.append(n)
			n = n/2
		else:
			seq_list.append(n)
			n = 3*n + 1
	return seq_list

def len_sequence(n):
	seq_list = []
	while n > 1:
		if n % 2 == 0:
			seq_list.append(n)
			n = n/2
		else:
			seq_list.append(n)
			n = 3*n + 1
	return len(seq_list)

def solve_14():
	total_seq_lst = []
	for i in xrange(1, 1000000):
		z = len_sequence(i)
		total_seq_lst.append(z)
	#return max(total_seq_lst)
	return max(total_seq_lst)

def solve_14_again():
	for i in xrange(1, 1000000):
		z = sequence(i)
		q = len(sequence(i))
		if q == 524:
			return (i, q)

# def solve_14_again_yeah():
# 	for i in xrange(1, 100000):
# 		z = sequence(i)
# 		q = len(sequence(i))
# 		total = [i, q]
		

x = solve_14_again()
print x
# print len(sequence(999999))
# 524 = longest sequence