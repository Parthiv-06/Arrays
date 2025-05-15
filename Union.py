# # def union(arr1,arr2):
# #     n1=len(arr1)
# #     n2=len(arr2)
# #     i=0
# #     j=0
# #     Union=[0]*(n1+n2)
# #     u=0
# #     while i<=n1 and j<=n2:
# #         if arr1[i]<arr2[j] and Union[u-1]!=arr1[i]:
# #             Union[u]=arr1[i]
# #             u+=1
# #             i+=1
# #         elif arr1[i]>arr2[j] and Union[u-1]!=arr2[j]:
# #             Union[u]=arr2[j]
# #             u+=1
# #             j+=1
# #     while i<=n1 :
# #         if Union[u-1]!=arr1[i]:
# #             Union[u]=arr1[i]
# #             i+=1
# #             u+=1
# #     while j<=n2:
# #         if Union[u-1]!=arr2[j]:
# #             Union[u]=arr2[j]
# #             j+=1
# #             u+=1
# #     return Union
# # arr1=[1,2,3,4,5]
# # arr2=[2,3,4,4,5]
# # print(union(arr1,arr2))

# def union(arr1,arr2):
#     i=0
#     j=0
#     Union=[]
#     while i<=len(arr1) and j<=len(arr2):
#         if arr1[i]<arr2[j]:
#             if len(Union)==0 or Union[-1]!= arr1[i]:
#                 Union.append(arr1[i])
#             i+=1
#         elif arr1[i]>arr2[j]:
#             if len(Union)==0 or Union[-1]!=arr2[j]:
#                 Union.append(arr2[j])
#             j+=1
#     while i<=len(arr1):
#         if Union[-1]!=arr1[i]:
#             Union.append(arr1[i])
#         i+=1
#     while j<=len(arr2):
#         if Union[-1]!=arr2[j]:
#             Union.append(arr2[j])
#         j+=1
#     return Union
# arr1=[1,2,3,4,5]
# arr2=[2,3,4,4,5]
# print(union(arr1,arr2))




def find_union(arr1, arr2):
    i, j = 0, 0  # Pointers
    union = []  # Union list

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  # Case 1 and 2
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:  # Case 3
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < len(arr1):  # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):  # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = find_union(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(*union)


