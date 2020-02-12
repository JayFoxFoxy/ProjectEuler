num = 0
reversenumber = 0
lastnumber = 0

def reverse(num):
	reverse = 0
	while(int(num) > 0):
        	reminder = num % 10
        	reverse = (reverse * 10) + reminder
        	num = num // 10
	return reverse

for i in range(100, 999, 1):
	for j in range(100, 999, 1):
		num = int(i) * int(j)
		#print(num)
		reversenumber = reverse((int)(num))
		#print(reversenumber)
		if num == reversenumber:
			if num > lastnumber:
				lastnumber = num

print(lastnumber)
			#exit()
