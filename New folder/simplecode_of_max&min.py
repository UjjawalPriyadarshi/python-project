arr = [12, 13, 45 ,85, 55, 2]

maximum = arr[0]

for i in range(len(arr)):
	if arr[i] > maximum:
		maximum = arr[i]



print("maximum element in this array is ", maximum)

minimum = arr[0]

for i in range(len(arr)):
	if arr[i] < minimum:
		minimum = arr[i]

print("minimum element in this array is ", minimum)
