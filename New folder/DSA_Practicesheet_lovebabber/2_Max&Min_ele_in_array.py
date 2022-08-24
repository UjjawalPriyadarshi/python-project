arr = [12, 13, 45 ,85, 55, 2]
Max=arr[0]

for i in range (len(arr)):
    if arr[i] > Max:
        Max = arr[i]
print("Maximum element of this list is",Max)

Min = arr[0]
for i in range(len(arr)):
    if arr[i] < Min:
        Min = arr[i]

print("Minimum element of this list is ", Min)

