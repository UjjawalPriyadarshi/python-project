def findkmax(k, array):
    array.sort(reverse=True)
    print("Kth max element is:",array[k - 1])
def findkmin(k, array):
    array.sort()
    print("Kth min element is:",array[k - 1])
array=[1,2,3,4,5,6]
k=1
findkmax(k, array)
findkmin(k, array)