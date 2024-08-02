import sys
n,m = map(int,input().split())
coin = list(map(int,input().split()))
INT_MIN = - sys.maxsize
dp = [ INT_MIN for _ in range(m)]
dp[0] =0

for i in range(1,m):
    for j in range(n):
        if dp[i-coin[j]] == INT_MIN:
            continue
        if i >= coin[j]:
            dp[i] = max(dp[i],dp[i-coin[j]]+1)
print(dp[m-1] if dp != INT_MIN else -1)