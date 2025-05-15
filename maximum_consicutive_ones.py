def max_consicutive_ones(arr):
    n=len(arr)
    count1=0
    max_count1=0
    for i in range(n):
        if arr[i]==1:
            count1+=1
        else:
            count1=0
        max_count1=max(count1,max_count1)
    return max_count1
arr=[1,0,1,1,1,1,0,1]
print(max_consicutive_ones(arr))
