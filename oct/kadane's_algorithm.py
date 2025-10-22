# # def kadane_algorithm(arr):
# #     curr_max=0
# #     gmax=0
# #     for i in range(len(arr)):
# #         if curr_max<0:
# #             curr_max=0
# #         curr_max+=arr[i]
# #         gmax=max(gmax,curr_max)
# #     return gmax
# # arr=[-2,1,-3,4,-1,2,1,-5,4]
# # print(kadane_algorithm(arr))

# def kadane_algo(arr):
#     gm,cm=0,0
#     for i in range(len(arr)):
#         if cm<0:
#             cm=0
#         cm+=arr[i]
#         gm=max(gm,cm)
#     return gm
# arr=[-2,1,-3,4,-1,2,1,-5]
# print(kadane_algo(arr))

def kadane(arr):
    cm,gm=0,0
    for i in range(len(arr)):
        if cm<0:
            cm=0
        cm+=arr[i]
        gm=max(gm,cm)
    return gm
arr=[-2,1,-3,4,-1,2,1,-5,4]
print(kadane(arr))
