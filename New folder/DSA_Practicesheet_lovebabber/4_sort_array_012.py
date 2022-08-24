def sortarray(arr, n, min_no, max_no):
	m = max_no - min_no+1
	c = [0]*m
	for i in range(n):
		c[arr[i]-min_no] += 1

	for i in range(m):
		for j in range((c[i])):
			print((i+min_no), end = " ")

arr = [0, 1, 0, 0, 1, 2, 2, 0]
min_no , max_no = 0,3
n= len(arr)
sortarray(arr, n, min_no, max_no)