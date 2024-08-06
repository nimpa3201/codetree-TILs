import sys
n,m = map(int,input().split())
nums = list(map(int,input().split()))
dp = [sys.maxsize for _ in range(m+1)]
dp[0] =0

for j in range(n):
    for i in range(m,nums[j]-1,-1):
        if i >= nums[j]:
            dp[i] = min(dp[i],dp[i-nums[j]]+1)     

print("Yes" if dp[m] !=sys.maxsize else "No" )