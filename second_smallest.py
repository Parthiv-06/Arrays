def second_smallest(arr):
    n=len(arr)
    small=float('inf')
    sec_small=float('inf')
    for i in range(n):
        if arr[i]<small:
            sec_small=small
            small=arr[i]
        elif arr[i]<sec_small and arr[i]!=small:
            sec_small=arr[i]
    return sec_small
arr=[1, 2, 4, 7, 7, 5]
print(second_smallest(arr))