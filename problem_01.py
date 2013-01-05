threes_and_fives = [x for x in range (1,1000) if x%3==0 or x%5==0]
sum3and5s = 0

for x in threes_and_fives:
  sum3and5s = sum3and5s + x
	

print sum3and5s
