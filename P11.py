import numpy as np
import time as tm


def convertToArray(numbers):
	
	count = 0
	l = np.zeros([20, 20])
	for i in range(20):
		for j in range(20):
			aux = str(numbers[count]) + str(numbers[count+1])
			l[int(i)][int(j)] = aux
			count += 2
			

	return l

def arrayDiv(l):
	newL = np.zeros([4, 4])
	row = 0
	col = 0
	
	bigger = 0
	
	while col + 4 <= 20:
		while row + 4 <= 20:
			for i in range(4):
				for j in range(4):
					newL[i][j] = l[col+i][row+j]
			#print(newL)
			bigger = bigMult(newL, bigger)
			#print("result: ", int(bigger))
			row +=1
		col += 1
		row = 0
	
	#print(int(bigger))
	return int(bigger)

def bigMult(l, n):
	bigger = 1

	for i in range(np.size(l,0)):
		for j in range(np.size(l,1)):
			bigger = bigger * l[i][j]
		#print(bigger)
		if bigger > n:
			n = bigger
		bigger = 1

	bigger = 1
	
	for i in range(np.size(l,1)):
		for j in range(np.size(l,0)):
			bigger = bigger * l[j][i]
		#print(bigger)
		if bigger > n:
			n = bigger
		bigger = 1
	
	bigger = 1
	
	for i in range(np.size(l,0)):
		bigger = bigger * l[i][i]
	#print(bigger)
	if bigger > n:
		n = bigger
	bigger = 1
	
	row = 0

	for i in range(np.size(l,0)-1,-1,-1):
		bigger = bigger * l[row][i]
		row += 1	
	#print(bigger)
	if bigger > n:
		n = bigger
	bigger = 1
	
	return n 
			
					 
#--MAIN--

timeStart = tm.time()

filename = input("What is the name of the file of the input: ")
filename += ".txt"		
with open(filename, 'r') as file:
    numbers = file.read().replace('\n', '')

#numbersList = np.zeros((20,20))
#numbersList = np.empty([1,1])
#np.append(numbersList, 1)
#np.append(numbersList, 2)
#print(numbersList)
numbersList = convertToArray(numbers) 
#print(numbersList)

a = np.zeros([20,20])

bigger = arrayDiv(numbersList)

print("The result is: ", bigger)
print("Time: ", tm.time() - timeStart, " sec!")

#a[5][5] = 20
#print(a)
#arrayDiv(numbersList)
