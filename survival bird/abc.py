# arr = [4, 54, 1, 5, 7, 9, 3]
# n = len(arr)
# mini = None
# for i in range(n-1):

#     print(abs(arr[i]-arr[i+1]))
#     diff = abs(arr[i]-arr[i+1])

#     if i == 0:
#         mini = diff

#     elif diff<mini:
#         mini = diff


# # print(mini)


def puzzle(arr): 
    n = len(arr)
    mini = None

    for i in range(n-1):
        diff = (abs(arr[i] - arr[i+1]))

        if i == 0:
            mini = diff

        elif diff < mini:
            mini = diff

    return mini


#driver code
arr = [1,6,7,8,5]


print(puzzle(arr))





    # print(abs(arr[i]-arr[i+1]))
