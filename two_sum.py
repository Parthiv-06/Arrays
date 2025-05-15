def two_sum(arr,tar):
    arr.sort()
    i=0
    j=len(arr)-1
    while i<j:
        if arr[i]+arr[j]<tar:
            i+=1
        elif arr[i]+arr[j]>tar:
            j-=1
        else:
            return arr[i],arr[j]
arr=[2,6,5,8,11]
print(two_sum(arr,14))