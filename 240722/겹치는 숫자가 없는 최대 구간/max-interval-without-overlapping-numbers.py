n = int(input())
arr = list(map(int,input().split()))
R =-1
s= set()
ans =0
for L in range(n):
    while R+1 < n and arr[R+1] not in s:
        R+=1
        s.add(arr[R])
       
    ans = max(ans,R-L+1)
    s.remove(arr[L])
print(ans)