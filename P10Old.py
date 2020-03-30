def checkPrimeNumber(number):
	aux = 0
	count = 0
	houses = 2
	start = 0
	
	if (number <=10):
		count = number
	else:
		count = 100
	if (number % 2 == 0):
		start = 2
	else:
		start = 3	

	if (number == 2):
		return number
	elif (number == 3):
		return number
	else:
		for i in range(start, number, houses):
			#print(i)
			if (int(number) % int(number) == 0 and int(number) % 1 == 0 and int(number) % i != 0):
				aux = number
			else:
				aux = 0
				return aux
	return aux
		


times = input("How many times you want to sum: ")

count = 2
total = 0

getNumber = 0

while (count <= int(times)):
	getNumber = checkPrimeNumber(count)
	total += getNumber
	#print(total)
	if (getNumber != 0):
		print(getNumber)
	
	getNumber = 0
	count += 1

print("The result: ")
print (total)
