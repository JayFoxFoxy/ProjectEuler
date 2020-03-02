total = input("Insert the total: ")

mult = 0

last = int(total) / 2

for i in range(1,int(last)):
	for j in range(1,int(last)):
		for x in range(1,int(last)):
			if ((int(i)**2) + (int(j)**2) == (int(x)**2)):
				if (int(i) + int(j) + int(x) == int(total)):
					if (int(i) < int(j) and int(j) < int(x)):
						print(i)
						print(j)
						print(x)
						suma = int(i) * int(j) * int(x)
						print(suma)
