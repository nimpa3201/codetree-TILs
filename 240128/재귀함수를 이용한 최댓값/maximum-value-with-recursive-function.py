def fun(arr,k):
    global ans
    if len(arr) ==k+1:
        return ans 
    else:
        if ans < arr[k]:
            ans = arr[k]
        return fun(arr,k+1)
n = int(input())
arr= list(map(int,input().split())) 
ans =arr[0]
print(fun(arr,0))
# 6
# 1 5 7 9 2 6