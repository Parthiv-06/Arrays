def pascal(row):
    
    res=1
    ans=[1]
    for i in range(row):
        res*=(row-i)
        res//=(i+1)
        ans.append(res)
    return ans
def triangle(n):
    ans_triangle=[]
    for row in range(1,n+1):
        ans_triangle.append(pascal(row))
    return ans_triangle
row=4
print(triangle(row))
