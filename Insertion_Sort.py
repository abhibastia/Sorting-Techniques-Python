
#---------------------------------------
# Insertion Sort
#---------------------------------------
# not optimized
def insertionSort_swap(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break


# optimized - shifts instead of swapping		
def insertionSort_shift(A):
	for i in range(1, len(A)):
		temp = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > temp:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = temp
			
A = [6,7,5,4,8,3,11,2]
#insertionSort_swap(A)
insertionSort_shift(A)
print(A)
