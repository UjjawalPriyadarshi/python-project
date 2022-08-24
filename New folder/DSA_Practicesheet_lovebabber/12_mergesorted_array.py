def mergesortedarray(arr1, arr2):
	i, j = 0, 0
	len1 = len(arr1)
	len2 = len(arr2)
	arr = []

	while ((i < len1) and (j < len2)):
		if(arr1[i] < arr2[j]):
			arr.append(arr1[i])
			i = i+1
		else:
			arr.append(arr2[j])
			j = j+1

	while(i < len1):
		arr.append(arr1[i])
		i = i+1
	while(j < len2):
		arr.append(arr2[j])

	return arr

arr1 = [1,4,6,7,9]
arr2 = [3,5,8]
arr = mergesortedarray(arr1, arr2)
print(arr)