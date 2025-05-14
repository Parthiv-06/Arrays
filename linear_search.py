def linear_search(arr,tar):
    n=len(arr)
    for i in range(n):
        if arr[i]==tar:
            return f"the given number is found at {i}thh index"
    return "the given number is not found"
arr=[1,2,3,4,5,6]
tar=4
print(linear_search(arr,tar))