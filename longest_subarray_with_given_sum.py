def longest_subarray_with_given_suum(arr,tar):
    sum=0
    presum={}
    n=len(arr)
    length,maxlength=0,0
    for i in range(n):
        sum+=arr[i]
        if sum==tar:
            maxlength=max(maxlength,i+1)
        rem=sum-tar
        if rem in presum:
            length=i-presum[rem]
            maxlength=max(maxlength,length)
        if sum not in presum:
            presum[sum]=i
    return maxlength
arr=[2,3,0,5]
print(longest_subarray_with_given_suum(arr,5))