def stock_management(arr):
    n=len(arr)
    mini=float('inf')
    max_pro=0
    for i in range(n):
        price=0
        mini=min(mini,arr[i])
        max_pro=max(max_pro,arr[i]-mini)
    return max_pro
arr=[7,1,5,3,6,4,8]
print(stock_management(arr))