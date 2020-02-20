#---------------------------------------#
# Selection Sort                        #
#---------------------------------------#			
def selectionSort(A):
	for i in range (0, len(A) - 1):
		minIndex = i
		for j in range (i+1, len(A)):
			if A[j] < A[minIndex]:
				minIndex = j
		if minIndex != i:
			A[i], A[minIndex] = A[minIndex], A[i]
			
A = [9,5,3,11,4,7,6,1]
selectionSort(A)
print(A)
