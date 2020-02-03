total = 0
aux1 = 1
aux2 = 0
number = 0

repeat = input("Please insert the total ammount of the repetition: ");

while total != int(repeat):
	total = aux1 + aux2
	aux2 = aux1
	aux1 = total
	number += 1

print(number)
