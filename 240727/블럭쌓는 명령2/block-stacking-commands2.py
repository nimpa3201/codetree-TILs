n,k = map(int,input().split())
arr = [0 for _ in range(n+1)]
for _ in range(k):
    s,e = map(int,input().split())
    for i in range(s,e+1):
        arr[i]+=1
print(max(arr[1:]))