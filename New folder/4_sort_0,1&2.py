def sort012(a , arr_size):
    low = 0
    high = arr_size - 1
    mid = 0
    while mid <= high:
        if a[mid] == 0:
            a[low],a[mid] = a[mid],a[low]
            low = low + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid],a[high] = a[high],a[low]
            high = high - 1
    return a
def printarray(a):
    for k in a :
        print(k, end = '')

arr = [0,1,1,0,1,2,1,2,0,0,0,1]
arr_size = len(arr)
arr = sort012(arr, arr_size)
print("array after segregation:")
printarray(arr)