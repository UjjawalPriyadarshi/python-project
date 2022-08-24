def  removeduplicate(arr, n):
    if n == 0 or n == 1:
        return n #return new size of modification array

    temp = list(range(n))

    j = 0; #transerve element
    for i in range(0, n-1):
        if arr[i] != arr[i+1]: # if curr element is not equal to next element then store curr ele
            temp[j] = arr[i]
            j += 1

    temp[j] = arr[n-1]
    j += 1

    for i in range(0, j):
        arr[i] = temp[i]
    return  j

#driver code
arr = [1,2,2,3,4,4,4,4,5,5,5,5]
n = len(arr)
n = removeduplicate(arr,n)

#print updated array
for i in range(n):
    print("%d"%(arr[i]),end = " ")
