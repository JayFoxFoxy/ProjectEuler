#Solution: 70600674

import numpy as np
import time as tm


def convertToArray(numbers):
	
	count = 0
	l = np.zeros([20, 20])
	#print(l)
	for i in range(20):
		for j in range(20):
			aux = str(numbers[count]) + str(numbers[count+1])
			l[int(i)][int(j)] = aux
			count += 2
			

	return l

#--MAIN--

timeStart = tm.time()

filename = input("What is the name of the file of the input: ")
filename += ".txt"		
with open(filename, 'r') as file:
    numbers = file.read().replace('\n', '')

#print(numbers)

#numbersList = np.zeros((20,20))
#numbersList = np.empty([1,1])
#np.append(numbersList, 1)
#np.append(numbersList, 2)
#print(numbersList)
numbersList = convertToArray(numbers) 
print(numbersList)

a = np.zeros([20,20])

print("Time: ", tm.time() - timeStart, " sec!")

#a[5][5] = 20
#print(a)
