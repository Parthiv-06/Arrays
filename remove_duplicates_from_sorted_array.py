def remove_duplicates_from_sorted_array(arr):
    n=len(arr)
    i=0
    for j in range(n):
        if arr[i]!= arr[j]:
            i+=1
            arr[i]=arr[j]
    return i+1
arr=[1,1,2,2,2,3,3]
k=remove_duplicates_from_sorted_array(arr)
for i in range(k):
    print(arr[i])

