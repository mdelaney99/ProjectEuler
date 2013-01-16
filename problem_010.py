# find the sum of all the primes below two million

#recycling prime number generation script from problem 7....
primes = [2,3,5]
current = 7

# check all possible numbers as factors
def checker(n):
  if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
		return False
	check = 7
	while check < (n**0.5+1):
		if n % check == 0:
			return False
		check += 2
	return True

#modifying here - keep checking numbers until last prime is over 2mm
while primes[-1] < 2000000:
	if checker(current) == True:
		primes.append(current)
	current += 2
			
# by definition of while loop above, we have one prime over 2mm, removing it
del primes[-1]

#summing rest, which should be all under 2mm
theAnswer = sum(primes)

print theAnswer
