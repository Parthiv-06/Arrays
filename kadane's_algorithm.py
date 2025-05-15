def kadane_algo(arr):
    ans_s,ans_e,start=-1,-1,0
    maxi=0
    res=[]
    summ=0
    for i in range(len(arr)):
        if summ==0:
            start=i
        summ+=arr[i]
        if summ>maxi:
            maxi=summ
            ans_s=start
            ans_e=i
        if summ<0:
            summ=0
    for i in range(ans_s,ans_e+1):
        print(arr[i])
    return res
arr=[-2,1,-3,4,-1,2,1,-5,-4]
kadane_algo(arr)