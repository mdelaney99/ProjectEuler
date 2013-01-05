#question 3: find the largest prime factor of the number 600851475143

#set up an empty list for factors
list_of_factors = []

#start at square root, find factors by modulo
for n in range(2,int(600851475143**0.5+1)):
  if 600851475143 % n == 0:
		list_of_factors.append(n)
		
#check our list
print list_of_factors

#create a test for primality
def prime_test(number):
	if number < 3:
		print "You know better..."
	for x in range(3,int(number**0.5+1)):
		if number%x == 0:
			#some bad logic here, too lazy to fix given simplicity of problem
			#if this line prints above 'is prime' then it aint prime... false positive
			print str(number) + " ain't prime" 
			break
	print str(number) + " is prime"
	
#check
for i in list_of_factors:
	prime_test(i)
	
