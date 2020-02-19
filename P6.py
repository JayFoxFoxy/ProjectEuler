squareSum = 0
naturalSum = 0

for i in range(101):
	squareSum += i**2
	naturalSum += i

#print(naturalSum)
naturalSum = naturalSum ** 2
#print(squareSum)
#print(naturalSum)
print(naturalSum - squareSum)
