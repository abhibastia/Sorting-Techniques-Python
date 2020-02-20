#---------------------------------------#
# Bubble Sort                           #
#---------------------------------------#
# not optimized			
def bubbleSort1(A):
	for i in range (0, len(A) - 1):
		for j in range (0, len(A) - i - 1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
		#print("i=",i,A)	#to check the array after each iteration	
				
# optimized to exit if no swaps occur		
def bubbleSort2(A):
	for i in range (0, len(A) - 1):   #outer 0 to n-1
		isSwapped = False
		for j in range (0, len(A) - i - 1):   #inner 0 to n-i-1 as last item is sorted
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
				isSwapped = True
		print("i=",i,isSwapped)
		if not isSwapped:
			return
			
A = [4,7,6,1,2,5,8,9]
print("Before ",A)
bubbleSort2(A)
print("After ",A)
