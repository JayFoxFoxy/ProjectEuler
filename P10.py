#Sieve of Eratosthenes - array with numbers, start with number 2, multiplied by a count that starts as 2. The count will increment 1 by 1 till reachs the total number of the total prime numbers that we want to sum. next will start with the next number that was not on the multiplied numbers of the last multiplications and go on, till reach the limit.

#Instead of numbers, we are using true or false, if its prime its true and it is not prime, then its false. Thats because the boolean have less lenght than the decimal and cost less time to calculate.

#A array initialized true with the lenght of the limit. Will start in 2 and multiply till reach the limit. Then the number 3 its true, so it will multiply till reach the limit. Then the number 5 its true, so it will multiply till reach the limit and go on till no other position its true.

import time

def isPrime(l):
	primes = [2,3,5,7]
	k = 0
	count = 2
	for i in range(2,len(l)):
		if l[i]:
			while k < len(l):
				l[k] = False
				k = int(i) * count
				#print(k)
				count += 1
		k = 0
		count = 2
	return l


#Main
limit = input("What is the limit of the sum of the primes: ")
sun = 0

startTime = time.time()
primeArray = [True] * int(limit)
primeArray[1] = False

primeArray = isPrime(primeArray)
#print(primeArray)

for i in range(1,int(limit)):
	if primeArray[i]:
		print(int(i))
		sun += int(i)

print("Time: ", time.time() - startTime, " Sec!")
print("The sum of all of the prime numbers until ", limit, " is: ", sun)
