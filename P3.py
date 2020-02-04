number = 0

number = input("Insert the number: ")

n = int(number)
#print(n)
last = 0
aux = 0
total = 1
i = 1

while i < int(number):
	if int(number) % int(i) == 0:
		last = int(i)
		#print(last)
		if total < int(number):
			total = total * last
			aux = last
			#print(total) 
		if total >= int(number):
			print(aux)
			exit()
	i += 1

print(aux)
