n = int(input())
arr= [ 0 for _ in range(101)]
for _ in range(n):
    s,e = map(int,input().split())
    for i in range(s,e+1):
        arr[i]+=1
print(max(arr))