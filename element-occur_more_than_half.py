def element_occur_more_than_half(arr):
    cnt=0
    el=0
    cnt_el=0
    for i in range(len(arr)):
        if cnt==0:
            el=arr[i]
            cnt+=1
        if arr[i]!=el:
            cnt-=1
    if cnt==0:
        return "No element is occured more than the half of the times"
    for i in range(len(arr)):
        if arr[i]==el:
            cnt_el+=1
    if cnt_el>(len(arr)//2):
        return el
arr=[2,2,1,1,1,2,2]

print(element_occur_more_than_half(arr))