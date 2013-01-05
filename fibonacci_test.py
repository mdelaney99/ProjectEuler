def gen_fibonaccis(untilN):
  untilN = int(untilN)
	fib_list = []
	a = 0
	b = 1
	print a
	fib_list.append(a)
	fib_list.append(b)
	print b
	for i in range(untilN-2): # n-2 as we just printed first two already (a & b)
		c = a + b
		print c
		fib_list.append(c)
		a = b
		b = c
	print "---------------------"
	return fib_list
	
gen_fibonaccis(35)
