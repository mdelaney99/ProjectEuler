# find the 10001 prime

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

#keep checking numbers until we fill a list with 10001 primes
while len(primes) < 10002:
	if checker(current) == True:
		primes.append(current)
	current += 2
			
# printing [0] to ensure I am counting from right starting point
print primes[0]
print "-----------------"
print primes[10000]
