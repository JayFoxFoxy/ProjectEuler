total = 0
aux1 = 1
aux2 = 0
number = 0

repeat = input("Please insert the total ammount of the repetition: ");

while int(aux1) < int(repeat):
	
	total = aux1 + aux2
	aux2 = aux1
	aux1 = total
	
	#print(aux1)
	#print(aux2)
	#print(total)

	if total % 2 == 0:
		number += total

print(number)
