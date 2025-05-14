def left_rotate_an_array(arr,k):
    n=len(arr)
    temp=[0]*n
    for i in range(n-k):
        temp[i]=arr[i+k]
    for j in range(k):
        temp[(n-k)+j]=arr[j]
    return temp
arr=[1,2,3,4,5,6,7]
print(left_rotate_an_array(arr,2))