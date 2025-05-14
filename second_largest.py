def second_largest(arr):
    n=len(arr)
    lar=float('-inf')
    sec_lar=float('-inf')
    for i in range(n):
        if arr[i]>lar:
            sec_lar=lar
            lar=arr[i]
        elif arr[i]>sec_lar and arr[i]!=lar:
            sec_lar=arr[i]
    return sec_lar

arr=[1, 2, 4, 7, 7, 5]
print(second_largest(arr))