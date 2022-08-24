def rotateArray(array):
	array[:] = array[-1:] + array[:-1]

array = [1,2,3,4,5]
rotateArray(array)
print(*array)