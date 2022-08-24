
def sort012( a, n):
	low = 0
	high = n - 1
	mid = 0
	while mid <= high:
		if a[mid] == 0:
			a[low], a[mid] = a[mid], a[low]
			low = low + 1
			mid = mid + 1
		elif a[mid] == 1:
			mid = mid + 1
		else:
			a[mid], a[high] = a[high], a[mid]
			high = high - 1
	return a
	
# Function to print array
def printArray( a):
	for k in a:
		print(k,end=' ')

# Driver Program
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n = len(arr)
arr = sort012( arr, n)
print ("Array after segregation :",)
printArray(arr)

# Contributed by Harshit Agrawal
