#Sieve of eratosthenes algorythm

def removeNonPrimes(numbers, total):
	auxList = [2,3,5,7]
	index = 0
	#print(auxList[index])
	n = 0
	aux = 2
	for i in auxList:
		print(i)
		while(n<=int(total)):
			n = int(i) * aux
			#print(n)
			if n in numbers:
				numbers.remove(n)
			aux+=1
		aux = 2
		n = 0		
	#print(numbers)
	return numbers

def sumList(numbers):
	total = 0
	for i in numbers:
		total += int(i)

	return total

#Main
number = input("Insert the total: ")
#print(number)

numbers = list(range(2,int(number)))
#print(numbers)

numbers = removeNonPrimes(numbers, number)
print(numbers)

print("The total of all the sum of ", number, " is: ", sumList(numbers))
