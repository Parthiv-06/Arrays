def rearrage_in_alternate_signs(arr):
    n=len(arr)
    arr.sort()
    neg=[]
    pos=[]
    for i in range(n):
        if arr[i]<0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    for i in range(n//2):
        arr[2*i]=neg[i]
        arr[(2*i)+1]=pos[i]
    return arr
arr=[1,2,-4,-5]
print(rearrage_in_alternate_signs(arr))