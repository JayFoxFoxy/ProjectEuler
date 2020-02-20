num = 2
check = 0
check2 = 0
count = 0
aux = 0

limit = input("What is the limit: ")

while(count < int(limit)):
	if(num % 1 == 0):
		check = 1
	if(num % num == 0):
		check2 = 1
	for i in range(1, num + 1):
		if( num % i == 0 and i != 1 and i != num):
			check = 0
			check2 = 1
		#print(i)
	if(check == 1 and check2 == 1):
		count+=1
	num += 1

print(num-1)
