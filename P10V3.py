def primeNumbers10():

	primeNumbers = []
	check = 0
	
	primeNumbers.append(2)
	#primeNumbers.append(3)
	
	for i in range(3,11,2):
		#print("i = ", i)
		for j in range(3,int(i)):
			#print(j)
			#print(int(i) % int(j))
			if(int(j) != int(i) and int(i) % int(j) == 0):
				check = 1
		if (check == 0):
			primeNumbers.append(i)
			check = 0	
	return primeNumbers
	#print(primeNumbers)

def notPrimesMult(listin, total):
	auxList = []
	count = 0
	aux = 2
	for i in listin:
		while(count < int(total)):
			auxList.append(int(i) * int(aux))
			count = int(i) * int(aux)
			aux += 1
		count = 0
		aux = 2
	auxList.sort()
	
	auxRes = []
	for i in auxList:
		if i not in auxRes:
			auxRes.append(i)
	#print(auxRes)	
	return auxRes
	

def primesN(listin, total):
	primes = []
	for i in range(4, int(total)+1):
		if i not in listin:
			primes.append(i)
	#print(primes)	
	return(primes)

def sumListValues(listin):
	sumlist = 0
	for i in listin:
		sumlist += int(i)
	return(sumlist)

def deleteValuesList(listin, listaux, total):
	count = 1
	mult = 0
	for i in listaux:
		while(int(count)<int(total)):
			mult = int(i) * int(count)
			if mult in listin:
				print(i," - ",mult)
				listin.remove(mult)
			count+=1
		count = 1

	return listin

#********MAIN********
auxNumbers = primeNumbers10()
#print(auxNumbers)

totalNumbers = input("Insert total of the numbers: ")
print("Total Numbers: ", totalNumbers)
#print(totalNumbers)

#notPrimes = []
#notPrimes = notPrimesMult(auxNumbers, totalNumbers)

#print(notPrimes)

primeNumbers = list(range(2,int(totalNumbers)+1))
print("aux numbers: ", auxNumbers)
#primeNumbers.append(2)
#primeNumbers.append(3)
#primeNumbers.extend(primesN(notPrimes, totalNumbers))
primeNumbers = deleteValuesList(primeNumbers, auxNumbers, totalNumbers) 
primeNumbers.extend(auxNumbers)
primeNumbers.sort()
print("Prime numbers: ", primeNumbers)
#print("Sum of all prime numbers: ", sumListValues(primeNumbers))
