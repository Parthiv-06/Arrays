def move_zeroes_to_end(arr):
    n=len(arr)
    j=-1
    for i in range(n):
        if arr[i]==0:
            j=i
            break
    if j==-1:
        return arr
    for i in range(j+1,n):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    return arr
arr=[2,1,3,0,8,0,9,0,1]
print(move_zeroes_to_end(arr))