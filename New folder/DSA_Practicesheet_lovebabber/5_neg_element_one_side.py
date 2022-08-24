def rearrange(arr,n):
    j = 0
    for i in range(0, n):
        
        if (arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j+1

    print(arr)

arr = [-2, 5, 9, 8, -8, -5, -6, 2]
n = len(arr)
rearrange(arr, n)