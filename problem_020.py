# what is the sum of the individual digits of the number 100!

# create variables, start N out at 100 to kick off factorial
factorialN = 100
sumNum = 0

# compute the factorial
for x in range(99,1,-1):
  factorialN = factorialN * x
	
numString = str(factorialN)

# sum the digits
for x in range(0, (len(numString))):
	sumNum += int(numString[x])

print "Sum is " + str(sumNum)
