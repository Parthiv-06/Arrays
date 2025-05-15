def find_missing_number_in_an_array(arr,n):
    summm=sum(arr)
    summ=(n*(n+1))//2
    return summ-summm
arr=[1,2,3,4,5,6,8]
print(find_missing_number_in_an_array(arr,8))