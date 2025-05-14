def largest(arr):
    n=len(arr)
    largest_element=0
    for i in range(n):
        largest_element=max(arr[i],largest_element)
    return largest_element
arr=[2,5,1,3,0]
print(largest(arr))
