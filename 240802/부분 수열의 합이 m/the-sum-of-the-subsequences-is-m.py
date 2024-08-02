import sys
INF = sys.maxsize

n, m = map(int, input().split()) # m 합, n 숫자 개수
nums = list(map(int, input().split()))

dp = [INF for _ in range(m + 1)]
dp[0] = 0
dp_num = [[] for _ in range(m + 1)]

for j in range(n):
    for i in range(m, nums[j] - 1, -1):  # 중복 방지
        if i >=nums[j]:
            dp[i] =min(dp[i],dp[i-nums[j]]+1)

print(dp[m]if dp[m] != INF else -1])