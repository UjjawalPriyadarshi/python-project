def findkmax(k, array):
    array.sort(reverse = True)
    print("kth max element is:",array[k-1])

def findkmin(k, array):
    array.sort()
    print("kth min element is:",array[k-1])

array = [8,5,7,4,6,2]
k=3
findkmax(k, array)
findkmin(k, array)