import sys
INT_MIN = -sys.maxsize
n = int(input())
arr= list(map(int,input().split()))
dp = [INT_MIN for _ in range(n)]
dp[0] = arr[0]

for i in range(1,n):
    dp[i] = max(dp[i-1]+arr[i],arr[i])
print(max(dp))