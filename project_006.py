# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumOfSquares = 0
sumOfNumbers = 0

for x in range(1,101):
  sumOfNumbers += x
	sumOfSquares += x**2
	
print "-----------------"
print "Difference is:"
print str(sumOfSquares) + " - " + str(sumOfNumbers) + "^2"
print (((sumOfNumbers)**2)-sumOfSquares)
