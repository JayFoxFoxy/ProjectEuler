#Trial Division

import math, time

def printN(n):
	divisors = [1, int(n)]
	for x in range(2, int(math.sqrt(int(n)))+1):
		#aux = int(n) // int(x)
		if int(n) % int(x) == 0:
			#print(x)
			divisors.append(int(x))
			if int(x) != int(n) // int(x):
				divisors.append(int(n) // int(x))
				#print(int(n)//int(x))

	#print(divisors)
	#print(len(divisors))
	return len(divisors)



#Main
number = input("Insert total amount of divisors: ")
startTime = time.time()
count = 0
n = 0
aux = 1

while int(count) < int(number):
	print(n)
	n = n + aux
	aux += 1
	count = printN(n)

print("The value of the triangle number is : ", n)
print("Time elapsed: ", time.time()-startTime)
