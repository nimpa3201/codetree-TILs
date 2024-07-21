n = int(input())
arr = list(map(int,input().split()))
arr.sort()
L,R = 0, n-1
ans = arr[L]+arr[R]
while L < R:
    v = arr[L]+arr[R]
    if abs(ans) > abs(v):
        ans =v
    
    if v< 0:
        L+=1
    else:
        R-=1
print(abs(ans))