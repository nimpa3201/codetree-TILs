import sys
n,m = map(int,input().split())
coin = list(map(int,input().split()))
INT_MIN = - sys.maxsize
dp = [ INT_MIN for _ in range(m+1)]
dp[0] =0

for i in range(1,m+1):
    for j in range(n):
        if i >= coin[j] and dp[i-coin[j]] == INT_MIN:
            continue
        if i >= coin[j]:
            dp[i] = max(dp[i],dp[i-coin[j]]+1)
print(dp[m] if dp[m] != INT_MIN else -1)