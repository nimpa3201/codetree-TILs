import sys
n = int(input())
arr =[0]+ list(map(int,input().split()))
INT_MIN = -sys.maxsize

dp =[INT_MIN for _ in range(n+1)]
dp[0] =0

for i in range(1,n+1):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))