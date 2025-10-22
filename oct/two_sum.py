def two_sum(arr,tar):
    mpp={}
    for i in range(len(arr)):
        if tar-arr[i] in mpp:
            return i,mpp[tar-arr[i]]
        mpp[arr[i]]=i
arr=[2,5,7,8,9]
tar=12
print(two_sum(arr,tar))