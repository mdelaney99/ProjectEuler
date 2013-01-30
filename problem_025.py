# The 12th term, F12, is the first term to contain three digits. 
# What is the first term in the Fibonacci sequence to contain 1000 digits?

def findThatShit():
  fib_list = []
	a = 0
	b = 1
	print b
	fib_list.append(b)
	while len(str(fib_list[-1])) < 1000:
		c = a + b
		fib_list.append(c)
		a = b
		b = c
	print fib_list[-1]
	print len(fib_list)
	
	
findThatShit()
