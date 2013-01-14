# find the one pythagorean triplet for which  a + b + c = 1000
# where a pythagorean triplet is defined as three natural numbers a,b,c where a < b < c, and a^2 + b^2 = c^2

realA = 0
realB = 0
realC = 0
a = 0
b = 0
c = 0

print "Working..."
print ""

for a in range(999, 2, -1):
  for b in range(1000-a, 1, -1):
		c = 1000 - b - a
		sumABC = a + b + c
		squaredAB = a**2 + b**2
		if squaredAB == c**2:
			realA = a
			realB = b
			realC = c
			
print "Found these: " + str(realA) + " "+ str(realB) + " "+ str(realC) + " "
print "Their product is " + str(realA * realB * realC)
