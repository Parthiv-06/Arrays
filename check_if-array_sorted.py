def check_if_sorted(arr):
    n=len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return "the array is not sorted"
    return "ths given array is sorted"
arr=[1,2,3,4,2,5]
print(check_if_sorted(arr))