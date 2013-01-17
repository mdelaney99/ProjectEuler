# what is the sum of the individual digits of the number 2^1000

bigNumber = 2**1000
numString = str(bigNumber)
sumNum = 0

for x in range(0, (len(numString))):
  sumNum += int(numString[x])

print "Sum is " + str(sumNum)
