import time as tm

def testDivisors(n):
	divArray = [False] * int(n)
	for i in range(len(divArray)):
		#print(i)	
		if int(n) % int(i+1) == 0:
			divArray[i] = True

	div = countDivisors(divArray)
	return div

def countDivisors(l):
	count = 0
	for i in range(len(l)):
		if l[i] == True:
			count += 1
	return count
		


#---Main---
numbers = input("How many divisors: ")

startTime = tm.time()

n = 0
aux = 1
divisors = 0

while int(divisors) < int(numbers):
	#print(n)
	n += aux
	aux += 1
	divisors = testDivisors(n)		
	#print(divisors)
	print(n)

print("The result is: ", n)
print("Time: ", tm.time() - startTime, " Sgs")
