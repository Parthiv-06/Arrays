def find_number_occuring_once_while_others_twice(arr):
    xord=0
    n=len(arr)
    for i in range(n):
        xord=xord^arr[i]
    return xord
arr=[1,1,2,2,3,4,4]
print(find_number_occuring_once_while_others_twice(arr))