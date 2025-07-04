# def next_permutation(arr):
#     n=len(arr)
#     break_point=-1
#     for i in range(n-2,-1,-1):
#         if arr[i]<arr[i+1]:
#             breakpoint=i
#             break
#     if breakpoint==-1:
#         return reversed(arr)
#     for j in range(n-1,breakpoint+1,-1):
#         if arr[j]>arr[breakpoint]:
#             arr[j],arr[breakpoint]=arr[breakpoint],arr[j]
#             break
#     arr[breakpoint+1:]=reversed(arr[breakpoint+1:0])
#     return arr
# arr=[2, 1, 5, 4, 3, 0, 0]
# print(next_permutation(arr))


from typing import List

def nextGreaterPermutation(A: List[int]) -> List[int]:
    n = len(A) # size of the array.

    # Step 1: Find the break point:
    ind = -1 # break point
    for i in range(n-2, -1, -1):
        if A[i] < A[i + 1]:
            # index i is the break point
            ind = i
            break

    # If break point does not exist:
    if ind == -1:
        # reverse the whole array:
        A.reverse()
        return A

    # Step 2: Find the next greater element
    #         and swap it with arr[ind]:
    for i in range(n - 1, ind, -1):
        if A[i] > A[ind]:
            A[i], A[ind] = A[ind], A[i]
            break

    # Step 3: reverse the right half:
    A[ind+1:] = reversed(A[ind+1:])

    return A

if __name__ == "__main__":
    A = [2, 1, 5, 4, 3, 0, 0]
    ans = nextGreaterPermutation(A)

    print("The next permutation is: [", end="")
    for it in ans:
        print(it, end=" ")
    print("]")

